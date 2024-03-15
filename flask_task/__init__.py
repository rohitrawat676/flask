import sys
from flask import Flask
from flask_task.users.controller import users
from flask_task.api.controller import api
from flask_task.authentication.controller import auth
from flask_sqlalchemy import SQLAlchemy


def create_app():
    ''' This is a Create_app method in  __init__ file where we use app initialise & configure value & set blueprint & app_context etc '''

    app = Flask(__name__, template_folder='../templates')

    app.register_blueprint(users, url_prefix="/data_display")
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(auth, url_prefix="/auth")

    app.app_context().push()

    return app
