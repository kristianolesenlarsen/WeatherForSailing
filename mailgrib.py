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


### valid timestring
# 0,3,...180 hrs

### valid parameters:
# PRMSL: mean sea-level pressure
# WIND: surface wind gradient
# HGT: 500mb (milibars) height above sea-level
# SEATMP: sea temperature
# AIRTMP: air temperature

def genQuery(latBottom, latTop, lonLeft, lonRight, model = 'gfs', inc = 1, params = 'WIND', timestring = '24,48,72', subscribe = False):
    #model: lat0, lat1, lon0, lon1 |inc, inc | times | params
    query = '{}:{}N,{}N,{}W,{}W|{},{}|{}|{}'.format(model,latBottom, latTop, lonRight, lonLeft, str(inc), str(inc), timestring, params)
    if subscribe:
        query + 'sub' + query
    return query


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
    # implement carrying info in the filename

    
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


q = genQuery(latBottom = 45, latTop = 60, lonLeft = 0, lonRight= 30, inc = 0.5, timestring = '00')
sendmail(q, user,pwd)


#Retrieve an attachment from a Message.
#   borrowed from https://gist.github.com/jasonrdsouza/1674794 with gratitude

def getattachment(user, pwd):
    detach_dir = './data' # directory where to save attachments (default: current)
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

            filename =  mail['Subject'][4:] + datetime.datetime.now().date().strftime('%d-%H')
            att_path = os.path.join(detach_dir, filename) + '.grb'
            print(att_path)
            #Check if its already there
            if not os.path.exists(att_path):
                open(att_path, 'w').close()
                fp = open(att_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                print('new file added!')


getattachment(user,pwd)











"""
below is testing stuff
"""
import requests


#possibly dont get anl files?
def getNOAAdata(year = '2017', month = '01', day = '01', hour = '0000'):
    base = 'https://nomads.ncdc.noaa.gov/data/gfsanl/{}/{}/'.format(''.join([year, month]), ''.join([year, month, day]))
    filename = 'gfsanl_4_{}_{}_000.grb2'.format(''.join([year, month, day]), hour)
    link = base + filename
    resp = requests.get(link, stream = True)
    i = 0

    f = open('./data/{}'.format(filename), 'wb')
    for chunk in resp.iter_content():
        f.write(chunk)
        print(i)
        i += 1
    return link



# these grib files suck
import gdal
import numpy as np
import geopandas as gp

a = './data/40N,60N,140W,120W.grb'
b = './data/gfsanl_4_20170726_0000_006.grb2'
c = './data/gfs_4_20170726_0000_384.grb2'

f = gdal.Open(a)


# saildocs email gribs
# pressure, pressure, pressure, wind-speed (u), wind-speed (u), wind-speed (u), wind-speed (v), wind-speed (v), wind-speed (v)




f.

f.GetRasterBand(363).GetMetadata()


band = f.GetRasterBand(363)



arr = band.ReadAsArray()

arr[360][719]

f.GetGeoTransform()

f.GetRasterBand(3).GetMetadata_Dict()
