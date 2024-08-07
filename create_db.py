from main import app
from db import db
from models import User
import os

with app.app_context():
    db.create_all()
    
    # Add an admin user
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin')
        admin.set_password(os.getenv("ADMIN_PASSWORD"))
        db.session.add(admin)
        db.session.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")
