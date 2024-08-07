from flask import Flask
from flask_migrate import Migrate
from db import db
from models import User, Project

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['UPLOAD_FOLDER'] = 'static/images/projects'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
