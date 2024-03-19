import logging
from flask import render_template, url_for, Flask, redirect, request, Blueprint, jsonify
from flask_task.api.operations import api_health, api_test


api = Blueprint('api_test1', __name__)


@api.route('/health', methods=['GET'])
def apis_health():
    api_healths = api_health()
    return api_healths


@api.route('/test1', methods=['POST'])
def api_test1():
    apis_test1 = api_test()
    return apis_test1
