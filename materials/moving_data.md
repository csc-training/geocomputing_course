# Moving data

## Moving files between a local computer and a supercomputer

* [Moving files between a local computer and a supercomputer](https://docs.csc.fi/data/moving/)

### Puhti Web Interface

- Very easy, no installations needed.
- For smaller amounts of data, < 10 Gb.
- Upload, download, moving, creating folders.
- [Puhti Web Interface](https://puhti.csc.fi)
- [Puhti Web Interface in Docs](https://docs.csc.fi/computing/webinterface/)

### Graphical data transfer tools on local computer

- For example: _FileZilla_ and _WinSCP_
- For medium amounts of data, < 1 Tb.
- Very easy, but installation required.
- [Graphical data transfer tools in Docs](https://docs.csc.fi/data/moving/graphical_transfer/)
   
### Command line tools
- For any amount of data, practically required if data size > 1 Tb.

#### scp

- The most usual Linux tool for moving file
- `scp` works even in Windows Powershell
- [`scp` in Docs](https://docs.csc.fi/data/moving/scp/)

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
- [`rsync` in Docs](https://docs.csc.fi/data/moving/rsync/)

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
	- ftp, rsync ?
	- wget/curl if HTTP-urls avaialable
	- OGC APIs, STAC ?

### wget

- [`wget` in Docs](https://docs.csc.fi/data/moving/wget/)

``` 
# One file:
wget http://wwwd3.ymparisto.fi/d3/gis_data/spesific/syvyyskayra.zip 
# One folder:
wget -r -nc ftp://ftp.aineistot.metsaan.fi/Metsamaski/Maakunta/ --cut-dirs=2
```


## Moving data as part of workflow

> ToDo: Example of moving data into local scratch eg from Allas



:::{admonition} Possible trouble with file transfer between Windows and Linux
:class: note, dropdown

When you transfer text files from a Windows system to a Unix system (Mac, Linux, BSD, Solaris, etc.) this can cause problems. Windows encodes its files slightly different than Unix, and adds an extra character to every line.

On a Unix system, every line in a file ends with a `\n`` (newline). On Windows, every line in a file ends with a \r\n (carriage return + newline). This causes problems sometimes.

Though most modern programming languages and software handles this correctly, in some rare instances, you may run into an issue. The solution is to convert a file from Windows to Unix encoding with the `dos2unix`` command.

You can identify if a file has Windows line endings with `cat -A filename``. A file with Windows line endings will have ^M$ at the end of every line. A file with Unix line endings will have $ at the end of a line.

To convert the file, run `dos2unix filename`. Conversely, to convert back to Windows format, you can run `unix2dos filename`.

From [HPC Carpentry](https://carpentries-incubator.github.io/hpc-intro/).

:::

:::{admonition} Trouble with script execution
:class: note

Sometimes when we transfer scripts the permissions might get messed up. A script you could run with `./myscript.sh` on your own computer cannot be run anymore after transfering to the supercomputer.

TODO: write some explanation about `chmod` 

:::

