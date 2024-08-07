from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from db import db
from models import User, Project
from routes import admin_dashboard, delete_project_image, index, admin, login, logout, add_project, edit_project, delete_project

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['UPLOAD_FOLDER'] = 'static/images/projects'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.add_url_rule('/', 'index', index)
app.add_url_rule('/admin', 'admin', admin)
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout)
app.add_url_rule('/admin_dashboard', 'admin_dashboard', admin_dashboard)
app.add_url_rule('/add_project', 'add_project', add_project, methods=['GET', 'POST'])
app.add_url_rule('/edit_project/<int:project_id>', 'edit_project', edit_project, methods=['GET', 'POST'])
app.add_url_rule('/delete_project/<int:project_id>', 'delete_project', delete_project, methods=['POST'])
app.add_url_rule('/delete_project_image/<int:project_id>', 'delete_project_image', delete_project_image)

if __name__ == '__main__':
    app.run(debug=True)