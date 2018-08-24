#!/usr/bin/env python
from flask_script import Manager
from itsdangerous import TimestampSigner

from complainio import create_app

manager = Manager(create_app)


@manager.option('-u', dest='user', help='User name')
def generate_api_key(user):
    secret_key = manager.app.config['SECRET_KEY']

    signer = TimestampSigner(secret_key)
    print(f'apikey="{signer.sign(user).decode()}"')


if __name__ == '__main__':
    manager.run()
