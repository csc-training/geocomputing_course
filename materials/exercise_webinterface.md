# Exercise: Roihu web interface

:::{admonition} Timing
:class: note
* Time: 30 min
:::

:::{admonition} Goals
:class: note

* Getting familiar with the Roihu web interface
* First contact with the supercomputer
    * Files: moving, viewing, editing
    * Graphical tools: Visual Studio Code, QGIS, Jupyter, RStudio
    * See info about Roihu and your project 

:::

:::{admonition} Prerequisites
:class: important

* [CSC user account](https://docs.csc.fi/accounts/how-to-create-new-user-account/) and [project](https://docs.csc.fi/accounts/how-to-create-new-project/) with [access to Roihu](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

:::

## Get familiar with Roihu web interface

* Open [Roihu web interface](https://roihu.csc.fi) and log in

:::{admonition} Change the default project

* `project_2020458` is an example project name, replace with your own CSC project name.
:::

### Info
* Roihu general status: bottom of front page
* Own projects, remaining billing units: `Tools` -> `Project view`
* Disk usage of own projects: `Tools` -> `Disk quotas`
* Running jobs: `Jobs` -> `Active jobs`


### Files 
* `Files` -> ...

:::{admonition} Moving data

The web interface can be used for moving up to 10GB of data. If you have more data, use other tools. More info on [moving data](moving_data.md).

:::

### Graphical applications
#### Desktop with QGIS

* QGIS, GRASS GIS, SAGA GIS, SNAP etc are available via Desktop
* [CSC Docs: Desktop](https://docs.csc.fi/computing/webinterface/desktop/)

* Open the Desktop launch page: from front page or `Apps -> Desktop`
* Use settings: 
  * (Reservation: `geocomputing_day1`, only during course)
  * Project: `project_2020458`
  * Partition: interactive (`small` during course)
  * Number of CPU cores: 1
  * Memory (Gb): 4
  * Time: 0:15:00
  * `Launch`
* Wait a moment for Desktop to start -> `Launch Desktop`
* Start QGIS: ´Applictions` -> `Geosciences` -> `QGIS`
* Open Statistic Finland Paavo post code data
   *  `Layer` -> `Add layer` -> `Add vector layer`
      * Source Type: `File`
      * Source: `...` -> `/dataset/project_2019680/tilastokeskus/paavo/2023/pno_tilasto_2023.shp`
* See file information with GDAL
   * `Processing` -> `Toolbox` -> `GDAL` -> `Vector miscellanious` -> `Vector information`
   * The open dataset is selected by default
   * `Run`
   * Note, if interested in moving from graphical QGIS to scripting:
      * The GDAL commandline command is displayed in the lower part of dialog box and log.
      * `Advanced` menu provides this command also as `qgis_processing` command and as PyQGIS code.

![](./images/QGIS_GDAL.png)
      
* End the session:
   * Close QGIS.
   * Close the web tab
   * Find the session in the Active sessions view and select `Cancel`
      * This only ends the Desktop session, any files written during the session would be available also afterwards.

:::{admonition} QGIS in practice on supercomputer

* QGIS is designed for desktop use and it mostly uses only 1 core, so running it on a supercomputer is rather slower than on desktop. QGIS is in Roihu and LUMI mainly for easy viewing of input and output data. 
* With `qgis_processing` or PyQGIS scripts it is possible to parallelize your data analysis. In general other Python packages are faster, but if you have these scripts already available, they can be used.

:::

#### Extra

* Look from [CSC Docs](https://docs.csc.fi) how to start SNAP or some other tool of your interest in web interface.

    
:::{admonition} Key points
:class: important

* Web interface provides easy access to Roihu and its graphical tools.
* QGIS, SNAP, Jupyter, RStudio, Visual Studio Code are the most used tools.

:::
