import logging
import os

from flask import Flask

logger = logging.getLogger(__name__)


def create_app(environment=os.getenv('ENVIRONMENT', 'Development')):
    app = Flask(__name__)
    app.config.from_object(f'complainio.config.{environment}')

    from complainio.views.api_v1 import api_v1
    app.register_blueprint(api_v1)

    return app
