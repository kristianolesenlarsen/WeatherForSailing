import requests
import json
import pygal
import datetime
from math import *

key = '5ec23cf02b8ef50a23c22f504bd7dc00'
calls = 0


def get_loc_by_ip():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)

    return [j['latitude'], j['longitude'], j['city'], j['region_name'], j['country_name']]


#def get_loc_by_gps():
#
#
#
#

def get_weather_at_loc(pk):
    # ensure we dont start using money - later update this to reset calls if a day has passed
    global calls
    if calls > 900:
        print('no more calls!')
        return None
    else:
        calls += 1

    link = 'https://api.darksky.net/forecast/' + pk + '/' + str(get_loc_by_ip()[0]) + ',' + str(get_loc_by_ip()[1]) + '?units=si'
    resp = requests.get(link).json()

    return resp


#def illustrate_currently(weather):


weather = get_weather_at_loc(key)

weather

### PYGAL VIZ
#
# show some figures about the weather comming up
#
#



def show_windspeed(weather):
    gauge = pygal.SolidGauge(
        half_pie=True, inner_radius= 0.7,
        style=pygal.style.styles['default'](value_font_size=10))

    formatter = lambda x: '{:.10g}m/s'.format(x)
    gauge.value_formatter = percent_formatter

    gauge.add('Gusts', [{'value': weather['currently']['windSpeed'], 'max_value': weather['currently']['windGust']}],
              formatter=formatter)
    gauge.add('Windspeed', [{'value': weather['currently']['windSpeed'], 'max_value':15}],
              formatter=formatter)
    return gauge.render()

show_windspeed(weather)


def show_temp_overday(weather):
    d = {'time': [], 'temp': []}
    for i in range(0,len(weather['hourly']['data'])):
        time = datetime.datetime.fromtimestamp(weather['hourly']['data'][i]['time']).strftime('%H')
        d['time'].append(time)
        d['temp'].append(weather['hourly']['data'][i]['temperature'])


    line_chart = pygal.Line()
    line_chart.title = 'Hourly temperatures - next 48 hrs'
    line_chart.x_labels = map(str, d['time'])
    line_chart.add('temperature', d['temp'])
    return line_chart.render()

show_temp_overday(weather)


def show_winddir_overday(weather):
    d = {'time': [], 'winddir': []}
    for i in range(0,len(weather['hourly']['data'])):
        time = datetime.datetime.fromtimestamp(weather['hourly']['data'][i]['time']).strftime('%H')
        d['time'].append(time)
        d['winddir'].append(weather['hourly']['data'][i]['windBearing'])


    line_chart = pygal.Line()
    line_chart.title = 'Daily wind bearing'
    line_chart.x_labels = map(str, d['time'])
    line_chart.add('Wind direction', d['winddir'])

    radar_chart = pygal.Radar()
    radar_chart.title = 'Daily Wind bearing'
    radar_chart.x_labels = map(str, d['time'])
    radar_chart.add('Wind direction', d['winddir'])
    radar_chart.render()

    return [radar_chart.render(),line_chart.render()]

show_winddir_overday(weather)[0]
show_winddir_overday(weather)[1]



line_chart = pygal.Bar()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
line_chart.render()

def show_rain_overdays(weather):
    d = {'time': [], 'rain': [], 'clouds': []}
    for i in range(0,len(weather['daily']['data'])):
        time = datetime.datetime.fromtimestamp(weather['daily']['data'][i]['time']).strftime('%d')
        d['time'].append(time)
        d['rain'].append(weather['daily']['data'][i]['precipProbability'])
        d['clouds'].append(weather['daily']['data'][i]['cloudCover'])
    line_chart = pygal.Bar()
    line_chart.title = 'Daily rain probability'
    line_chart.x_labels = map(str, d['time'])
    line_chart.add('Risk of rain', d['rain'])
    line_chart.add('Cloud cover', d['clouds'])
    return line_chart.render()

show_rain_overdays(weather)



def show_temperature(weather):
    gauge_chart = pygal.Gauge(human_readable=True)
    gauge_chart.title = 'Current temperature'
    gauge_chart.range = [0, 35]
    gauge_chart.add('temperature', weather['currently']['temperature'])
    return gauge_chart.render()

show_temperature(weather)
