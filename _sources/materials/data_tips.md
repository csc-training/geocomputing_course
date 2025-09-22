# Best practice tips for data

- Take **backups** of important files. Data on Puhti disks is not backed up.
	- Allas is the best option for backups at CSC.
	- GitHub or similar for code.
- Supercomputer disks do not work well with **too many small files**
	- Plan your analysis in a way that too many files are not needed.
	- Keep the small files in one zip-file, unzip it only on local fast disks during the analysis. 
	- Don't create a lot of files in one folder
- [CSC Docs: Best practice performance tips for using Lustre](https://docs.csc.fi/computing/lustre/#best-practices)
- Keep data that is needed longer also in Allas.
- When working with big vector data sets, consider using a **database**:
	- Only file databases (SQLite, GeoPackage) can be kept on supercomputer disks.
	- For PostgreSQL and PostGIS use [CSC Pukki Database-as-a-service](https://docs.csc.fi/cloud/dbaas/).
	- For any other database set up virtual machine in cPouta.
- Pay attention to data pre-processing:
	- Remove unnecessary data (clip, select, generalize).
	- Index the relevant columns of your vector data for faster searches.

## Disk status

- Display usage and quota of all your disk areas: `csc-workspaces`

![](./images/disk_status.png)


- Display the amount of data and number of files within a given folder: `LUE`
- [CSC Docs: LUE tutorial](https://docs.csc.fi/support/tutorials/lue/)

```bash
module load lue
lue --display-level=2 /scratch/project_2015299/

path, total size, in dir size, % of total, % of dir
---------------------------------------------------
/scratch/project_2015299/dirA        8.4GB  356KB 100.0 100.0
    results                            3.7GB  458MB 44.15 44.15
        simu1                              2.8GB  522MB 32.84 74.38 NOSIZE:1
        simu2                              521MB  521MB 6.02  13.64 NOSIZE:1
    installation                       1.4GB  48KB  16.2  16.2 
        gcc10                              351MB  351MB 4.05  25.02
        clang15                            351MB  351MB 4.05  25.02
        intel                              350MB  350MB 4.04  24.94
```


## Virtual rasters

When working with big raster datasets, virtual rasters might be very helpful. Virtual rasters are a useful GDAL concept for managing large raster datasets that are split into map sheets that do not overlap. Technically a virtual raster is just a small XML file that tells GDAL where the actual data files are, but from user's point of view virtual rasters can be treated much like any other raster format. Virtual rasters can include raster data in any file format GDAL supports. Virtual rasters are useful because they allow handling of large datasets as if they were a single file eliminating the need for locating correct files.

* Virtual rasters are not useful for managing time-series or overlapping rasters, for example remote sensing tiles.
* Supported by any GDAL based tool, including Python and R spatial packages, ArcGIS, FME, GrassGIS, MapInfo, QGIS, and SagaGIS. 
* [CSC Docs: Virtual rasters tutorial](https://docs.csc.fi/support/tutorials/gis/virtual-rasters/), inc code examples for R and Python.


