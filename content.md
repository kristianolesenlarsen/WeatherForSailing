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
          <a class="navbar-brand" href="test.html">WeatherForSailing</a>
        </div>
        <ul class="nav navbar-nav">
          <li class="active"><a href="content.html">Top</a></li>
          <li><a href="#p1">Wind compass</a></li>
          <li><a href="#p2">Wind vectors</a></li>
          <li><a href="#p3">Wind systems</a></li>
        </ul>
      </div>
    </nav>

<!-- /NAVBAR -->

<!-- PART 1 -->
      <h3>Wind compass</h3>
      <a name = "p1">

      <div class="row">
        <div class="col-md-8">
        <div class="center">
        <script src="js/compass.js" class = "img-responsive"></script>
        </div>
        </div>
        <div class="col-md-4">This chart shows the development of wind for the following 48 hours after last update, starting from the dot.</div>
      </div>

<!-- /PART 1 -->
<!-- PART 2 -->
      <h3> Local wind vectors </h3>
      <a name = "p2">

      <div class="row">
        <div class="col-md-4">
        Current wind directions around vessel, color represent temperatures with red being hot and blue cold. Note wind direction data are not very reliable and shouldn't be considered final.
        </div>
        <div class="col-md-8">
        <img class ="img-responsive" src="map.png">
        </div>

<!-- /PART 2 -->
<!-- PART 3 -->

        <h3>Large scale wind systems</h3>
        <a name="p3">

        <div class="row">
          <div class="col-md-8">
          <img class="img-responsive" src="map-eu2.png">
          </div>
          <div class="col-md-4"> Lorem Ipsum</div>
        </div>
<!-- /PART 3 -->


<!--    </div> -->
    </div> <!-- /container -->

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../../../assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
