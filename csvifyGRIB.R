# This is so far the only way i've been able to get GRIB data to a more usable format


library("rgdal")
library("jsonlite")
library("ggmap")
library("ggplot2")
library("viridis")



setwd("C:/Users/Kristian/Documents/GitHub/WeatherForSailing/data")


df = read.csv('wide.csv')
df$speed = sqrt(df$UGRD^2 + df$VGRD^2)

map = get_map(c(15, 55) , zoom = 4, maptype = 'satellite')





# fix some easy way to change this
fname = "45N,60N,30W,0W02-00.grb"

gribdata = readGDAL(fname)
df2 = as.data.frame(gribdata)
rm(gribdata)

df2$speed = sqrt(df2$band1^2 + df2$band2^2)



setwd("C:/Users/Kristian/Documents/GitHub/WeatherForSailing")




p = ggmap(map) +
  geom_tile(data = df, aes(x = x, y = y,  fill = speed), alpha = 0.6) +
  geom_contour(data = df, aes(x = x, y = y, z = speed, colour = ..level..), bins = 5) +
  scale_fill_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 8) +
  scale_color_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 8) +
  theme_nothing()


p


q = ggmap(map) +
  geom_tile(data = df2, aes(x = x, y = y,  fill = speed), alpha = 0.6) +
  geom_contour(data = df, aes(x = x, y = y, z = speed, colour = ..level..), bins = 5) +
  scale_fill_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 8) +
  scale_color_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 8) +
  theme_nothing()

q


#ggsave('map-eu3.png')



library('maps')

world = map_data("world")

worldmap = ggplot(world,aes(x = long, y = lat, group = group)) +
  geom_polygon(fill = 'white', colour = 'black') +
  geom_tile(data = df, aes(x = x, y = y,  fill = speed, alpha = speed), alpha = 0.6, inherit.aes = F) +
  geom_contour(data = df, aes(x = x, y = y, z = speed, colour = ..level..), bins = 5, inherit.aes = F) +
  scale_fill_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 8) +
  scale_color_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 8) +
  scale_y_continuous(breaks = (-2:2) * 30) +
  scale_x_continuous(breaks = (-4:4) * 45) +
  coord_map("ortho", orientation = c(50,12,0))

worldmap

