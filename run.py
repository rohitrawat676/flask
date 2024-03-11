import sys
import os
from dotenv import load_dotenv, dotenv_values
from flask_task import create_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = create_app()

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)


db.create_all()

# new_user = User(username='rohitrawat676', email='rohitrawat676@gmail.com')
# db.session.add(new_user)
# db.session.commit()

# users = User.query.all()
# for user in users:
#     print(user.username, user.email)

# user = User.query.filter_by(username='rohitrawat676').first()
# user.email = 'rohitrawat2089@example.com'
# db.session.commit()

# user = User.query.filter_by(username='rohitrawat676').first()
# db.session.delete(user)
# db.session.commit()


def run_flask(env):
    ''' This is a flask enviroment selection method of enviroment variable from dev.env & stage.env file '''

    if env == 'dev.env' or env == 'stage.env':
        load_dotenv(env)
        app.run(debug=True, host=os.environ.get(
            'HOSTNAME'), port=os.environ.get('PORT'))
    else:
        print("Please specify environment. Usage: python run.py <environment> like dev.env or stage.env")


if __name__ == '__main__':

    if len(sys.argv) > 1:
        environment = sys.argv[1]
        run_flask(environment)
    else:
        print("Please specify environment. Usage: python run.py <environment>")
