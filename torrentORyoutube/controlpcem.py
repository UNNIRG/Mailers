'''mail a youtube link computer will automatically play it'''
import fetchMail,playyt
#import mailMe
import sys,subprocess,imapclient
import time,datetime
username=''
password=''
secret_key='secret_code'
#mailMe.mailme(username,password)
delay=datetime.timedelta(minutes=15)
imapobj=imapclient.IMAPClient('imap.gmail.com',ssl=True)
imapobj.login(username,password)
imapobj.select_folder('INBOX',readonly=True)
while True:
    try:
        subject,body=fetchMail.fetchmail(username,imapobj) #body contains the url
        if subject!=secret_key:
            print('secret key does not match')
            sys.exit()
        playyt.playyt(url=body)
        #subprocess.Popen(['qbittorrent',body])
        #subprocess.run(['killall', '-s', 'SIGSTOP', 'qbittorrent']) 
        imapobj.logout()
    except Exception as e:
        print(e)
    #time.sleep(delay.total_seconds())
    break





