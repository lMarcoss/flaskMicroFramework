import os


class Config(object):
    SECRET_KEY = 'my_secret_key'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskuser:password@localhost:3312/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class IntegrationConfig(Config):
    DEBUG = True
