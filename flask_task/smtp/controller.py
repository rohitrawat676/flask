import logging
from distutils import config
from flask import render_template, url_for, redirect, request, Blueprint, Response, jsonify
from flask_task.smtp.operations import send_email
from config import BaseConfig
import logging

smtpmail = Blueprint('smtpmail', __name__)


@smtpmail.route('/mail', methods=['GET', 'POST'])
def stmp_send():
    ''' SMTP Post Email Send '''

    if request.method == 'POST':

        sender_email = BaseConfig.SENDER_EMAIL
        sender_password = BaseConfig.SENDER_PASSWORD
        receiver_email = BaseConfig.RECEIVER_EMAIL
        subject = 'Test Email'
        message = 'This is a test email sent from Python.'

        mail = send_email(sender_email, sender_password,
                          receiver_email, subject, message)
        return mail

    return render_template('smtpmail.html')
