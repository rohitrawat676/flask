from flask import Blueprint, render_template


def display():

    data = [{
        'Hospital': "Flex",
        'Specialist': "Cancer",
        'Type': "Goverment",
        'Location': "Noida"
    },
        {
        'Hospital': "Max",
        'Specialist': "Heart Attack",
        'Type': "Private",
        'Location': "Dehradun"
    },
        {
        'Hospital': "AIIMS",
        'Specialist': "Urologst",
        'Type': "Semi-Goverment",
        'Location': "Delhi"
    }
    ]

    return render_template('display.html', title='Display', data=data)
