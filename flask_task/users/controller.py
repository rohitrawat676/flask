from flask import render_template, url_for, Flask, redirect, request, Blueprint
from flask_task.users.operations import display

# Setting blueprint for json data display as tabular form
users = Blueprint('users', __name__)


# Defining route for display json data as tabular form
@users.route("/display")
@users.route("/")
def table_display():
    disp = display()
    return disp
