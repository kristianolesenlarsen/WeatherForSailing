# This is so far the only way i've been able to get GRIB data to a more usable format


install.packages(c('rgdal', 'viridis'))

library("rgdal")
library("jsonlite")
library("ggmap")
library("ggplot2")
library("viridis")



setwd("C:/Users/Kristian/Documents/GitHub/WeatherForSailing/data")

# fix some easy way to change this
fname = "25N,70N,300W,30W29-00.grb"
#fname = "gfsanl_4_20170726_0000_006.grb2"


gribdata = readGDAL(fname)
df = as.data.frame(gribdata)


df$speed = sqrt(df$band1^2 + df$band2^2)
df$unif = runif(length(df$x),0,1)

map = get_map(c(5, 55) , zoom = 3, color = 'bw')


setwd("C:/Users/Kristian/Documents/GitHub/WeatherForSailing")



p = ggmap(map) +
#  geom_point(data = df, aes(x = x, y = y))# +
#  geom_segment(data = subset(df, unif < 0.1), aes(x = x, y = y, xend = x + band1*0.01, yend = y+band2)) +
  geom_tile(data = df, aes(x = x, y = y, z = speed, fill = speed),  alpha = 0.3) +
  geom_contour(data = df, aes(x = x, y = y, z = speed, colour = ..level..), alpha = 0.6) +
  scale_color_viridis(option = "plasma") +
  scale_fill_viridis(option = "plasma") +
  theme_nothing()


p

ggsave('map-eu.png', p)
