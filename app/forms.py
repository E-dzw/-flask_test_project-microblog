from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,Length
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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("{} is registrated, please use defferent username.".format(username.data))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("{} is registrated, please use defferent email".format(user.email))

class EditProfileForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    about_me=TextAreaField("About me",validators=[Length(min=0, max=140)])
    submit=SubmitField("Submit")
    
    #表单类不能覆盖FlaskForm类的init的方法,如果需要重写init方法,那么必须在init方法内显示的执行父类的init方法.
    def __init__(self, original_username, *args, **kwargs):  
        # ,formdata=..., **kwargs
        super().__init__(*args, **kwargs)
        self.original_username=original_username
    
    def validate_username(self,username):
        if self.original_username != username.data:
            user=User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError("please use different username.")