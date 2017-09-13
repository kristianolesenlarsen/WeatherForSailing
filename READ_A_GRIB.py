import keys
import datetime
import requests
import pandas as pd
import gdal
import numpy as np
import re
import time
import json


"""
GRIB_files()
internal for storing the properties of a specific GRIB file
"""
class GRIB_file():
    def __init__(self, filepath):
        self.GRIB = gdal.Open(filepath)
        self.width = self.GRIB.RasterXSize
        self.height = self.GRIB.RasterYSize
        self.geotransform = self.GRIB.GetGeoTransform()
        self.info = gdal.Info(self.GRIB)
        self.no_bands = len([m.start() for m in re.finditer('Band', self.info)])

        # I need some kind of way to define the bbox that is more correct than these guesses
    def getTopY(self):
        place = [m.start() for m in re.finditer(',', self.filepath)][0]
        comma = [m.start() for m in re.finditer('N', self.filepath)][1]
        return int(self.filepath[place +1 : comma])

    def getLeftX(self):
        place = [m.start() for m in re.finditer(',', self.filepath)][2]
        comma = [m.start() for m in re.finditer('E', self.filepath)][1]
        return int(self.filepath[place +1 : comma])

    def get_bbox(self):
        Xgeo = lambda x, y : self.geotransform[0] + x*self.geotransform[1] + y*self.geotransform[2]
        Ygeo = lambda x, y : self.geotransform[3] + x*self.geotransform[4] + y*self.geotransform[5]

"""
GRIB_band()
Internal for storing a single grib band
"""
class GRIB_band(GRIB_file):
    def __init__(self, filepath, band_number):
        GRIB_file.__init__(self, filepath)
        self.band_number = band_number
        self.band = self.GRIB.GetRasterBand(band_number)
        self.metadata = self.band.GetMetadata_Dict()
        self.comment = [self.metadata['GRIB_COMMENT']]
        self.forecast_time = [self.metadata['GRIB_FORECAST_SECONDS']]
        self.array = self.band.ReadAsArray()
        self.projection = self.GRIB.GetProjection()

    # convert a band into a list (why do we want this?)
    def listify_band(self):
        infodict = {}
        datalist = []
        # all the metadata info
        infodict['band'] = self.band_number
        infodict['comment'] = self.metadata['GRIB_COMMENT']
        infodict['forecast'] = self.metadata['GRIB_FORECAST_SECONDS']
        infodict['id'] = self.metadata['GRIB_ELEMENT']

        for y_index in range(0,len(self.array)):                        # for each y
            for x_index in range(0,len(self.array[y_index])):           # for each x
                datalist.append(self.array[y_index][x_index])

        return [datalist, infodict]


"""
GRIB() the class you call when you want to read a grib file
"""
class GRIB(GRIB_file):
    def __init__(self, filepath):
        self.filepath = filepath
        GRIB_file.__init__(self, self.filepath)

    def read_band(self, band_number):
        return GRIB_band(self.filepath, band_number)
