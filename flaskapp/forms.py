from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError
from server import User

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[
                           DataRequired(), length(8, 25)])
    email = StringField("email", validators=[Email(), DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[
                           DataRequired(), length(5, 25)])

    password = PasswordField('password', validators=[DataRequired()])

    submit = SubmitField('Login')
