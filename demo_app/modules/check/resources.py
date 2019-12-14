import logging
from flask import Blueprint, jsonify, make_response, request
from demo_app.helpers.requestid import requestid
from demo_app.extensions.unleash import UNLEASH

check_blueprint = Blueprint('status', __name__, url_prefix='/check')  # pylint: disable=C0103


FLAG_BANE = 'ivantest'


@requestid
@check_blueprint.route('', methods=['GET'])
def check():
    context = {
        'userId': request.args.get('userId')
    }

    flag_value = UNLEASH.client.is_enabled(FLAG_BANE, context)
    logging.debug(f"Got feature flag value of: {flag_value}")

    return make_response(jsonify(f'Hello, World! Your feature flag is: {flag_value}'), 200)
