# Allas – object storage

## What it is for?

* Allas is a storage service for all CSC computing and cloud services
* For CSC project lifetime: ~3-5 years
* Default quota 10 TB / project, can be extended until 200TB for free
* Accessable from CSC computing services and own computer
* Private data available for project members only
* Possibility to make data public or share with other CSC project
* For computation the data has to be typically copied to the computing environment
* [CSC Dosc: Allas](https://docs.csc.fi/data/Allas/)

What it is NOT?

- **A file system** (even though many tools try to fool you to think so). It is just a place static data objects.
- **A data management environment**. Tools for etc. search, metadata, version control and access management are minimal.
- **A foolproof back up service**. Project members can delete all the data with just one command.

## Allas: terminology

- Access to Allas is provided per **CSC project**
	- All project members have equal rights to the data, everybody can add and delete.
- Main data unit is **buckets**
 	- Name of the bucket must be unique within Allas
  	- For data organization and access administration
- Data is stored as **objects** within a bucket
	- Practically: object = file
	- In reality, there is no hierarcical directory structure within a bucket, although it sometimes looks like that.
		- Object name can be `/data/myfile.zip` and some tools may display it as `data` folder with `myfile.zip` in it.

### Things that users should consider 

- Should I store each file as a separate object or should I collect it into bigger chunks?
	- Depends how you want to use the data later, access to single files or not. 
- Should I use compression?
- What will happen to my data later on?

## Working with Allas 

- Supports two protocols: S3 and SWIFT. 
	- **For new projects S3 is recommended**
  	- SWIFT might soon be depricated, prefer S3.
	- **Avoid cross-using SWIFT and S3 based objects!**


## Allas tools

- Web interfaces: cPouta, soon also Puhti and Mahti web interface
- Graphical tools: Cyberduck, WinSCP, S3 browser
- Command line tools: a-commands, s3cmd, rclone
- From scripting:
	- Python: boto3 library
	- R: aws3 library
- For connecting these require projects S3 access key and secret key
	- Easiest to use Puhti to get to know these
- [CSC Docs: Allas clients](https://docs.csc.fi/data/Allas/) -> Allas clients


!["Allas"](./images/allas-access-flavors.png "Allas")

### cPouta webinterface

- [cPouta webinterface](https://pouta.csc.fi/dashboard) -> object store -> containers
- See what data is in Allas, upload/download of **single files**.
- Log in with CSC username and password

### Graphical data transfer tools on local computer

- For example: **S3 browser**,  **WinSCP** and **CyberDuck**
- For medium amounts of data, < 1 Tb.
- Very easy, but installation required.
- WinSCP is slower than others.
- [CSC Docs: Cyberduck](https://docs.csc.fi/data/Allas/using_allas/cyberduck/)


### Commandline tools

- For any amount of data, practically required if data size > 1 Tb.
- For example: a-commands, s3cmd, rclone


#### s3cmd
- [CSC Docs: s3cmd](https://docs.csc.fi/data/Allas/using_allas/s3_client/) 

```bash
# Set up Allas connection
module load allas
allas-conf --mode s3cmd
```

:::{admonition} Get your S3 credentials

`allas-conf --mode s3cmd` output includes your S3 credentials: access key and secret key, these are needed for creating the connection with other tools.

:::

```
# Create a new bucket
# s3cmd mb <name_of_your_bucket>
s3cmd mb s3://project_200xxxx-cscusername

# Upload (later syncronize) a folder to Allas
# s3cmd sync <local_folder> s3://<name_of_your_bucket>
s3cmd sync /scratch/project_2000xxxx/students/cscusername/geocomputing/gdal s3://project_200xxxx-cscusername

# List all buckets
s3cmd ls

# List all files in one bucket
# s3cmd ls s3://<name_of_your_bucket>
s3cmd ls s3://project_200xxxx-cscusername
s3cmd ls s3://project_200xxxx-cscusername/gdal
```

## Accessing data directly from object storage

* Many GIS tools have good support for working with cloud storage, look for S3 in documentation.
* GDAL supports reading and writing directly to Allas.
	* Applies also to other GDAL based tools: Python (rasterio, geopandas) and R (sf, terra).
 	* Writing might be more limited.
* QGIS can read rasters and vectors.
* ArcGIS Pro can read rasters.
* [CSC Docs: Tutorial - Using geospatial files directly from cloud, inc Allas](https://docs.csc.fi/support/tutorials/gis/gdal_cloud/)
	*  Connection set up details
* [Example Python code for working with Allas and rasterio and geopandas](https://github.com/csc-training/geocomputing/blob/master/python/allas)
* [Example R code for workign with Allas and terra and sf](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R)
