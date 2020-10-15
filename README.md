# INAGE 2 GeoJSON

Converts an image file to GeoJSON.


## Installing

`pip install image2geojson`


## Usage

~~~
usage: image2geojson [-h]
                   file output lat lng

positional arguments:
    file            source image
    output          output GeoJSON file
    lat             latitude of the center point
    lng             longitude of the center point

~~~

## Example

~~~
$ image2geojson screen.png output.json 47.11122 3.1291276
~~~
