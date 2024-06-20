# Supercomputers

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


 

### Graphical tools -> scripts
![](./images/gui_script.png)

* Supercomputers have some support for working with graphical tools
* GIS tools have often weak support for parallization 
* **Main work is done with scripts**
* Scripts can make analysis parallel
* Scripts also increase reproducibility of your work

:::{admonition} Embarrassingly parallel analyses
:class: note

* Many similar, but independent tasks.
* Tasks split by:
  * Input data: map sheets, rows in a dataframe, data from different time periods etc.
  * Analysis parameters: different scenarios, different variables etc.
* Note, that especially with map sheets extra care might be needed for border areas, for example use overlapping map sheets with [virtual rasters](https://docs.csc.fi/support/tutorials/gis/virtual-rasters/).

:::

:::{admonition} Computing speed
:class: important

* Single core speed: supercompter ~ laptop
* **To increase speed, use many cores**:
  * **Scripts for parallization**
  * Tools that support parallelization out-of-the-box
  * GPU tools
* Running a single core tool/script on many cores will not help
:::
