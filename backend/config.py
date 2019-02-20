import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'

    MONGO_URI = os.environ.get('DATABASE_URL') or 'mongodb://localhost:27017/pagie'

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    SERVER_NAME = "127.0.0.1:5000"

    JWT_ACCESS_TOKEN_EXPIRES = 3600
