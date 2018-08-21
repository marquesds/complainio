import logging


class Config:
    DEBUG = False
    TESTING = False
    LOGS_LEVEL = logging.INFO


class Testing(Config):
    TESTING = True


class Development(Config):
    DEBUG = True
    LOGS_LEVEL = logging.DEBUG


class Production(Config):
    pass
