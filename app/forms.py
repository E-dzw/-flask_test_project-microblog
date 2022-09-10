from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('login in')

class RegistrationForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password",validators={DataRequired()})
    password2=PasswordField("Repeat your password",validators=[DataRequired(),EqualTo("password")])
    email=StringField("E-mail",validators=[DataRequired(),Email()])
    submit=SubmitField("Register")

    def validata_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            return ValidationErr("%s is registrated, please use another username without registrated !!!"%user.username)

    def validata_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            return ValidationErr("%s is registrated, please use another email without registrated !!!"%user.email)