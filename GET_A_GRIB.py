# sends and recieves mail containing GRIB files as attachments
import time
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


class GRIBmail():
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    # generate a mail query for saildocs
    def genQuery(self, latTop, latBottom, lonLeft, lonRight, model = 'gfs', inc = 1, params = 'WIND', timestring = '24,48,72', subscribe = False):
        #model: lat0, lat1, lon0, lon1 |inc, inc | times | params

        query = '{}:{}N,{}N,{}E,{}E|{},{}|{}|{}'.format(model,latBottom, latTop, lonLeft, lonRight, str(inc), str(inc), timestring, params)
        if subscribe:
            query = 'sub ' + query
        print('query:', query)
        return query.replace(' ','')

    """
     query: email body content
     send: if true the email is send (so we can get mail subject without sending it)
    """
    def sendQuery(self, query, send = True):

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
    def getAttachment(self):
        detach_dir = './data/raw' # directory where to save attachments (default: current)
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

    """ getMailWrapper - a wrapper to get grib data from saildocs
     - user: a gmail address
     - pwd: password for the gmail account
     - bottom: lowest latitude northward
     - top: highest latitude northward
     - left: leftmost longitude eastward
     - right: rightmost longitude eastward
     - model: saildocs parameter for model
     - inc: grid increment
     - params: variables to get in grib file
     - timestring: forecast hours (you can get 00, 24, 48, 72... 180)
     - subscribe: if true, you subscribe to updated GRIBS of the same area
     - send: if false the request to saildocs isn't send
    """
    ### valid timestring
    # 0,3,...180 hrs

    ### valid parameters:
    # PRMSL: mean sea-level pressure
    # WIND: surface wind gradient
    # HGT: 500mb (milibars) height above sea-level
    # SEATMP: sea temperature
    # AIRTMP: air temperature
    # WAVES: wave height

    def wrapper(self, top, bottom, left, right, model = 'gfs', inc = 1, params = 'WIND', timestring = '24,48,72', subscribe = False, send = True):
        STRING_MIN = 25
        STRING_MAX = 40
        STRING_CUT = 45

        q = self.genQuery(latTop = top, latBottom = bottom, lonLeft = left, lonRight = right, model = model, inc = inc, params = params, timestring = timestring, subscribe = subscribe)
        if len(q) > STRING_CUT:
            splitcomma = q[STRING_MIN:STRING_MAX].find(',')
            if splitcomma != -1:
                q1 = q[0:splitcomma + STRING_MIN + 1]
                q2 = q[splitcomma + STRING_MIN + 1: len(q)]
                q = """
                {}=
                {}
                """.format(q1, q2)
            else:
                print('error in generating query')
        self.sendQuery(q)
        print(q)
        if send:
            time.sleep(180)
        self.getAttachment()
        return  ['./data/raw/{}N,{}N,{}E,{}E.grb'.format(bottom, top, left, right), [top, bottom, left, right]]




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
