import jwt
from flask import render_template, url_for, Flask, redirect, request, Blueprint, Response, jsonify
from functools import wraps
from flask import current_app
from flask_task.authentication.operations import get_token

# Initializing blueprint for api
auth = Blueprint('auth', __name__)

# Defining route for get token
@auth.route('/get_token', methods=['POST'])
def data_token():
    token = get_token()
    return token
