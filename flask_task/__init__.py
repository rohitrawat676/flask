from flask import Flask
from flask.config import Config
from flask_task.users.routes import users
from flask_task.api.routes import api


def create_app(config_class=Config):
    ''' This is a Create_app method in  __init__ file where we use app initialise & configure value & set blueprint & app_context etc '''

    app = Flask(__name__, template_folder='../templates')

    app.config.from_object(Config)

    app.register_blueprint(users, url_prefix="/data_display")
    app.register_blueprint(api, url_prefix="/api")

    app.app_context().push()

    return app
