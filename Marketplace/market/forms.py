from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField



class RegisterForm(FlaskForm):
    username = StringField(label='User Name: ')
    email_address = StringField(label='Email Address: ')
    password1 = PasswordField(label='Password: ')
    password2 = PasswordField(label='Confirm password: ')
    submit = SubmitField(label='Create account')
