import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging


def send_email(sender_email: str, sender_password: str,
               receiver_email: str, subject: str,
               message: str) -> str:
    '''
    SMTP send email
    @param sender_email: str
    @param sender_password: str
    @param receiver_email: str
    @param subject: str
    @param message: str
    returns str

    '''
    # Logger info set for sending smtp email
    logging.info("SMTP Email Send")

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_name = 'Rohit Rawat'
    sender_email = sender_email
    sender_password = sender_password

    msg = MIMEMultipart()
    msg['From'] = f'{sender_name} <{sender_email}>'
    msg['To'] = ','.join([receiver_email])
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    try:

        server.login(sender_email, sender_password)

        server.sendmail(sender_email, msg['To'].split(','), msg.as_string())
        print('Email sent successfully!')
        return "Email sent successfully!"
    except smtplib.SMTPAuthenticationError:
        return "SMTP authentication error: Please check your email and password."
    except smtplib.SMTPException as e:
        return f"SMTP error occurred: {e}"
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        server.quit()
