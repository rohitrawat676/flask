from os import environ as env
from dotenv import load_dotenv, dotenv_values


class BaseConfig:
    DEBUG = True
    TESTING = False


class DevelopmentConfig(BaseConfig):

    load_dotenv('dev.env')

    HOSTNAME = env.get('DEV_HOSTNAME')
    PORT = env.get('DEV_PORT')
    SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI_DEV')


class StageConfig(BaseConfig):

    load_dotenv('stage.env')

    HOSTNAME = env.get('STAGE_HOSTNAME')
    PORT = env.get('STAGE_PORT')
    SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI_STAGE')
