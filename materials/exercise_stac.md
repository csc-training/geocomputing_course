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

## Get familiar with STAC and Jupyter

* Open [Puhti web interface](https://puhti.csc.fi) and log in

:::{admonition} Change the default project and username

* `project_200xxxx` is example project name, replace with your own CSC project name.
* `cscusername` is example username, replace with your username.
:::

#### Jupyter

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

* End the session:
   * Delete the Notebook.
   * Close the web tab
   * In Active sessions view: `Cancel`
    
:::{admonition} Key points
:class: important

* Web interface provides easy access to Puhti and its graphical tools.
* QGIS, SNAP, Jupyter, RStudio, Visual Studio Code are the most used tools.

:::
