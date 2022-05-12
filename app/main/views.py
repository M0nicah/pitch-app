import os
import secrets
from flask import render_template, request, url_for,flash,redirect
from PIL import Image
import app
from ..forms import PitchForm, RegistrationForm, LoginForm, UpdateAccountForm
from app import db
from app.main import main
from  app.models import User, Pitch
from flask_login import current_user, login_required, login_user,logout_user

pitch = [
    {
        'author': 'Test User',
        'title': 'Test Pitch',
        'body': 'Test Tester Testing',
        'date_posted': 'May 6, 2020'
    },
    {
        'author': 'John User',
        'title': 'Johns Pitch',
        'body': 'John Tester Testing',
        'date_posted': 'May 2, 2020'
    }
]
@login_required
@main.route("/")
def index():
    pitch = Pitch.query.all()
    return render_template('index.html', pitch=pitch)

@main.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account successfully created for {form.username.data}', 'success')
        return redirect(url_for('main.index'))
    return render_template('signup.html', title='Register', form = form)


@main.route("/login", methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('main.index')) #prevents the user from double logging in
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.email == form.email.data:
            print(user)
            flash(f'Login Successfull', 'success')
            return redirect(url_for('main.index'))
    else:
        flash(f'Enter credentials to log in', 'danger')
    return render_template('login.html', title='Login', form = form)

@main.route('/logout')
def logout():
    '''
    Function that handles logout
    Returns:
        Log out user to login page
    '''
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/pitch/new', methods=['GET', 'POST'] )
@login_required
def new_pitch():
    form=PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, body=form.body.data)
        db.session.add(pitch)
        db.session.commit()
        flash('Your Pitch has been posted successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('pitches.html',title='New Pitch', form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@main.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.profilepic = picture_file
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.add(pitch)
            db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    profilepic = url_for('static', filename='profile_pics/' + current_user.profilepic)
    return render_template('user.html', title='Profile', profilepic=profilepic, form=form)