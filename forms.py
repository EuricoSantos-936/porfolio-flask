from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL

class ProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    mini_description = StringField('Mini Description - To show on cards', validators=[DataRequired()])
    stack_used = StringField('Stack Used - ex. Flask - Tkinter - React', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired(), URL()])
    link_github = StringField('GitHub Link', validators=[DataRequired(), URL()])
    image = FileField('Image')
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
