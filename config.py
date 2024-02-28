import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEYL')
    DATABASE_URI = os.environ.get('DATABASE_URIL')


