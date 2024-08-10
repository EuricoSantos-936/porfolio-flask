from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from db import db
from models import User
from routes import admin_dashboard, delete_project_image, index, admin, login, logout, add_project, edit_project, delete_project, download_cv
import os

app = Flask(__name__)
app.config.from_object('config')
@app.context_processor
def inject_env_vars():
    return dict(emailjs_public_key=os.getenv('EMAILJS_PUBLIC_KEY'))

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
app.add_url_rule('/download_cv','download_cv' , download_cv )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
