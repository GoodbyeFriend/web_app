from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], id = "username")
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Sign In')