'''mail a youtube link computer will automatically play it'''
import imaplib
import fetchmail,sendMail,imagemanip
import time
username=''
password=''
delay=60*15
imabobj = imaplib.IMAP4_SSL('imap.gmail.com')
imabobj.login(username,password)
while True:
    fetchmail.fetchmail(username,imabobj)
    imagemanip.imagemanip()
    sendMail.mailme(username,password)
    print('everything done')
    time.sleep(delay)



