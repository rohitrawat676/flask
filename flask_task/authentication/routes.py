from flask import render_template, url_for, Flask, redirect, request, Blueprint, Response, jsonify
from functools import wraps


auth = Blueprint('auth', __name__)


def authenticate(username, password):
    return username == 'rohit676' and password == 'rohitrawat676'


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization

        if not auth or not authenticate(auth.username, auth.password):
            return jsonify({'message': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated


@auth.route('/login')
@requires_auth
def protected_route():
    return jsonify({'message': 'You have accessed the protected route'})
