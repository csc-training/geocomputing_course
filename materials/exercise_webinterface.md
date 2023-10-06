# Exercise - Puhti web interface

:::{admonition} Timing
:class: note
* Time: 60 min
:::

:::{admonition} Goals
:class: note

* Getting familiar with the Puhti web interface
* First contact with the supercomputer
    * Files: moving, viewing, editing
    * Graphical tools: Visual Studio Code, QGIS, Jupyter, RStudio
    * See info about Puhti and your project 

:::

:::{admonition} Prerequisites
:class: important

* [CSC user account](https://docs.csc.fi/accounts/how-to-create-new-user-account/) and [project](https://docs.csc.fi/accounts/how-to-create-new-project/) with [access to Puhti](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

:::

## Get familiar with Puhti web interface

* Open [Puhti web interface](https://puhti.csc.fi) and log in

### Info
* Puhti general status: bottom of front page
   * Sometimes when the `Disk lag` here is high, reading and writing files might get slow.
* Own projects, remaining billing units: `Tools` -> `Project view`
* Disk usage of own projects: `Tools` -> `Disk quotas`
* Running jobs: `Jobs` -> `Active jobs`

:::{admonition} Change the default project and username

* `project_200xxxx` is example project name, replace with your own CSC project name.
* `cscusername` is example username, replace with your username.
:::

### Files 
* Open home directory: `Files` -> `Home Directory`
* Create new directory and open it
* Create new `.txt` file with your name
* Move the new file under scratch: 
   * Mark check-box in front of the file
   * Click `Copy/Move`
   * Open `/scratch/project_200xxxx`
   * Click `Move`
* Open your scratch folder
* Download your file to your local computer
* Delete the file
  
:::{admonition} Moving data

Web interface is for moving up to 10Gb data, if you have more data use other tools. More info in [moving data](moving_data.md)

:::
  

### Graphical applications
#### Jupyter

* For Python: any CSC module or own installation
* [CSC Docs: Jupyter](https://docs.csc.fi/computing/webinterface/jupyter/)

* Open the Jupyter launch page: from front page or `Apps -> Jupyter`
* Use settings: 
  * (Reservation: `geocomputing`, only during course)
  * Project: `project_200xxxx`
  * Partition: `interactive` (`small` during course)
  * Number of CPU cores: 1
  * Memory (Gb): 2
  * Local disk: 0
  * Time: 0:15:00
  * Python: [geoconda](https://docs.csc.fi/apps/geoconda/)
  * Jupyter type: Lab
  * Working directory: `/users/cscusername`
  * `Launch`
* Wait a moment for Jupyter to start -> `Connect to Jupyter`
* Create new Notebook: `+` -> Notebook: Python 3
* Open Statistic Finland Paavo post code data and plot it, add code and run the it with `Shift + Enter`.

```
import geopandas
src = geopandas.read_file('/appl/data/geo/tilastokeskus/paavo/2023/pno_tilasto_2023.shp')
src.plot()
```

* End the session:
   * Delete the Notebook.
   * Close the web tab
   * In Active sessions view: `Delete`

#### Desktop with QGIS

* QGIS, GRASS GIS, SAGA GIS, SNAP etc are available via Desktop
* [CSC Docs: Desktop](https://docs.csc.fi/computing/webinterface/desktop/)

* Open the Desktop launch page: from front page or `Apps -> Desktop`
* Use settings: 
  * (Reservation: `geocomputing`, only during course)
  * Project: `project_200xxxx`
  * Partition: interactive (`small` during course)
  * Number of CPU cores: 1
  * Memory (Gb): 4
  * Local disk: 0
  * Time: 0:15:00
  * `Launch`
* Wait a moment for Desktop to start -> `Launch Desktop`
* Double-click the QGIS icon
* Open Statistic Finland Paavo post code data
   *  `Layer` -> `Add layer` -> `Add vector layer`
      * Source Type: `File`
      * Source: `/appl/data/geo/tilastokeskus/paavo/2023/pno_tilasto_2023.shp`
* See file information with GDAL
   * `Processing` -> `Toolbox` -> `GDAL` -> `Vector miscellanious` -> `Vector information`
   * The open dataset is selected by default
   * `Run`
   * Note, if interested in moving from graphical QGIS to scripting:
      * The GDAL commandline command is displayed in the lower part of dialog box and log.
      * `Advanced` menu provides this command also as `qgis_processing` command and as PyQGIS code.
* End the session:
   * Close QGIS.
   * Close the web tab
   * In Active sessions view: `Delete`
      * This only ends the Desktop session, any files written during the session would be available also afterwards.

:::{admonition} QGIS in practice on supercomputer

* QGIS is designed for desktop use and it mostly uses only 1 core, so running it on supercomputer is rather slower than on desktop. QGIS is in Puhti and LUMI mainly for easy viewing of input and output data. 
* With `qgis_processing` or PyQGIS scripts it is possible to paralellize your data analysis. In general other Python packages are faster, but if you have these scripts already available, they can be used.

:::

#### Extra

* Look from [CSC Docs](https://docs.csc.fi) how to start SNAP or some other tool of your interest in web interface.

    
:::{admonition} Key points
:class: important

* Web interface provides easy access to Puhti and its graphical tools.
* QGIS, SNAP, Jupyter, RStudio, Visual Studio Code are the most used tools.

:::
