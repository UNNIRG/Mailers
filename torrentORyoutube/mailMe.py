import smtplib
from email.message import EmailMessage
def mailme(username,password):
    mserver=smtplib.SMTP('smtp.gmail.com',587)
    mserver.ehlo()
    mserver.starttls()
    mserver.login(username,password)

    message = EmailMessage()
    message['From'] = username
    message['To'] = username
    message['Subject'] = 'Noice'
    body=''
    message.set_content(body)
    mserver.send_message(message)
    mserver.quit()

