import logging
from flask import render_template, url_for, Flask, redirect, request, Blueprint, jsonify
from flask_task.models import db, ApiPost


def api_health():
    ''' This Is Get Api '''

    # Logger info set for get api
    logging.info("This Is Get Api")
    try:
        result = {"data": "Sbi Bank", "status": 200}

        response = {'success': True, 'result': result}
        return jsonify(response), 200

    except Exception as e:
        logging.exception(
            "Exception occurred during a get health api request.")
        return jsonify({'error': str(e)}), 500


def api_test():
    ''' This Is Post Api '''

    # Logger info set for post api
    logging.info("This Is Get Api")
    try:
        request_data = request.get_json()
        print(request_data["collage"])
        return jsonify(request_data), 200

    except Exception as e:
        logging.exception("Exception occurred during a Post api request.")
        return jsonify({'error': str(e)}), 500