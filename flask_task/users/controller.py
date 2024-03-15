from flask import render_template, url_for, Flask, redirect, request, Blueprint
from flask_task.users.operations import display
users = Blueprint('users', __name__)


@users.route("/display")
@users.route("/")
def table_display():
    disp = display()
    return disp
