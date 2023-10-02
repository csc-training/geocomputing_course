# STAC

## STAC - background

* Started in 2018, rapidly developing
* New de facto metadata and search standard
* May become an OGC standard in the future.
* Describes datasets at the level of individual files.
* It is most commonly used for remote sensing data, but it is suitable for any data with time and location information.
* Users: ESA, USGS, Microsoft Planetary computer, Google
Earth Engine,
* In Finland: FMI and CSC.

## Terminology

>TODO: add images from presentation/paituli page

## Cloud-optimized file formats

* Enables partial loading of data
    * Only loads data for a specific area
    * Generalized version of the data is available
* Rasters: Cloud-Optimized GeoTiff (COG)
* Point clouds: Cloud-Optimized Point Clouds (COPC)
* Vectors: ?

## Static STAC = linked JSON files

## STAC API

STAC API
* Search API
* Fits big datasets
* Main focus on Item level
* Search criteria:
    * Collection
    * Location: point, bbox, GeoJSON polygon
    * Time
    * Optional other Item values, for example cloud coverage

## Tools for working with STAC

* Catalog search: STAC Index
* In web browser: STAC Browser
* QGIS: STAC plugin
* Python: pystac-client, stackstac, xarray and dask
* R: rstac, gdalcubes
* PDAL: STAC reader
* ArcGIS for Python API
* Java, Julia, Ruby, Scala...

> TODO: add links

## CSC Paituli STAC, Finnish spatial datasets
* ESA, Sentinel-2 products, Level-2A
* ESA/FMI, Sentinel-1 daily and 11 days backscatter mosaics: VV and VH polarisation.
* ESA/FMI, Sentinel-2 11-days and annual surface reflectance mosaics.
* ESA/SYKE, Sentinel-2 monthly index mosaics: NDVI, NDBI, NDMI, NDSI, NDTI.
* ESA, Sentinel-1 backscatter tiles: VV and VH polarisation.
* USGS/SYKE, Landsat (4 and 5) yearly index mosaics: NDVI, NDBI, NDMI, NDSI, NDTI.
* NLS, Digital terrain model products: DTM, aspect, slope.
* Finnish Forest center, Canopy height model.
* LUKE, Multi-source forest inventory products.
* LUKE, Forest wind damage risk map.
* FMI, Daily wind damage risk map.

## CSC Paituli STAC, Finnish spatial datasets

PLANS from GeoCubes:

* Finnish Forest center, Forest stand class
* FMI, Wind
* GTK, Superficial deposits
* NLS, Peatland
* NLS, Building
* NLS, Orthophoto*
* MAVI, Field parcels
* SYKE, Corine Land Cover
* SYKE, Vegetation height
* SYKE, Canopy cover

\* These datasets have several bands in on file, Python stackstac does not support it, but search works.

## CSC Paituli STAC, Finnish spatial datasets

PLANS from Paituli:

* LUKE, erosion risk maps
* LUKE, cartographic wetness index
* LUKE, topographic wetness index
* LUKE, snow damage risk
* NLS, orthophoto and infrared orthophoto*
* NLS, basic and topographic maps*, 2005->
* FMI, historic weather in 10km grids*: min/mean/max temperature, precipitation, snow, sea level air pressure, humidity, radiotion*, 1961->
* NLS, lidar ??

## CSC Paituli STAC

* Description: https://paituli.csc.fi/stac.html
* End-point: https://paituli.csc.fi/geoserver/ogc/stac
* STAC Browser Paituli STAC:lle
* Example scripts:
    * Python
    * R
* Feedback: servicedesk@csc.fi

## How to make own data available via STAC?
* Data:
    * Data in cloud-optimized format
    * Rasters: one band = one file
    * Each file must have URL or S3
* STAC
    * Static: create STAC JCON files
    * API: deploy a STAC server + add data to database
* Contact giscoord@csc.fi if you want to add to Paituli STAC

## Behind the scenes
* GeoServer OpenSearch for EO community module
* PostGIS database
* rio-stac Python tool
* GeoPortti FIRI project
* Eetu Huusko, Kylli Ek

## Further links
* Paituli STAC: https://paituli.csc.fi/stac.html
* CSC EO tutorial:
https://docs.csc.fi/support/tutorials/gis/eo_guide/
