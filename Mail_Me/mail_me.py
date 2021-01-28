#!/usr/bin/env python3
import emails
from health_checks import check_cpu
def get_user(): 
    "Gets data from user"   
    user=''
    password=''
    return user,password

if __name__ == '__main__':
    user,password = get_user()
    subject = 'System Warning'
    if check_cpu():
        body='Your systems cpu usage is going above 70%'
        message=emails.generate_mail(user,user,subject,body)
        emails.send_mail(message,user,password)



