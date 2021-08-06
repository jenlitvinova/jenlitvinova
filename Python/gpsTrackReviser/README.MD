GPS-Track Reviser is a QGIS plugin that was developed as part of my MSc in Geospatial Technologies curriculum. The purpose of this plugin is to rectify the incorrect timestamps that
result from the conversion from .gpx to .shp using ogr2ogr. 

– Input: Converted Shapefile with points + original GPX file
– Output: Corrected Shapefile with rectified timestamps

Required elements in GUI:
– GPX and SHP file selection (start with simple textfield first and try QFileDialog later)

Rough workflow:
1. Parse GPX file and store values
2. Iterate over features in Shapefile and update the timestamp
3. Add Shapefile to map view
