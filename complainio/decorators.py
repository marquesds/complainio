from functools import wraps

from flask import request, g, current_app
from itsdangerous import BadSignature
from werkzeug.exceptions import Unauthorized


def requires_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth:
            raise Unauthorized('API key required')

        auth = auth.split()
        auth_params = dict([a.strip(',').split('=', 1) for a in auth])

        apikey = auth_params.get('apikey', '').strip('"')
        if not apikey:
            raise Unauthorized('API key required')

        try:
            profile = current_app.signer.unsign(apikey)
        except BadSignature:
            raise Unauthorized('Invalid API key')

        g.profile = profile
        g.apikey = apikey

        return f(*args, **kwargs)

    return decorated
