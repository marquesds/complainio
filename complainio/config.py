import logging
import os


class Config:
    DEBUG = False
    TESTING = False
    LOGS_LEVEL = logging.INFO

    MONGO_URI = os.getenv('MONGO_URI')


class Testing(Config):
    TESTING = True

    MONGO_URI = ''


class Development(Config):
    DEBUG = True
    LOGS_LEVEL = logging.DEBUG

    MONGO_URI = 'mongodb://localhost:27017/complainio'


class Production(Config):
    pass
