import pygal
import datetime
from math import *
import io
import numpy as np
import pandas as pd
import weather
from pygal.style import Style

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import folium
from folium.plugins import HeatMap




### PYGAL VISUALIZATIONS #######################################################
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



c1 = '#E853A0'
c2 = '#E8537A'
c3 = '#E95355'
c4 = '#E87653'
c5 = '#E89B53'


c6 = '#c6138e'
c7 = '#f45fb4'
c8 = '#b1e4fa'
c9 = '#18a7ed'
c0 = '#005570'


custom_style = Style(
  background='transparent',
  plot_background='transparent',
  foreground=c0,
  foreground_strong=c9,
  foreground_subtle='#630C0D',
  opacity='.6',
  opacity_hover='.9',
  transition='400ms ease-in',
  colors=(c0, c8 , c4, c5, c1))




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


def show_temp_overdays(weather, name):
    d = {'time': [], 'temp_max': [], 'temp_min': []}
    for i in range(0,len(weather['daily']['data'])):
        time = datetime.datetime.fromtimestamp(weather['daily']['data'][i]['time']).strftime('%d')
        d['time'].append(time)
        d['temp_max'].append(weather['daily']['data'][i]['temperatureMax'])
        d['temp_min'].append(weather['daily']['data'][i]['temperatureMin'])

    line_chart = pygal.Line(style=custom_style)
    line_chart.title = 'Daily temperatures - 8 days'
    line_chart.x_labels = map(str, d['time'])
    line_chart.add('daily max', d['temp_max'])
    line_chart.add('daily min', d['temp_min'])
    return line_chart.render_to_file('./svg/' + name + '.svg')


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

    radar_chart = pygal.Radar(style = custom_style)
    radar_chart.title = 'Daily Wind bearing'
    radar_chart.x_labels = map(str, d['time'])
    radar_chart.add('Wind direction', d['winddir'])
    radar_chart.render()

    return [radar_chart.render_to_file('./svg/' + name1 + '.svg'),line_chart.render_to_file('./svg/' + name2 + '.svg')]



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


def show_temperature(weather, name):
    gauge_chart = pygal.Gauge(human_readable=True, style = custom_style)
    gauge_chart.title = 'Current temperature'
    gauge_chart.range = [0, 35]
    gauge_chart.add('temperature', weather['currently']['temperature'])
    return gauge_chart.render_to_file('./svg/' + name + '.svg')




### PLOTLY VISUALIZATIONS ######################################################
#
#
#


def plotly_winddir(weather):
    d = {'time': [], 'winddir': [], 'windspeed': []}
    for i in range(0,len(weather['hourly']['data'])):
        time = int(datetime.datetime.fromtimestamp(weather['hourly']['data'][i]['time']).strftime('%H'))
        d['time'].append(time)
        d['winddir'].append(weather['hourly']['data'][i]['windBearing'])
        d['windspeed'].append(weather['hourly']['data'][i]['windSpeed'])

    trace1 = go.Scatter(
        r = d['windspeed'],
        t = d['winddir'],
        mode='lines',
        name='Wind direction',
        text = d['time'],
        marker = dict(
        color = 'none',
        line = dict(
        color = c0,
        width = 2
        )
        )
    )

    trace2 = go.Scatter(
        r= [d['windspeed'][0], d['windspeed'][0],d['windspeed'][0],d['windspeed'][0],d['windspeed'][0]],
        t= [d['winddir'][0],   d['winddir'][0],d['winddir'][0],d['winddir'][0],d['winddir'][0]],
        mode='markers',
        name='time=now',
        text=['t=0'],
        marker = dict(
        color = 'none',
        line = dict(
        color = c0,
        width = 2
        )
        )
    )

    data = [trace1,trace2]
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
#    plotly.offline.plot(fig)   #activate to get local output as well
    return plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')

def webready_plotly_winddir(weather):
    with open('js/compass.js','w') as f:
        f.write("document.write('")
        f.write(plotly_winddir(weather))
        f.write("')")


### WEATHER SUMMARIES ##########################################################
#
#
#

def weathersummaries(weather):
    with io.open('js/dailysummary.js','w', encoding = 'utf-8') as f:
        f.write("document.write('")
        f.write(weather['hourly']['summary'])
        f.write("')")
    with io.open('js/weeklysummary.js','w', encoding = 'utf-8') as f:
        f.write("document.write('")
        f.write(weather['daily']['summary'])
        f.write("')")
    with io.open('js/time.js','w', encoding = 'utf-8') as f:
        f.write("document.write('")
        f.write( str(datetime.datetime.now()) )
        f.write("')")



### FOLIUM EXPERIMENTS ##########################################################
#
#
#
def folium_cityweather(datafile, outfile):
    df = pd.read_csv(datafile, encoding = 'latin1')
    df.columns = map(str.lower, df.columns)

    locNow = weather.get_loc_by_ip()

    df['icon'] = df['icon'].replace(['01d', '02d'], 'asterisk')
    df['icon'] = df['icon'].replace(['03d','04d'], 'cloud')
    df['icon'] = df['icon'].replace(['09d', '10d'], 'tint')
    df['icon'] = df['icon'].replace(['11d', '13d','50d'], 'map-marker')

    df['color'] = 'blue'
    df.loc[df.icon == 'asterisk','color'] = 'yellow'
    df.loc[df.icon == 'cloud','color'] = 'lightgray'
    df.loc[df.icon == 'map-marker','color'] = 'green'

    map_osm = folium.Map(location = [locNow[0],locNow[1]], tiles = 'Cartodb Positron', control_scale = True, zoom_start = 4)

    for i in ['wind_new', 'clouds_new', 'precipitation_new','temp_new']:
        url = 'http://tile.openweathermap.org/map/' + i + '/{z}/{x}/{y}.png?appid=' + keys.key2
        folium.TileLayer(
        tiles = url,
        attr = 'tile.openweathermap.org',
        name = i[:-4],
        overlay = True
        ).add_to(map_osm)


    mc = folium.MarkerCluster(name = 'local weather').add_to(map_osm)

    for row in range(0,len(df)):
        folium.Marker([df['lat'][row],df['lon'][row]],
        #    radius = df['temp'][row],
        icon = folium.Icon(color = df['color'][row], icon = df['icon'][row]),
        popup = 'Location: ' + df['name'][row] + ', ' + 'Temperature: ' + str(df['temp'][row])).add_to(mc)

    folium.LayerControl().add_to(map_osm)

    mc.save(outfile)


import keys

folium_cityweather('./data/bbox.csv','./plots/bbox.html')
