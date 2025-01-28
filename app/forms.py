from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField ('Email', validators=[Email("Enter correct email")])
    remember_me = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Sign In')