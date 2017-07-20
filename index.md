---
layout: default
---

## Some plotly testing
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<div class="center">

<div id="f1acb939-c910-4968-bb5c-9391d448b288" style="height: 100%; width: 100%;" class="plotly-graph-div"></div>

<script type="text/javascript">window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("f1acb939-c910-4968-bb5c-9391d448b288", [{"type": "scatter", "r": [7.02, 7.22, 7.45, 7.68, 7.85, 7.93, 7.97, 7.96, 7.9, 7.81, 7.68, 7.53, 7.35, 7.19, 7.02, 6.86, 6.75, 6.75, 6.82, 6.82, 6.67, 6.46, 6.28, 6.16, 6.07, 5.99, 5.87, 5.77, 5.81, 6.11, 6.55, 6.84, 6.86, 6.72, 6.6, 6.46, 6.32, 6.23, 6.24, 6.31, 6.32, 6.24, 6.11, 6.08, 6.23, 6.46, 6.65, 6.78, 6.88], "t": [110, 113, 114, 114, 114, 115, 116, 116, 115, 111, 109, 109, 109, 109, 108, 106, 104, 104, 105, 106, 106, 105, 105, 106, 108, 109, 108, 107, 106, 104, 104, 104, 105, 107, 107, 106, 103, 101, 99, 99, 99, 98, 98, 99, 97, 96, 96, 98, 102], "mode": "lines", "name": "Wind direction", "text": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "marker": {"color": "none", "line": {"color": "#005570", "width": 2}}}, {"type": "scatter", "r": [7.02, 7.02, 7.02, 7.02, 7.02], "t": [110, 110, 110, 110, 110], "mode": "markers", "name": "time=now", "text": ["t=0"], "marker": {"color": "none", "line": {"color": "#005570", "width": 2}}}], {"title": "Wind direction and -speed", "showlegend": false, "font": {"size": 16}, "legend": {"font": {"size": 16}}, "radialaxis": {"ticksuffix": "m/s"}, "orientation": -90}, {"showLink": true, "linkText": "Export to plot.ly"})</script>
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

  <div class = "left">
  <object data="svg/temp_overday.svg" type="image/svg+xml"></object>
  </div>
  <div class = "right"> Temperatures for the comming 48 hours </div>



## ... and for the next 8 days
  <div class = "left"> and over the next 8 days </div>
  <div class = "right">
  <object data="svg/temp_overdays.svg" type="image/svg+xml"></object>
  </div>

# Wind bearing

  <div class = "left">
  <object data="svg/windbearing_line.svg" type="image/svg+xml"></object>
  </div>
  <div class = "right"> Wind-bearing for the comming 48 hours </div>


  <div class = "left">
  <object data="svg/windbearing_radar.svg" type="image/svg+xml"></object>
  </div>
  <div class = "right"> Radar format
  </div>


## windspeed and windgusts

  <div class = "left"> Shows the average wind speed alone and as a fraction of the highest recorded gusts </div>
  <div class = "right">
  <object data="svg/windspeed.svg" type="image/svg+xml"></object>
  </div>
