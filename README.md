# A site for providing weather information suitable to sailors
... or at least experimenting with the idea.

Please note this is all very much under development.

## getting weather data from GRIB files
NOAA releases GRIB files with weather global weather forecasts from the GFS model, but collecting these directly from the NOAA haven't worked for me yet. Instead i collect them via [saildocs](saildocs.com), which serves certain variables of GFS forecasts via email. `GET_A_GRIB.py` contains code to collect and unpack these.

### Getting GRIB by email
To use this you need a gmail account with a folder named >saildocs<, and manually tell gmail to store mail from saildocs here. You also need a .py file named `keys.py` with the following content:

```python
user = "YOUR_EMAIL_ADDRESS@gmail.com"
pwd = "YOUR_GOOGLE_APP_PASSWORD"
```
If you dont use 2-factor authentication on your google account you should consider activating it, or you might need to modify this a bit.

the function `genMailQuery()` produces valid queries for saildocs, and required the lat-lon bounding box as parameters, as well as a range of optional parameters for forecast variables and forecast times.

`sendMailQuery()` interacts with your gmail account to send requests to saildocs, while `getMailAttachment` downloads the latest received email (this is possibly dependent on your gmail account sorting mails by date) and stores the attached GRIB file in `./data/raw` (to change this modify it in GET_A_GRIB.py).

Finally `getMailWrapper()` is a wrapper around all the email-related functions, which automatically send a request and downloads the response, while ensuring to sleep long enough for the email to be received before trying to download. It tak

```python
""" getMailWrapper - a wrapper to get grib data from saildocs
 - user: a gmail address
 - pwd: password for the gmail account
 - latBottom: lowest latitude northward
 - latTop: highest latitude northward
 - lonLeft: leftmost longitude eastward
 - lonRight: rightmost longitude eastward
 - model: saildocs parameter for model
 - inc: grid increment
 - params: variables to get in grib file
 - timestring: forecast hours (you can get 00, 24, 48, 72... 180)
 - subscribe: if true, you subscribe to updated GRIBS of the same area
 - send: if false the request to saildocs isn't send
"""
### valid timestrings are  
# 0,3,...,180 hrs

### valid model parameters:
# PRMSL: mean sea-level pressure
# WIND: surface wind gradient
# HGT: 500mb (milibars) height above sea-level
# SEATMP: sea temperature
# AIRTMP: air temperature
# WAVES: wave height
```
Thus getting GRIB files should be as simple ass calling `getMailWrapper()` with the above parameters supplied.

### Unpacking GRIB files
The function `GRIBtoDict()` uses GDAL to convert GRIB data to a dictionary, and `fromDictToWindJSON()` converts dictionaries produced by the previous function to json files that resembles those produced by the grib2json utility. __Note:__ _there are issues with projections and orientation when converting between grib files and dicts/jsons. Don't expect these functions to behave as intended._


## Getting weather data from various API's.

The file `weather.py` contains three classes, two of which are designed to access API's. The last class is simply a couple of functions used to pack api responses as csv files.

`class fromOpenAPI()` Contains functions to interact with the openweatherdata API. To see which requests are supported, look at the code. It should be fairly straight forward what is required. Like the GRIB files this relies on you creating a `keys.py` file, with the relevant authorization codes for the API.

`class fromDarkskyAPI()` is similar to the above, but uses the DarkSky API. Note that darksky charges money for using their API for more than 1000 requests per day.

## Plotting
`plots.py` contains definitions for a number of plots, while `runplots.py` gathers all the required data from API's and GRIB files and then runs the plots from `plots.py` use these as you like. `map.html` contains the leaflet map with wind animations and requires GRIB data to work.

the `.R` files contain various attempts at plotting maps as well. Not all are used on the webpage.



### Interactive Map
The map is heavily reliant on [danwild/leaflet-velocity](https://github.com/danwild/leaflet-velocity?files=1) and in turn all the work he credits.
