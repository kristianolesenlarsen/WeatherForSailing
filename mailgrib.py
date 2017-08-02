# this can send and recieve mails/attachments - it's a waste of time to try and implement GRIB data
# since their documentation is worse than that of ancient civilizations.
import keys
import datetime
import requests
import pandas as pd
import gdal
import numpy as np
import re


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



def genMailQuery(latBottom, latTop, lonLeft, lonRight, model = 'gfs', inc = 1, params = 'WIND', timestring = '24,48,72', subscribe = False):
    #model: lat0, lat1, lon0, lon1 |inc, inc | times | params
    query = '{}:{}N,{}N,{}W,{}W|{},{}|{}|{}'.format(model,latBottom, latTop, lonRight, lonLeft, str(inc), str(inc), timestring, params)
    if subscribe:
        query + 'sub' + query
    return query

### sendemail ##################################################################
#
# query: email body content
# send: if true the email is send (so we can get mail subject without sending it)

def sendMailQuery(query, user, pwd, send = True):
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


#Retrieve an attachment from a Message.
#   borrowed from https://gist.github.com/jasonrdsouza/1674794 with gratitude

def getMailAttachment(user, pwd):
    detach_dir = './data/raw' # directory where to save attachments (default: current)
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
            #Check if its already there
            if not os.path.exists(att_path):
                open(att_path, 'w').close()
                fp = open(att_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                print('new file added!')



#possibly dont get anl files?
def getNOAAdata(year = '2017', month = '01', day = '01', hour = '0000'):
    base = 'https://nomads.ncdc.noaa.gov/data/gfsanl/{}/{}/'.format(''.join([year, month]), ''.join([year, month, day]))
    filename = 'gfsanl_4_{}_{}_000.grb2'.format(''.join([year, month, day]), hour)
    link = base + filename
    resp = requests.get(link, stream = True)
    i = 0

    f = open('./data/raw/{}'.format(filename), 'wb')
    for chunk in resp.iter_content():
        f.write(chunk)
        print(i)
        i += 1
    return link


def getMailWrapper(query, user, pwd, latBottom, latTop, lonLeft, lonRight, model = 'gfs', inc = 1, params = 'WIND', timestring = '24,48,72', subscribe = False, send = True):
    q = genMailQuery(latBottom, latTop, lonLeft, lonRight, inc, params, timestring)
    sendMailQuery(q, user,pwd)
    getMailAttachment(user,pwd)

#latBottom = 15, latTop = 80, lonLeft = 20, lonRight= 310, inc = 0.5, params = 'WIND,PRMSL,AIRTEMP', timestring = '00'


def getTop(GRIB):
    place = [m.start() for m in re.finditer(',', GRIB)][0]
    comma = [m.start() for m in re.finditer('N', GRIB)][1]

    return int(GRIB[place +1 : comma])

def getLeft(GRIB):
    place = [m.start() for m in re.finditer(',', GRIB)][2]
    comma = [m.start() for m in re.finditer('W', GRIB)][1]

    return int(GRIB[place +1 : comma])


# ATT: x,y are returned wrongly
def GRIBtoDict(GRIB, topLeft = None, delete_original = True):
    f = gdal.Open(GRIB)
    print('opened file')
    #basic info on the thing
    width = f.RasterXSize
    height = f.RasterYSize
    # get transformation
    gt = f.GetGeoTransform()

    print('doing min max stuff')
    #bbox of GRIB data
    if topLeft:
        minx = topleft[1] #left
        maxy = topLeft[0] #gt[3]
        print(minx, maxy)
    if not topLeft:
        minx = getLeft(GRIB)
        maxy = getTop(GRIB)

    print(minx, maxy)
    stepx = gt[2]
    stepy = gt[5]

    # number of bands
    s = gdal.Info(GRIB)
    nbands = len([m.start() for m in re.finditer('Band', s)])

    # dict to be returned with metadata for all the stuff
    outerHelp = {}

    endResult = {'x':[], 'y': []}

    for b in range(1, nbands + 1):
        print('new band')
        helpMeDict = {}
        band = f.GetRasterBand(b)
        meta = band.GetMetadata_Dict()
        #this is stupidly complicated, but it converts the timestamp to a readable date
        time = datetime.datetime.fromtimestamp(int(re.findall('\d+', band.GetMetadata_Dict()['GRIB_REF_TIME'])[0])).strftime("%Y-%m-%d %H")

        # fill out the helper dict
        #helpMeDict['var'].append(meta['GRIB_ELEMENT'])
        helpMeDict['band'] = [str(b)]
        helpMeDict['comment'] = [meta['GRIB_COMMENT']]
        helpMeDict['forecast'] = [meta['GRIB_FORECAST_SECONDS']]
        helpMeDict['time'] = [time]

        outerHelp[meta['GRIB_ELEMENT']] = helpMeDict


        #define new column in output
        endResult[meta['GRIB_ELEMENT']] = []
        """
        maybe arr[i] is the y-coordinates, and for each arr[i] the values are the corresponding x's?
        so where do they begin???
        """
        array = band.ReadAsArray()

        for y_index in range(0,len(array)):                        # for each y
            for x_index in range(0,len(array[y_index])):           # for each x
                if b == 1:                                         # Only add lon/lat once
                    # something is wrong with this
                    endResult['x'].append( minx + stepx * x_index )
                    endResult['y'].append( maxy + stepy * y_index )
                endResult[meta['GRIB_ELEMENT']].append(array[y_index][x_index])

    if delete_original:
        try:
            os.remove(f.GetFileList()[0])
        except:
            print("couldn't remove file")
    print("DONE!")
    return [endResult, outerHelp]




filename =
test = GRIBtoDict(,  delete_original = False)
pd.DataFrame.from_dict(test[0]).to_csv('./data/wide.csv')
