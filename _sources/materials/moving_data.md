# Moving data

## Local computer <-> supercomputer
### Puhti Web Interface

- Graphical, no installations needed.
- Limited functionality compared to other options.
- For smaller amounts of data, < 10 Gb.
- Upload, download, moving, creating folders.
- [Puhti Web Interface](https://puhti.csc.fi) -> Files
- [CSC Docs: Puhti Web Interface](https://docs.csc.fi/computing/webinterface/)

### Graphical data transfer tools on local computer

- For example: **FileZilla**,  **WinSCP** and **CyberDuck**
- For medium amounts of data, < 1 Tb.
- Easy drag-and-drop for moving, but installation required.
- WinSCP is slower than others.
- [CSC Docs: Graphical data transfer tools](https://docs.csc.fi/data/moving/graphical_transfer/)

!["FileZilla"](./images/filezilla.jpg "FileZilla")
   
### Command line tools on local computer
- For any amount of data, practically required if data size > 1 Tb.
- Requires knowing the commands.

#### scp

- The most usual Linux tool for moving files
- `scp` works even in Windows Powershell
- [CSC Docs: `scp`](https://docs.csc.fi/data/moving/scp/)

```
# One file:
scp /path/to/a_file cscusername@puhti.csc.fi:/scratch/project_200xxxx/data_dir

# One folder:
scp -r /path/to/directory cscusername@puhti.csc.fi:/scratch/project_200xxxx/directory 
```


#### rsync

- Best for big data transfers: does not copy what is already there, can resume a copy process which disconnected.
- Can warn against accidental over-writes.
- Available on Linux, Mac and Windows Subsystem Linux (WSL).
- Windows Powershell does not have `rsync`, MobaXterm has `rsync`, but it removes write permissions of copied files
- [CSC Docs: `rsync`](https://docs.csc.fi/data/moving/rsync/)

```
# One file:
rsync --info=progress2 -a /path/to/a_file cscusername@puhti.csc.fi:/scratch/project_200xxxx/data_dir

# One folder:
rsync --info=progress2 -a /path/to/directory cscusername@puhti.csc.fi:/scratch/project_200xxxx/directory
```
* `--info=progress2` shows time left and percentage


:::{admonition} Firewall limitations

Some organizations, for example research institutes with IT-services from Valtori, have stricter rules and need to use proxy for connecting to CSC. Ask your IT-service or other Puhti users in your organization for extra-guidelines. 

:::



## External data services -> supercomputer

- When downloading from exernal services try to download directly to CSC, not via your local computer
- Check what APIs/tools the service supports:
	- Standard APIs: OGC APIs, [STAC](https://csc-training.github.io/geocomputing_course/materials/stac.html)
	- Custom service APIs
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

:::{admonition} More options :class: note

* [CSC Docs: Moving files between a local computer and a supercomputer](https://docs.csc.fi/data/moving/)

:::



:::{admonition} Possible trouble with file transfer between Windows and Linux
:class: seealso, dropdown

When you transfer text files from a Windows system to a Unix system (Mac, Linux etc.) this can cause problems. Windows encodes its files slightly different than Unix, and adds an extra character to every line.

On a Unix system, every line in a file ends with a `\n` (newline). On Windows, every line in a file ends with a `\r\n` (carriage return + newline). This causes problems sometimes.

Though most modern programming languages and software handles this correctly, in some instances, you may run into an issue. 

You can identify if a file has Windows line endings with `cat -A filename`. A file with Windows line endings will have ^M$ at the end of every line. A file with Unix line endings will have $ at the end of a line.

The solution is to convert a file from Windows to Unix encoding. Many code editors have a setting for choosing the correct end-of-line (EOL) character. 

If the Windows style file is already in HPC, it can be fixed with the `dos2unix` command. To convert the file, run `dos2unix filename`. Conversely, to convert back to Windows format, you can run `unix2dos filename`.

From [HPC Carpentry](https://carpentries-incubator.github.io/hpc-intro/).

:::

:::{admonition} Trouble with script execution?
:class: seealso, dropdown

Sometimes when we transfer scripts the permissions might get messed up. A script you could run with `./myscript.sh` on your own computer cannot be run anymore after transfering to the supercomputer.

You can use `ls -l` to see permissions (r: read, w: write, x: execute):

```
-rw-r--r--. 1 user group 1526 Sep 30 01:50 myfile.py
| |  |  | | |   |     |    |         |        |    
| |  |  | | |   |     |    |         |        L filename
| |  |  | | |   |     |    |         L date and time
| |  |  | | |   |     |    L size in kB
| |  |  | | |   |     L groupname
| |  |  | | |   L username
| |  |  | | L number of hardlinks
| |  |  | L alternate access method
| |  |  L permissions of other
| |  L permissions of group
| L permissions of user 
L file (-), directory (d), symbolic link (l)
```

What if we want to give different sets of users different permissions?

 The command [chmod](https://www.freecodecamp.org/news/how-to-change-file-permissions-with-the-chmod-command-on-linux/) among others also accepts special numeric codes. The numeric codes are as follows: read = 4, write = 2, execute = 1. For each user we will assign permissions based on the sum of these permissions (must be between 7 and 0).

Let’s make an example file and give everyone permission to do everything with it.

```bash
touch example
ls -l example
chmod 777 example
ls -l example
```

How might we give ourselves and our colleagues within the same project permission to do everything with a file, but allow no one else to do anything with it.

From [HPC Carpentry](http://www.hpc-carpentry.org/hpc-shell)

:::{admonition} Solution
:class: topic, dropdown

```
chmod 770 example
```
We want all permissions so: 4 (read) + 2 (write) + 1 (execute) = 7 for user (first position) and group (second position), no permissions, i.e. 0, for all others (third position).
:::

:::

