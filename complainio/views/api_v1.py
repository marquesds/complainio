from flask import Blueprint, request, jsonify

from complainio.dao import ComplainDAO
from complainio.schemas import ComplainSchema

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')


@api_v1.route('/health', methods=['GET'])
def healthcheck():
    return 'Everything is fine!'


@api_v1.route('/complains', methods=['POST'])
def save_complain():
    complain_dao = ComplainDAO()

    complain = ComplainSchema().load(request.get_json())
    if complain.errors:
        return jsonify({'errors': complain.errors}), 400
    else:
        complain_dao.save(complain=complain.data)
        return jsonify({}), 201
