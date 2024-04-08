import jwt
import logging
from flask import render_template, url_for, Flask, redirect, request, Blueprint, Response, jsonify
from flask import current_app


def get_token():
    '''Get Token Function for auth'''

    logging.info('Get Token Function for auth')

    username = request.json.get('username')
    password = request.json.get('password')

    if not (username == 'rohit676' and password == 'rohitrawat676'):
        return jsonify({'message': 'Authentication failed'}), 401

    token = jwt.encode({'username': username},
                       current_app.config['SECRET_KEY'], algorithm='HS256')

    # Return the token in the response
    return jsonify({'token': token})
