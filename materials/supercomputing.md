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
* **CSC specialist support**, 
* **Free of charge for open science** at Finnish universities and research institutes.

## Supercomputers in Kajaani

![](./images/lumi2.jpg)

Name | CPUs | GPUs | Pre-installed GIS tools | Finnish spatial data locally | Scope |
--- | --- | --- | --- | --- | --- |
**Puhti** | 28 000 | 240 Nvidia V100 | **20** | **Yes** | Finland |
**Mahti** | 90 000 | 96 Nvidia A100 | 1 | No | Finland |
**LUMI** | **100 000** | **10 000** AMD MI250X | 5 | No | EU |

Puhti:
* From interactive single core to medium scale parallel analysis
* **The first option to consider for Finnish academic projects**
* [CSC Docs: Technical details about Puhti](https://docs.csc.fi/computing/systems-puhti/)

Mahti:
* For medium and large scale parallel analysis
* Projects move from Puhti to Mahti, once Puhti recources become limiting.
* [CSC Docs: Technical details about Mahti](https://docs.csc.fi/computing/systems-mahti/)

LUMI:
* For very large scale analysis
* **For companies and international projects**
* [LUMI Docs: Hardware overview](https://docs.lumi-supercomputer.eu/hardware/)


## Puhti compared to other options

|  | Puhti supercomputer*| cPouta virtual machine| my laptop |
|---|---| ---|---|
|Max per job: CPU | **4000** | 48 | 4 |
|Max per job: memory, Gb | **1500** | 240 | 18 |
|Max per job: GPU | **80** | 4 | 1 |
|Pre-installed GIS tools | **Yes** | No | No |
|Main Finnish datasets  | **Yes** | No | No |
|Admin rights | No | **Yes** | Yes |


:::{admonition} Computing speed
:class: important

* Single core speed: supercompter ~ laptop
* **For speed up, use many cores**:
  * **Scripts for parallization**
  * Tools that support parallelization out-of-the-box
  * GPU tools
* Running a single core tool/script on many cores will not help
:::
 

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

## Technical skills needed for using supercomputers

* Domain knowledge:
   * [GIS tools](software.md)
   * [Spatial data sources](https://research.csc.fi/open-gis-data)
* Basic Linux skills: 
    * [Terminal](terminal.md)
    * [Moving data](moving_data.md)
	   * [CSC Linux tutorial](https://docs.csc.fi/support/tutorials/env-guide/)
* Supercomputer basics
* **Scripting skills and how to write parallel scripts**, one of these: 
   * Python:
       * [CSC Docs: Python GIS learning materials](https://docs.csc.fi/apps/geoconda/#references)
       * [CSC Docs: Python parallel jobs](https://docs.csc.fi/apps/python/#python-parallel-jobs)
       * [CSC Docs: Dask tutorial](https://docs.csc.fi/support/tutorials/dask-python/)
    * R:
       * [CSC Docs: Spatial R learning materials](https://docs.csc.fi/apps/r-env-for-gis/#references)
       * [CSC Docs: Parallel jobs using R](https://docs.csc.fi/support/tutorials/parallel-r/)
    * bash:
       * [CSC bash tutorial](https://docs.csc.fi/support/tutorials/env-guide/linux-bash-scripts/)
    * Julia, MATLAB etc
