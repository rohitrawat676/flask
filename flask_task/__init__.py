from flask import Flask
from flask_task.users.routes import users


def create_app():
    
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
   
    app.app_context().push()
    
    from flask_task import users
    
    app.register_blueprint(users, url_prefix="/data_display")

    return app
