# Getting data into CSC environment

## From own computer to supercomputer -> rsync

* does not copy what is already there
* can resume a copy process which disconnected
* efficient for small files 
* can compress data
* can warn against accidental over-writes
* available on Linux and Mac and WSL (windows subsystem linux)

### rsync syntax

```
rsync --info=progress2 -a file-name      username@cluster:receiving-directory

rsync --info=progress2 -a directory-name username@cluster:receiving-directory/directory-name
```

* `progress2` shows time left and percentage
* for puhti: `samantha@puhti.csc.fi`
* for compression use `-az` instead of `-a`

## From own computer to object storage

Linux: https://github.com/CSCfi/allas-cli-utils

Windows/Mac: https://docs.csc.fi/data/Allas/accessing_allas/#accessing-allas-with-windows-or-mac

## From internet to supercomputer

``` wget URL```

## From Paituli to supercomputer

## Data available on Puhti

* Large commonly used geospatial datasets with open license
* Removes transfer bottleneck
* Located at: `/appl/data/geo/`
* All Puhti users have read access

  * ~13 TB of datasets available:
    * Paituli data 
    * SYKE open datasets
    * LUKE Multi-source national forest inventory
    * NLS Virtual rasters for DEMs
    * Sentinel and Landsat mosaics

[List of spatial data in computing environment](https://docs.csc.fi/data/datasets/spatial-data-in-csc-computing-env/)


## Data available on Allas

Some users share their downloaded and preprocessed data with everyone: 

* Sentinel-2 L2A data of Finland, growing season (10.5-1.9) 2016-2020
* Your data?


