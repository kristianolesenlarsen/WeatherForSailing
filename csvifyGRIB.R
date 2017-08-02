# This is so far the only way i've been able to get GRIB data to a more usable format


library("rgdal")
library("jsonlite")
library("ggmap")
library("ggplot2")
library("viridis")



setwd("C:/Users/Kristian/Documents/GitHub/WeatherForSailing/data")

df2 = read.csv('WAVES.csv')
df2[df2 == 9999.00] = NA



df = read.csv('WIND,AIRTMP.csv')
df$speed = sqrt(df$UGRD^2 + df$VGRD^2)

df[df == 9999.00] = NA

map = get_map(c(-10, 51) , zoom = 3, maptype = 'satellite')

#ggmap(map)



setwd("C:/Users/Kristian/Documents/GitHub/WeatherForSailing/plots")


# Wind
p = ggmap(map) +
  geom_tile(data = df, aes(x = x, y = y,  fill = speed, alpha = speed)) +
  geom_contour(data = df, aes(x = x, y = y, z = speed, colour = ..level..), bins = 5) +
  scale_fill_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 9) +
  scale_color_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 9) +
  theme_nothing()


# Waves
p2 = ggmap(map) +
  geom_tile(data = subset(df2, !is.na(HTSGW)), aes(x = x, y = y,  fill = HTSGW, alpha = HTSGW)) +
  geom_contour(data = subset(df2, !is.na(HTSGW)), aes(x = x, y = y, z = HTSGW, colour = ..level..), bins = 5) +
  scale_fill_gradient2(low = 'blue', mid = 'yellow', high = 'red', midpoint = 2) +
  scale_color_gradient2(low = 'blue', mid = 'yellow', high = 'red', midpoint = 2) +
  theme_nothing()

# Temp
p3 = ggmap(map) +
  geom_tile(data = df, aes(x = x, y = y,  fill = TMP), alpha = 0.4) +
  geom_contour(data = df, aes(x = x, y = y, z = TMP, colour = ..level..), bins = 5) +
  scale_fill_gradient2(low = 'blue', mid = 'yellow', high = 'red', midpoint = 16) +
  scale_color_gradient2(low = 'yellow', mid = 'yellow', high = 'red', midpoint = 16) +
  theme_nothing()


# Sea level temperatures
#p4 = ggmap(map) +
#  geom_tile(data = df2, aes(x = x, y = y,  fill = TMP, alpha = TMP)) +
#  geom_contour(data = df2, aes(x = x, y = y, z = TMP, colour = ..level..), bins = 5) +
#  scale_fill_gradient2(low = 'blue', mid = 'yellow', high = 'green', midpoint = 2) +
#  scale_color_gradient2(low = 'blue', mid = 'yellow', high = 'green', midpoint = 2) +
#  theme_nothing()




ggsave('Windspeed.png',p)
ggsave('Waves.png',p2)
ggsave('Temp.png',p3)
#ggsave('Sealeveltemp.png', p4)

