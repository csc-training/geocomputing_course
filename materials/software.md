# GIS tools

## GIS tools available in Puhti

* [Ames Stereo Pipeline](https://docs.csc.fi/apps/ames-stereo.md) for processing stereo images
* [ArcGIS Python API](https://docs.csc.fi/apps/arcgis.md) 
* [CloudCompare](https://docs.csc.fi/apps/cloudcompare.md) for visualizing, editing and processing poing clouds
* [FORCE](https://docs.csc.fi/apps/force.md) for mass-processing of medium-resolution satellite images
* [GDAL](https://docs.csc.fi/apps/gdal.md) for geospatial data formats
* [Geoconda](https://docs.csc.fi/apps/geoconda.md) - Python spatial analysis libraries
* [GRASS GIS](https://docs.csc.fi/apps/grass.md) General purpose GIS software family for viewing, editing and analysing geospatial data
* [LAStools](https://docs.csc.fi/apps/lastools.md) for LiDAR datasets
* [OpenDroneMap](https://docs.csc.fi/apps/opendronemap.md) for processing aerial drone imagery
* [Orfeo ToolBox](https://docs.csc.fi/apps/otb.md) for remote sensing applications
* [PCL](https://docs.csc.fi/apps/pcl.md) for 2D/3D image and point cloud processing
* [PDAL](https://docs.csc.fi/apps/pdal.md) for point cloud translations and processing
* [QGIS](https://docs.csc.fi/apps/qgis.md) General purpose GIS software family for viewing, editing and analysing geospatial data
* [R for GIS](https://docs.csc.fi/apps/r-env-for-gis.md) R spataial analysis libraries
* [SAGA GIS](https://docs.csc.fi/apps/saga-gis.md) General purpose GIS software family for viewing, editing and analysing geospatial data
* [Sen2Cor](https://docs.csc.fi/apps/sen2cor.md) for atmospheric-, terrain and cirrus correction of the Sentinel-2 products
* [Sen2mosaic](https://docs.csc.fi/apps/sen2mosaic.md) for download, preprocessing and mosaicing of Sentinel-2 products
* [SNAP](https://docs.csc.fi/apps/snap.md) for remote sensing applications
* [WhiteboxTools](https://docs.csc.fi/apps/whiteboxtools.md) an advanced geospatial data analysis platform
* [Zonation](https://docs.csc.fi/apps/zonation.md) Spatial conservation prioritization framework
* [pytorch](https://docs.csc.fi/apps/pytorch.md) for deep learning
* [tensorflow](https://docs.csc.fi/apps/tensorflow.md) for deep learning 


## GIS tools available in Mahti

* [Geoconda](geoconda.md) - Python spatial analysis libraries
* [pytorch](https://docs.csc.fi/apps/pytorch.md) for deep learning
* [tensorflow](https://docs.csc.fi/apps/tensorflow.md) for deep learning 

## GIS tools available in LUMI

* [GDAL](https://docs.csc.fi/apps/gdal.md) for geospatial data formats
* [GRASS GIS](https://docs.csc.fi/apps/grass.md) General purpose GIS software family for viewing, editing and analysing geospatial data
* [PDAL](https://docs.csc.fi/apps/pdal.md) for point cloud translations and processing
* [QGIS](https://docs.csc.fi/apps/qgis.md) General purpose GIS software family for viewing, editing and analysing geospatial data
* [SAGA GIS](https://docs.csc.fi/apps/saga-gis.md) General purpose GIS software family for viewing, editing and analysing geospatial data
* [pytorch](https://docs.csc.fi/apps/pytorch.md) for deep learning
* [tensorflow](https://docs.csc.fi/apps/tensorflow.md) for deep learning 

## Documentation
* [Puhti and Mahti softwate pages](https://docs.csc.fi/apps/by_discipline/#geosciences)
* [LUMI software pages](https://docs.lumi-supercomputer.eu/software/)

 Something missing?
      Ask us :)
      servicedesk@csc.fi

## Geospatial software NOT available in supercomputers

* Servers -> these can be run in cPouta
	* Web map servers
		* GeoServer, MapServer
	* Database
		* PostGIS, MongoDB
	* Web map services
		OpenLayers, Leaflet
	* [Installation guidelines for ArcPy, GeoServer, MetaShape, PostGIS and containers (for example OpenDroneMap) in cPouta](https://github.com/csc-training/geocomputing/tree/master/pouta).
* Tools available for Windows only -> no good option from CSC services
	* ArcGIS, TerraScan 
	
## Modules

* Puhti is a shared computing environment 
* Software is loaded with modules
	* Mutually incompatible software
	* One module: single program or group of similar programs
	* Modules load applications, adjust path settings and set environment variables
	* Check documentation for available module names and versions.

Example. Loading module for R

```
module load r-env 
```



	