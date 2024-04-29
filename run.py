import sys
from os import environ
from flask_task import create_app
from flask_task.utilities.logger import logger_log
from flask_task.models import db
from config import dev, stage

app = create_app()

logger_log()


def run_flask():
    ''' This is a flask enviroment selection method of enviroment variable from dev.env & stage.env file '''

    hostname = app.config['HOSTNAME']
    env_port = app.config['PORT']

    db.init_app(app)

    app.run(debug=True, host=hostname, port=env_port)


if __name__ == '__main__':

    if len(sys.argv) > 1:

        enviroment = ['alpha', 'dev', 'stage', 'prod']
        flag = ""
        for item in enviroment:
            if sys.argv[1].lower() == item.lower():
                env = globals()[sys.argv[1]]
                app.config.from_object(env)
                run_flask()
                break
            else:
                flag = 1
        if flag == 1:
            print("Please specify environment. Usage: python run.py <environment>")

    else:
        print("Please specify environment. Usage: python run.py <environment>")
