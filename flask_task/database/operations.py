import json
import logging
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_task.models import User
from flask_task.models import db, ApiPost


user_data = []


def create_user():
    '''Database Create User'''

    # Logger info set for creation database
    logging.info('Database Create User')

    db.create_all()

    # Creating new user
    new_user = User(username='rohitrawat676', email='rohitrawat676@gmail.com')
    db.session.add(new_user)
    db.session.commit()

    # Fetching all user
    users = User.query.all()

    for user in users:
        user_data.append(
            {'id': user.id, 'username': user.username, 'email': user.email})

    json_data = json.dumps(user_data, indent=4)

    return json_data


def get_user_by_username():
    '''Filter Username User'''

    # Logger info set for filter username
    logging.info('Filter Username User')

    users = User.query.filter_by(username='rohitrawat676').first()
    for user in users:
        user_data.append(
            {'id': user.id, 'username': user.username, 'email': user.email})

    json_data = json.dumps(user_data, indent=4)

    return json_data


def data_save():
    '''Database Create User'''

    db.create_all()

    # Post api info save database
    logging.info('Database Create User')

    data = request.json
    id = data.get('id')
    username = data.get('username')
    email = data.get('email')

    if username and email:
        new_post = ApiPost(id=id, username=username, email=email)
        db.session.add(new_post)
        db.session.commit()
        return 'Post created successfully', 201
    else:
        return 'Missing title or content', 400
