---
layout: default
---

# Weather summaries
**Today:** <script src="js/dailysummary.js"></script>

**This week:** <script src="js/weeklysummary.js"></script>

## 48 hour wind direction prognosis
<script src="https://unpkg.com/scrollreveal/dist/scrollreveal.min.js"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<div class="center">
<script src="js/compass.js"></script>
</div>

<script>
window.sr = ScrollReveal();
sr.reveal('.fader');
sr.reveal('.left');
sr.reveal('.right');
</script>

<div class="fader">
## Wind field
<div class = "left"> <img src="map.png"> </div>
<div class = "right"> Current wind directions around vessel </div>
</div>
## Current temperature

  <div class = "left"> Gauges the current temperature. Lorem ipsum something something lorem ipsum something something lorem ipsum something something. Lorem ipsum something something lorem ipsum something something lorem ipsum something something. Lorem ipsum something something lorem ipsum something something lorem ipsum something something. </div>
  <div class = "right">
  <object data="svg/temp_now.svg" type="image/svg+xml"></object>
  </div>


## risk of rain

  <div class="left">
  <object data="svg/rain.svg" type="image/svg+xml"></object>
  </div>
  <div class = "right"> 8-day forecast for the risk of rain (and other precipation), as well as cloud coverage. Lorem ipsum something something lorem ipsum something something lorem ipsum something something. Lorem ipsum something something lorem ipsum something something lorem ipsum something something. Lorem ipsum something something lorem ipsum something something lorem ipsum something something.
  </div>


## Temperature for the next 48 hours

  <div class = "left">
  <object data="svg/temp_overday.svg" type="image/svg+xml"></object>
  </div>
  <div class = "right"> Hourly temperatures for the coming 48 hours, notice that the second axis will vary from day to day.
  </div>



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


## About

Weather data supplied by [darksky.net](https://darksky.net/). Last updated <script src="js/dailysummary.js"></script>
