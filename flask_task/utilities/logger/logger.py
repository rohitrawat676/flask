import logging
from logging.handlers import RotatingFileHandler

# Logger Initializing
logger = logging.getLogger()


def logger_log():
    '''looger set up for tracking action or auditing'''
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('flask_task/utilities/logger/app.txt')
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
