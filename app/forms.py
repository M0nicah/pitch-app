from turtle import title
from click import confirm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from app.models import User, Pitch

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit_form = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_form = SubmitField('Log in')

class PitchForm(FlaskForm):
    '''
    Class that handles pitch creation buy users
    '''
    title = StringField('Title', validators=[DataRequired])
    body = StringField('Enter your pitch', validators=[DataRequired()])
    submit = SubmitField('Post') 


def validate_username(self, username):
    if User.query.filter_by(username=username.data).first():
        raise ValidationError("Username already taken!")

def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')