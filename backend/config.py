import os

def form_connection_string(driver, user, password, host, database):
    if user and password:
        return '{driver}://{user}:{password}@{host}/{database}'.format(
            driver=driver,
            user=user,
            password=password,
            host=host,
            database=database
        )
    return '{driver}://{host}/{database}'.format(
        driver=driver,
        host=host,
        database=database
    )


class Config(object):
    # app config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    PROPAGATE_EXCEPTIONS = True
    JWT_ACCESS_TOKEN_EXPIRES = 86400

    # UX features
    REQUIRE_INVITE = True
    CALENDAR_DAYS = 30

    # database
    DB_DRIVER = os.environ.get('DB_DRIVER') or 'mongodb'
    DB_HOST = os.environ.get('DB_HOST') or 'mongo:27017'
    DB_NAME = os.environ.get('DB_NAME') or 'pagie'
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    MONGO_URI = form_connection_string(
        driver=DB_DRIVER,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME
    )
