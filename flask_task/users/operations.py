import logging
from flask import Blueprint, render_template


def display():
    '''Display JSON Data as Table'''

    # Looger info set for display json data
    logging.info('Display JSON Data')

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
