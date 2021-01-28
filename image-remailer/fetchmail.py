from email.header import decode_header
import imaplib,email,time,datetime
def fetchmail(username,imabobj):
    date=datetime.datetime.now().strftime('%d-%b-%Y')
    imabobj.select('inbox',readonly=True)
    while True:
        _, uids = imabobj.search(None, 'SINCE', date , 'FROM' ,username )
        if uids==[]:
            time.sleep(10)
            continue
        _, data = imabobj.fetch(uids[0], "(RFC822)")
        body=data[0][1]
        mail = email.message_from_bytes(body)
        print(decode_header(mail["Subject"])[0][0])
        for part in mail.walk():
            if part.get_content_maintype()=='image' and part.get('Content-Disposition') is not None:
                open(part.get_filename(), 'wb').write(part.get_payload(decode=True))
        imabobj.store(uids[0], "+FLAGS", "\\Deleted")
        imabobj.close()
        imabobj.logout()
