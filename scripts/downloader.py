import smtplib
import time
import imaplib
import email

YOUR_EMAIL      = "lebeau.florian.13@gmail.com"
YOUR_PASSWORD   = "nairolfuaebel"
SMTP_SERVER     = "imap.gmail.com"
SMTP_PORT       = 993
EMAIL_SUBJECT   = "test"
HOST_SERVERS    = ['uptobox', '1fichier', 'dl.free.fr', 'mega.nz']


def extract_body(msg):
    if msg.is_multipart():
        body = extract_body(msg.get_payload(0)) # extract body message
        body = body.decode("utf-8") # convert Bytes to string
        body = body.split("\r\n") # split body string in list
        body = list(filter(None, body)) # remove empty values from list
        return(body)
    else:
        return msg.get_payload(None, True)

def fct_readmail():
    ### Gmail connection
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(YOUR_EMAIL, YOUR_PASSWORD)
    mail.select('inbox')

    type, data = mail.search(None,'(UNSEEN SUBJECT "%s")' % EMAIL_SUBJECT)
    mail_ids = data[0]
    for email_number in mail_ids.split():
        print("-------------------------------")
        print("Print containt of mail n°" + str(email_number))
        typ, email_data = mail.fetch(email_number, '(RFC822)')
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        msg = email.message_from_string(raw_email_string)
        email_body = extract_body(msg)

        email_body = [link for link in email_body if  any(s.lower() in link.lower() for s in HOST_SERVERS)] # remove text that are not in HOST_SERVERS

        # email_from = msg['from']
        # email_to = msg['to']
        # email_subject = msg['subject']
        print('Message : ' + str(email_body))

        mail.store(email_number, '+FLAGS', '\\Deleted') # remove email
    mail.expunge()
    mail.logout()

def runtest():
    print("Start script")
    fct_readmail()


if __name__ == '__main__':
    runtest()
