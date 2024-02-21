from flask import Flask

login_view = 'users.login'
login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    
    from flask import users
    app.register_blueprint(users)

    return app
