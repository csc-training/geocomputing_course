# Linux basics

A terminal is the standard way to interact with a supercomputer. It is worth learning the basics and getting comfortable with the "black box", to make efficient use of the resources.

* Login to the [Roihu web interface](https://roihu.csc.fi), and start a login shell.
* Check which directory you are in (type the command and hit `Enter`):

```bash
pwd
```
* Check the contents of the directory:

```bash
ls -l
```

* Change the to a another directory:

```bash
cd /scratch/project_2020458/students
pwd
```

* Make a new directory with your username:

```bash
mkdir $USER
ls -l
```

* Go to the new directory.

```bash
cd $USER      
```

:::{admonition} Auto complete
:class: seealso
If you just type `cd` and the first letter of the folder name, then hit the `tab` key, the terminal completes the name. Handy!
:::

* Download a file into this new folder.

```bash
wget https://raw.githubusercontent.com/csc-training/csc-env-eff/master/part-1/prerequisites/my-first-file.txt
ls -l 
```

* Check the contents of the file:

```bash
less my-first-file.txt
# To exit the less, hit `q`.
```

* Make a copy of this file:

```bash
cp my-first-file.txt $USER-second-file.txt    
ls -l
less $USER-second-file.txt                    
```

* To move or rename a file:
```bash
mv $USER-second-file.txt $USER-third-file.txt
ls -l
less $USER-third-file.txt   
```

* Remove all files and folders created above

```bash
cd ..
rm -r $USER
ls -l
```

:::{admonition} Re-executing commands from `history`
:class: seealso
If you remember *a part of a command* that you have used recently you can search for it with the command `history | grep string`. This will show all your used commands that have included the string `string` (replace this with the pattern you are searching for).
:::
