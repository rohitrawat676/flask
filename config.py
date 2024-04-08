from os import environ as env
from dotenv import load_dotenv, dotenv_values


class BaseConfig:

    def __init__(self, env):
        self.env = env

    if (env == 'dev.env'):
        load_dotenv('dev.env')
    else:
        load_dotenv('stage.env')

    DEBUG = True
    TESTING = False

    HOSTNAME = env.get('HOSTNAME')
    PORT = env.get('PORT')
    SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI')

    MYSQL_HOST = env.get('MYSQL_HOST')
    MYSQL_USER = env.get('MYSQL_USER')
    MYSQL_PASSWORD = env.get('MYSQL_PASSWORD')

    MYSQL_DB = env.get('MYSQL_DB')

    SENDER_PASSWORD = env.get('SENDER_PASSWORD')
    SENDER_EMAIL = env.get('SENDER_EMAIL')
    RECEIVER_EMAIL = env.get('RECEIVER_EMAIL')
