import sys
from flask_task import create_app
# from flask_sqlalchemy import SQLAlchemy

app = create_app()

# db = SQLAlchemy(app)


def run_flask(env):
    
    ''' This is a flask enviroment selection method of enviroment variable from dev.env & stage.env file '''
    
    if env == 'stage':
        app.config['DEBUG'] = True
        app.run(host=app.config.get('STAGE_HOSTNAME'),
                port=app.config.get('STAGE_PORT'))
    elif env == 'development':
        app.config['DEBUG'] = False
        app.run(host=app.config.get('DEV_HOSTNAME'),
                port=app.config.get('DEV_PORT'))
    else:
        print("Invalid environment. Please use 'development' or 'production'.")
        return

print(run_flask.__doc__)

if __name__ == '__main__':

    # db.init_app(app)

    # enviroment = input("Enter the enviroment: ")

    # if enviroment == "stage":
    #     app.run(host=app.config.get('STAGE_HOSTNAME'),
    #             port=app.config.get('STAGE_PORT'))
    # elif enviroment == "dev":
    #     app.run(host=app.config.get('DEV_HOSTNAME'),
    #             port=app.config.get('DEV_PORT'))
    # else:
    #  app.run(debug=True)

    if len(sys.argv) > 1:
        environment = sys.argv[1]
        run_flask(environment)
    else:
        print("Please specify environment. Usage: python run.py <environment>")
