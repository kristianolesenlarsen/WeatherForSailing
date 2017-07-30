import keys

import requests
import json
import csv
import pandas as pd
import os
import io
import numpy as np
import time


def get_loc_by_ip():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)

    return [j['latitude'], j['longitude'], j['city'], j['region_name'], j['country_name']]


# def get_loc_by_gps():
#
#
#
#


class fromOpenAPI():
    def __init__(self, key):
        self.pk = key

    def CurrentWeatherBbox(self, left, right, bottom, top, zoom, **kwargs):
        args = list(map(str,[left, bottom, right, top, zoom]))
        base = 'http://api.openweathermap.org/data/2.5/box/city?bbox='
        for i in args:
            base = base + i + ','
        # add appid from keyfile
        base = base[:-1] + '&appid=' + self.pk
        # optional GET options such as 'unit', 'cnt' etc
        for i in kwargs.items():
            base = base + '&{}={}'.format(i[0],i[1])
        return requests.get(base).json()

    def CurrentWeatherCircle(self, lat,lon,count, **kwargs):
#        loc = list(map(str, [lat,lon,count]))     #why is this not working?
        loc = [str(lat), str(lon), str(count)]
        base = 'http://api.openweathermap.org/data/2.5/find?'
        # add required parameters to URL
        base = base + 'lat={}&lon={}&cnt={}'.format(loc[0], loc[1], loc[2]) + '&appid=' + self.pk
        # add optional paramters
        for i in kwargs.items():
            base = base + '&{}={}'.format(i[0],i[1])
        return requests.get(base).json()

    def WeatherByLatLon(self, lat, lon, Type = 'current', **kwargs):
        loc = list(map(str, [lat,lon]))
        base = 'http://api.openweathermap.org/data/2.5/'
        # do you want current weather or forecast?
        if Type == 'current':
            base = base + 'weather?'
        elif Type == 'forecast':
            base = base + 'forecast?'
        else:
            print("choose Type as 'current'(default) or 'forecast'")
        #lat, lon and appid
        base = base + 'lat={}&lon={}'.format(loc[0],loc[1]) + '&appid=' + self.pk
        # optional URL params
        for i in kwargs.items():
            base = base + '&{}={}'.format(i[0],i[1])
        return requests.get(base).json()

    def WeatherByID(self, ID, Type = 'current', **kwargs):
        ID = str(ID)
        base = 'http://api.openweathermap.org/data/2.5/'
        if Type == 'current':
            base = base + 'weather?id='
        elif Type == 'forecast':
            base = base + 'forecast?id='
        else:
            print("choose Type as 'current'(default) or 'forecast'")
        base = base + ID  + '&appid=' + self.pk
        # optional URL params
        for i in kwargs.items():
            base = base + '&{}={}'.format(i[0],i[1])
        return requests.get(base).json()

    # lat: north/south
    # lon: west/east

    def WeatherGrid(self, left, right, bottom, top, splits, filename, **kwargs):
        latlon = []
        lr = np.linspace(left, right,round(splits))
        bt = np.linspace(bottom, top, round(splits))

        for lat in bt:
            for lon in lr:
                latlon.append([lat,lon])
        print('estimated download duration:', len(latlon)/50, 'minutes')

        open(filename,'w').close()      #wipe file of old data

        for i in latlon:
            json = self.WeatherByLatLon(i[0],i[1], **kwargs)
            csvf = csvFunctions().appendInCsv(json = json, filename = filename)
            row = csvf[0]
            time.sleep(1)

        # add a header to the csv file
        df = pd.read_csv(filename)
        df.columns = csvf[1]
        df.to_csv(filename, index = False)

        print("finished downloading")
        return None





class csvFunctions():
    def appendInCsv(self, json, filename):
        row = []
        unfolded = self.unfoldJSON(json, 'now')

        for i in unfolded:
            row.append(unfolded[i][0])

        with io.open(filename,'a', encoding = 'utf-8') as f:
            writer = csv.writer(f, lineterminator = '\n')
            writer.writerow(row)

        return [row, unfolded.keys()]

    def unfoldJSON(self, json, source):
        inRaw = ['dt', 'id', 'name']
        inMain = ['humidity', 'pressure', 'temp']
        inWind = ['deg','speed']


        dat = {
        'clouds': [],
        'dt': [],
        'id': [],
        'humidity': [],
        'pressure': [],
        'temp': [],
        'name': [],
        'deg': [],
        'speed': []
        }

        if source == 'circle':
            strip = json['list']
            inRaw.append('rain')
            dat['rain'] = []
            dat['icon'] = []
            dat['lat'] = []
            dat['lon'] = []
            inCoords = ['lat', 'lon']
            what = 'all'
        if source == 'now':
            strip = [json]
            dat['lat'] = []
            dat['lon'] = []
            inCoords = ['lat', 'lon']
            what = 'all'
        if source == 'bbox':
            strip = json['list']
            dat['Lat'] = []
            dat['Lon'] = []
            dat['icon'] = []
            inCoords = ['Lat', 'Lon']
            what = 'today'

        for i in range(0,len(strip)):
            for raw in inRaw:
                dat[raw].append(strip[i][raw])
            for main in inMain:
                dat[main].append(strip[i]['main'][main])
            for wind in inWind:
                dat[wind].append(strip[i]['wind'][wind])
            for coords in inCoords:
                dat[coords].append(strip[i]['coord'][coords])
            dat['clouds'].append(strip[i]['clouds'][what])
            dat['icon'].append(strip[i]['weather'][0]['icon'])
        return dat

    def toCSV(self, json, filename, source = 'circle'):
        dat = self.unfoldJSON(json, source)
        pd.DataFrame.from_dict(dat).to_csv(filename, index = False)

        return dat



class fromDarkskyAPI():
    def __init__(self):
        pass

    def get_weather_at_loc(self, pk, method = 'ip'):
        if method == 'gps':
            #implement gps location (some day ... )
            lat = str(get_loc_by_ip()[0])
            lon = str(get_loc_by_ip()[1])
            print('gps not yet implemented! defaulting to IP')
        if method == 'manual':
            lat = input('latitude: ')
            lon = input('longitude: ')
        else:
            lat = str(get_loc_by_ip()[0])
            lon = str(get_loc_by_ip()[1])

        link = 'https://api.darksky.net/forecast/' + pk + '/' + lat + ',' + lon + '?units=si'
        resp = requests.get(link).json()

        return resp


    def get_weather_at_latlon(self, lat, lon, pk):
        link = 'https://api.darksky.net/forecast/' + pk + '/' + str(lat) + ',' + str(lon) + '?units=si'
        resp = requests.get(link).json()

        return resp

    # extend: measures grid size in lat,lon deviations from current position
    #
    # TODO: more sophisticated grid generation
    def get_weather_around_loc(self, extend, incr, pk, temporal = False, hourly = False):
        pos = get_loc_by_ip()
        lat0 = pos[0]
        lon0 = pos[1]

        if hourly:
            subset = 'hourly'
            tempfix = 'temperature'

        if not hourly:
            subset = 'daily'
            tempfix = 'temperatureMax'

        if not temporal:
            v = self.get_weather_at_latlon(lat0,lon0,pk)[subset]['data'][0]

            grid = {'lat': [lat0],
                    'lon':[lon0],
                    'speed': [v['windSpeed']],
                    'direction': [v['windBearing']],
                    'temp': [v[tempfix]]}

            for i in np.linspace(lat0-extend, lat0+extend, incr):
                for j in np.linspace(lon0 - extend, lon0 + extend, incr):

                    w = self.get_weather_at_latlon(i, j, pk)[subset]['data'][0]

                    grid['lat'].append(i)
                    grid['lon'].append(j)

                    grid['speed'].append(w['windSpeed'])
                    grid['direction'].append(w['windBearing'])
                    grid['temp'].append(w[tempfix])

            return grid

        if temporal:
            v = self.get_weather_at_latlon(lat0,lon0,pk)[subset]['data']

            grid = {'time': [],
             'lat': [],
             'lon':[],
             'speed': [],
             'direction': [],
             'temp': []}

            for k in range(0,len(v)):
                grid['lat'].append(lat0)
                grid['lon'].append(lon0)
                grid['time'].append(v[k]['time'])

                grid['speed'].append(v[k]['windSpeed'])
                grid['direction'].append(v[k]['windBearing'])
                grid['temp'].append(v[k][tempfix])

            for i in np.linspace(lat0-extend, lat0+extend, incr):
                for j in np.linspace(lon0 - extend, lon0 + extend, incr):

                    w = self.get_weather_at_latlon(i, j, pk)[subset]['data']

                    for t in range(0,len(w)):
                        grid['lat'].append(i)
                        grid['lon'].append(j)
                        grid['time'].append(w[t]['time'])

                        grid['speed'].append(w[t]['windSpeed'])
                        grid['direction'].append(w[t]['windBearing'])
                        grid['temp'].append(w[t][tempfix])

            return grid

        return None
