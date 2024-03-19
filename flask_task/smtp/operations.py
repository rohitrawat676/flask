import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender_email, sender_password, receiver_email, subject, message):

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_name = 'Rohit Rawat'
    sender_email = sender_email
    sender_password = sender_password

    msg = MIMEMultipart()
    msg['From'] = f'{sender_name} <{sender_email}>'
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    try:

        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email, msg.as_string())
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
