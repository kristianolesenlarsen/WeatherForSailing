library('ggplot2')
library('ggmap')


df = read.csv('windgrid.csv')

lat0 = max(df$lat) - (max(df$lat) - min(df$lat))/2
lon0 = max(df$lon) - (max(df$lon) - min(df$lon))/2

df$dummy = ifelse(df$lat == lat0 & df$lon == lon0,1,0)

n = ifelse(max(df$lat) - min(df$lat) >3 , 6, 7)

map = get_map(c(subset(df, dummy == 1)$lon, subset(df, dummy == 1)$lat), zoom = n, color = 'bw')


df$dx = df$speed * cos(df$direction)*0.02
df$dy = df$speed * sin(df$direction)*0.02


p <- ggmap(map) +
#  geom_point(data = df, aes(x = lon, y = lat)) +
  geom_segment(data = df, aes(x = lon, y = lat, xend = lon + dx, yend = lat + dy, color = temp),arrow = arrow(length = unit(0.05,"cm"))) +
  geom_point(data = subset(df, dummy == 1), aes(x = lon, y = lat), color = "red") +
  scale_color_gradient(low = 'blue', high = 'red') +
  theme_nothing()

ggsave(filename = 'map.png', p)
