from flask import render_template, url_for, Flask, redirect, request, Blueprint, jsonify


api = Blueprint('api_test1', __name__)


@api.route('/health', methods=['GET'])
def api_health():

    try:
        result = {"data": "Sbi Bank", "status": 200}

        response = {'success': True, 'result': result}
        return jsonify(response), 200

    except Exception as e:

        return jsonify({'error': str(e)}), 500


@api.route('/test1', methods=['POST'])
def api_test():

    try:
        request_data = request.get_json()
        print(request_data["collage"])
        return jsonify(request_data), 200

    except Exception as e:

        return jsonify({'error': str(e)}), 500
