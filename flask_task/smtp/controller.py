from flask import render_template, url_for, redirect, request, Blueprint, Response, jsonify
from flask_task.smtp.operations import send_email

smtpmail = Blueprint('smtpmail', __name__)


@smtpmail.route('/mail', methods=['GET', 'POST'])
def stmp_send():

    if request.method == 'POST':

        sender_email = 'rohitrawat676@gmail.com'
        sender_password = 'ozggoacowdpjtbeu'
        receiver_email = 'rohitrawat8126844298@gmail.com'
        subject = 'Test Email'
        message = 'This is a test email sent from Python.'

        mail = send_email(sender_email, sender_password,
                          receiver_email, subject, message)
        return mail

    return render_template('smtpmail.html')
