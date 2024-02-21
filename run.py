from flask_task import create_app
from flask_task.users.routes import users

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
