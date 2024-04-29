from flask import render_template, url_for, redirect, request, Blueprint, Response, jsonify
from flask_task.database.operations import create_user, get_user_by_username, data_save

# Initializing blueprint for api
db = Blueprint('db', __name__)

# Defining route for get token


@db.route('/query')
def data_get():
    token = create_user()
    return token


@db.route('/postapi', methods=['GET', 'POST'])
def data_saver():
    datasave = data_save()
    return datasave
