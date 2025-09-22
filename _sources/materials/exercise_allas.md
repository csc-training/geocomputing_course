# Allas exercise

:::{admonition} Timing 
:class: note

15 min

:::

:::{admonition} Goals 
:class: note

Learn how to:
* Configure connection to Allas and get S3 credentials
* Sync local folder to Allas (manual back-up)
* See what data is in Allas
* Use s3cmd. 
  * [CSC Docs: s3cmd](https://docs.csc.fi/data/Allas/using_allas/s3_client/) 
:::

:::{admonition} Prerequisites 
:class: important

* [CSC user account](https://docs.csc.fi/accounts/how-to-create-new-user-account/) and [project](https://docs.csc.fi/accounts/how-to-create-new-project/) with [access to Puhti and Allas](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).
* Basic Linux skills

:::

:::{admonition} Change the default project and username

* `project_2015299` is an example project name, replace with your own CSC project name.
* `cscusername` is an example username, replace with your username.
:::

* Open [Puhti web interface](https://puhti.csc.fi) and log in
* Open `Login node shell` from Tools menu.
* Set up Allas connection

     
```bash
module load allas
allas-conf --mode s3cmd
# It asks to select the project, select the project with the corresponding number. 
# The configuration takes a moment, please wait.
```

:::{admonition} Get your S3 credentials

`allas-conf --mode s3cmd` output includes your S3 credentials: access key and secret key, these are needed for creating the connection with other tools.

:::

```
# Create a new bucket
# s3cmd mb <name_of_your_bucket>

s3cmd mb s3://project_2015299-cscusername

# Upload (later syncronize) a folder to Allas
# s3cmd sync <local_folder> s3://<name_of_your_bucket>
s3cmd sync /appl/data/geo/mml/dem10m/2019/W3/W33/ s3://project_2015299-cscusername

# List all buckets
s3cmd ls

# List all files in one bucket
# s3cmd ls s3://<name_of_your_bucket>
s3cmd ls s3://project_2015299-cscusername

# Read and write directly to Allas with GDAL
# Make GDAL avaialble
module load geoconda

# See metadata of a file from GDAL exercise
gdalinfo /vsis3/project_2015299-cscusername/W3333.tif

# Enable writing with GDAL
export CPL_VSIL_USE_TEMP_FILE_FOR_RANDOM_WRITE=YES

# Make the .tif file to Cloud-Optimized GeoTiff
gdal_translate /vsis3/project_2015299-cscusername/W3333.tif /vsis3/project_2015299-cscusername/W3333_COG.tif -of COG

# See metadata of the new file
gdalinfo /vsis3/project_2015299-cscusername/W3333_COG.tif

# Delete all from Allas
s3cmd del --recursive --force s3://project_2015299-cscusername
s3cmd rb s3://project_2015299-cscusername
```

:::{admonition} Key points 
:class: important

* Take a moment to plan your bucket and object naming, so that it would be easy to use later.
* Allas is a good place to keep a back-up of your data.
* Many GIS tools can read (and write) directly to Allas.
:::
