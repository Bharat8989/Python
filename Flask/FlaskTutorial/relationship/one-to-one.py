from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# =========================
# USER MODEL
# =========================
class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(290),
        nullable=False
    )

    # One-to-One Relationship
    profile = db.relationship(
        'Profile',
        uselist=False,
        back_populates='user'
    )


# =========================
# PROFILE MODEL
# =========================
class Profile(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    bio = db.Column(
        db.String(290),
        nullable=False
    )

    # Foreign Key
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        unique=True,
        nullable=False
    )

    # One-to-One Relationship
    user = db.relationship(
        'User',
        back_populates='profile'
    )


# Create Database Tables
with app.app_context():
    db.create_all()


# =========================
# HOME ROUTE
# =========================
@app.route('/')
def home():
    return 'Home Page'


# =========================
# ADD USER + PROFILE
# =========================
@app.route('/user-add')
def add_user():

    # Create User Object
    user = User(
        name='Test User'
    )

    # Create Profile Object
    profile = Profile(
        bio='Test User Profile'
    )

    # Connect Profile with User
    user.profile = profile

    # Add User to Database
    db.session.add(user)

    # Save Changes
    db.session.commit()

    return jsonify({
        'message': 'User added successfully'
    })


# =========================
# GET ALL USERS
# =========================
@app.route('/users')
def get_users():

    users = User.query.all()

    user_list = []

    for user in users:

        user_data = {
            'id': user.id,
            'name': user.name,
            'bio': user.profile.bio if user.profile else None
        }

        user_list.append(user_data)

    return jsonify(user_list)


# =========================
# RUN APPLICATION
# =========================
if __name__ == "__main__":
    app.run(debug=True)