from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='employee')
    profile = db.relationship('Profile', backref='user', uselist=False)
    attendance = db.relationship('Attendance', back_populates='user')
    payroll = db.relationship('Payroll', back_populates='user')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    address = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Profile('{self.user_id}', '{self.bio}', '{self.address}', '{self.phone}')"

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    check_in = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    check_out = db.Column(db.DateTime, nullable=True)

    user = db.relationship('User', back_populates='attendance')

    def __repr__(self):
        return f"Attendance('{self.user_id}', '{self.check_in}', '{self.check_out}')"

class Payroll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    bonus = db.Column(db.Float, nullable=True)
    deductions = db.Column(db.Float, nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship('User', back_populates='payroll')

    def __repr__(self):
        return f"Payroll('{self.user_id}', '{self.salary}', '{self.date}')"

User.attendance = db.relationship('Attendance', order_by=Attendance.id, back_populates='user')
User.payroll = db.relationship('Payroll', order_by=Payroll.id, back_populates='user')
