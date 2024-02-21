from flask import render_template, url_for, flash, redirect, request, Blueprint

users = Blueprint('users', __name__)

@users.route("/login")
def display():
    
    data = {
        'Hospital': "Flex",
        'Specialist' : "Cancer",
        'type': "Goverment"  
    }

    return render_template('display.html', title='Display', data=data)