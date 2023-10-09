# Allas – object storage

What it is?

* Allas is a **storage service**, technically object storage
* **For CSC project lifetime: 1-5 years**
* **Capacity: 10 - 200 for free**, more with contract
* Accessible from CSC computing services, own laptop or other servers
* Private data - access for project members only
* Possibility to make data public or share with other CSC project
* For computation the data has to typically be copied to the computing environment
* [CSC Dosc: Allas](https://docs.csc.fi/data/Allas/)
* LUMI-O is very similar to Allas
* [LUMI Docs: LUMI-O](https://docs.lumi-supercomputer.eu/storage/lumio/)
	
What it is NOT?

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
	- In reality, there is no hierarcical directory structure within a bucket, although it sometimes looks like that.
		- Object name can be `/data/myfile.zip` and some tools may display it as `data` folder with `myfile.zip` file.

### Things to consider 

- Should each file be stored as a separate object or should I collect it into bigger chunks?
	- Depends how you want to use the data later, access to single files or not. 
- Compression?
- What will happen to the data later on?

## Allas APIs

- S3 and SWIFT. 
	- **For new projects S3 is recommended**
  	- SWIFT might be soon depricated.
	- Avoid cross-using SWIFT and S3 based objects!


## Tools for Allas

- **Web interfaces**:
	- **cPouta**, soon also Puhti and Mahti web interface
  	- [cPouta webinterface](https://pouta.csc.fi/dashboard) -> object store -> containers
	- See what data is in Allas, upload/download of single files.
	- Log in with CSC username and password
- **Graphical tools**:
	- **S3 browser**, Cyberduck, WinSCP
	- For medium amounts of data, < 1 Tb.
	- Very easy, but installation required.
	- WinSCP is slower than others. 
- **Command line tools**:
	- **s3cmd**, a-commands, rclone
	- For any amount of data, practically required if data size > 1 Tb.
- **For scripting**:
	- Python: **boto3** library
	- R: **aws3** library
- For connecting, these require **S3 access key and secret key**
	- Easiest to use Puhti for getting these
- [CSC Docs: Allas clients](https://docs.csc.fi/data/Allas/) -> Allas clients


### s3cmd
- [CSC Docs: s3cmd](https://docs.csc.fi/data/Allas/using_allas/s3_client/) 

## Accessing data directly from object storage

* Many GIS tools have good support for working with cloud storage, look for S3 in documentation.
* **GDAL** supports reading and writing directly to Allas.
	* Applies also to other GDAL based tools: **Python (rasterio, geopandas)** and **R (sf, terra)**.
 	* Writing might be more limited.
* **QGIS** can read rasters and vectors.
* **ArcGIS** Pro can read rasters.
* [CSC Docs: Tutorial - Using geospatial files directly from cloud, inc Allas](https://docs.csc.fi/support/tutorials/gis/gdal_cloud/)
	* [Example Python code for working with Allas and rasterio and geopandas](https://github.com/csc-training/geocomputing/blob/master/python/allas)
	* [Example R code for workign with Allas and terra and sf](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R)

## Allas exercise

:::{admonition} Timing 
:class: note

15 min

:::

:::{admonition} Goals 
:class: note

Learn how to:
* Configure connection to Allas and get S3 credentials
* Sync local folder to Allas (manual back-up)
* See what data is Allas
:::

:::{admonition} Prerequisites 
:class: important

* [CSC user account](https://docs.csc.fi/accounts/how-to-create-new-user-account/) and [project](https://docs.csc.fi/accounts/how-to-create-new-project/) with [access to Puhti and Allas](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).
* Basic Linux skills

:::

:::{admonition} Change the default project and username

* `project_200xxxx` is example project name, replace with your own CSC project name.
* `cscusername` is example username, replace with your username.
:::

* Open [Puhti web interface](https://puhti.csc.fi) and log in
* Open `Login node shell` from Tools menu.
* Set up Allas connection

     
```bash
module load allas
allas-conf --mode s3cmd
# It asks to select the project, select the project by number. 
# The configuration takes a moment, please wait.
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
s3cmd sync /appl/data/geo/mml/dem10m/2019/W3/W33/ s3://project_200xxxx-cscusername

# List all buckets
s3cmd ls

# List all files in one bucket
# s3cmd ls s3://<name_of_your_bucket>
s3cmd ls s3://project_200xxxx-cscusername

# Read and write directly to Allas with GDAL
# Make GDAL avaialble
module load geoconda

# See metadata of a file from GDAL exercise
gdalinfo /vsis3/project_200xxxx-cscusername/W3333.tif

# Enable writing with GDAL
export CPL_VSIL_USE_TEMP_FILE_FOR_RANDOM_WRITE=YES

# Make the .tif file to Cloud-Optimized GeoTiff
gdal_translate /vsis3/project_200xxxx-cscusername/W3333.tif /vsis3/project_200xxxx-cscusername/W3333_COG.tif -of COG

# See metadata of the new file
gdalinfo /vsis3/project_200xxxx-cscusername/W3333_COG.tif

# Delete all from Allas
s3cmd del --recursive --force s3://project_200xxxx-cscusername
```

:::{admonition} Key points 
:class: important

* Take a moment to plan your bucket and object naming, so that it would be easy to use later.
* Allas is a good place to keep a back-up of your data.
* Many GIS tools can read (and write) directly to Allas.
:::
