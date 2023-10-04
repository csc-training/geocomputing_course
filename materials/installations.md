# Installing own tools

## Adding some packages to existing modules

* Generally easiest option.
* [CSC Docs: Installing **Python** packages to existing modules](https://docs.csc.fi/apps/python/#installing-python-packages-to-existing-modules)
  * geoconda, tensorflow, pytorch, python-data ...
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

> [!IMPORTANT]  
> In these scripts `project_200xxxx` has been used as example project name. Change the project name to your own CSC project name.
> `cscusername` is example username, replace with your username.

Make Tykky tools available
```
module purge
module load tykky
```

Create a new directory for the installation and make the folder above it to your working directory
```
mkdir -p /scratch/project_200xxxx/students/cscusername/lastools
cd /scratch/project_200xxxx/students/cscusername
```

Create the new instalaltion
```
wrap-container -w /opt/LAStools docker//:pydo/lastools:latest --prefix lastools
```

* `-w /opt/LAStools` - where are the tools located inside the container, that should be available
* `docker//:pydo/lastools:latest` - the existing Docker iamge
* `--prefix lastools` - location of the new installation 

Add the location of your new installation to your PATH
```
export PATH="/scratch/project_200xxxx/students/cscusername/lastools/bin:$PATH"
```

> [!IMPORTANT]  
> PATH defines where system is looking for tools. Changing PATH like above is valid until the Puhti session is alive. PATH (or PYTHONPATH) has to be set each session again, so it is good to add it to your batch job file.
