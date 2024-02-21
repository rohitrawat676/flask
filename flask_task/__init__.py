from flask import Flask
from flask_task.users.routes import users

def create_app():
    
    app = Flask(__name__)
    
    from flask_task import users
    
    app.register_blueprint(users, url_prefix="/data_display")

    return app
