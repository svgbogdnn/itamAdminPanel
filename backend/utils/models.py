from app import db
from datetime import datetime

class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)  # full name
    email = db.Column(db.String(128), unique=True, nullable=False)  # email address
    phone_number = db.Column(db.String(15), nullable=True)  # optional phone number
    password = db.Column(db.String(128), nullable=False)  # hashed password
    role = db.Column(db.String(20), nullable=False, default="student")  # user role
    profile_picture = db.Column(db.String(256), nullable=True)  # optional profile picture url
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)  # registration date
    status = db.Column(db.String(20), nullable=False, default="offline")  # online/offline status
    last_login = db.Column(db.DateTime, nullable=True)  # last login timestamp

class courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)  # primary key
    name = db.Column(db.String(255), nullable=False)  # name of the course
    description = db.Column(db.Text, nullable=False)  # short description
    tutor_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))  # foreign key to users
    status = db.Column(db.String(50), default='active')  # course status (active/finished)
    duration = db.Column(db.Interval, nullable=True)  # duration of the course
    start_date = db.Column(db.Date, nullable=True)  # start date
    end_date = db.Column(db.Date, nullable=True)  # end date
    course_code = db.Column(db.String(50), unique=True, nullable=True)  # unique course code
    category = db.Column(db.String(100), nullable=True)  # optional category like "math", "science"
