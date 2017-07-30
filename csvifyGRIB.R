# This is so far the only way i've been able to get GRIB data to a more usable format


library("rgdal")
library("jsonlite")
library("ggmap")
library("ggplot2")
library("viridis")



setwd("C:/Users/Kristian/Documents/GitHub/WeatherForSailing/data")

# fix some easy way to change this
fname = "25N,70N,300W,30W29-00.grb"
#fname = '40N,60N,140W,120W29-00.grb'
#fname = "gfsanl_4_20170726_0000_006.grb2"


gribdata = readGDAL(fname)
df = as.data.frame(gribdata)
rm(gribddata)


#df$speed = sqrt(df$band4^2 + df$band7^2)
df$speed = sqrt(df$band1^2 + df$band2^2)
df$unif = runif(length(df$x),0,1)

#map = get_map(c(-130, 55) , zoom = 3, maptype = 'satellite')
map = get_map(c(5, 55) , zoom = 3, maptype = 'satellite')


setwd("C:/Users/Kristian/Documents/GitHub/WeatherForSailing")



p = ggmap(map) +
  scale_x_continuous(limits = c(min(df$x), max(df$x)), expand = c(0, 0)) +
  scale_y_continuous(limits = c(min(df$y), max(df$y)), expand = c(0, 0)) +
#  geom_point(data = df, aes(x = x, y = y))# +
#  geom_segment(data = subset(df, unif < 0.1), aes(x = x, y = y, xend = x + band1*0.01, yend = y+band2), arrow = arrow(length = unit(0.5, 'cm'))) +
  geom_tile(data = df, aes(x = x, y = y,  fill = speed, alpha = speed), alpha = 0.6) +
  geom_contour(data = df, aes(x = x, y = y, z = speed, colour = ..level..), bins = 5) +
  scale_fill_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 8) +
  scale_color_gradient2(low = 'blue', mid = 'green', high = 'yellow', midpoint = 8) +
 # scale_color_viridis(option = "inferno") +
  #scale_fill_viridis(option = "inferno") #+
  theme_nothing()

ggsave('map-eu2.png')
