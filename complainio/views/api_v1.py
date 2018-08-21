from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')


@api_v1.route('/health', methods=['GET'])
def healthcheck():
    return 'Everything is fine!'
