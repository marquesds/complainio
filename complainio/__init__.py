import json
import logging
import os

from bson import ObjectId
from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()
logger = logging.getLogger(__name__)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def create_app(environment=os.getenv('ENVIRONMENT', 'Development')):
    app = Flask(__name__)
    app.config.from_object(f'complainio.config.{environment}')
    logger.setLevel(app.config['LOGS_LEVEL'])

    app.json_encoder = JSONEncoder

    if not environment == 'Testing':
        mongo.init_app(app)

    from complainio.views.api_v1 import api_v1
    app.register_blueprint(api_v1)

    return app
