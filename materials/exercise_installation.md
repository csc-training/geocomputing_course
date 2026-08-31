## Installation exercise 
### Tykky installation based on existing Docker image

* We will install `lastools` based on [pydo's lastools Docker image](https://hub.docker.com/r/pydo/lastools).
* We use the `projappl` disk, which is the best place for software installations.
* Lastools is already available on Roihu, also as a newer Linux-native installation.
* During the course we will use an interactive job for doing the installation,
  because we will have 50 users doing it at the same time, which stresses the
  shared file system. Usually installations are done on a login node.

:::{admonition} Change the default project

* `project_2020458` is an example project name, replace with your own CSC project name.
:::

* Open [Roihu web interface](https://roihu.csc.fi) and log in
* Open Compute node shell (outside of the course, also Login node shell could be used)
  * Reservation: geocomputing_day2 (only during the course)
  * Project: project_2020458
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
mkdir -p /projappl/project_2020458/students/$USER/lastools
cd /projappl/project_2020458/students/$USER
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
export PATH="/projappl/project_2020458/students/$USER/lastools/bin:$PATH"
```
Test your new installation.
```
lasinfo -version
lasinfo -i /appl/data/geo/mml/laserkeilaus/2008_latest/2018/W444/1/W4444G4.laz
```

:::{admonition} PATH setting

PATH defines where the system looks for tools. Changes to PATH, like those
above, are in effect while the Roihu session is alive. PATH (or PYTHONPATH)
has to be set again in each session, so it is good to add it to your batch job
file.

:::