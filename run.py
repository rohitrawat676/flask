import sys
import os
from dotenv import load_dotenv, dotenv_values
from os import environ
from flask_task import create_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_task.utilities.logger import logger_log
from flask_task.models import User, db

app = create_app()

logger_log()


def run_flask():
    ''' This is a flask enviroment selection method of enviroment variable from dev.env & stage.env file '''

    hostname = app.config['HOSTNAME']
    env_port = app.config['PORT']
    db = SQLAlchemy(app)

    db.create_all()

    app.run(debug=True, host=hostname, port=env_port)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        if sys.argv[1] == 'dev.env':
            app.config.from_object('config.DevelopmentConfig')
            run_flask()
        elif sys.argv[1] == 'stage.env':
            app.config.from_object('config.StageConfig')
            run_flask()
        else:
            print("Please specify environment. Usage: python run.py <environment>")
    else:
        print("Please specify environment. Usage: python run.py <environment>")
