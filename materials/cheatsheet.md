# CSC and Unix cheatsheet
adapted from https://docs.csc.fi/img/csc-quick-reference/csc-quick-reference.pdf
Note that this is simplified for beginners usage, once you get more experienced, you'll notice that there is more (and better) options for everything, and that not everything written here is "the whole truth".

## Service names

* Puhti, Mahti, LUMI - supercomputers
* Pouta, Rahti - cloud services
* Allas - object storage

## Unix commands and hints
(all text within <> is replaced with real names, e.g. `cp /home/user/my-file.txt scratch/project_200xxxx/new-directory`)
Check out all options of the commands with `man <command>` (for *man*ual), exit with `q`.

### File system exploration
* `ls` - list current directory contents
* `cd <directory-to-change-to>` - change the current directory
    * `cd ..` - change to "one level higher" in directory tree
    * `cd` - (without argument) change to $HOME 
* `pwd` - print full path of the current directory

### File manipulation
* `cp <file-to-copy> <destination>` - copy a file 
* `mv <file-to-move> <destination/new-file-name>` - move or rename a file 
* `rm <file-to-remove>` - delete a file 
* `mkdir <new-directory-name>` - create a directory
* `touch <new-file-name>` - create an empty new file

### Permissions
* `chmod <whowhatwhich> <file-name>` - change file permissions 
    * who -> u: user , g: group , o: others, a: all
    * what -> -:remove permission, +: add permission
    * which -> r: read, w: write, x: execute
    * example `chmod u+x my-batch-job-script.sh` adds execution rights for current user to the file
* `chgrp` - change file/folder owner

### Check file contents
* `less <text-file>` - see text file (exit with `q`)
* `cat <file-name>` - see file content
* `head <file-name>` - list ten first lines of the file 
* `tail -100 <file-name>` - show the last 100 lines 

### Other
* `history` - show history of commands run
* `grep` - find rows containing a string
    * example: `history | grep "some strings"` would show you all commands in your history that contain "some string" (| is called a pipe)
* `echo "some text"` - prints some text to terminal
* `exit` - quit the session on commandline 
* `<some command> > <file-name>` - output of a command to a file 
* `<some command> >> <file-name>` - append output of a command to a file
* `which <application-name>` - shows path to the executable of an application


### Variables
Defining a variable: `MYPATH=/home/user/something`
Using a defined or environment (predefined!) variable: `$MYPATH`, e.g. to print its content: `echo $MYVAR`
Some environment variables:
* `$HOME` : users home directory
* `$PATH` : path where executables are looked for
* `$USERNAME`: current username
* `$HOSTNAME`: current host system name


## Command line editors 

### Nano
Process to edit a file in nano:
* `nano <file-name>` - (create and) open file with nano
    * edit your file
    * when done, use `CTRL + o` key combination 
    * (edit the filename and) press enter
    * use `CTRL + x` key combination to exit the editor

### Vi
Process to edit a file in vi:
* `vi <file-name>` - (create and) open file with vi
    * press `i` to switch to "edit mode"
    * edit your file
    * when done, press `esc` to switch to "normal mode"
    * press `:wq` to save (*w*rite) the file and exit (*q*uit) the editor

## File transfer

* `scp <file name> <username@puhti.csc.fi:/scratch/project_200xxxx/dir_name>` - copy a file from current computer to Puhti
* `wget <some-url>` or  `curl <some-url>` - get a file from the internet

## CSC modules

* Geoinformatics applications and how to use them: https://docs.csc.fi/apps/by_discipline/#geosciences
* `module load <application-name>` - initialize the environment of an application
* `module list` - list loaded applications
* `module purge` - remove application environments

## CSC batch jobs

* `sbatch <batch-job-file>` - submit a job
* `sacct` - info about job status
* `squeue` - see the job status in the queue
* `scancel <jobid>` - cancel a job
* `seff <jobid>` - info about completed jobs

## Support and links

* E-mail support: servicedesk@csc.fi
* Weekly virtual user support session (every Wed at 14): https://ssl.eventilla.com/usersupportcoffee
* Accounts, projects, forgotten password: https://my.csc.fi/
    * on Puhti: `csc-workspaces`
* CSC services and info: https://research.csc.fi/
* How to use them: https://docs.csc.fi/, https://docs.csc.fi/support/FAQ/, https://docs.csc.fi/support/tutorials/
* Geoinformatics examples: https://github.com/csc-training/geocomputing

## Git "the way you need it"

[Cheatsheet by Aalto Scientific Computing](https://aaltoscicomp.github.io/cheatsheets/git-the-way-you-need-it-cheatsheet.pdf)
