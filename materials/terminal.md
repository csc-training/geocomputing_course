# Terminal


TODO: adopt to webinterface  task

## Why would you want to use the terminal?

A typing-based interface is often called a command-line interface, or CLI, to distinguish it from a graphical user interface, or GUI. The heart of a CLI is a read-evaluate-print loop, or REPL: when the user types a command and then presses the Enter (or Return) key, the computer reads it, executes it, and prints its output. 

Shell is standard way to interact with a supercomputer. It is worth learning the basics and getting comfortable with the "black box".

:::{admonition} Some terminal magic
:class: tip

Did you every want to count all the files in a directory? Or lines in a file? Apart from opening the file in an editor, turning on line numbers or counting them manually you can also use a neat little command line tool called `wc`.

Check out the documentation for `wc` and see if you can find out how to 
1. Count the number of lines/characters of file XX.
2. Count all files in our course scratch directory.

If this was too easy, can you count only files that end with `.tif`? What about only those lines in our file XX that include the string `2023` ?

You can use the "login shell" via the Puhti webinterface for this exercise.

:::{admonition} Solution
:class: tip, dropdown

`man wc` for finding the documentation. Use `q` to exit the documentation.

1. `wc -m XX` to count the characters in the file. Or `cat XX | wc -m` -> XX
2. `ls /scratch/project_200xxxx | wc -l` , we pipe the output of `ls` which is a list of files into `wc` which by defining `-l`
 prints out the amount of newlines (= number of lines) -> XX

Count all tif files: `ls *.tif | wc -l` -> XX
Count all lines that include `2023`:  `cat XX | grep "2023" | wc -w` -> XX

:::
:::

## Basic Linux commands

Do you remember on how you edited some files in the webinterface? Lets do the same thing again; only from the command line:

### Navigating folders

1. Login to the Puhti webinterface, and start a login shell; first, check which folder you are in by typing `pwd` and hitting `Enter`:

```bash
pwd
```

{:start="2"}
2. Check if there are any files:

```bash
ls
```

{:start="3"}
3. Make a directory and see if it appears:

```bash
mkdir YourNameTestFolder    # replace YourName
ls
```

{:start="4"}
4. Go to that folder.

```bash
cd YourNameTestFolder       # replace YourName
```

💡 Note: if you just type `cd` and the first letter of the folder name, then hit `tab` key, the terminal completes the name. Handy!


Add an empty file into this directory. 

```bash
touch YourNameFile      # replace YourName
```

Check that it is empty:

```bash
cat YourNameFile        # replace YourName
```

Fill it with some content:


💬 These exercises are done with the `nano` editor, but you can use your favorite editor too.

💡 Here's a [nano cheat sheet](https://www.nano-editor.org/dist/latest/cheatsheet.html)


1. Open the file with `nano`:

```bash
nano YourName-first-file.txt      # replace YourName
```

{:start="2"}
2. Edit the file. Type something there!
3. Exit `nano` with `Ctrl+X`, type `Y` to confirm saving and press enter to accept the filename.
4. Check that the modifications are actually there:

```bash
less YourName-first-file.txt      # replace YourName
```

{:start="5"}
5. Exit the preview with `q`.


## Exploring files


1. Download a file into this new folder. Use the command `wget` for downloading from a URL:

```bash
wget https://github.com/csc-training/csc-env-eff/raw/master/_hands-on/linux_prerequisites/my-first-file.txt
```

{:start="2"}
2. Check what kind of file you got and what size it is using the `ls` command with some extra options:

```bash
ls -lth         # options are l for long format, t for sorting by time and h for convenient size units. Anything that starts with a hashtag is a comment and is not executed
```

{:start="3"}
3. Use the `less` command to check out what the file looks like:

```bash
less my-first-file.txt
```

{:start="4"}
4. To exit the `less` preview of the file, hit `q`.

💡 Tip: Instead of `less` you can use `cat` which prints the content of the file(s) straight into the command line. For long texts `less` is recommended.

{:start="5"}
5. Make a copy of this file:

```bash
cp my-first-file.txt YourName-first-file.txt    # replace YourName
ls -lth
less YourName-first-file.txt                    # replace YourName
```

{:start="6"}
6. Remove the file we originally downloaded (leave your own copy).

```bash
rm my-first-file.txt
ls
```

💡 Tip: If you don't want to have duplicate files you can use `mv` to 'move/rename' the file. Syntax is the same: `mv /path/to/source/oldname /path/to/destination/newname`.

## More information

- Learn [how to edit that file](https://csc-training.github.io/csc-env-eff/hands-on/linux_prerequisites/basic-file-editing.html) in the next tutorial!

💡 For more information of a given command line `command`: type `man command` or `command --help` where `command` is replaced with the one that you need help with.

💡 Tip: If you remember *a part of a command* that you have used recently you can search for it with the command `history | grep string`. This will show all your used commands that have included the string `string` (replace this with the pattern you are searching for).



:::{admonition} Advanced topic: Developing scripts remotely
:class: tip, dropdown

- It's possible to use a local editor and push edited files easily into Puhti (or Rahti, ...) via SSH
   - For example, an IDE like _Visual Studio Code_ or a text editor like _Notepad++_
- Follow these [detailed instructions to set them up](https://docs.csc.fi/support/tutorials/remote-dev/)
- Note that [Visual Studio Code](https://docs.csc.fi/computing/webinterface/vscode/) and [Jupyter Notebooks](https://docs.csc.fi/computing/webinterface/jupyter/) are also available through the Puhti web interface

:::

