# Supercomputers

## Why use a supercomputer?

* **Computing resource needs**:
  * CPU and GPU time
  * Memory
  * Storage
* “Outsource” heavy computations, keep own computer for other usage
* **Ready computing environment**, pre-installed GIS-tools
* Run many experiments at same time
* Data availability
* Collaboration possibility
* Good documentation, examples for spatial data analysis
* **CSC specialist support**, 
* **Free of charge for open science** at Finnish universities and research institutes.

## Supercomputers in Kajaani

![](./images/lumi2.jpg)

Name | CPUs | GPUs | Pre-installed GIS tools | Finnish spatial data locally | Scope |
--- | --- | --- | --- | --- | --- |
Puhti | 28 000 | 240 Nvidia V100 | **20** | **Yes** | Finland |
Mahti | 90 000 | 96 Nvidia A100 | 1 | No | Finland |
LUMI | **100 000** | **10 000 AMD** MI250X | 5 | No | EU |

Puhti:
* From interactive single core to medium scale parallel analysis
* **The first option to consider for Finnish academic projects**

Mahti:
* For medium and large scale parallel analysis
* Projects move from Puhti to Mahti, once Puhti recources become limiting.

LUMI:
* For very large scale analysis
* **For companies and international projects**


# Puhti supercomputer compared to other options

|  | Puhti supercomputer*| cPouta virtual machine| my laptop |
|---|---| ---|---|
|Max per job: CPU | **4000** | 48 | 4 |
|Max per job: memory Gb | **1500** | 240 | 18 |
|Max per job: GPU | **80** | 4 | 1 |
|Pre-installed GIS tools | **Yes** | No | No |
|Main Finnish datasets  | **Yes** | No | No |
|Admin rights | No | **Yes** | Yes |


:::{admonition} Computing speed
:class: important

* Supercomptuer single core speed ~ laptop single core speed
* **For speed up, use many cores:
  * Scripts for parallization
  * Tools that support parallelization out-of-the-box
  * GPU tools


Application needs to make use of this!)
:::
 

### Graphical tools -> scripts
![](./images/gui_script.png)

* Supercomputers have some support for working with graphical tools
* Main work is done with scripts
* GIS tools have often weak support for parallization
* Scripts can make analysis parallel
* Scripts also increase reproducibility of your work

:::{admonition} Embarrassingly parallel analyses
:class: note

* Many similar, but independent tasks.
* In GIS scope it is often possible to split  or analysis parameters:
  * Input data: map sheets, rows in a dataframe, data from different time periods etc.
  * Analysis parameters: different scenarios, different variables etc.

* Note, that especially with map sheets extra care might be needed for border areas, for example use overlapping map sheets.

:::







