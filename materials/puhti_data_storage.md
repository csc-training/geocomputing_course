# Disk areas

In this section, you will learn how to use different disk areas in HPC environment at CSC.

## Puhti disk areas

![](./images/disk-systems.svg)

| Name     |Access   |Path                 |Cleaning      |Capacity|Number of files| Use |
|------------|--------|--------------------|---------------------|--------------|----------------|----------------|
|**[home](https://docs.csc.fi/computing/disk/#home-directory)**    |Personal|`/users/<user-name>` |No            |10 GiB              |100 000 files  | personal settings and files |
|**[projappl](https://docs.csc.fi/computing/disk/#projappl-directory)**|Project |`/projappl/<project>`|No            |50 GiB              |100 000 files  | installation files |
|**[scratch](https://docs.csc.fi/computing/disk/#scratch-directory)** |Project |`/scratch/<project>` |180 days      |1 TiB              |1 000 000 files  | main working area |

### Temporary fast disks 

- [Login node local tmp](https://docs.csc.fi/computing/disk/#login-nodes)  `$TMPDIR` for compiling, cleaned frequently.
	
- [NVMe](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage) - `$LOCAL_SCRATCH` in batch jobs, 
    - NVMe is accessible only during your job allocation, inc. interactive job.
	- You must copy data in and out during your batch job. 
    - If your job reads or writes a lot of small files, using this can give 10x performance boost.

## LUMI disk areas
- [LUMI disks](https://docs.lumi-supercomputer.eu/storage/)

## Disk status

- Display usage and quota of all your disk areas: `csc-workspaces` 

![](./images/disk_status.png)


## Some best practice tips

- Take **backups** of important files. Data on Puhti disks is not backed up.
	- Allas is best CSC option for back-up.
	- Github or similar for code.
- Supercomputer disks do not work well with **too many small files** (see the file limits above)
	- Plan your analysis in a way that too many files are not needed.
    - Keep the small files in one zip-file, unzip it only on local fast disks during the analysis. 
	- Don't create a lot of files in one folder
- [Best practice performance tips for using Lustre](https://docs.csc.fi/computing/lustre/#best-practices)
- **Databases**:
	- Only file databases (SQLite, GeoPackage) can be kept in supercomputer disks.
	- For PostgreSQL (but not PostGIS) use CSC [Database-as-service](https://docs.csc.fi/cloud/dbaas/).
	- For any other database set up virtual machine in cPouta.