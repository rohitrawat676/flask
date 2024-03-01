from os import environ as env
from dotenv import load_dotenv, dotenv_values


class Config:
    
    ''' this is a Config class which access enviroment variable from dev.env & stage.env file '''

    config = {
        **dotenv_values("dev.env"),
        **dotenv_values("stage.env"),
    }

    DEV_HOSTNAME = config['DEV_HOSTNAME']
    DEV_PORT = config['DEV_PORT']
    STAGE_HOSTNAME = config['STAGE_HOSTNAME']
    STAGE_PORT = config['STAGE_PORT']


print(Config.__doc__)