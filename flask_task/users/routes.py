from flask import render_template, url_for, flash, redirect, request, Blueprint

users = Blueprint('users', __name__)

@users.route("/display")

def display():
    
    data = {
        'Hospital': "Flex",
        'Specialist' : "Cancer",
        'type': "Goverment"  
    }
    
    record = "recards"

    return render_template('display.html', title='Display', data=data, record = record)