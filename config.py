import os
from os import environ as env
from dotenv import load_dotenv, dotenv_values


class Config:

    ''' This is a Config class which access enviroment variable from dev.env & stage.env file '''

    config = {
        **dotenv_values("dev.env"),
        **dotenv_values("stage.env"),
    }

    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URI = os.environ.get('DATABASE_URI')
    DEV_HOSTNAME = config['DEV_HOSTNAME']
    DEV_PORT = config['DEV_PORT']
    STAGE_HOSTNAME = config['STAGE_HOSTNAME']
    STAGE_PORT = config['STAGE_PORT']
