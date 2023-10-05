# Spatial data in Puhti

* Large commonly used **Finnish geospatial datasets with open license**
* Removes transfer bottleneck
* Located at: `/appl/data/geo/`
* **All Puhti users have read access**

* ~13 TB of datasets available:
	* Paituli data, with virtual mosaics for raster data
	* Finnish Environmental Institute (SYKE) open datasets
	* LUKE Multi-source national forest inventory: 2013, 2015, 2017, 2019 and 2021.
	* Forest center: canopy height, forest mask, gridcells, forest resource plots

* [CSC Docs: Spatial data in CSC computing environment](https://docs.csc.fi/data/datasets/spatial-data-in-csc-computing-env/)

## Paituli

* **Spatial data download service**
* ~300 Finnish datasets
* All datasets open to everyone
* Also historical versions of several datasets
* Possibility to publish own datasets for universities and research institutes
* OKM supports financially, CSC maintains, free of charge for end users
* [Paituli service](https://paituli.csc.fi)

Paituli data access in Puhti:

* As files in `/appl/data/geo/`
* Majority via OGC APIs, both old and new standards
* **Raster datasets via [STAC](stac.md)**

### Some popular datasets

* NLS, administrative borders
* **NLS, topographic database**
* NLS, basic map and topographic maps
* NLS, DEM - 2, 10 and 25m
* **NLS, orthoimages (only infrared in Puhti)**
* Statistics Finland, population grid 1 km
* Statistics Finland, municipalities key figures
* Statistics Finland, educational institutions
* **Väylä, Digiroad**
* Statistics Finland, traffic accidents
* Statistics Finland, Paavo - statistics at post code level
* **NLS, lidar**
* Finnish Digital agency, addresses of buildings
* LUKE, occurrence map for less common tree species
* Finnish Food Agency, Field plots
* **FMI, daily and monthly weater statistics and predictions**
* University of Helsinki, Luomus, biodiversity threats
