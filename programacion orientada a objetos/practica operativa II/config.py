import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'database', 'datos.db')

SQLALCHEMY_DATABASE_URI = f'sqlite:///{database_path}'
SECRET_KEY = secrets.token_urlsafe(32)
SQLALCHEMY_TRACK_MODIFICATIONS = False
