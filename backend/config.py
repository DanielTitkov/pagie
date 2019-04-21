import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    PROPAGATE_EXCEPTIONS = True

    MONGO_URI = os.environ.get('DATABASE_URL') or 'mongodb://localhost:27017/pagie'

    JWT_ACCESS_TOKEN_EXPIRES = 86400

    REQUIRE_INVITE = True
    CALENDAR_DAYS = 30
