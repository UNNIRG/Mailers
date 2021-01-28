#!/usr/bin/env python3
from email.message import EmailMessage
import smtplib
def generate_mail(sender,reciepirnt,subject,body):
    """Generates the email to be sent"""
    message = EmailMessage()
    message['From'] = sender
    message['To'] = reciepirnt
    message['Subject'] = subject
    message.set_content(body)
    return message
def send_mail(message,user,password):
    """Sends the generated mail"""
    try:
        mail_server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        mail_server.ehlo()
        mail_server.login(user=user,password=password)
        mail_server.send_message(message)
        mail_server.quit()
    except Exception as e:
        print(e)