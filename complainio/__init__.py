import logging
import os

from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()
logger = logging.getLogger(__name__)


def create_app(environment=os.getenv('ENVIRONMENT', 'Development')):
    app = Flask(__name__)
    app.config.from_object(f'complainio.config.{environment}')

    if not environment == 'Testing':
        mongo.init_app(app)

    from complainio.views.api_v1 import api_v1
    app.register_blueprint(api_v1)

    return app
