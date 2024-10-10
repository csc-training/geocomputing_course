# GIS tools

* Puhti has the widest GIS software portfolio of the CSC supercomputers, and possibly of all supercomputers in the world.
* Pre-installed software makes it easy to start working on Puhti.
* GIS tools are originally not planned for supercomputers -> limited ability to utilize the computing power.
* GIS installations at CSC have been done partly with GeoPortti funding.

## GIS tools available in Puhti

* [Ames Stereo Pipeline](https://docs.csc.fi/apps/ames-stereo/) for processing stereo images
* [ArcGIS Python API](https://docs.csc.fi/apps/arcgis/) 
* [CloudCompare](https://docs.csc.fi/apps/cloudcompare/) for visualizing, editing and processing point clouds
* [FORCE](https://docs.csc.fi/apps/force/) for mass-processing of medium-resolution satellite images
* [GDAL](https://docs.csc.fi/apps/gdal/) for geospatial data formats
* **[Geoconda](https://docs.csc.fi/apps/geoconda/)** - Python spatial analysis libraries
* [GRASS GIS](https://docs.csc.fi/apps/grass/) - General purpose GIS software family for viewing, editing and analysing geospatial data
* [LAStools](https://docs.csc.fi/apps/lastools/) for LiDAR datasets
* [MATLAB](https://docs.csc.fi/apps/matlab/)
* [OpenDroneMap](https://docs.csc.fi/apps/opendronemap/) for processing aerial drone imagery
* [Orfeo ToolBox](https://docs.csc.fi/apps/otb/) for remote sensing applications
* [PCL](https://docs.csc.fi/apps/pcl/) for 2D/3D image and point cloud processing
* [PDAL](https://docs.csc.fi/apps/pdal/) for point cloud translations and processing
* [QGIS](https://docs.csc.fi/apps/qgis/) - General purpose GIS software family for viewing, editing and analysing geospatial data
* **[R for GIS](https://docs.csc.fi/apps/r-env-for-gis/)** - R spatial analysis libraries
* [SAGA GIS](https://docs.csc.fi/apps/saga-gis/) - General purpose GIS software family for viewing, editing and analysing geospatial data
* [Sen2Cor](https://docs.csc.fi/apps/sen2cor/) for atmospheric, terrain and cirrus correction of the Sentinel-2 products
* [Sen2mosaic](https://docs.csc.fi/apps/sen2mosaic/) for downloading, preprocessing and mosaicing of Sentinel-2 products
* **[SNAP](https://docs.csc.fi/apps/snap/)** for remote sensing applications
* [WhiteboxTools](https://docs.csc.fi/apps/whiteboxtools/) - An advanced geospatial data analysis platform
* [Zonation](https://docs.csc.fi/apps/zonation/) - Spatial conservation prioritization framework
* **[pytorch](https://docs.csc.fi/apps/pytorch/)** for deep learning
* **[tensorflow](https://docs.csc.fi/apps/tensorflow/)** for deep learning 


## GIS tools available in Mahti

* [Geoconda](https://docs.csc.fi/apps/geoconda/) - Python spatial analysis libraries
* [pytorch](https://docs.csc.fi/apps/pytorch/) for deep learning
* [tensorflow](https://docs.csc.fi/apps/tensorflow/) for deep learning 

## GIS tools available in LUMI

* [GDAL](https://docs.csc.fi/apps/gdal/) for geospatial data formats
* [GRASS GIS](https://docs.csc.fi/apps/grass/) - General purpose GIS software family for viewing, editing and analysing geospatial data
* [PDAL](https://docs.csc.fi/apps/pdal/) for point cloud translations and processing
* [QGIS](https://docs.csc.fi/apps/qgis/) - General purpose GIS software family for viewing, editing and analysing geospatial data
* [SAGA GIS](https://docs.csc.fi/apps/saga-gis/) - General purpose GIS software family for viewing, editing and analysing geospatial data
* [pytorch](https://docs.csc.fi/apps/pytorch/) for deep learning
* [tensorflow](https://docs.csc.fi/apps/tensorflow/) for deep learning
* Additional, easy to install yourself [EasyBuild recepies](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs) for CGAL, GDAL, GEOS, ncview, PROJ, R.


:::{admonition} GIS tools NOT available on supercomputers
:class: caution

* **Servers** -> these can be run in cPouta
	* Web map servers:
		* GeoServer, MapServer
	* Database:
		* PostGIS, MongoDB
	* Web map services:
		* OpenLayers, Leaflet
	* [Installation guidelines for ArcPy, GeoServer, MetaShape, PostGIS and containers (for example OpenDroneMap) in cPouta](https://github.com/csc-training/geocomputing/tree/master/pouta).
* Tools available for **Windows only** -> no good option from CSC services
	* ArcGIS, TerraScan

:::

:::{admonition} Commercial tools
:class: seealso, dropdown

* MATLAB:
	* Users from universities: license from university + CSC license -> OK
 	* Users from research institutes: need own licence, because MathWorks considers research institute users as commercial
* LasTools:
	* Some tools available for "free"
   	* No license from CSC
  	* Easy to use your own license
* ArcGIS Python API:
	* For many tools, a connection to ArcGIS Online is required.
* In general, only tools with floating licenses can be used
 	* Tools with node-locked licenses -> cPouta  
:::

## GIS tools with R, Python or CLI support

| Software | R | Python | CLI | 
| --- | --- | --- | --- |
| CloudCompare | - | [CloudComPy*](https://www.simulation.openfields.fr/documentation/CloudComPy/html/) | Yes |
| GRASS | [rgrass*](https://cran.r-project.org/web/packages/rgrass/index.html) | [GRASS GIS Python libraries](https://grass.osgeo.org/grass82/manuals/libpython/index.html) | [Yes](https://grasswiki.osgeo.org/wiki/Shell_scripting) |
| OrfeoToolBox | - | [OTB Python API*](https://www.orfeo-toolbox.org/CookBook/PythonAPI.html) | [Yes](https://www.orfeo-toolbox.org/CookBook/CliInterface.html) |
| PDAL | - | [pdal](https://pdal.io/en/latest/python.html) | [Yes](https://pdal.io/en/latest/apps/index.html) |
| QGIS | [qgisprocess*](https://cloud.r-project.org/web/packages/qgisprocess/index.html) | [PyQGIS](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/) | [qgis_process](https://docs.qgis.org/latest/en/docs/user_manual/processing/standalone.html) |
| SagaGIS | [Rsagacmd](https://cran.r-project.org/web/packages/Rsagacmd/index.html) | PySAGA* | [saga_cmd](https://sourceforge.net/p/saga-gis/wiki/Executing%20Modules%20with%20SAGA%20CMD/) |
| SNAP | - | [snappy](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python), [snapista](https://snap-contrib.github.io/snapista/gettingstarted.html) | [GPT](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/70503475/Bulk+Processing+with+GPT) |
| WhiteboxTools | [whiteboxR*](https://github.com/opengeos/whiteboxR) | [WhiteboxTools](https://www.whiteboxgeo.com/manual/wbt_book/python_scripting/using_whitebox_tools.html)| [Yes](https://www.whiteboxgeo.com/manual/wbt_book/command_prompt.html) |

Additionally Ames Stereo Pipeline, FORCE, LasTools, OpenDroneMap, PCL and Zonation have a command-line interface.

\* are not available in Puhti currently, but should be possible to install, ask if you need any of them.


:::{admonition} Modules
:class: important

* Supercomputers are a shared computing environment with many mutually incompatible tools installed
* By default only basic Linux tools are available
* Pre-installed tools are available via modules
* One module: single program or group of similar programs
* Usage:
	* Check documentation for available module names and versions.
 	* Load on or more modules -> the system can find the provided tools
	* Use tools from the loaded module(s)

Example: loading the module for GDAL

```
module load gdal
gdalinfo /xx/data.tif
```

:::

## Documentation

* [CSC Docs: Applications -> geosciences](https://docs.csc.fi/apps/by_discipline/#geosciences)
* [LUMI Docs: Software pages](https://docs.lumi-supercomputer.eu/software/)
* [CSC Research pages: GIS software](https://research.csc.fi/gis-software)
* [Geocomputing examples](https://github.com/csc-training/geocomputing)
