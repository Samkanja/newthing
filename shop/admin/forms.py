from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,  Length,Email,EqualTo

class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])


#class RegistrationForm(FlaskForm):
    #name = StringField('Name',
                           #validators=[DataRequired(), Length(min=2, max=20)])
    #username = StringField('Username',
                          # validators=[DataRequired(), Length(min=2, max=20)])
    #email = StringField('Email',
                        #validators=[DataRequired(), Email()])
    #password = PasswordField('Password', validators=[DataRequired()])
    #confirm = PasswordField('Confirm Password',
                                     #validators=[DataRequired(), EqualTo('password')])
    