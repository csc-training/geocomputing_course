# Allas – object storage

## What it is for?

- Allas is a storage service for all CSC computing and cloud services
* Project lifetime data storage, ~3-5 years
- Default quota 10 TB / Project, can be extended until 200TB for free
* Accessable from CSC computing services and own computer
* Private data available for project members only
* Possibility to make data public or share with other CSC project
- For computation the data has to be typically copied to the computing environment
- [CSC Dosc: Allas](https://docs.csc.fi/data/Allas/)

### Allas: what it is NOT

- **Allas is not a file system** (even though many tools try to fool you to think so). It is just a place for a pile of static data objects.
- **Allas is not a data management environment**. Tools for etc. search, metadata,version control and access management are minimal.
- **Allas is not a foolproof back up service**. Project members can delete all the data with just one command.

## Allas: terminology

- Storage space in Allas is provided per **CSC project**
- All project members have equal access to the data and possibility to delete it
- Project space can have multiple *buckets* ( up to 1000)
- There is only one level of hierarchy of buckets (no buckets within buckets)
- Data is stored as **objects** within a bucket
- Objects can contain any type of data (generally: object = file)
- In Allas you can have 500 000 objects / bucket
- Name of the bucket must be unique within Allas
- Objects have metadata that can be enriched 
- In reality, there is no hierarcical directory structure, although it sometimes looks like that.
	- Object name can be /data/myfile.zip and some tools may display that as a file in a folder.

### Things that users should consider 

- Should I store each file as a separate object or should I collect it into bigger chunks?
- Should I use compression?
- Who can access and delete the data: Projects and accession permissions?
- What will happen to my data later on?
- How to keep track of all the data I have in Allas?

## Working with Allas 

- Supports two protocols: S3 and SWIFT. 
	- SWIFT might soon be depricated, prefer S3.
	- **Avoid cross-using SWIFT and S3 based objects!**


## Allas clients

- Web interfaces: cPouta
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

- [cPouta webinterface][https://pouta.csc.fi/dashboard) -> object store -> containers
- See what data is in Allas, upload/download of **single files**.
- Puhti web interface likely to get also some Allas suppport
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
- [CSC Docs: s3cmd](https://docs.csc.fi/data/Allas/using_allas/s3_client/) 

```bash
# Set up Allas connection
module load allas
allas-conf --mode s3cmd
```

:::{admonition} Get your S3 credentials :class: tip

`allas-conf --mode s3cmd` output includes your S3 credentials: access key and secret key, these are needed for creating the connection in your local machine.

:::

```
# List all buckets
s3cmd ls

# List all files in one bucket
s3cmd ls s3://my_bucket

# Create a new bucket
s3cmd mb s3://project_200xxx-cscusername

# Upload (later syncronize) a folder to Allas
s3cmd sync /scratch/project_2000xxx/students/cscusername/ s3://my-bucket
```

## Accessing data directly from object storage

* GDAL and other GDAL based tools (eg some Python and R packages and QGIS)
* no need to download data

Read public file on Allas:

```
# Make GDAL tools available
module load geoconda
# See metadata of a file in Allas
gdalinfo /vsicurl/https://a3s.fi/<name_of_your_bucket>/<name_of_your_file>
```

Read private file on Allas: 

```
# Set up Allas connection, if needed, see above
gdalinfo /vsis3/<name_of_your_bucket>/<name_of_your_file>
```