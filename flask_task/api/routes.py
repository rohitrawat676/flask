import logging
from flask import render_template, url_for, Flask, redirect, request, Blueprint, jsonify


api = Blueprint('api_test1', __name__)

@api.route('/health', methods=['GET'])
def api_health():
    logging.info("This Is Get Api")
    try:
        result = {"data": "Sbi Bank", "status": 200}

        response = {'success': True, 'result': result}
        return jsonify(response), 200

    except Exception as e:
        logging.exception("Exception occurred during a get health api request.")
        return jsonify({'error': str(e)}), 500


@api.route('/test1', methods=['POST'])
def api_test():
    logging.info("This Is Get Api")
    try:
        request_data = request.get_json()
        print(request_data["collage"])
        return jsonify(request_data), 200

    except Exception as e:
        logging.exception("Exception occurred during a Post api request.")
        return jsonify({'error': str(e)}), 500
