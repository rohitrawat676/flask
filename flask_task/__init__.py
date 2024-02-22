from flask import Flask
from flask_task.users.routes import users
from flask.config import Config
import os

def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config.from_object(Config)
    
    app.app_context().push()
    
    from flask_task import users
    
    app.register_blueprint(users, url_prefix="/data_display")

    return app
