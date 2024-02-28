from flask import Flask
from flask.config import Config
from flask_task import users
from flask_task.users.routes import users


def create_app(config_class=Config):
    
    app = Flask(__name__)

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    
    app.config.from_object(Config)
    
    app.register_blueprint(users, url_prefix="/data_display")
    
    app.app_context().push()
    
    return app

