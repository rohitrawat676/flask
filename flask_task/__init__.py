import logging
import sys
from flask import Flask
from flask.config import Config
from flask_task.users.routes import users
from flask_task.api.routes import api
from flask_task.authentication.routes import auth
from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import SQLAlchemy


def create_app(config_class=Config):
    ''' This is a Create_app method in  __init__ file where we use app initialise & configure value & set blueprint & app_context etc '''

    app = Flask(__name__, template_folder='../templates')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('flask_task/utilities/logger/logger.py')
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    app.config.from_object(Config)

    app.register_blueprint(users, url_prefix="/data_display")
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(auth, url_prefix="/auth")

    app.app_context().push()

    return app
