# sends and recieves mail containing GRIB files as attachments

import keys
import datetime
import requests
import pandas as pd
import gdal
import numpy as np
import re
import time
import json


import email, imaplib, os
imaplib._MAXLINE = 100000
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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

    ### sendemail ##################################################################
    #
    # query: email body content
    # send: if true the email is send (so we can get mail subject without sending it)

    def sendQuery(self, query, send = True):

        fromaddr = self.user
        toaddr = "query@saildocs.com"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "saildocs request"
        # implement carrying info in the filename


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


"""
getTop/Left - find coordinates in saildocs query filenames, to ease the bbox finding. are helpers in GRIBtoDict()
 - GRIB: path to a grib file
"""

def getTopY(GRIB):
    place = [m.start() for m in re.finditer(',', GRIB)][0]
    comma = [m.start() for m in re.finditer('N', GRIB)][1]

    return int(GRIB[place +1 : comma])

def getLeftX(GRIB):
    place = [m.start() for m in re.finditer(',', GRIB)][2]
    comma = [m.start() for m in re.finditer('E', GRIB)][1]

    return int(GRIB[place +1 : comma])


""" GRIBtoDict - convert a GRIB file to a dict  with properly named 'columns'. Produces a list as output with [0] being the actual data, and [1] containing
various metadata on the variables.

 - GRIB: path to a grib file to be opened
 - topLeft: a two element list containing coordinates for the top left corner of the bbox in the format [top, left]
 - delete_original: should the original grib file be deleted after use?
"""

# ATT: x,y are returned in a slightly shady way, dont trust output to be correct. (plot some winds to see that they look to be facing correctly)
def GRIBtoDict(GRIB, topLeft = None, delete_original = True):
    f = gdal.Open(GRIB)
    print('opened file')
    #basic info on the thing
    width = f.RasterXSize
    height = f.RasterYSize
    # get transformation
    gt = f.GetGeoTransform()

    #bbox of GRIB data
    if topLeft:
        minx = topleft[1] #left
        maxy = topLeft[0] #gt[3]
        print(minx, maxy)
    if not topLeft:
        minx = getLeftX(GRIB)
#        maxx = 60
        maxy = getTopY(GRIB)
#        miny = 10
#    print('bbox:',minx, maxx, miny, maxy)

    stepx = gt[1]
    stepy = gt[5]
    print('steps:', stepx, stepy)

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
        time = datetime.datetime.fromtimestamp(int(re.findall('\d+', meta['GRIB_REF_TIME'])[0])).strftime("%Y-%m-%d %H")

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
                    endResult['x'].append( minx +  stepx * x_index )
                    endResult['y'].append( maxy + stepy * y_index ) #begin in upper left corner
                endResult[meta['GRIB_ELEMENT']].append(array[y_index][x_index])

    if delete_original:
        try:
            os.remove(f.GetFileList()[0])
        except:
            print("couldn't remove file")
    print("DONE! see result in output[0]")
    return [endResult, outerHelp]




""" fromDictToWindJSON: takes the dict produced by GRIBtoDict() and converts it into an animation friendly json file
 - u: u component of wind
 - v: v component of wind
 - dx: increments in longitude
 - dy: increments in latitude
 - latTop, latBottom, lonLeft,lonRight: bbox
 - filename: output json filename
"""
# TODO is to make transfer from GRIBtoDict to this automatic
#also some of these values are static to match grib2json output - this is worth fixing


def fromDictTowindJSON(u, v, dx, dy, latTop, latBottom, lonLeft, lonRight, filename):

    if lonRight < 0:
        lonRight = 360 + lonRight # if right side (end) is negative, subtract it from 360 to convert from [-180,180] to [0,360]
    if lonLeft < 0:
        lonLeft = 360 + lonLeft # same with left side (beginning)

    if lonLeft > lonRight:
        lonRight = 360 + lonRight

    print('x (left to right):', lonLeft, lonRight)
    print('y (top to bottom):', latTop, latBottom)

    print('origin:', latTop, lonLeft)
#    lonRight = lonRight - 20
#    lonLeft = lonLeft -20

    time = datetime.datetime.now().date().strftime('%Y-%M-%d %H-%M %Z')
    nx = int(round((lonLeft - lonRight)/(dx),0))
    ny = int(round((latTop -latBottom)/(dy),0))
    if nx < 0:
        nx = -nx
    if ny < 0:
        ny = -ny

    out = [{'header': {'parameterUnit': 'm.s-1',
                        'parameterNumber': 2,
                        'dx': dx,
                        'dy': dy,
                        'parameterNumberName': "eastward_wind",
                        'la1': latTop,
                        'la2': latBottom,
                        'parameterCategory': 2,
                        'lo2': lonRight,
                        'nx': nx,
                        'ny': ny,
                        'refTime': time,
                        'lo1': lonLeft},
                        'data': u
                        },
            {'header': { 'parameterUnit': 'm.s-1',
                         'parameterNumber': 3,
                         'dx': dx,
                         'dy': dy,
                         'parameterNumberName': "northward_wind",
                         'la1': latTop,
                         'la2': latBottom,
                         'parameterCategory': 2,
                         'lo2': lonRight,
                         'nx': nx,
                         'ny': ny,
                         'refTime': time,
                         'lo1': lonLeft},
                         'data': v
                        }]
    with open(filename, 'w') as f:
        json.dump(out, f)

    return out



"""
# bodgy approach to get whole earth
for i in ['WIND,AIRTMP','WAVES']:
    filename = GRIBmail(user = keys.user, pwd = keys.pwd).wrapper(5, 80, -70,50, timestring = '00', params = i, inc = 0.5, send = True)
    test = GRIBtoDict(filename,  delete_original = False)
    pd.DataFrame.from_dict(test[0]).to_csv('./data/{}.csv'.format(i))
    time.sleep(180)


"""
# why is this not working?
g = GRIBmail(user = keys.user, pwd = keys.pwd)
getOut = g.wrapper(65,  -10, -80, 12, timestring = '00', params = 'WIND', inc = 1, send = True)
filename = getOut[0]

test = GRIBtoDict(filename,  delete_original = False)

getOut[1]
coords = getOut[1]

g= fromDictTowindJSON(test[0]['UGRD'], test[0]['VGRD'], 1, 1, latTop = coords[0]  , latBottom =  coords[1], lonLeft =  coords[2], lonRight = coords[3], filename = 'data/windy.json')


# second half
getOut2 = getMailWrapper(user, pwd, 80, -50, -179, 0, timestring = '00', params = 'WIND', inc = 1, send = True)
filename2 = getOut2[0]

test2 = GRIBtoDict(filename2,  delete_original = False)

coords2 = getOut2[1]

g= fromDictTowindJSON(test2[0]['UGRD'], test2[0]['VGRD'], 1, 1, latTop = coords2[0]  , latBottom =  coords2[1], lonLeft =  coords2[2], lonRight = coords2[3], filename = 'data/windy2.json')
