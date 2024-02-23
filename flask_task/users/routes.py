from flask import render_template, url_for, Flask, redirect, request, Blueprint

users = Blueprint('users', __name__)

@users.route("/display")
@users.route("/")
def display():
    
    data = [{
        'Hospital': "Flex",
        'Specialist' : "Cancer",
        'Type': "Goverment", 
        'Location': "Noida" 
        
    },
    {
        'Hospital': "Max",
        'Specialist' : "Heart Attack",
        'Type': "Private", 
        'Location': "Dehradun" 
    },
    {
        'Hospital': "AIIMS",
        'Specialist' : "Urologst",
        'Type': "Semi-Goverment", 
        'Location': "Delhi" 
    }
    ]

    return render_template('display.html', title='Display', data=data)