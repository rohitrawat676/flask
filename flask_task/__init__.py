from flask_task import Flask

# login_view = 'users.login'

def create_app():
    app = Flask(__name__)
    
    from flask_task import users
    
    app.register_blueprint(users)

    return app
