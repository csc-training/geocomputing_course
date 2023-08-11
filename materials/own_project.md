# Own project hints

* keep scripts under version control (also simplifies collaboration and synchronising different computers, e.g. git(hub))
* on Puhti: 
    * scripts in `/projappl/project_200xxxx/your_groupname/`
    * data in `/scratch/project_200xxxx/your_groupname/` -> raw data, intermediate and final results
    * personal configuration scripts in `/users/your_username/`
    * Puhti webinterface / `scp` for data transfer: own computer - Puhti
    * `wget` for data transfer:  internet - Puhti

On project organization: [CodeRefinery lesson - Reproducible research](https://coderefinery.github.io/reproducible-research/organizing-projects/)<br>
[CodeRefinery lesson - Modular code development](https://coderefinery.github.io/modular-type-along/instructor-guide/)


## Moving from GUI to CLI/scripts

Some GUI tools provide the commands that correspond to GUI tool either in documentation or as part of the tool.
> Show QGIS -> GDAL commands

Google the toolname from eg QGIS and the desired scripting language to get some ideas.


## Moving from own computer to HPC

### Your own scripts

* no hard coded filepaths such as `/my/home/dir/file.txt`
  * read from stdin or config file instead
* modular code
  * easier to parallelize, if needed
* know your dependencies
* know your resources
* make sure your code works as expected before moving to HPC

#### Python

* Package availability: `module load geoconda` and `list-packages` ([adding Python packages for your own usage](https://docs.csc.fi/apps/python/#installing-python-packages-to-existing-modules))

#### R

#### Other


#### Making use of HPC resources

* internal vs external parallelization
* 

