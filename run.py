import sys
import os
from dotenv import load_dotenv, dotenv_values
from flask_task import create_app


app = create_app()


def run_flask(env):
    ''' This is a flask enviroment selection method of enviroment variable from dev.env & stage.env file '''

    load_dotenv(env)

    app.run(debug=True, host=os.environ.get(
        'HOSTNAME'), port=os.environ.get('PORT'))


if __name__ == '__main__':

    if len(sys.argv) > 1:
        environment = sys.argv[1]
        run_flask(environment)
    else:
        print("Please specify environment. Usage: python run.py <environment>")
