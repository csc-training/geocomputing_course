# Best practice tips for data

- Take **backups** of important files. Data on Puhti disks is not backed up.
	- Allas is the best CSC option for back-up.
	- Github or similar for code.
- Supercomputer disks do not work well with **too many small files**
	- Plan your analysis in a way that too many files are not needed.
	- Keep the small files in one zip-file, unzip it only on local fast disks during the analysis. 
	- Don't create a lot of files in one folder
- [CSC Docs: Best practice performance tips for using Lustre](https://docs.csc.fi/computing/lustre/#best-practices)
- Keep data that is needed longer also in Allas.
- **Databases**:
	- Only file databases (SQLite, GeoPackage) can be kept in supercomputer disks.
	- For PostgreSQL and PostGIS use [CSC Pukki Database as a Service](https://docs.csc.fi/cloud/dbaas/).
	- For any other database set up virtual machine in cPouta.

## Disk status

- Display usage and quota of all your disk areas: `csc-workspaces`

![](./images/disk_status.png)


- Display the amount of data and number of files within a given folder: `LUE`
- [CSC Docs: LUE tutorial](https://docs.csc.fi/support/tutorials/lue/)

```bash
module load lue
lue --display-level=2 /scratch/project_200xxxx/

path, total size, in dir size, % of total, % of dir
---------------------------------------------------
/scratch/project_200xxxx/dirA        8.4GB  356KB 100.0 100.0
    results                            3.7GB  458MB 44.15 44.15
        simu1                              2.8GB  522MB 32.84 74.38 NOSIZE:1
        simu2                              521MB  521MB 6.02  13.64 NOSIZE:1
    installation                       1.4GB  48KB  16.2  16.2 
        gcc10                              351MB  351MB 4.05  25.02
        clang15                            351MB  351MB 4.05  25.02
        intel                              350MB  350MB 4.04  24.94
```




