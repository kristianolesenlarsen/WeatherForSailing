---
layout: null
---


<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../../../favicon.ico">

    <title>Weather data content</title>

    <!-- Bootstrap core CSS -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/css/bootstrap-theme.css" rel="stylesheet">


    <!-- Custom styles for this template -->
    <link href="assets/css/grid.css" rel="stylesheet">
  </head>

  <body>
    <div class="container">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>



<!-- NAVBAR -->
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="index.html">WeatherForSailing</a>
        </div>
        <ul class="nav navbar-nav">
          <li class="active"><a href="content.html">Top</a></li>
          <li><a href="#p1">Wind compass</a></li>
          <li><a href="#p2">Wind systems</a></li>
          <li><a href="#p21">Temperatures</a></li>
          <li><a href="#p3">Wind vectors</a></li>
          <li><a href="#p4">Thermometer</a></li>
        </ul>
      </div>
    </nav>

<!-- /NAVBAR -->

<!-- PART 1 -->
      <a name = "p1"></a>
      <h3>Wind compass</h3>


      <div class="row">
        <div class="col-md-8">
        <script src="js/compass.js" class = "img-responsive"></script>

        </div>
        <div class="col-md-4">This chart shows the development of wind for the following 48 hours after last update, starting from the dot. It's constructed with the <code> plots.webready_plotly_winddir(weather)</code> function, which takes <code>weather</code> as it's returned from <code>weather.fromDarkskyAPI().get_weather_at_loc</code>. This function requires a key to the DarkSky Api.
        </div>
      </div>
<!-- /PART 1 -->

<!-- PART 2 -->
        <a name = "p2"></a>
        <h3> Atlantic winds </h3>
        <div class="row">
          <div class="col-md-4">
          This plot shows the windspeeds across the Atlantic Ocean and Europe, with <span style="color:yellow"> yellow </span> being the fastest, and the almost transparent <span style="color:blue"> blue </span> being low winds. Data are gathered from GRIB files from Saildocs.
        </div>
        <div class="col-md-8">
          <img class ="img-responsive" src="plots/Windspeed.png">
        </div>
<!-- /PART 2 -->

<!-- PART 2.1 -->
      <a name="p21"></a>
      <h3> 2M air temperatures </h3>

      <div class="row">
        <div class="col-md-8">
          <img class="img-responsive" src="plots/Temp.png">
        </div>
        <div class="col-md-4">
          This map shows air temperatures 2 meters above ocean level.

        </div>
      </div>
<!-- /PART 2.1 -->

<!-- PART 3 -->
        <a name = "p3"></a>
        <h3> Local wind vectors </h3>
        <div class="row">
          <div class="col-md-4">
          Current wind directions around vessel, color represent temperatures with red being hot and blue cold. Note wind direction data are not very reliable and shouldn't be considered final.
        </div>
        <div class="col-md-8">
          <img class ="img-responsive" src="plots/map.png">
        </div>
<!-- /PART 3 -->
<!-- PART 4 -->
      <a name="p4"></a>
      <h3>Current temperature</h3>

      <div class="row">
        <div class="col-md-8">
        <object data="svg/temp_now.svg" type="image/svg+xml" class = "img-responsive"></object>
        </div>
        <div class="col-md-4">
        Gauges the current temperature. This is made with the python module <code>pygal</code> which provide a nice and easy interface to produce a number of standard plots. For example this was made only by importing pygal and calling
        <br>
        <pre><code> def show_temperature(weather, name):
            gauge_chart = pygal.Gauge(human_readable=True, style = custom_style)
            gauge_chart.title = 'Current temperature'
            gauge_chart.range = [0, 35]
            gauge_chart.add('temperature', weather['currently']['temperature'])
            return gauge_chart.render_to_file('./svg/' + name + '.svg')
        </code></pre>
        </div>
      </div>
<!-- /PART 2 -->

<!-- FOOTER -->
<footer class="footer">
    <div class="container">
      <span class="text-muted">Weather data supplied by <a href="https://darksky.net/poweredby">DarkSky.net</a>, <a href="openweathermap.org/">OpenWeatherMap</a> and GRIB data from <a href ="http://saildocs.com/">Saildocs</a>. Last updated <script src="js/time.js"></script>
      </span>
    </div>
  </footer>
<!-- /FOOTER -->


   </div>
    </div> <!-- /container -->

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../../../assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
