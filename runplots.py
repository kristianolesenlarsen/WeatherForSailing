import weather

# get current weather
weather = get_weather_at_loc(key, 'ip')

# pygal plots
show_windspeed(weather, 'windspeed')
show_temp_overday(weather, 'temp_overday')
show_temp_overdays(weather, 'temp_overdays')
show_winddir_overday(weather, 'windbearing_radar','windbearing_line')
show_rain_overdays(weather, 'rain')
show_temperature(weather, 'temp_now')

# plotly plots
webready_plotly_winddir(weather)

# weather summaries
weathersummaries(weather)
