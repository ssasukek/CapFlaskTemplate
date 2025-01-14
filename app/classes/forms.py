# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of of a class. Forms are managed by the 
# Flask-WTForms library.

from flask.app import Flask
from flask import flash
from flask_wtf import FlaskForm
from mongoengine.fields import EmailField
import mongoengine.errors
#from wtforms.fields.html5 import URLField, DateField, DateTimeField, EmailField
from wtforms.validators import URL, NumberRange, Email, Optional, InputRequired, ValidationError, DataRequired, EqualTo
from wtforms import PasswordField, StringField, SubmitField, validators, TextAreaField, HiddenField, IntegerField, SelectField, FileField, BooleanField
from app.classes.data import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me?')
    submit = SubmitField()

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])  
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        try:
            User.objects.get(username=username.data)
        except mongoengine.errors.DoesNotExist:
            flash(f"{username.data} is available.")
        else:
            raise ValidationError('This username is taken.')

    def validate_email(self, email):
        try:
            User.objects.get(email=email.data)
        except mongoengine.errors.DoesNotExist:
            flash(f'{email.data} is a unique email address.')
        else:
            raise ValidationError('This email address is already in use. if you have forgotten your credentials you can try to recover your account.')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class ProfileForm(FlaskForm):
    #email = StringField('Email', validators=[DataRequired(), Email()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role',choices=[("Teacher","Teacher"),("Student","Student")])
    fav_color = SelectField('Color', choices=[("Blue","Blue"),("Red","Red"),("White","White"),("Black","Black")])

class PageForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    directions = StringField('Directions', validators=[DataRequired()])
    content = StringField('Story Text', validators=[DataRequired()])
    image = FileField("Image")
    c1 = SelectField("Choice 1", choices=[], validate_choice=False)
    c2 = SelectField("Choice 2", choices=[], validate_choice=False)
    c3 = SelectField("Choice 3", choices=[], validate_choice=False)
    submit = SubmitField('Submit')

    

class PostForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Post', validators=[DataRequired()])
    submit = SubmitField('Post')
    rate_game = SelectField('Rate', choices = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')
    
class DonationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = TextAreaField('Leave a message', validators=[DataRequired()])
    submit = SubmitField('Submit')
    money = SelectField ('Amount', choices =[("10","$10"), ("20","$20"), ("50","$50"), ("100","$100")])