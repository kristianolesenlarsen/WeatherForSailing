library('ggplot2')
library('ggmap')
library("gganimate")



df = read.csv('windgrid.csv')


lat0 = max(df$lat) - (max(df$lat) - min(df$lat))/2
lon0 = max(df$lon) - (max(df$lon) - min(df$lon))/2

df$dummy = ifelse(round(df$lat,4) == round(lat0,4) & round(df$lon,4) == round(lon0,4) & df$time == min(df$time),1,0)
df$time_2 = as.Date(df$time_2, format = "%d-%H")

n = ifelse(max(df$lat) - min(df$lat) >3 , ifelse(max(df$lat) - min(df$lat) >6, 5, 6), 7)


f = ifelse(max(df$lat) - min(df$lat) >3 , ifelse(max(df$lat) - min(df$lat) >6, 0.1, 0.05), 0.03)

df$dx = df$speed * cos(df$direction)*f
df$dy = df$speed * sin(df$direction)*f


df_static = unique(subset(df, time == min(time)))
map = get_map(c(subset(df_static, dummy == 1)$lon, subset(df_static, dummy == 1)$lat), zoom = n, color = 'bw')


p <- ggmap(map) +
#  geom_point(data = df, aes(x = lon, y = lat)) +
  geom_segment(data = df_static, aes(x = lon, y = lat, xend = lon + dx, yend = lat + dy, color = temp),arrow = arrow(length = unit(0.08,"cm"))) +
  geom_point(data = subset(df_static, dummy == 1), aes(x = lon, y = lat), color = "red") +
  scale_color_gradient(low = 'blue', high = 'red') +
  theme_nothing()

ggsave(filename = 'map.png', p)


################################################################################
###
###

df = read.csv("./data/test2.csv")


lat0 = max(df$lat) - (max(df$lat) - min(df$lat))/2
lon0 = max(df$lon) - (max(df$lon) - min(df$lon))/2


n = ifelse(max(df$lat) - min(df$lat) >3 , ifelse(max(df$lat) - min(df$lat) >6, 5, 6), 7)


f = ifelse(max(df$lat) - min(df$lat) >3 , ifelse(max(df$lat) - min(df$lat) >6, 0.1, 0.05), 0.03)

df$dx = df$speed * cos(df$deg)*f
df$dy = df$speed * sin(df$deg)*f


map = get_map(c(lon0, lat0), zoom = n, color = 'bw')


p <- ggmap(map) +
geom_raster(data = df, aes(x = lon, y = lat, fill = temp), interpolate = TRUE, alpha = 0.4) +
#  geom_point(data = df, aes(x = lon, y = lat)) +
#  geom_segment(data = df, aes(x = lon, y = lat, xend = lon + dx, yend = lat + dy, color = temp),alpha = 0.5,arrow = arrow(length = unit(0.08,"cm"))) +
#  geom_point(data = subset(df_static, dummy == 1), aes(x = lon, y = lat), color = "red") +
scale_fill_gradient(low = 'blue', high = 'red')

p

ggsave(filename = 'temp.png', p)



################################################################################
###
###


p2 <- ggmap(map, aes(frame = time_2)) +
#  geom_point(data = df, aes(x = lon, y = lat)) +
  geom_segment(data = df, aes(frame = time, x = lon, y = lat, xend = lon + dx, yend = lat + dy, color = temp),arrow = arrow(length = unit(0.05,"cm"))) +
  geom_point(data = unique(subset(df_static, dummy == 1)), aes(x = lon, y = lat), color = "red") +
  scale_color_gradient(low = 'blue', high = 'red')

gganimate(p2, 'test.gif', interval = 0.3)
