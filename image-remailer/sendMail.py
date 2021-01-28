import smtplib,mimetypes,os
from email.message import EmailMessage
def mailme(username,password):
    logo='catlogo.png'
    mserver=smtplib.SMTP('smtp.gmail.com',587)
    mserver.ehlo()
    mserver.starttls()
    mserver.login(username,password)
    message = EmailMessage()
    message['From'] = username
    message['To'] = username
    message['Subject'] = 'All images are ready'
    image_list=os.listdir()
    for img in image_list:
            if not(img.endswith('.png') or img.endswith('.jpg')) or img==logo:
                continue    
            mimetype,_=mimetypes.guess_type(img)
            main,sub=mimetype.split('/',1)
            with open(img,'rb') as im:
                message.add_attachment(im.read(),
                maintype=main,
                subtype=sub,
                filename=img
                )
            os.remove(img)
    mserver.send_message(message)
    mserver.quit()
