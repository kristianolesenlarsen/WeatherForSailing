# this can send and recieve mails/attachments - it's a waste of time to try and implement GRIB data
# since their documentation is worse than that of ancient civilizations.
import keys
import datetime

import email, imaplib, os
imaplib._MAXLINE = 100000
#import getpass

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


### setup ######################################################################
# create a folder in gmail called 'saildocs'
# get an app key from google if you use 2 factor auth
#

user = keys.user
pwd = keys.pwd

### sendemail ##################################################################
#
# query: email body content
# send: if true the email is send (so we can get mail subject without sending it)

def sendmail(query, user, pwd, send = True):
    fromaddr = user
    toaddr = "query@saildocs.com"
    timeNow = datetime.datetime.now().date().strftime('%d-%H')

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "saildocs request" + ' ' + timeNow

    if send:
        try:
            body = query
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, pwd)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
        except:
            print('Something went wrong...')
            return None

    return 'Re: ' + msg['subject']


# sendmail('send gfs:50N,60N,140W,120W', user,pwd)


#Retrieve an attachment from a Message.
#   borrowed from https://gist.github.com/jasonrdsouza/1674794 with gratitude

def getattachment(user, pwd):
    detach_dir = './grb' # directory where to save attachments (default: current)
    # connecting to the gmail imap server
    m = imaplib.IMAP4_SSL("imap.gmail.com")
    m.login(user,pwd)
    m.select("saildocs") # here you a can choose a mail box like INBOX instead
    # use m.list() to get all the mailboxes
    resp, items = m.search(None, 'ALL') # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
    items = items[0].split() # getting the mails id
    print('items in folder:', items)
    for emailid in items:
        resp, data = m.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
        email_body = data[0][1] # getting the mail content

        mail = email.message_from_bytes(email_body) # parsing the mail content to get a mail object

        print('mail: ' + "[" + mail["From"] +"] :" + mail["Subject"])
        #Check if any attachments at all
        if mail.get_content_maintype() != 'multipart':
            continue
        # we use walk to create a generator so we can iterate on the parts and forget about the recursive headach
        for part in mail.walk():
            # multipart are just containers, so we skip them
            if part.get_content_maintype() == 'multipart':
                continue

            # is this part an attachment ?
            if part.get('Content-Disposition') is None:
                continue

            filename =  mail['Subject'][4:]
            att_path = os.path.join(detach_dir, filename) + '.grb'

            #Check if its already there
                # finally write the stuff
                fp = open(att_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()

# getattachment(user,pwd)
