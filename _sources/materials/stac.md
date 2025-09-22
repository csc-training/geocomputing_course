# STAC

STAC - Spatio-Temporal Asset Catalog

## STAC - background

* Started in 2018, rapidly developing
* New de facto metadata and **search standard**
* **Describes datasets at the level of individual files**
* It is most commonly used for remote sensing data, but it is suitable for any data with time and location information.
* Users: ESA, USGS, Microsoft Planetary computer, Google Earth Engine
* In Finland: FMI and CSC.

## STAC concepts
![](./images/STAC.png)

## Search with STAC API

* Suitable also for very big datasets
* Main focus on Item level
* Search criteria:
    * Collection
    * **Location**: point, bbox, GeoJSON polygon
    * **Time**
    * Optional other Item values, for example cloud coverage

## Tools for working with STAC

* In web browser: **STAC Browser**, STAC Index
* QGIS: STAC plugin
* **Python: pystac-client, stackstac, xarray and dask**
* R: rstac, gdalcubes
* PDAL: STAC reader
* ArcGIS for Python API
* Java, Julia, Ruby, Scala...

## CSC Paituli STAC, Finnish spatial datasets

* ~100 different datasets, inlcuding:
* [Paituli raster datasets](https://paituli.csc.fi/metadata.html)
   * LUKE, erosion risk maps
   * LUKE, topographic wetness index
   * LUKE, snow damage risk
   * NLS, orthophoto and infrared orthophoto*, 1996->
   * NLS, basic and topographic maps*, 2005->
   * FMI, historic weather in 10km grids*: min/mean/max temperature, precipitation, snow, sea level air pressure, humidity, radiotion, 1961->
* [GeoPortti Geocubes datasets](https://vm0160.kaj.pouta.csc.fi/geocubes/datasets/)
   * Finnish Forest center, Forest stand class
   * FMI, Wind
   * GTK, Superficial deposits
   * **NLS, Orthophoto\***
   * MAVI, Field parcels
   * **SYKE, Corine Land Cover**
   * **SYKE, Vegetation height**
* [FMI Tuulituhohaukka](https://pta.data.lit.fmi.fi/stac/root.json)
   * **ESA/FMI, Sentinel-1 daily and 11 days backscatter mosaics: VV and VH polarisation.**
   * **ESA/FMI, Sentinel-2 11-days and annual surface reflectance mosaics.**
   * **ESA/SYKE, Sentinel-2 monthly index mosaics: NDVI, NDBI, NDMI, NDSI, NDTI.**
   * ESA, Sentinel-1 backscatter tiles: VV and VH polarisation.
   * USGS/SYKE, Landsat (4 and 5) yearly index mosaics: NDVI, NDBI, NDMI, NDSI, NDTI.
   * **NLS, Digital terrain model products: DTM, aspect, slope.**
   * **Finnish Forest center, Canopy height model.**
   * **LUKE, Multi-source forest inventory products.**
   * LUKE, Forest wind damage risk map.
   * FMI, Daily wind damage risk map.
* ESA, **[Sentinel-2 products](https://a3s.fi/sentinel-readme/README.txt)**, processed to Level-2A (Surface Reflectance), a selection of mostly cloud-free products from Finland. Downloaded to CSC Allas by Maria Yli-Heikkilä (LUKE), Arttu Kivimäki (NLS/FGI) and Matias Heino (Aalto).

\* These datasets have several bands in one file, Python `stackstac` does not support it, but search works.


 
:::{admonition} Next steps 
:class: important

* Read more about STAC in general from [Paituli STAC description](https://paituli.csc.fi/stac.html)
* [See what data is available with Paituli STAC](https://radiantearth.github.io/stac-browser/#/external/paituli.csc.fi/geoserver/ogc/stac/v1?.language=en)
* **Test out the example scripts**:
    * **[Python](https://www.github.com/csc-training/geocomputing/blob/master/python/STAC)**
    * [R](https://www.github.com/csc-training/geocomputing/blob/master/R/STAC)
* Use Paituli STAC, end-point: `https://paituli.csc.fi/geoserver/ogc/stac/v1`
::: 
