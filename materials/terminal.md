# Terminal


## Why would you want to use the terminal?

A terminal is a text input and output environment. A shell is the primary interface that users see when they log in, whose primary purpose is to start other programs. 

A typing-based interface is often called a command-line interface, or CLI, to distinguish it from a graphical user interface, or GUI. The heart of a CLI is a read-evaluate-print loop, or REPL: when the user types a command and then presses the Enter (or Return) key, the computer reads it, executes it, and prints its output. 

Shell is the standard way to interact with a supercomputer. It is worth learning the basics and getting comfortable with the "black box", to make efficient use of the resources.

The terms terminal, command line and shell are often used interchangably, even though they mean slightly different things. 

## Basic Linux commands

Do you remember on how you edited some files in the web interface? Let's do the same thing again; only from the command line:

### Navigating folders

1. Login to the Puhti web interface, and start a login shell; first, check which directory you are in by typing `pwd` and hitting `Enter`:

```bash
pwd
```

2. We would like to create a new directory in our projects scratch students directory with our name, let's move there:

```bash
cd /scratch/project_200xxxx/students
```


3. Make a directory with your name (you can either type it or use the variable $USER) and see if it appears:

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
If you just type `cd` and the first letter of the folder name, then hit `tab` key, the terminal completes the name. Handy!
:::

## Exploring files


1. Download a file into this new folder. Use the command `wget` for downloading from a URL:

```bash
wget https://raw.githubusercontent.com/csc-training/csc-env-eff/master/part-1/prerequisites/my-first-file.txt
```

2. Check what kind of file you got and what size it is using the `ls` command with some extra options:

```bash
ls -l         # options are l for long format, 
```

3. Use the `less` command to check out what the file looks like:

```bash
less my-first-file.txt
```

4. To exit the `less` preview of the file, hit `q`.

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

:::{admonition} Moving files
:class: seealso
If you don't want to have duplicate files you can use `mv` to 'move/rename' the file. Syntax is the same: `mv /path/to/source/oldname /path/to/destination/newname`.
:::


:::{admonition} Re-executing commands from `history`
:class: seealso
If you remember *a part of a command* that you have used recently you can search for it with the command `history | grep string`. This will show all your used commands that have included the string `string` (replace this with the pattern you are searching for).
:::
