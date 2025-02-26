from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email, EqualTo, ValidationError
from main.models import User


class RegistrationForm(FlaskForm): # inheritance
    username = StringField("Username", 
                           validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username): 
        user = User.query.filter_by(username=username.data).first()
        if user:
            return False
        return True        
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            return False
        return True

class LoginForm(FlaskForm): # inheritance
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")



