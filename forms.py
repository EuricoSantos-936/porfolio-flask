from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, URL

class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    github = StringField('Github Link', validators=[DataRequired(), URL()])
    link = StringField('Project Link', validators=[DataRequired(), URL()])
    image = StringField('Image URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Add Project')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
