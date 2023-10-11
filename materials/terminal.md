# Terminal


## Why would you want to use the terminal?

A typing-based interface is often called a command-line interface, or CLI, to distinguish it from a graphical user interface, or GUI. The heart of a CLI is a read-evaluate-print loop, or REPL: when the user types a command and then presses the Enter (or Return) key, the computer reads it, executes it, and prints its output. 

Shell is the standard way to interact with a supercomputer. It is worth learning the basics and getting comfortable with the "black box".

:::{admonition} Some terminal magic
:class: tip

Did you every want to count all the files in a directory? Or lines in a file? Apart from opening the file in an editor, turning on line numbers or counting them manually you can also use a neat little command line tool called `wc`.

Check out the documentation for `wc` and see if you can find out how to 
1. Count the number of lines/characters of file `/appl/data/geo/syke/natura/Readme_natura.txt`.
2. Count all directories in `/appl/data/geo/syke`.

If this was too easy, can you count only the directory and file names that include `2021` in the syke directory? 

You can use the "login shell" via the Puhti webinterface for this exercise.

:::{admonition} Solution
:class: dropdown

`man wc` for finding the documentation. Use `q` to exit the documentation.

1. `wc -m /appl/data/geo/syke/natura/Readme_natura.txt` to count the characters in the file. Or `cat /appl/data/geo/syke/natura/Readme_natura.txt | wc -m` -> 177
2. `ls /appl/data/geo/syke | wc -l` , we pipe the output of `ls` which is a list of files into `wc` which by defining `-l`
 prints out the amount of newlines (= number of lines) -> 200

Count all directory and file names that include `2021`:  `ls *2021* | wc -l` -> 156

:::
:::


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

2. Check if there are any files:

```bash
ls
```

3. Make a directory with your name (you can either type it or use the variable $USER) and see if it appears:

```bash
mkdir $USER    
ls
```

4. Go to that directory.

```bash
cd $USER      
```

:::{admonition} Auto complete
:class: seealso
If you just type `cd` and the first letter of the folder name, then hit `tab` key, the terminal completes the name. Handy!
:::


Add an empty file into this directory. 

```bash
touch $USER-first-file.txt    
```

Check that it is empty:

```bash
cat $USER-first-file.txt        
```

Fill it with some content:

:::{admonition} Command line editor
:class: seealso
These exercises are done with the `nano` editor, but you can use your favorite editor too.
Here's a [nano cheat sheet](https://www.nano-editor.org/dist/latest/cheatsheet.html).
:::


1. Open the file with `nano`:

```bash
nano $USER-first-file.txt     
```

2. Edit the file. Type something there!
3. Exit `nano` with `Ctrl+X`, type `Y` to confirm saving and press enter to accept the filename.
4. Check that the modifications are actually there:

```bash
less $USER-first-file.txt     
```

5. Exit the preview with `q`.


## Exploring files


1. Download a file into this new folder. Use the command `wget` for downloading from a URL:

```bash
wget https://github.com/csc-training/csc-env-eff/raw/master/_hands-on/linux_prerequisites/my-first-file.txt
```

2. Check what kind of file you got and what size it is using the `ls` command with some extra options:

```bash
ls -lth         # options are l for long format, t for sorting by time and h for convenient size units. 
```

3. Use the `less` command to check out what the file looks like:

```bash
less my-first-file.txt
```

4. To exit the `less` preview of the file, hit `q`.

:::{admonition} Tip
:class: seealso
Instead of `less` you can use `cat` which prints the content of the file(s) straight into the command line. For long texts `less` is recommended.
:::

5. Make a copy of this file:

```bash
cp my-first-file.txt $USER-second-file.txt    
ls -lth
less $USER-second-file.txt                    
```

6. Remove the file we originally downloaded (leave your own copy).

```bash
rm my-first-file.txt
ls
```

:::{admonition} Moving files
:class: seealso
If you don't want to have duplicate files you can use `mv` to 'move/rename' the file. Syntax is the same: `mv /path/to/source/oldname /path/to/destination/newname`.
:::


:::{admonition} Re-executing commands from `history`
:class: seealso
If you remember *a part of a command* that you have used recently you can search for it with the command `history | grep string`. This will show all your used commands that have included the string `string` (replace this with the pattern you are searching for).
:::






