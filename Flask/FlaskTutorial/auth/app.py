import bcrypt
from datetime import datetime, timezone
from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)

# Database Configuration (Using SQLite database file)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# FIX: Added a Secret Key to allow secure session tracking cookies
app.secret_key = 'super_secret_session_encryption_key'

from flask_sqlalchemy import SQLAlchemy
# Initialize SQLAlchemy
db = SQLAlchemy(app)


# ---- 1. REGISTER TABLE MODEL ----
class Register(db.Model):
    __tablename__ = 'alluser'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    mobile_number = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    # Establish relationship mapping link to query history easily from the dashboard
    login_history = db.relationship('Login', backref='user', lazy=True)

    def __init__(self, username, email, mobile_number, password):
        self.username = username
        self.email = email
        self.mobile_number = mobile_number
        
        # Encrypting password using standard bcrypt.hashpw and bcrypt.gensalt
        hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_bytes.decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))


# ---- 2. LOGIN AUDIT HISTORY TABLE MODEL ----
class Login(db.Model):
    __tablename__ = 'login_history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # Foreign Key linking this activity record to the specific User ID in 'alluser' table
    user_id = db.Column(db.Integer, db.ForeignKey('alluser.id', ondelete='CASCADE'), nullable=False)
    
    # FIX: Modern Timezone-safe UTC standard initialization
    login_time = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    status = db.Column(db.String(50), default='Success', nullable=False)

    def __init__(self, user_id, status='Success'):
        self.user_id = user_id
        self.status = status


# FIX: Moved db.create_all() down HERE so BOTH tables are properly created on startup
with app.app_context():
    db.create_all()


# ---- 3. ROUTE CONTROLLERS ----

@app.route('/')
def index():
    return render_template('home.html')

# ---- USER REGISTRATION ----
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        mobile_number = request.form.get('mobile_number')
        password = request.form.get('password')
        
        existing_user = Register.query.filter((Register.username == username) | (Register.email == email)).first()
        if existing_user:
            return "Registration error: Username or Email is already taken.", 400

        new_user = Register(username=username, email=email, mobile_number=mobile_number, password=password)
        
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
        
    return render_template('register.html')


# ---- USER LOGIN ----
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return "Error: Please fill in all fields.", 400

        user = Register.query.filter_by(email=email).first()

        if user and user.check_password(password):
            # Store session variables to keep user logged in across pages
            session['user_id'] = user.id
            session['username'] = user.username
            
            # LOG EVENT: Add a new entry into your login tracker table
            login_log = Login(user_id=user.id, status='Success')
            db.session.add(login_log)
            db.session.commit()
            
            return redirect('/dashboard')
        else:
            return "Authentication failed: Invalid Email or Password.", 401
            
    return render_template('login.html')


# ---- SECURE DASHBOARD LANDING VIEW ----
@app.route('/dashboard' ,methods =['GET'])
def dashboard():
    # FIX: Securely use .get() instead of a hard bracket lookup to prevent KeyError crashes
    user_id = session.get('user_id')
    username = session.get('username')
    
    if not username:
        return redirect('/login')  # Safely redirect unauthorized traffic back to login page

    # Fetch this specific user's login logs to render in the HTML table
    user_logs = Login.query.filter_by(user_id=user_id).order_by(Login.login_time.desc()).all()
    
    # Render template with variables passed cleanly to match our Jinja code
    return render_template('dashboard.html', username=username, logs=user_logs, total_logins=len(user_logs))


# ---- LOGOUT CONTROLLER ----
@app.route('/logout')
def logout():
    session.clear()  # Clear cookies to destroy user session context
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
