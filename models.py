from db import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    mini_description = db.Column(db.String(255), nullable=True)
    stack_used = db.Column(db.String(255), nullable=True)
    link = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    link_github = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Project {self.name}>'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
