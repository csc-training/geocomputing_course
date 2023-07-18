# Moving data from supercomputer to object storage

``` 
module load allas
allas-conf --mode s3cmd
```

# Accessing data directly from object storage

* GDAL and other GDAL based tools (eg some Python and R packages and QGIS)
* no need to download data

Read public file on Allas:
```
gdalinfo /vsicurl/https://a3s.fi/<name_of_your_bucket>/<name_of_your_file>
```

Read private file on Allas: 
```
module load allas
allas-conf --mode s3cmd
gdalinfo /vsis3/<name_of_your_bucket>/<name_of_your_file>

```

# Moving data as part of workflow

> Example of moving data into local scratch eg from Allas