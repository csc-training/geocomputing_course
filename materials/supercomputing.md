# Why and how?

## Why use a supercomputer?

* **Computing resource needs**:
  * CPU and GPU time
  * Memory
  * Storage
* **Ready computing environment**, pre-installed GIS-tools
* Run several computations at same time
* Spatial data availability
* Fast internet connection to data services
* Collaborate with your project members
* “Outsource” heavy computations, keep own computer for other usage
* **Good documentation, examples for spatial data analysis**
* **CSC specialist support** 
* **Free of charge for open science** at Finnish universities and research institutes.
  

## How to use supercomputers? 
### Graphical tools -> scripts
![](./images/gui_script.png)

* **Main work is done with scripts**
* Also graphical tools available on supercomputers, but mainly for viewing input and output files
* Many graphical tools also have scripting options, see [GIS tools](software.md) for more info.
* Scripts also increase reproducibility of your work

### Faster computing
* Running most common GIS scripts will be as fast on supercomputer as on laptop
* To speed up use **parallel computing** or GPUs.
   * Most GIS-tools have no GPU-support, so the main option is to use parallel computing
   * Deep learning libraries run much faster on GPU.

#### Parallel computing
* Only few GIS tools have built-in support for parallization 
* With scripts and dividing the data any tool can be run in parallel

#### Embarrassingly parallel analyses
* Many similar, but independent tasks.
* Tasks split by:
  * Input data: map sheets, rows in a dataframe, data from different time periods etc.
  * Analysis parameters: different scenarios, different variables etc.
* Note, that especially with map sheets extra care might be needed for border areas, for example use overlapping map sheets with [virtual rasters](https://docs.csc.fi/support/tutorials/gis/virtual-rasters/).
