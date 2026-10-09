# Spatial data in Roihu

* Large commonly used **Finnish geospatial datasets with open licenses**
* Removes transfer bottleneck
* **All Roihu users have read access**
* ~20 TB of datasets available:
	* **Paituli data**, with virtual mosaics for raster data
	* **Finnish Environmental Institute (SYKE) open datasets**: CORINE land use etc
	* **Forest center: canopy height**, forest mask, gridcells, forest resource plots
    * **NLS automatically classified lidar data**
* LUMI does not have spatial data on local disk.
* [CSC Docs: Spatial data in CSC computing environment](https://docs.csc.fi/data/datasets/spatial-data-in-csc-computing-env/)

## Paituli

* **Spatial data download service**
* ~300 Finnish datasets
* All datasets open to everyone
* Also **historical versions** of several datasets
* Possibility to publish own datasets for universities and research institutes
* Ministry of education and culture supports financially, CSC maintains
* [Paituli](https://paituli.csc.fi)

!["Paituli"](./images/paituli.png "Paituli")

### Paituli data access in Roihu:

* As files in `/dataset/project_2019680`
* **Raster datasets via [STAC](stac.md)**
* Rasters divided to mapsheets as **[virtual rasters](https://docs.csc.fi/support/tutorials/gis/virtual-rasters/)**
* Majority via [OGC APIs](https://paituli.csc.fi/webservices.html), both old and new standards

### Some popular datasets

* NLS, administrative borders
* **NLS, topographic database**
* NLS, basic map and topographic maps
* NLS, DEM - 2, 10 and 25m
* Statistics Finland, population grid 1 km
* Statistics Finland, municipalities key figures
* Statistics Finland, educational institutions
* **Väylä, Digiroad**
* Statistics Finland, traffic accidents
* Statistics Finland, Paavo - statistics at post code level
* **NLS, lidar**
* Finnish Digital agency, addresses of buildings
* **LUKE, Multi-source national forest inventory**
* LUKE, occurrence map for less common tree species
* Finnish Food Agency, Field plots
* **FMI, daily and monthly weater statistics and predictions**
* University of Helsinki, Luomus, biodiversity threats
