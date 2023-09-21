# [Moving files between a local computer and Puhti](https://docs.csc.fi/data/moving/)

## [Puhti Web Interface](puhti.csc.fi)

- Very easy, no installations needed.
- For smaller amounts of data, < 10 Gb.
- Upload, download, moving, creating folders.

## [Graphical data transfer tools](https://docs.csc.fi/data/moving/graphical_transfer/) on local computer

- For example: _FileZilla_ and _WinSCP_
- For medium amounts of data, < 1 Tb.
- Very easy, but installation required.
   
## Command line tools
- For any amount of data, practically required if data size > 1 Tb.

### [`scp`](https://docs.csc.fi/data/moving/scp/) 

- The most usual Linux tool for moving file
- `scp` works even in Windows Powershell

```
# One file:
scp /path/to/a_file cscusername@puhti.csc.fi:/scratch/project_xxxx/data_dir
# One folder:
scp -r /path/to/data_directory cscusername@puhti.csc.fi:/scratch/project_#####/data_dir 
```


### rsync
- [`rsync`](https://docs.csc.fi/data/moving/rsync/)
- Does not copy what is already there
- Can resume a copy process which disconnected
- Efficient for small files 
- Can compress data
- Can warn against accidental over-writes
- Available on Linux and Mac and WSL (windows subsystem linux)
- Organization firewalls might have forbidden using rsync, especially in Valtori organizations
- Windows Powershell does not have `rsync`, _MobaXterm_ has `rsync`, but it removes write permissions of copied files

```
# One file:
rsync --info=progress2 -a /path/to/a_file cscusername@puhti.csc.fi:/scratch/project_xxxx/data_dir
# One folder:
rsync --info=progress2 -a /path/to/data_directory cscusername@puhti.csc.fi:/scratch/project_xxxx/data_dir
```
* `progress2` shows time left and percentage



## From external data services to supercomputer

- When downloading from exernal services try to download directly to CSC, not via your local computer
- Check what APIs/tools the service supports:
	- ftp, rsync ?
	- wget/curl if HTTP-urls avaialable
	- OGC APIs, STAC ?

### [wget](https://docs.csc.fi/data/moving/wget/)
- 

``` 
# One file:
wget http://wwwd3.ymparisto.fi/d3/gis_data/spesific/syvyyskayra.zip 
# One folder:
wget -r -nc ftp://ftp.aineistot.metsaan.fi/Metsamaski/Maakunta/ --cut-dirs=2
```


## Moving data as part of workflow

> TODO: Example of moving data into local scratch eg from Allas