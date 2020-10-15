#!/usr/bin/env python
#coding:utf-8
# Author:  jluispcardenas
# Purpose: package definition file
# Created: 02.10.2020
# License: MIT License
# Copyright (c) 2020  Jose Luis Cardenas

"""
A Python library to convert images to GeoJSON.
a simple example::
    import image2geojson

    geojson = image2geojson.convert('image.png', lat=22.229, lng=-88.22, 17)

"""

VERSION = 1.0

__author__ = "jluispcardenas <jluispcardenas@gmail.com>"

AUTHOR_NAME = 'Jose Luis Cardenas'
AUTHOR_EMAIL = 'jluispcardenas@gmail.com'
CYEAR = '2020'

import os
import cv2
import math
import json
import argparse

def convert(file, output, lng, lat):
    if not os.path.isfile(file):
        print("image file does not exist")
        sys.exit(1)

    im = cv2.imread(file)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #gray = cv2.medianBlur(gray, 5)

    ret, th1 = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    geojson = {"type": "FeatureCollection", "features": []}
    for cont in contours:
        if len(cont) < 3:
            continue

        item = {"type": "Feature", "creator" : "image2geojson", "properties": None, "geometry": {"type": "Polygon", "coordinates": [[]]}}
        coordinates = []
        for p in cont:
            coordinates.append(convert_to_lonlat(p[0][0], p[0][1], lng, lat))

        coordinates.append(coordinates[0])

        item["geometry"]["coordinates"][0] = coordinates;

        geojson["features"].append(item);

    with open(output, "a") as fp:
        fp.write(json.dumps(geojson))

def convert_to_lonlat(x, y, lng, lat):
    pi = math.pi
    r_earth = 6371000

    lat_diff = (y / r_earth) * (180 / pi)
    lng_diff = (x / r_earth) * (180 / pi) / math.cos(lat * pi/180)

    new_lat = lat - lat_diff
    new_lng = lng + lng_diff

    return (new_lng, new_lat)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Source image')
    parser.add_argument('output', help='output file')
    parser.add_argument('lng', help='longitude of the center point', type=float)
    parser.add_argument('lat', help='latitude of the center point', type=float)

    args = parser.parse_args()

    file = args.file
    output = args.output
    lng = args.lng
    lat = args.lat

    convert(file, output, lng, lat)
