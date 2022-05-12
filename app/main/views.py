from flask import render_template, url_for,flash,redirect
from ..forms import PitchForm, RegistrationForm, LoginForm
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
        if user and user.check_password(user.password, form.password.data):
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
def new_post():
    form=PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, body=form.body.data, author=User)
        db.session.add(pitch)
        db.session.commit()
        flash('Your Pitch has been posted successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('pitch.html',title='New Pitch', form=form)
    

# @main.route('/user/<username>')
# @login_required
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     posts = [
#         {'author': user, 'body': 'Test post #1'},
#         {'author': user, 'body': 'Test post #2'}
#     ]
#     return render_template('user.html', user=user, posts=posts)