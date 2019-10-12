from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), length(8,25)])
    
    password = PasswordField('password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    

    

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), length(5,25)])
    
    password = PasswordField('password', validators=[DataRequired()])
    
    submit = SubmitField('Login')

    