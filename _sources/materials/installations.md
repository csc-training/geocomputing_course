# Installing own tools

## Adding some packages to existing modules

* Generally the easiest option.
* [CSC Docs: Installing **Python** packages to existing modules](https://docs.csc.fi/support/tutorials/python-usage-guide/#installing-python-packages-to-existing-modules)
  * geoconda, tensorflow, pytorch, python-data etc.
  * The added package must be available via `pip`.
* [CSC Docs: **R** package installations](https://docs.csc.fi/apps/r-env/#r-package-installations) 
* [CSC Docs: **Julia**, adding packages to an environment](https://docs.csc.fi/apps/julia/#adding-packages-to-an-environment)

## Tykky

* The easiest way to create a custom installation is with Tykky
* Tykky has 3 options, new installation based on:
  * `conda` .yml file
  * `pip` requirement file
  * Existing Docker image
* [CSC Docs: Tykky](https://docs.csc.fi/computing/containers/tykky)
* [LUMI Docs: container-wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/) is the same as Tykky

:::{admonition} Do not use "normal" conda installations
:class: important

* "Normal" conda installations create a lot of files - up to hundreds of thousands
* Supercomputers do not like too many files
* Use Tykky to create containerized conda installation

:::

## Other
* [CSC Docs: Installing software](https://docs.csc.fi/computing/installing/), inc installing from source, Spack
* [LUMI Docs: Installing additional software](https://docs.lumi-supercomputer.eu/software/#installing-additional-software), inc installing from source, EasyBuild
* Generally useful? -> ask from servicedesk to install

## Installation exercise 
### Tykky installation based on existing Docker image

* We will install `lastools` based on [pydo's lastools Docker image](https://hub.docker.com/r/pydo/lastools).
* We use the `projappl` disk, which is the best place for software installations.
* Lastools is already available on Puhti, also as a newer Linux-native installation.
* During the course we will use an interactive job for doing the installation,
  because we will have 50 users doing it at the same time, which stresses the
  shared file system. Usually installations are done on a login node.

:::{admonition} Change the default project and username

* `project_20xxxxx` is an example project name, replace with your own CSC project name.
* `cscusername` is an example username, replace with your username.
:::

* Open [Puhti web interface](https://puhti.csc.fi) and log in
* Open Compute node shell (outside of the course, also Login node shell could be used)
  * Reservation: geocomputing_thu (only during the course)
  * Project: project_20xxxxx
  * Partition: small
  * Number of CPU cores: 1
  * Memory (GB): 4
  * Local disk (GB): 4
  * Time: 00:30:00

Make Tykky tools available
```
module load tykky
```

Create a new directory for the installation and make the folder **above** it your working directory
```
mkdir -p /projappl/project_20xxxxx/students/cscusername/lastools
cd /projappl/project_20xxxxx/students/cscusername
```

Create the new installation
```
wrap-container -w /opt/LAStools docker://pydo/lastools:latest --prefix lastools
```

* `-w /opt/LAStools` - where the tools are located inside the container, it should be accessible
* `docker//:pydo/lastools:latest` - the existing Docker image
* `--prefix lastools` - location of the new installation 

Add the location of your new installation to your PATH. Note that Tykky prints out the correct command for you.
```
export PATH="/projappl/project_20xxxxx/students/cscusername/lastools/bin:$PATH"
```
Test your new installation.
```
lasinfo -version
lasinfo -i /appl/data/geo/mml/laserkeilaus/2008_latest/2018/W444/1/W4444G4.laz
```

:::{admonition} PATH setting

PATH defines where the system looks for tools. Changes to PATH, like those
above, are in effect while the Puhti session is alive. PATH (or PYTHONPATH)
has to be set again in each session, so it is good to add it to your batch job
file.

:::
