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




# def get_loc_by_gps():
#
#
#
#

def get_weather_at_loc(pk, method = 'ip'):
    # ensure we dont start using money - later update this to reset calls if a day has passed
    if method == 'gps':
        #implement gps location
        lat = str(get_loc_by_ip()[0])
        lon = str(get_loc_by_ip()[1])
        print('gps not yet implemented! defaulting to IP')
    if method == 'manual':
        lat = input('latitude: ')
        lon = input('longitude: ')
    else:
        lat = str(get_loc_by_ip()[0])
        lon = str(get_loc_by_ip()[1])

    global calls
    if calls > 900:
        print('no more calls!')
        return None
    else:
        calls += 1

    link = 'https://api.darksky.net/forecast/' + pk + '/' + lat + ',' + lon + '?units=si'
    resp = requests.get(link).json()

    return resp



### PYGAL VISUALIZATIONS
#   show_windspeed(weather): plots average and max windspeed
#       weather: output from get_weather_at_loc
#
#   show_temp_overday(weather): plots average and max teperature per hour
#       weather: output from get_weather_at_loc
#
#   show_winddir_overday(weather): plots winddirection per hour
#       weather: output from get_weather_at_loc
#
#   show_rain_overdays(weather): plots daily probability of rain and cloud coverage for the comming 8 days
#       weather: output from get_weather_at_loc
#
#   show_temperature(weather): plots current temperature
#       weater: output from get_weather_at_loc

from pygal.style import Style
weather = get_weather_at_loc(key, 'ip')



custom_style = Style(
  background='transparent',
  plot_background='transparent',
  foreground='#53E89B',
  foreground_strong='#53A0E8',
  foreground_subtle='#630C0D',
  opacity='.6',
  opacity_hover='.9',
  transition='400ms ease-in',
  colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))




def show_windspeed(weather, name):
    gauge = pygal.SolidGauge(
        half_pie=True, inner_radius= 0.7,
        style = custom_style)
        #style=pygal.style.styles['default'](value_font_size=10))

    formatter = lambda x: '{:.10g}m/s'.format(x)
    gauge.value_formatter = formatter

    gauge.add('Gusts', [{'value': weather['currently']['windSpeed'], 'max_value': weather['currently']['windGust']}],
              formatter=formatter)
    gauge.add('Windspeed', [{'value': weather['currently']['windSpeed'], 'max_value':15}],
              formatter=formatter)
    return gauge.render_to_file('./svg/' + name + '.svg')

show_windspeed(weather, 'windspeed')


def show_temp_overday(weather, name):
    d = {'time': [], 'temp': []}
    for i in range(0,len(weather['hourly']['data'])):
        time = datetime.datetime.fromtimestamp(weather['hourly']['data'][i]['time']).strftime('%H')
        d['time'].append(time)
        d['temp'].append(weather['hourly']['data'][i]['temperature'])


    line_chart = pygal.Line(style = custom_style)
    line_chart.title = 'Hourly temperatures - next 48 hrs'
    line_chart.x_labels = map(str, d['time'])
    line_chart.add('temperature', d['temp'])
    return line_chart.render_to_file('./svg/' + name + '.svg')

show_temp_overday(weather, 'temp_overday')


def show_temp_overdays(weather, name):
    d = {'time': [], 'temp_max': [], 'temp_min': []}
    for i in range(0,len(weather['daily']['data'])):
        time = datetime.datetime.fromtimestamp(weather['daily']['data'][i]['time']).strftime('%d')
        d['time'].append(time)
        d['temp_max'].append(weather['daily']['data'][i]['temperatureMax'])
        d['temp_min'].append(weather['daily']['data'][i]['temperatureMin'])

    line_chart = pygal.Bar(style=custom_style)
    line_chart.title = 'Daily temperatures - 8 days'
    line_chart.x_labels = map(str, d['time'])
    line_chart.add('daily max', d['temp_max'])
    line_chart.add('daily min', d['temp_min'])
    return line_chart.render_to_file('./svg/' + name + '.svg')

show_temp_overdays(weather, 'temp_overdays')


def show_winddir_overday(weather, name1, name2):
    d = {'time': [], 'winddir': []}
    for i in range(0,len(weather['hourly']['data'])):
        time = datetime.datetime.fromtimestamp(weather['hourly']['data'][i]['time']).strftime('%H')
        d['time'].append(time)
        d['winddir'].append(weather['hourly']['data'][i]['windBearing'])


    line_chart = pygal.Line(style=custom_style)
    line_chart.title = 'Daily wind bearing'
    line_chart.x_labels = map(str, d['time'])
    line_chart.add('Wind direction', d['winddir'])

    radar_chart = pygal.Radar()
    radar_chart.title = 'Daily Wind bearing'
    radar_chart.x_labels = map(str, d['time'])
    radar_chart.add('Wind direction', d['winddir'])
    radar_chart.render()

    return [radar_chart.render_to_file('./svg/' + name1 + '.svg'),line_chart.render_to_file('./svg/' + name2 + '.svg')]

show_winddir_overday(weather, 'windbearing_line','windbearing_radar')


def show_rain_overdays(weather, name):
    d = {'time': [], 'rain': [], 'clouds': []}
    for i in range(0,len(weather['daily']['data'])):
        time = datetime.datetime.fromtimestamp(weather['daily']['data'][i]['time']).strftime('%d')
        d['time'].append(time)
        d['rain'].append(weather['daily']['data'][i]['precipProbability'])
        d['clouds'].append(weather['daily']['data'][i]['cloudCover'])

    line_chart = pygal.Bar(style = custom_style)
    line_chart.title = 'Daily rain probability'
    line_chart.x_labels = map(str, d['time'])
    line_chart.add('Risk of rain', d['rain'])
    line_chart.add('Cloud cover', d['clouds'])
    return line_chart.render_to_file('./svg/' + name + '.svg')

show_rain_overdays(weather, 'rain')



def show_temperature(weather, name):
    gauge_chart = pygal.Gauge(human_readable=True, style = custom_style)
    gauge_chart.title = 'Current temperature'
    gauge_chart.range = [0, 35]
    gauge_chart.add('temperature', weather['currently']['temperature'])
    return gauge_chart.render_to_file('./svg/' + name + '.svg')

show_temperature(weather, 'temp_now')









### PLOTLY VISUALIZATIONS
#
#
#
#
#
#
#
#
#

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np


def plotly_winddir(weather):
    d = {'time': [], 'winddir': [], 'windspeed': []}
    for i in range(0,len(weather['hourly']['data'])):
        time = int(datetime.datetime.fromtimestamp(weather['hourly']['data'][i]['time']).strftime('%H'))
        d['time'].append(time)
        d['winddir'].append(weather['hourly']['data'][i]['windBearing'])
        d['windspeed'].append(weather['hourly']['data'][i]['windSpeed'])
    print(d)

    trace1 = go.Scatter(
        r= d['windspeed'],
        t=d['winddir'],
        mode='lines',
        name='Wind direction',
        marker = dict(
        color = 'none',
        line = dict(
        color = '#E95355',
        width = 2
        )
        )
    )
    trace2 = go.Scatter(
    r=np.random.uniform(3,8,size=2),
    t=np.random.uniform(-14,-76,size=2),
    mode='markers',
    name='Trial 2',
    marker=dict(
        color='rgb(217,95,2)',
        size=110,
        opacity=0.7
    )
)

    data = [trace1, trace2]
    layout = go.Layout(
        title='Wind direction and -speed',

        showlegend = False,
        font=dict(
            size=16
        ),
        legend=dict(
            font=dict(
                size=16
            )
        ),
        radialaxis=dict(
            ticksuffix='m/s'
        ),
        orientation=-90
    )


    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig)


plotly_winddir(weather)
