# This is so far the only way i've been able to get GRIB data to a more usable format


library("rgdal")
library("jsonlite")
library("ggmap")
library("ggplot2")
library("viridis")



setwd("C:/Users/Kristian/Documents/GitHub/WeatherForSailing/data")


df = read.csv('test.csv')
df$speed = sqrt(df$UGRD^2 + df$VGRD^2)

# fix some easy way to change this
fname = "25N,70N,300W,30W29-00.grb"
#fname = '40N,60N,140W,120W29-00.grb'
#fname = "gfsanl_4_20170726_0000_006.grb2"


gribdata = readGDAL(fname)
df2 = as.data.frame(gribdata)
rm(gribdata)



min(df$x)
min(df2$x)

max(df$x)
max(df2$x)


min(df$y)
min(df2$y)

max(df$y)
max(df2$y)



df$speed = sqrt(df$IGRD^2 + df$VGRD^2)
#df$unif = runif(length(df$x),0,1)

#map = get_map(c(-130, 55) , zoom = 3, maptype = 'satellite')
map = get_map(c(5, 55) , zoom = 3, maptype = 'satellite')


setwd("C:/Users/Kristian/Documents/GitHub/WeatherForSailing")




p = ggmap(map) +
#  scale_x_continuous(limits = c(min(df$x), max(df$x)), expand = c(0, 0)) +
# scale_y_continuous(limits = c(min(df$y), max(df$y)), expand = c(0, 0)) +
#  geom_point(data = df, aes(x = x, y = y))# +
#  geom_segment(data = subset(df, unif < 0.1), aes(x = x, y = y, xend = x + band1*0.01, yend = y+band2), arrow = arrow(length = unit(0.5, 'cm'))) +
  geom_tile(data = df, aes(x = x, y = y,  fill = speed, alpha = speed), alpha = 0.6) +
  geom_contour(data = df, aes(x = x, y = y, z = speed, colour = ..level..), bins = 5) +
  scale_fill_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 8) +
  scale_color_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 8) +
 # scale_color_viridis(option = "inferno") +
  #scale_fill_viridis(option = "inferno") #+
  theme_nothing()


p


#ggsave('map-eu2.png')



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

