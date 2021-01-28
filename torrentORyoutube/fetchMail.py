import imapclient,pyzmail,time,datetime

def fetchmail(username,imapobj):
    today=datetime.datetime.now().strftime('%d-%b-%Y')
    #imapobj=imapclient.IMAPClient('imap.gmail.com',ssl=True)
    #imapobj.login(username,password)
    #imapobj.select_folder('INBOX',readonly=False)
    while True:
        uids=imapobj.search(['SINCE',today,'FROM',username])
        if uids == []:
            time.sleep(5)                  #wait 60 seconds to check mail again
            continue
        rawmessage=imapobj.fetch([uids[0]],['BODY[]','FLAGS'])
        msg=pyzmail.PyzMessage.factory(rawmessage[uids[0]][b'BODY[]'])
        subject=msg.get_subject()
        body=msg.text_part.get_payload().decode(msg.text_part.charset)
        imapobj.delete_messages(uids[0])
       
        return subject,body