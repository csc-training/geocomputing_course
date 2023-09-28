# Disk areas and Allas
In this section, you will learn how to manage different disk areas in HPC environment at CSC

# Main disk areas in Puhti

![](./images/disk-systems.svg){width=90%}

| Name     |Owner   |Path                 |Cleaning      |Capacity|Number of files| Use |
|------------|--------|--------------------|---------------------|--------------|----------------|----------------|
|**[home](https://docs.csc.fi/computing/disk/#home-directory)**    |Personal|`/users/<user-name>` |No            |10 GiB              |100 000 files  | personal settings and files |
|**[projappl](https://docs.csc.fi/computing/disk/#projappl-directory)**|Project |`/projappl/<project>`|No            |50 GiB              |100 000 files  | installation files |
|**[scratch](https://docs.csc.fi/computing/disk/#scratch-directory)** |Project |`/scratch/<project>` |180 days      |1 TiB              |1 000 000 files  | main working area |

- [LUMI disks](https://docs.lumi-supercomputer.eu/storage/)

# Additional temporary fast local disk areas 

- [Login node local tmp](https://docs.csc.fi/computing/disk/#login-nodes) - `$TMPDIR`, compiling, temporary, 
    - Each of the login nodes have 2900 GiB of fast local storage 
    - The local storage is meant for temporary storage and is cleaned frequently
	
- [NVMe](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage) - `$LOCAL_SCRATCH` in batch jobs, 
    - Interactive batch job, IO- and GPU-nodes have  
    - You must copy data in and out during your batch job. NVMe is accessible only during your job allocation.
    - If your job reads or writes a lot of small files, using this can give 10x performance boost


## Displaying current status of disk areas

-> displays all scratch and projappl directories you have access to.
- use `csc-workspaces` command to display available projects and quotas 


![](./images/disk_status.png){width=50%}

# Some best practice tips

- Take **backups** of important files. Data on Puhti disks is not backed up.
- Supercomputer disks do not work well with **too many small files** (see the file limits above)
	- Plan your analysis in a way that too many files are not needed.
    - Keep the small files in one zip-file, unzip it only on local fast disks during the analysis. 
	- Don't create a lot of files in one folder
- [Best practice performance tips for using Lustre](https://docs.csc.fi/computing/lustre/#best-practices)
- **Databases**:
	- Only file databases (SQLite, GeoPackage) can be kept in supercomputer disks, 
	- For PostgreSQL (but not PostGIS) use CSC [Database-as-service](https://docs.csc.fi/cloud/dbaas/) 
	- For any other database set up virtual machine in cPouta