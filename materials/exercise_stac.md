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

* `project_200xxxx` is example project name, replace with your own CSC project name.
* `cscusername` is example username, replace with your username.
:::

* [CSC Docs: Jupyter](https://docs.csc.fi/computing/webinterface/jupyter/)

* Open the Jupyter launch page: from front page or `Apps -> Jupyter`
* Use settings: 
  * (Reservation: `geocomputing_thu`, only during course)
  * Project: `project_200xxxx`
  * Partition: `interactive` (`small` during course)
  * Number of CPU cores: 1
  * Memory (Gb): 8
  * Local disk: 0
  * Time: 0:15:00
  * Python: [geoconda](https://docs.csc.fi/apps/geoconda/)
  * Module version: default
  * Working directory: `/scratch/project_200xxxx`
  * `Launch`
* Wait a moment for Jupyter to start -> `Connect to Jupyter`
* Open

## Preparations
* Open new Termianl window
* Make a folder for the exercise materials and make it your working directory
* Change the project name and username.
```
mkdir -p /scratch/project_200xxxx/students/cscusername
cd /scratch/project_200xxxx/students/cscusername
```

* Copy the example scripts to Puhti.
```
git clone https://github.com/csc-training/geocomputing.git
```

## STAC Notebook

1. In file exporer open: `students/cscusername/geocomputing/python/STAC
2. Open `STAC_CSC_example.ipynb` notebook
3. Follow the notebook, use `Shift+Enter` for running cells.

## End the session

 * Close the web tab
 * In Active sessions view: `Cancel`
    
:::{admonition} Key points
:class: important

* STAC is an easy option for finding and downloading raster data.
* Jupyter is a nice tool for interactively working with Python.

:::