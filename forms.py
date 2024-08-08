from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL

class ProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Name is required.")])
    description = TextAreaField('Description', validators=[DataRequired(message="Description is required.")])
    mini_description = StringField('Mini Description - To show on cards', validators=[DataRequired(message="Mini Description is required.")])
    stack_used = StringField('Stack Used - ex. Flask - Tkinter - React', validators=[DataRequired(message="Stack Used is required.")])
    link = StringField('Link', validators=[DataRequired(message="Link is required."), URL(message="Invalid URL format.")])
    link_github = StringField('GitHub Link', validators=[DataRequired(message="GitHub Link is required."), URL(message="Invalid URL format.")])
    image = FileField('Image')
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
