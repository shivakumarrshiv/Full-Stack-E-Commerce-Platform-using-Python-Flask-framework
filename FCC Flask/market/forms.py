from flask_wtf import FlaskForm #To create some awesome forms we use this flask package 
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,DataRequired,EqualTo,Email,ValidationError#these are the classes which provide additional features fot flask forms to validate or many uses
from market.models import User

class RegistrationForm(FlaskForm):
    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('User already exist! Please Try again with another Username')

    def validate_email_address(self,email_address_to_check):
        email=User.query.filter_by(email_address=email_address_to_check.data).first()
        if email:
            raise ValidationError('EmailID already exist!')

    
    username=StringField(label='Username', validators=[Length(min=2,max=30), DataRequired( )])
    email_address=StringField(label='Email Adress', validators=[Email(), DataRequired( )])
    password1=PasswordField(label='Password', validators=[Length(min=6),DataRequired( )])
    password2=PasswordField(label='Confirm Password', validators=[Length(min=6),EqualTo('password1'), DataRequired( )])
    submit=SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username=StringField(label='Username', validators=[DataRequired()])
    password=PasswordField(label='Password', validators=[DataRequired()])
    submit=SubmitField(label='Sign In')

class PurchaseForm(FlaskForm):
    submit=SubmitField(label='Purchase the item')

class SellForm(FlaskForm):
    submit=SubmitField(label='Sell Item')