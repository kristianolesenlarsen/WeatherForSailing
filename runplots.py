import weather
import time
import keys
import plots
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import GET_A_GRIB as GAG
import READ_A_GRIB as RAG
# inputs
#   get_weather_around_loc: extend, incr (how far to each side of current location, and in how many steps)
#   current weather circle: number of cities to catch
#   bbox: top, bottom, left, right, zoom



# get current weather
w = weather.fromDarkskyAPI().get_weather_at_loc(keys.key, 'ip')

# pygal plots
plots.show_windspeed(w, 'windspeed')
plots.show_temp_overday(w, 'temp_overday')
plots.show_temp_overdays(w, 'temp_overdays')
plots.show_winddir_overday(w, 'windbearing_radar','windbearing_line')
plots.show_rain_overdays(w, 'rain')
plots.show_temperature(w, 'temp_now')

# plotly plots
plots.webready_plotly_winddir(w)

# weather summaries
plots.weathersummaries(w)

#generate grid and save to dataframe
grid = weather.fromDarkskyAPI().get_weather_around_loc(4,8,keys.key, True, False)

time = []
for i in grid['time']:
    time.append(datetime.datetime.fromtimestamp(i).strftime('%d-%H'))

grid['time_2'] = time
df = pd.DataFrame.from_dict(grid,orient = 'index').T.to_csv('windgrid.csv', index = False)


#fire up fromOpenAPI
g = weather.fromOpenAPI(keys.key2)

curcir = g.CurrentWeatherCircle(weather.get_loc_by_ip()[0],weather.get_loc_by_ip()[1], 50)
bbox = g.CurrentWeatherBbox(8,13,54,58,10)

weather.csvFunctions().toCSV(curcir,'./data/curcir.csv', 'circle')
weather.csvFunctions().toCSV(bbox, './data/bbox.csv','bbox')

#folium plots
plots.folium_cityweather('./data/bbox.csv','./plots/bbox.html')


# getting GRIB data



for i in ['WIND,AIRTMP', 'WAVES']:
    saildocs = GAG.mail(user = keys.user, pwd = keys.pwd)
    query = saildocs.saildocs_query(10,90,180,20, E_or_W = 'W', timestring = '00')
    saildocs.send_query(query)
    time.sleep(180)
    path = saildocs.get_attachment()

path

weather = RAG.GRIB(path)

weather.no_bands
weather.read_band(1).metadata

u = weather.read_band(1)
v = weather.read_band(2)


s = np.sqrt(u.array*u.array + v.array*v.array)


plt.title('Winds across North America')
plt.imshow(s, cmap = 'RdPu_r', extent = (180,20,10,90))
plt.savefig('windmap.png')
plt.show()
