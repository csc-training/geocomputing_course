# Terminal

TODO: Shorten and share with prerequisites
TODO: Check advanced

## Why use?

TODO: fill

## Basic Linux commands

> ‼️ To begin make sure you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/) that is a member of a project which [has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

> ☝🏻 You should also have already [logged in to Puhti with SSH](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html) or via the Puhti web interface (and opened a login node shell).

## Navigating folders

1. Now that you have logged in to Puhti, check which folder you are in by typing `pwd` and hitting `Enter`:

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

## Basic file editing

> ‼️ To begin, make sure you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/) that is a member of a project which [has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

> ☝🏻 You should also have already [logged in to Puhti with SSH](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html).

> ☝🏻 Note: For graphical output to work you need to log in with `ssh -X cscusername@puhti.csc.fi`. On Windows/macOS you also need to have an X server installed and running. [See details in the previous tutorial](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html#remote-graphics). Another option is to use the Puhti web interface.

In the [previous tutorial](https://csc-training.github.io/csc-env-eff/hands-on/linux_prerequisites/basic-linux-commands.html) we downloaded a file called `my-first-file.txt`, made a copy of it named `YourName-first-file.txt`, and now we practice how to edit it!

💬 These exercises are done with the `nano` editor, but you can use your favorite editor too.

💡 Here's a [nano cheat sheet](https://www.nano-editor.org/dist/latest/cheatsheet.html)

## Processing text files

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

## Login with SSH

- SSH is a terminal program that gives you command-line access on the CSC supercomputer
- It is a versatile main interface to a supercomputer
   - Laptop &harr; Toyota, Supercomputer &harr; F1. F1 needs a specialist interface.
- Please read this page for an introduction on [how to log in with SSH](https://docs.csc.fi/computing/connecting/)
   - Mac and Linux have SSH. On Windows, Powershell can be used, but we recommend the Puhti web interface, or clients like MobaXterm or PuTTY
   - Note the [prerequisites to be able to access Puhti](https://docs.csc.fi/support/faq/how-to-get-puhti-access/)
- Plain SSH will not allow displaying remote graphics
   - Puhti web interface is often best for this, but can be enabled also by X11-tunneling (additional installations required on Windows, see link above)

# Advanced topic: Setting up SSH keys

- Using SSH keys is easier and safer than using a password with every login
- SSH keys can be easily used in Windows, Mac, Linux
- Consult our [tutorials on how to set up SSH keys for your account](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)
   - [Logging in to LUMI](https://docs.lumi-supercomputer.eu/firststeps/getstarted/) requires setting up an SSH key pair and registering the public key in [My CSC](https:/my.csc.fi)

# Advanced topic: Developing scripts remotely

- It's possible to use a local editor and push edited files easily into Puhti (or Rahti, ...) via SSH
   - For example, an IDE like _Visual Studio Code_ or a text editor like _Notepad++_
- Follow these [detailed instructions to set them up](https://docs.csc.fi/support/tutorials/remote-dev/)
- Note that [Visual Studio Code](https://docs.csc.fi/computing/webinterface/vscode/) and [Jupyter Notebooks](https://docs.csc.fi/computing/webinterface/jupyter/) are also available through the Puhti web interface

