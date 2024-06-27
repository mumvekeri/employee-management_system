from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from forms import RegistrationForm, LoginForm, UpdateAccountForm, ProfileForm
from models import User, Profile
from flask_login import login_user, current_user, logout_user, login_required
import os
import secrets
from PIL import Image

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        profile = Profile(user_id=user.id)
        db.session.add(profile)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    profile_form = ProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        profile_form.bio.data = current_user.profile.bio
        profile_form.address.data = current_user.profile.address
        profile_form.phone.data = current_user.profile.phone
    if profile_form.validate_on_submit():
        current_user.profile.bio = profile_form.bio.data
        current_user.profile.address = profile_form.address.data
        current_user.profile.phone = profile_form.phone.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('account'))
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form, profile_form=profile_form)


@app.route("/attendance", methods=['GET', 'POST'])
@login_required
def attendance():
    form = AttendanceForm()
    if form.validate_on_submit():
        if form.submit_check_in.data:
            attendance_record = Attendance(user_id=current_user.id)
            db.session.add(attendance_record)
            db.session.commit()
            flash('Checked in successfully!', 'success')
        elif form.submit_check_out.data:
            attendance_record = Attendance.query.filter_by(user_id=current_user.id).order_by(Attendance.id.desc()).first()
            if attendance_record and attendance_record.check_out is None:
                attendance_record.check_out = datetime.utcnow()
                db.session.commit()
                flash('Checked out successfully!', 'success')
            else:
                flash('No check-in record found or already checked out.', 'danger')
        return redirect(url_for('attendance'))
    attendance_records = Attendance.query.filter_by(user_id=current_user.id).all()
    return render_template('attendance.html', title='Attendance', form=form, attendance_records=attendance_records)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
   

