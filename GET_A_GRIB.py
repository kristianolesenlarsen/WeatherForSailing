# sends and recieves mail containing GRIB files as attachments
import keys
import email, imaplib, os
imaplib._MAXLINE = 100000
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# i need a better management of old files and better file naming

### setup ######################################################################
# create a folder in gmail called 'saildocs'
# get an app key from google if you use 2 factor auth
#

user = keys.user
pwd = keys.pwd


class mail():
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def saildocs_query(self, top, bottom, left, right, N_or_S = 'N', E_or_W = 'E', model = 'gfs', inc = 0.5, params = 'WIND', timestring = '24,38,72'):

        STRING_MIN = 20
        STRING_MAX = 45

        query = '{mod}:{to}{ns},{bot}{ns},{le}{ew},{ri}{ew}|{inc},{inc}|{ts}|{p}'.format(mod = model,
                                                                                          bot = str(bottom),
                                                                                          to = str(top),
                                                                                          ns = N_or_S,
                                                                                          le = str(left),
                                                                                          ri = str(right),
                                                                                          ew = E_or_W,
                                                                                          inc = str(inc),
                                                                                          ts = timestring,
                                                                                          p = params)
        print('query:', query)

        if len(query) > STRING_MAX:
            splitcomma = query[STRING_MIN:STRING_MAX].find(',')
            if splitcomma != -1:
                q1 = query[0:splitcomma + STRING_MIN + 1]
                q2 = query[splitcomma + STRING_MIN + 1: len(q)]
                query = """
                {}=
                {}
                """.format(q1, q2)

        return query

    """
     query: email body content
     send: if true the email is send (so we can get mail subject without sending it)
    """
    def send_query(self, query, send = True):

        fromaddr = self.user
        toaddr = "query@saildocs.com"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "saildocs request"
        # implement carrying info in the filename here
        if send:
            try:
                body = query
                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(fromaddr, self.pwd)
                text = msg.as_string()
                server.sendmail(fromaddr, toaddr, text)
                server.quit()
            except:
                print('Something went wrong...')
                return None

        return 'Re: ' + msg['subject']


    #Retrieve an attachment from a Message.
    #   borrowed from https://gist.github.com/jasonrdsouza/1674794 with gratitude
    def get_attachment(self, file_dir):
        detach_dir = file_dir # directory where to save attachments (default: current)
        # connecting to the gmail imap server
        m = imaplib.IMAP4_SSL("imap.gmail.com")
        m.login(self.user, self.pwd)
        m.select("saildocs") # here you a can choose a mail box like INBOX instead
        # use m.list() to get all the mailboxes
        resp, items = m.search(None, 'ALL') # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
        items = items[0].split() # getting the mails id
        print('items in folder:', items)

        resp, data = m.fetch(items[-1], '(RFC822)')
        body = data[0][1]

        mail = email.message_from_bytes(body) # parsing the mail content to get a mail object
        print('mail: ' + "[" + mail["From"] +"] :" + mail["Subject"])

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
            if os.path.exists(att_path):
                os.remove(att_path)
                print('removed old file')
            else:
                open(att_path, 'w').close()

            fp = open(att_path, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()
            print('new file added!')

        return att_path




#possibly dont get anl files?
def getNOAAdata(year = '2017', month = '01', day = '01', hour = '0000'):
    base = 'https://nomads.ncdc.noaa.gov/data/gfsanl/{}/{}/'.format(''.join([year, month]), ''.join([year, month, day]))
    filename = 'gfsanl_4_{}_{}_000.grb2'.format(''.join([year, month, day]), hour)
    link = base + filename
    resp = requests.get(link, stream = True)

    f = open('./data/raw/{}'.format(filename), 'wb')
    for chunk in resp.iter_content():
        f.write(chunk)

    return link
