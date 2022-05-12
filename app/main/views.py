from flask import render_template, url_for,flash,redirect
from ..forms import PitchForm, RegistrationForm, LoginForm
from app import db
from app.main import main
from  app.models import User, Pitch
from flask_login import current_user, login_required, login_user,logout_user

# pitch = [
#     {
#         'author': 'Test User',
#         'title': 'Test Pitch',
#         'message': 'Test Tester Testing',
#         'date': 'May 6, 2020'
#     },
#     {
#         'author': 'John User',
#         'title': 'Johns Pitch',
#         'message': 'John Tester Testing',
#         'date': 'May 2, 2020'
#     }
# ]

@main.route("/", methods=['GET', 'POST'])
@main.route("/index", methods=['GET', 'POST'])
# @login_required
def index():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(body=form.body.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been uploaded')
        return redirect(url_for('main.index'))
    all_pitches = Pitch.query.order_by(Pitch.date_posted.desc()).all()

    return render_template('index.html', form=form, Pitch=Pitch)

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
        if user is None or not user.check_password(form.password.data):
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

@main.route('/post/newPost', methods=['GET', 'POST'] )
@login_required
def new_post():
    form=PitchForm()
    if form.validate_on_submit():
        flash('Your Pitch has been posted successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('_pitch.html',title='New Pitch', form=form)
    

# @main.route('/user/<username>')
# @login_required
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     posts = [
#         {'author': user, 'body': 'Test post #1'},
#         {'author': user, 'body': 'Test post #2'}
#     ]
#     return render_template('user.html', user=user, posts=posts)