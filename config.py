import os
import secrets

DEBUG = True
SECRET_KEY = secrets.token_hex(15)
CSRF_ENABLED     = True
CSRF_SESSION_KEY = secrets.token_hex(15)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
DATABASE_CONNECT_OPTIONS = {}
