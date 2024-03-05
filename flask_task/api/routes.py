from flask import render_template, url_for, Flask, redirect, request, Blueprint, jsonify

api = Blueprint('api', __name__)


@api.route('/test1', methods=['GET'])
def api_endpoint():

    success = {'success' : {"data": "Success", "status": 200}}
    failure = {'failure' : {"error": "Error Occur", "status": 500}}

    return jsonify(success)
