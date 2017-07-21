import weather

key = '5ec23cf02b8ef50a23c22f504bd7dc00'
# get current weather
w = weather.get_weather_at_loc(key, 'ip')

# pygal plots
weather.show_windspeed(w, 'windspeed')
weather.show_temp_overday(w, 'temp_overday')
weather.show_temp_overdays(w, 'temp_overdays')
weather.show_winddir_overday(w, 'windbearing_radar','windbearing_line')
weather.show_rain_overdays(w, 'rain')
weather.show_temperature(w, 'temp_now')

# plotly plots
weather.webready_plotly_winddir(w)

# weather summaries
weather.weathersummaries(w)

#generate grid and save to dataframe
grid = get_weather_around_loc(4,8,key, True, False)

time = []   
for i in grid['time']:
    time.append(datetime.datetime.fromtimestamp(i).strftime('%d-%H'))

grid['time_2'] = time
df = pd.DataFrame.from_dict(grid,orient = 'index').T.to_csv('windgrid.csv', index = False)



# something something ... run the R script
#import subprocess
#subprocess.check_call(['Rscript', 'vectorfield.R'], shell=False)
