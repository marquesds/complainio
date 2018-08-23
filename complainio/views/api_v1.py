from flask import Blueprint, request, jsonify

from complainio.dao import ComplainDAO
from complainio.schemas import ComplainSchema

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')


@api_v1.route('/health', methods=['GET'])
def healthcheck():
    return 'Everything is fine!'


@api_v1.route('/complains', methods=['POST'])
def save_complain():
    complain = ComplainSchema().load(request.get_json())
    if complain.errors:
        return jsonify({'errors': complain.errors}), 400
    else:
        complain_dao = ComplainDAO()
        complain_id = complain_dao.save(complain=complain.data)
        return jsonify({'id': complain_id}), 201


@api_v1.route('/complains/<complain_id>', methods=['GET'])
def get_complain_by_id(complain_id):
    complain_dao = ComplainDAO()
    complain = complain_dao.get(complain_id)
    if not complain:
        return jsonify({}), 404
    else:
        return jsonify(complain), 200


@api_v1.route('/complains', methods=['GET'])
def get_all_complains():
    complain_dao = ComplainDAO()
    complains = complain_dao.all()
    if not complains:
        return jsonify({}), 404
    else:
        return jsonify(complains), 200
