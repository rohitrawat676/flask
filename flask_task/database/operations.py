import json
import logging
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_task.models import User
from flask_task.models import db


user_data = []


def create_user():
    '''Database Create User'''

    logging.info('Database Create User')

    db.create_all()

    new_user = User(username='rohitrawat676', email='rohitrawat676@gmail.com')
    db.session.add(new_user)
    db.session.commit()

    users = User.query.all()

    for user in users:
        user_data.append(
            {'id': user.id, 'username': user.username, 'email': user.email})

    json_data = json.dumps(user_data, indent=4)

    return json_data


def get_user_by_username():
    '''Filter Username User'''

    logging.info('Filter Username User')

    users = User.query.filter_by(username='rohitrawat676').first()
    for user in users:
        user_data.append(
            {'id': user.id, 'username': user.username, 'email': user.email})

    json_data = json.dumps(user_data, indent=4)

    return json_data
