from flask import render_template, url_for, redirect, request, Blueprint, Response, jsonify
from flask_task.database.operations import create_user, get_user_by_username

db = Blueprint('db', __name__)


@db.route('/query')
def data_get():
    token = create_user()
    return token
