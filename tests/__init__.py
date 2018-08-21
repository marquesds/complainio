import unittest

from complainio import create_app, logger


class BaseTestCase(unittest.TestCase):
    logger.disabled = True
    maxDiff = None

    def create_app(self):
        app = create_app('Testing')
        app.app_context().push()
        return app

    def setUp(self):
        """ Before each test, set up a blank database """
        self.app = self.create_app()
        self.client = self.app.test_client()
