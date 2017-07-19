---
layout: default
---

## Some plotly testing
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<div class="center">
<div id="2034612f-e026-43a9-b7fb-8b9cd139bfea" style="height: 100%; width: 100%;" class="plotly-graph-div"></div>

<script type="text/javascript">window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("2034612f-e026-43a9-b7fb-8b9cd139bfea", [{"type": "scatter", "r": [3.85, 4.05, 4.21, 4.29, 4.35, 4.39, 4.43, 4.49, 4.64, 4.81, 4.95, 5.01, 5.04, 5.09, 5.15, 5.23, 5.39, 5.58, 5.81, 6, 6.16, 6.27, 6.27, 6.1, 5.82, 5.52, 5.22, 4.88, 4.54, 4.24, 3.95, 3.65, 3.31, 2.95, 2.62, 2.32, 2.05, 1.84, 1.6, 1.39, 1.35, 1.38, 1.67, 2.62, 1.63, 1.94, 1.42, 1.54, 2.52], "t": [138, 135, 130, 125, 120, 116, 113, 111, 111, 112, 111, 109, 106, 104, 105, 107, 109, 110, 111, 113, 117, 121, 124, 124, 124, 123, 121, 121, 121, 118, 115, 113, 112, 111, 109, 102, 93, 89, 97, 107, 104, 88, 31, 351, 347, 56, 83, 98, 111], "mode": "lines", "name": "Wind direction", "text": [16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "marker": {"color": "none", "line": {"color": "#E95355", "width": 2}}}, {"type": "scatter", "r": [3.85, 3.85, 3.85, 3.85, 3.85], "t": [138, 138, 138, 138, 138], "mode": "markers", "name": "time=now", "marker": {"color": "none", "line": {"color": "#E95355", "width": 2}}}], {"title": "Wind direction and -speed", "showlegend": false, "font": {"size": 16}, "legend": {"font": {"size": 16}}, "radialaxis": {"ticksuffix": "m/s"}, "orientation": -90}, {"showLink": true, "linkText": "Export to plot.ly"})
</script>
</div>

## risk of rain

<div class="left">
<object data="svg/rain.svg" type="image/svg+xml"></object>
</div>
  <div class = "right"> 8-day forecast for the risk of rain or other precipation and the cloud cover fraction </div>



## Current temperature

  <span class = "left"> Gauges the current temperature </span>
  <div class = "right"><object data="svg/temp_now.svg" type="image/svg+xml"></object></div>



# Temperature for the next 48 hours

  <div class = "left"> <object data="svg/temp_overday.svg" type="image/svg+xml"> </div>
  <span class = "right"> Temperatures for the comming 48 hours </span>



## ... and for the next 8 days
<div class="lr">
  <span class = "left"> and over the nex 8 days </span>
  <span class = "right"><img src="svg/temp_overdays.svg" /></span>
</div>

# Wind bearing
<div class="lr">
  <span class = "left"> <img src="svg/windbearing_line.svg" /> </span>
  <span class = "right"> Wind-bearing for the comming 48 hours </span>
</div>

<div class="lr">
  <span class = "left"> <img src="svg/windbearing_radar.svg" /> </span>
  <span class = "right"> Radar format </span>
</div>


## windspeed and windgusts
<div class="lr">
  <span class = "left"> Shows the average wind speed alone and as a fraction of the highest recorded gusts </span>
  <span class = "right"><img src="svg/windspeed.svg" /></span>
</div>
