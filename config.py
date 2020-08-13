import os


class Config(object):
    SECRET_KEY = 'my_secret_key'


class DevelopmentConfig(Config):
    DEBUG = True


class IntegrationConfig(Config):
    DEBUG = True
