from flask import render_template, url_for, Flask, redirect, request, Blueprint, jsonify

health = Blueprint('health', __name__)

api_test1 = Blueprint('api_test1', __name__)


@health.route('/health', methods=['GET'])
def api_health():

    # success = {'success': {"data": "Success", "status": 200}}
    # failure = {'failure': {"error": "Error Occur", "status": 500}}

    try:
        result = {"data": "Sbi Bank", "status": 200}

        response = {'success': True, 'result': result}
        return jsonify(response), 200

    except Exception as e:

        return jsonify({'error': str(e)}), 500


@api_test1.route('/test1', methods=['POST'])
def api_test():

    try:
        request_data = request.get_json()
        print(request_data["collage"])
        return jsonify(request_data), 200

    except Exception as e:

        return jsonify({'error': str(e)}), 500
