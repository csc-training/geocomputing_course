# Installing own tools

## Adding some packages to existing modules

* Generally easiest option.
* [CSC Docs: Installing **Python** packages to existing modules](https://docs.csc.fi/apps/python/#installing-python-packages-to-existing-modules)
  * geoconda, tensorflow, pytorch, python-data etc.
  * The added package must be available via `pip`.
* [CSC Docs: **R** package installations](https://docs.csc.fi/apps/r-env/#r-package-installations) 
* [CSC Docs: **Julia**, adding packages to an environment](https://docs.csc.fi/apps/julia/#adding-packages-to-an-environment)

## Tykky

* The easiest way to create an own installation is with Tykky
* Tykky has 3 options, new installation based on:
  * `conda` .yml file
  * `pip` requirement file
  * Existing Docker image
* [CSC Docs: Tykky](https://docs.csc.fi/computing/containers/tykky)
* [LUMI Docs: container-wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/) is the same as Tykky

## Other
* [CSC Docs: Installing software](https://docs.csc.fi/computing/installing/), inc installing from source, Spack
* [LUMI Docs: Installing additional software](https://docs.lumi-supercomputer.eu/software/#installing-additional-software), inc installing from source, EasyBuild
* Generally useful? -> ask from servicedesk to install

## Installation exercise 
### Tykky installation based on existing Docker image

* We will install `lastools` based on [pydo's lastools Docker image](https://hub.docker.com/r/pydo/lastools).
* We use the `projappl` disk, which is the best place for software installations.
* Lastools is in Puhti already available, also as newer Linux-native installation.
* During the course we will use interactive job for doing the installation because of 50 persons doing it at the same time. Usually installations are done on login node.

:::{admonition} Change the default project and username

* `project_200xxxx` is example project name, replace with your own CSC project name.
* `cscusername` is example username, replace with your username.
:::

* Open [Puhti web interface](https://puhti.csc.fi) and log in
* Open Login node shell
* During the course only, open interactive job:
```
srun --reservation=geocomputing_fri --account=project_2008648 --mem=4000 --ntasks=1 --time=0:20:00 --gres=nvme:4 --pty bash -i
```

Make Tykky tools available
```
module load tykky
```

Create a new directory for the installation and make the folder **above** it to your working directory
```
mkdir -p /projappl/project_200xxxx/students/cscusername/lastools
cd /projappl/project_200xxxx/students/cscusername
```

Create the new instalaltion
```
wrap-container -w /opt/LAStools docker://pydo/lastools:latest --prefix lastools
```

* `-w /opt/LAStools` - where are the tools located inside the container, that should be available
* `docker//:pydo/lastools:latest` - the existing Docker iamge
* `--prefix lastools` - location of the new installation 

Add the location of your new installation to your PATH. Note that Tykky prints out the correct command for you.
```
export PATH="/projappl/project_200xxxx/students/cscusername/lastools/bin:$PATH"
```
Test your new installation.
```
lasinfo -version
lasinfo -i /appl/data/geo/mml/laserkeilaus/2008_latest/2018/W444/1/W4444G4.laz
```

:::{admonition} PATH setting

PATH defines where system is looking for tools. Changing PATH like above is valid until the Puhti session is alive. PATH (or PYTHONPATH) has to be set each session again, so it is good to add it to your batch job file.

:::
