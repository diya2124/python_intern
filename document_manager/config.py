import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    ALLOWED_EXTENSIONS = {'pdf', 'md'}
    DATABASE_PATH = os.path.join(BASE_DIR, 'instance', 'documents.db')
    SECRET_KEY = 'your-secret-key'
