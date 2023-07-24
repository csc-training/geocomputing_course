# Installing own software

Always remember to add what you did to your PATH or PYTHONPATH!

## Python

### Adding Python packages to existing modules

Add a package on top of a module with pip:

```
module load geoconda
export PYTHONUSERBASE=/projappl/<your_project>/my-python-env
pip install --user somepackage
```

Using the self-installed packages:

```
module load geoconda
export PYTHONPATH=/projappl/<your_project>/my-python-env/lib/python3.9/site-packages/
```

### Own Python environments

The easiest way to create an own Python environment when all packages can be installed via Conda or pip is to use [tykky](https://docs.csc.fi/computing/containers/tykky/).

Prerequisites: a Conda `environment.yml`

```
module purge
module load tykky
# create a new directory for the installation
mkdir /projappl/<your_project>/<yournamehere>
# create your own environment into the just created installation directory
conda-containerize new --prefix <install_dir> environment.yml
# add your environment to your path
export PATH="<install_dir>/bin:$PATH"
```

## R

### Adding R packages to `r-env`

On commandline create a R version specific directory: 
```
mkdir /projappl/<project>/project_rpackages_<rversion>
```
In R:

```
# Add this to your R code:
.libPaths(c("/projappl/<project>/project_rpackages_<rversion>", .libPaths()))
libpath <- .libPaths()[1]

# Check that the folder is now visible:
.libPaths() # It should be first on the list

```

To use in R script, add:
```
.libPaths(c("/projappl/<project>/project_rpackages_<rversion>", .libPaths()))
```


## Other software

* Generally useful? -> ask from servicedesk to install
* Niche? -> try yourself using containers (tykky)
