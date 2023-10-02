# Moving data

## Moving files between a local computer and a supercomputer

* [CSC Docs: Moving files between a local computer and a supercomputer](https://docs.csc.fi/data/moving/)

### Puhti Web Interface

- Very easy, no installations needed.
- For smaller amounts of data, < 10 Gb.
- Upload, download, moving, creating folders.
- [Puhti Web Interface](https://puhti.csc.fi) -> Files
- [CSC Docs: Puhti Web Interface](https://docs.csc.fi/computing/webinterface/)

### Graphical data transfer tools on local computer

- For example: _FileZilla_,  _WinSCP_ and *CyberDuck*
- For medium amounts of data, < 1 Tb.
- Very easy, but installation required.
- WinSCP is slower than others.
- [CSC Docs: Graphical data transfer tools](https://docs.csc.fi/data/moving/graphical_transfer/)
   
### Command line tools on local computer
- For any amount of data, practically required if data size > 1 Tb.

#### scp

- The most usual Linux tool for moving file
- `scp` works even in Windows Powershell
- [CSC Docs: `scp`](https://docs.csc.fi/data/moving/scp/)

```
# One file:
scp /path/to/a_file cscusername@puhti.csc.fi:/scratch/project_xxxx/data_dir
# One folder:
scp -r /path/to/directory cscusername@puhti.csc.fi:/scratch/project_#####/directory 
```


#### rsync

- Does not copy what is already there
- Can resume a copy process which disconnected
- Efficient for small files 
- Can compress data
- Can warn against accidental over-writes
- Available on Linux and Mac and WSL (windows subsystem linux)
- Organization firewalls might have forbidden using rsync, especially in Valtori organizations
- Windows Powershell does not have `rsync`, _MobaXterm_ has `rsync`, but it removes write permissions of copied files
- [CSC Docs: `rsync`](https://docs.csc.fi/data/moving/rsync/)

```
# One file:
rsync --info=progress2 -a /path/to/a_file cscusername@puhti.csc.fi:/scratch/project_xxxx/data_dir
# One folder:
rsync --info=progress2 -a /path/to/directory cscusername@puhti.csc.fi:/scratch/project_xxxx/directory
```
* `progress2` shows time left and percentage



## From external data services to supercomputer

- When downloading from exernal services try to download directly to CSC, not via your local computer
- Check what APIs/tools the service supports:
	- OGC APIs, STAC
	- ftp, rsync
	- wget/curl if HTTP-urls avaialable

### wget

- [CSC Docs: `wget`](https://docs.csc.fi/data/moving/wget/)

``` 
# One file:
wget http://wwwd3.ymparisto.fi/d3/gis_data/spesific/syvyyskayra.zip 
# One folder:
wget -r -nc ftp://ftp.aineistot.metsaan.fi/Metsamaski/Maakunta/ --cut-dirs=2
```



