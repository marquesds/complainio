from flask import Blueprint, request, jsonify

from complainio.dao import ComplainDAO
from complainio.decorators import requires_api_key
from complainio.schemas import ComplainSchema, LocaleSchema

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')


@api_v1.route('/health', methods=['GET'])
def healthcheck():
    return 'Everything is fine!'


@api_v1.route('/complains', methods=['POST'])
@requires_api_key
def save_complain():
    complain = ComplainSchema().load(request.get_json())
    if complain.errors:
        return jsonify({'errors': complain.errors}), 400
    else:
        complain_dao = ComplainDAO()
        complain_id = complain_dao.save(complain=complain.data)
        return jsonify({'id': complain_id}), 201


@api_v1.route('/complains/<complain_id>', methods=['GET'])
@requires_api_key
def get_complain_by_id(complain_id):
    complain_dao = ComplainDAO()
    complain = complain_dao.get(complain_id)
    if not complain:
        return jsonify({}), 404
    else:
        return jsonify(complain), 200


@api_v1.route('/complains', methods=['GET'])
@requires_api_key
def get_all_complains():
    complain_dao = ComplainDAO()
    complains = complain_dao.all()
    if not complains:
        return jsonify({}), 404
    else:
        return jsonify(complains), 200


@api_v1.route('/complains/<complain_id>', methods=['PUT'])
@requires_api_key
def update_complain_document_by_id(complain_id):
    complain = ComplainSchema().load(request.get_json())
    if complain.errors:
        return jsonify({'errors': complain.errors}), 400
    else:
        complain_dao = ComplainDAO()
        complain_dao.update(complain_id, complain.data)
        return jsonify({}), 200


@api_v1.route('/complains/<complain_id>', methods=['DELETE'])
@requires_api_key
def delete_complain_by_id(complain_id):
    complain_dao = ComplainDAO()
    complain_dao.delete(complain_id)
    return jsonify({}), 204


@api_v1.route('/complains/count', methods=['GET'])
@requires_api_key
def get_all_complain_count_by_locale():
    complain_dao = ComplainDAO()
    grouped_complains = complain_dao.get_complain_count_per_locale()
    return jsonify(grouped_complains), 200


@api_v1.route('/complains/count', methods=['POST'])
@requires_api_key
def get_complain_count_by_locale():
    locale = LocaleSchema().load(request.get_json())
    if locale.errors:
        return jsonify({'errors': locale.errors}), 400
    else:
        complain_dao = ComplainDAO()
        complain = complain_dao.get_specific_complain_count_by_locale(locale.data)
        if complain:
            return jsonify(complain), 200
        else:
            return jsonify({}), 404
