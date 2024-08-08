from dotenv import load_dotenv
import os
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
UPLOAD_FOLDER = 'static/images/projects'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024 
SQLALCHEMY_TRACK_MODIFICATIONS = False