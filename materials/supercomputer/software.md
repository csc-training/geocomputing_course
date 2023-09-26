## GIS tools available on Puhti

* [Ames Stereo Pipeline](ames-stereo.md) for processing stereo images
* [ArcGIS Python API](arcgis.md) 
* [CloudCompare](cloudcompare.md) for visualizing, editing and processing poing clouds
* [FORCE](force.md) for mass-processing of medium-resolution satellite images
* [GDAL](gdal.md) for geospatial data formats
* [Geoconda](geoconda.md) - Python spatial analysis libraries
* [GRASS GIS](grass.md) General purpose GIS software family for viewing, editing and analysing geospatial data
* [LAStools](lastools.md) for LiDAR datasets
* [OpenDroneMap](opendronemap.md) for processing aerial drone imagery
* [Orfeo ToolBox](otb.md) for remote sensing applications
* [PCL](pcl.md) for 2D/3D image and point cloud processing
* [PDAL](pdal.md) for point cloud translations and processing
* [QGIS](qgis.md) General purpose GIS software family for viewing, editing and analysing geospatial data
* [R for GIS](r-env-for-gis.md) R spataial analysis libraries
* [SAGA GIS](saga-gis.md) General purpose GIS software family for viewing, editing and analysing geospatial data
* [Sen2Cor](sen2cor.md) for atmospheric-, terrain and cirrus correction of the Sentinel-2 products
* [Sen2mosaic](sen2mosaic.md) for download, preprocessing and mosaicing of Sentinel-2 products
* [SNAP](snap.md) for remote sensing applications
* [WhiteboxTools](whiteboxtools.md) an advanced geospatial data analysis platform
* [Zonation](zonation.md) Spatial conservation prioritization framework
* Deep learning: pytorch, tensorflow
* [Puhti softwate pages](https://docs.csc.fi/apps/by_discipline/#geosciences)

In Mahti: geoconda, PyTorch, TensorFlow

In LUMI: 
* GDAL, QGIS, GRASS GIS, PDAL, SagaGIS, PyTorch, TensorFlow
* [LUMI software pages](https://docs.lumi-supercomputer.eu/software/)

 Something missing?
      Ask us :)
      servicedesk@csc.fi

## Geospatial software NOT available in Puhti

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



	