# Linux basics

A terminal is the standard way to interact with a supercomputer. It is worth learning the basics and getting comfortable with the "black box", to make efficient use of the resources.

1. Login to the Roihu web interface, and start a login shell; first, check which directory you are in by typing `pwd` and hitting `Enter`:

```bash
pwd
```

2. In our project's scratch storage, there is a directory called `students`. We would like to create a new subdirectory and give our username as its name. Let's move to `students`:

```bash
cd /scratch/project_2020458/students
```


3. Make a directory with your username (you can either type it or use the variable $USER) and see if it appears:

```bash
mkdir $USER    
ls -l
```

4. Go to that directory.

```bash
cd $USER      
```

:::{admonition} Auto complete
:class: seealso
If you just type `cd` and the first letter of the folder name, then hit the `tab` key, the terminal completes the name. Handy!
:::

1. Download a file into this new folder. Use the command `wget` for downloading from a URL:

```bash
wget https://raw.githubusercontent.com/csc-training/csc-env-eff/master/part-1/prerequisites/my-first-file.txt
```

2. Check what kind of file you got and what size it is using the `ls` command with some extra options:

```bash
ls -l         # option l is for long format
```

3. Use the `less` command to check what the contents of the file look like:

```bash
less my-first-file.txt
```

4. To exit the `less` view of the file, hit `q`.

5. Make a copy of this file:

```bash
cp my-first-file.txt $USER-second-file.txt    
ls -l
less $USER-second-file.txt                    
```

6. Remove the file we originally downloaded (leave your own copy).

```bash
rm my-first-file.txt
ls -l
```

7. To move or rename a file:
```bash
mv $USER-second-file.txt $USER-third-file.txt
```

:::{admonition} Re-executing commands from `history`
:class: seealso
If you remember *a part of a command* that you have used recently you can search for it with the command `history | grep string`. This will show all your used commands that have included the string `string` (replace this with the pattern you are searching for).
:::
