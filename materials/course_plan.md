# Geocomputing course plan

* CSC 
* CSC services
* CSC support

* Start with GUI via webinterface, no in depth info on resources, start QGIS or SNAP
    * talk about usecases
* basics of supercomputing, mainly resources
    * resource knowledge
    * fair share
* supercomputer setup
    * Puhti overview
    * login vs compute node
* compute node: interactive usage of some gdal/pdal/ogr command (show how to get it from QGIS)
    * running into limits of interactiveness
* the sbatch script
    * resource + command (same as above just together in one)
    * many commands in script -> python/R/bash script
* calling it "serial"
* now parallel; harnessing the power
    * external vs internal
    * external
        * script as usual
        * GNU parallel
        * array job
    * internal
        * depends on tool, does it have multi cpu option (multi, cores, n_cores or similar?)
        * R/Python: use dedicated packages 
* own project hints
    * script and tools
        * from script that runs on your computer to hpc enabled 
        * available tools
    * data
        * storage (directories and Allas)
        * transfer
        * strategies

-> Where to put Jupyter/Rstudio? Ask before course about state of scripting? If they all do script it can be in beginning, if not it could be as part of R/Python exercise?

