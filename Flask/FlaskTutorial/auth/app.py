import bcrypt
import logging  # 1. Brought in the default internal library engine
from datetime import datetime, timezone
from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)

# ---- 2. DETAILED LOGGING CONFIGURATION STRUCTURE ----
log_level = logging.DEBUG
log_file = 'app.log'
log_file_mode = 'a'
log_format = '%(asctime)s - [%(levelname)s] - %(filename)s:%(lineno)d - %(message)s'

logging.basicConfig(
    level=log_level,
    filename=log_file,
    filemode=log_file_mode,
    format=log_format
)

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
    
    login_history = db.relationship('Login', backref='user', lazy=True)

    def __init__(self, username, email, mobile_number, password):
        self.username = username
        self.email = email
        self.mobile_number = mobile_number
        
        hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_bytes.decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))


# ---- 2. LOGIN AUDIT HISTORY TABLE MODEL ----
class Login(db.Model):
    __tablename__ = 'login_history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('alluser.id', ondelete='CASCADE'), nullable=False)
    login_time = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    status = db.Column(db.String(50), default='Success', nullable=False)

    def __init__(self, user_id, status='Success'):
        self.user_id = user_id
        self.status = status


# Initialize database context structures
with app.app_context():
    logging.info("Initializing system architecture setup layers...")
    db.create_all()


# ---- 3. ROUTE CONTROLLERS WITH STRATEGIC LOGGING EVENTS ----

@app.route('/')
def index():
    logging.debug("Root path entry point accessed by remote client client.")
    return render_template('home.html')


# ---- USER REGISTRATION ----
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        mobile_number = request.form.get('mobile_number')
        password = request.form.get('password')
        
        logging.info(f"Processing a registration attempt for username: '{username}', email: '{email}'.")
        
        existing_user = Register.query.filter((Register.username == username) | (Register.email == email)).first()
        if existing_user:
            # High-priority Warning alert tracking unique field validation rejections
            logging.warning(f"Registration rejected. Duplicate data found for '{username}' or '{email}'.")
            return "Registration error: Username or Email is already taken.", 400

        try:
            new_user = Register(username=username, email=email, mobile_number=mobile_number, password=password)
            db.session.add(new_user)
            db.session.commit()
            
            logging.info(f"Successfully finalized database insertion record for profile: '{username}'.")
            return redirect('/login')
        except Exception as database_error:
            # Exception context capture logs full trace data on deep processing failures
            logging.error(f"Critical internal error executing registration transaction pipeline: {str(database_error)}")
            return "Internal Server Error", 500
        
    return render_template('register.html')


# ---- USER LOGIN ----
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        logging.info(f"Incoming session initialization request evaluated for address: '{email}'.")

        if not email or not password:
            logging.warning("Authentication interrupted due to missing request fields.")
            return "Error: Please fill in all fields.", 400

        user = Register.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            
            login_log = Login(user_id=user.id, status='Success')
            db.session.add(login_log)
            db.session.commit()
            
            logging.info(f"Authorization token matched. User session online for profile context '{user.username}'.")
            return redirect('/dashboard')
        else:
            logging.warning(f"Access Denied. Failed authentication credential signature on destination mapping target: '{email}'.")
            return "Authentication failed: Invalid Email or Password.", 401
            
    return render_template('login.html')


# ---- SECURE DASHBOARD LANDING VIEW ----
@app.route('/dashboard', methods=['GET'])
def dashboard():
    user_id = session.get('user_id')
    username = session.get('username')
    
    if not username:
        # Tracks potential security breach movements cleanly to warn system admins
        logging.warning(f"Unauthorized intrusion blocked at protected path '/dashboard' from network host source: {request.remote_addr}")
        return redirect('/login')

    logging.debug(f"Pulling transactional audit logs for authorized profile session: '{username}'.")
    user_logs = Login.query.filter_by(user_id=user_id).order_by(Login.login_time.desc()).all()
    
    return render_template('dashboard.html', username=username, logs=user_logs, total_logins=len(user_logs))


# ---- LOGOUT CONTROLLER ----
@app.route('/logout')
def logout():
    username = session.get('username', 'Unknown')
    session.clear()
    logging.info(f"User profile session successfully cleared from system host for client: '{username}'.")
    return redirect('/login')

@app.route('/users')
def user():
    return 'this is the profile info page '


if __name__ == '__main__':
    app.run(debug=True)
