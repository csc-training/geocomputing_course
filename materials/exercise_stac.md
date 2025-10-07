# Exercise: STAC

:::{admonition} Timing
:class: note
* Time: 20 min
:::

:::{admonition} Goals
:class: note

* Getting familiar with Jupyter in the Puhti web interface
* Learn to use STAC for searching for raster data

:::

:::{admonition} Prerequisites
:class: important

* [CSC user account](https://docs.csc.fi/accounts/how-to-create-new-user-account/) and [project](https://docs.csc.fi/accounts/how-to-create-new-project/)
with [access to Puhti](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

:::

## Open JupyterLab in Puhti web interface

* Open [Puhti web interface](https://puhti.csc.fi) and log in

:::{admonition} Change the default project and username

* `project_2015299` is an example project name, replace with your own CSC project name.
* `cscusername` is an example username, replace with your username.
:::

* [CSC Docs: Jupyter](https://docs.csc.fi/computing/webinterface/jupyter/)

* Open the Jupyter launch page: from front page or `Apps -> Jupyter`
* Use settings: 
  * (Reservation: `geocomputing_day1`, only during course)
  * Project: `project_2015299`
  * Partition: `interactive` (`small` during course)
  * Number of CPU cores: 1
  * Memory (Gb): 8
  * Local disk: 0
  * Time: 0:30:00
  * Python: [geoconda](https://docs.csc.fi/apps/geoconda/)
  * Module version: default
  * Working directory: `/scratch/project_2015299`
  * `Launch`
* Wait a moment for Jupyter to start -> `Connect to Jupyter`
* Open

## Preparations
* Open new Terminal window
* Make a folder for the exercise materials and make it your working directory
* Change the project name and username.
```
mkdir -p /scratch/project_2015299/students/cscusername
cd /scratch/project_2015299/students/cscusername
```

* Copy the example scripts to Puhti.
```
git clone https://github.com/csc-training/geocomputing.git
```

## STAC Notebook

1. In the file explorer, open `students/cscusername/geocomputing/python/STAC
2. Open `STAC_CSC_example_short.ipynb` notebook
3. Follow the notebook, use `Shift+Enter` for running cells.

## End the session

 * Close the web tab
 * Find the session in the Active sessions view and select `Cancel`
    
:::{admonition} Key points
:class: important

* STAC is an easy option for finding and downloading raster data.
* Jupyter is a nice tool for interactively working with Python.

:::
