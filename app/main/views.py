from flask import render_template, url_for,flash,redirect
from ..forms import RegistrationForm, LoginForm
# from flask_wtf import FlaskForm
from app.main import main
from ..models import User


pitch = [
    {
        'author': 'Test User',
        'title': 'Test Pitch',
        'message': 'Test Tester Testing',
        'date': 'May 6, 2020'
    },
    {
        'author': 'John User',
        'title': 'Johns Pitch',
        'message': 'John Tester Testing',
        'date': 'May 2, 2020'
    }
]

@main.route("/")
def index():
    return render_template('index.html', pitch=pitch)

@main.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account successfully created for {form.username.data}', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', title='Register', form = form)


@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@blog.com' and form.password.data == 'password':
            flash(f'Login Successfull', 'success')
            return redirect(url_for('index'))
    else:
        flash(f'Login Unsuccessful. Email or Password is incorrect', 'danger')
    return render_template('login.html', title='Login', form = form)
