# Allas – object storage

## What it is for?

- [Allas](https://docs.csc.fi/data/Allas/) is a storage service for all computing and cloud services
* Project lifetime data storage, ~3-5 years
- Default quota 10 TB / Project, can be extended until 200TB for free
* Connected to CSC services and own computer
* Private data available for project members
* Possibility to make data public or share with other CSC project
- For computation the data has to be typically copied to the computing environment


!["Allas"](./images/allas.png "Allas"){width=90%}


# Allas – object storage: what it is NOT

- **Allas is not a file system** (even though many tools try to fool you to think so). It is just a place for a pile of static data objects.
- **Allas is not a data management environment**. Tools for etc. search, metadata,version control and access management are minimal.
- **Allas is not a foolproof back up service**. Project members can delete all the data with just one command.

# Allas – object storage: terminology

<div class="column">
- Storage space in Allas is provided per **CSC project**
- All project members have equal access to the data and possibility to delete it
- Project space can have multiple *buckets* ( up to 1000)
- There is only one level of hierarchy of buckets (no buckets within buckets)
- Data is stored as **objects** within a bucket
- Objects can contain any type of data (generally: object = file)
</div>
<div class="column">
- In Allas you can have 500 000 objects / bucket
- Name of the bucket must be unique within Allas
- Objects have metadata that can be enriched 
- In reality, there is no hierarcical directory structure, although it sometimes looks like that.
</div>

# Things that users should consider 

- Should I store each file as a separate object or should I collect it into bigger chunks?
- Should I use compression?
- Who can use the data: Projects and accession permissions?
- What will happen to my data later on?
- How to keep track of all the data I have in Allas?

# Working with Allas 

- Supports two protocols: S3 and SWIFT. 
- **Avoid cross-using Swift and S3 based objects!**


## Allas clients

- Web interface
- s3cmd commanline tool
- Python: boto3 library
- R: aws3 library
- WinSCP
- [Full list of Allas clients](https://docs.csc.fi/data/Allas/) -> Allas clients

### cPouta Webinterface

- [cPouta Webinterface][https://pouta.csc.fi/dashboard) -> object store -> containers
- See what data is in Allas, upload/download of single files.

###  [s3cmd](https://docs.csc.fi/data/Allas/using_allas/s3_client/) 

- Commandline tool for working with Allas over S3

```bash
module load allas
allas-conf --mode s3cmd
# List all buckets
s3cmd ls
# List all files in one bucket
s3cmd ls s3://my_bucket
```

## Accessing data directly from object storage

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