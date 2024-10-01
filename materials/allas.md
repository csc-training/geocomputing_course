# Allas – object storage

What is it?

* Allas is a **storage service**, technically object storage
* **For CSC project lifetime: 1-5 years**
* **Capacity: 10 - 200 Tb for free**, more with contract
* Accessible from CSC computing services, own laptop or other servers
* Private data - access for project members only
* Possibility to make data public or share with other CSC project
* For computation the data has to typically be copied to the computing environment
* [CSC Docs: Allas](https://docs.csc.fi/data/Allas/)
* LUMI-O is very similar to Allas
* [LUMI Docs: LUMI-O](https://docs.lumi-supercomputer.eu/storage/lumio/)
	
What is it NOT?

- A file system (even though many tools try to fool you to think so). It is just a place to store static data objects.
- A data management environment. Tools for etc. search, metadata, version control and access management are minimal.
- A foolproof back up service. Project members can delete all the data with just one command.

!["Allas"](./images/allas-access-flavors.png "Allas")

## Allas terminology

- Access to Allas is provided per **CSC project**
	- All project members have equal rights to the data, everybody can add and delete.
- Main data unit is **buckets**
 	- Name of the bucket must be unique within Allas
  	- For data organization and access administration
- Data is stored as **objects** within a bucket
	- Practically: object = file
	- In reality, there is no hierarchical directory structure within a bucket, although it sometimes looks like that.
		- Object name can be `/data/myfile.zip` and some tools may display it as `data` folder with `myfile.zip` file.

### Things to consider 

- Should each file be stored as a separate object or should I collect it into bigger chunks?
	- Depends how you want to use the data later, access to single files or not. 
- Compression?
- What will happen to the data later on?

## Allas APIs

- S3 and SWIFT. 
	- **For new projects S3 is recommended**
  	- SWIFT might be soon deprecated.
	- Avoid cross-using SWIFT- and S3-based objects!

## Tools for Allas

- **Web interfaces**:
	- **cPouta, Mahti web interface**, soon also Puhti web interface 
  	- [cPouta web interface](https://pouta.csc.fi/dashboard) -> object store -> containers
	- cPouta web interface only to see what data is in Allas, upload/download of single files.
 	- [Mahti web interface](https://mahti.csc.fi) also for bigger amounts of data (based on rclone) 
	- Log in with CSC username and password
- **Graphical tools**:
	- **Cyberduck, S3 browser** (only for Windows), WinSCP
	- For medium amounts of data, < 1 Tb.
	- Very easy, but installation required.
	- WinSCP is slower than others. 
- **Command line tools**:
	- **s3cmd, rclone**, a-commands
	- For any amount of data, practically required if data size > 1 Tb.
- **For scripting**:
	- Python: **boto3** library
	- R: **aws3** library
- For connecting, these require **S3 access key and secret key**
	- Easiest to [use Puhti for getting these](https://docs.csc.fi/data/Allas/using_allas/s3_client/#configuring-s3-connection-in-supercomputers)
- [CSC Docs: Allas clients](https://docs.csc.fi/data/Allas/) -> Allas clients

## Accessing data directly from object storage

* Many GIS tools have good support for working with cloud storage, look for S3 in documentation.
* **GDAL** supports reading and writing directly to Allas.
	* Applies also to other GDAL based tools: **Python (rasterio, geopandas)** and **R (sf, terra)**.
 	* Writing might be more limited.
* **QGIS** can read rasters and vectors.
* **ArcGIS** Pro can read rasters.
* [CSC Docs: Tutorial - Using geospatial files directly from cloud, inc Allas](https://docs.csc.fi/support/tutorials/gis/gdal_cloud/)
	* [Example Python code for working with Allas and rasterio and geopandas](https://github.com/csc-training/geocomputing/blob/master/python/allas)
	* [Example R code for working with Allas and terra and sf](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R)
