# Recources and possibilies 

## Why use a supercomputer?

<p>&#8987; Resource needs (time, memory, storage, GPU)</p>
<p>&#128126; “Outsource” heavy computations, keep own computer free</p>
<p>&#127960; Prebuilt environments, application availability</p>
<p>&#128202; Run many experiments at same time</p>
<p>&#127760; Data availability</p>
<p>&#128101; Collaboration possibility</p>
<p>&#10067; CSC specialist support</p>
<p>&#128184; Free of charge for open science at Finnish universities and research institutes.</p>

## Supercomputer

Main differences to own computer:

* Not faster, but bigger
* For speed up: parallelism
* Memory and CPU(/GPU) availability (application needs to make use of this!)
* Non-interactive for heavy computations
* Resource knowledge

## Possibilities

* Use more memory/CPU/GPU than your own computer has available 

<p>&rarr; analyse large files, Machine learning model training </p>

* Speed up so called *embarrassingly parallel* analyses (many identical, but separate tasks) 

<p>&rarr; doing same thing to multiple map tiles/ data chunks </p>

## Harnessing the power

Supercomputer != laptop

### GUI -> script

> Interactive usage is limited in resources. The real power comes from parallelization for which we will need to write scripts.
> Scripts capture what needs to be done in text format and make it understandable for the computer to work with.
> Usage of scripts over GUI also increases reproducibility of your work.
> Demo e.g. Getting GDAL commands from QGIS

### CLI, Python, R

> Simple usecases may be sufficiently run with command line tools only. More complicated workflows can be implemented in any programming language of your choice. If you do not know any, we recommend you start with Python.
> Googling your usecase may provide an overview if there is Python or R packages or command line tools are available for your usecase. 

## CSC Supercomputers

Puhti - Mahti - LUMI

## Puhti

![](./images/puhti_a4.jpg)

## Mahti

![](./images/mahti_a4.jpg)


## LUMI

![](./images/lumi2.jpg)

Name | CPUs | GPUs | Pre-installed GIS tools | Finnish spatial data locally | Scope |
--- | --- | --- | --- | --- | --- |
Puhti | 28 000 | 240 Nvidia V100 | 20 | Yes | National |
Mahti | 90 000 | 96 Nvidia A100 | 1 | No | National |
LUMI | 100 000 | 10 000 AMD MI250X | 5 | No | EU |

Puhti:
* Use cases from interactive single core data processing to medium scale parallel simulations
* The first option to consider for Finnish academic projects

Mahti:
* Geared towards medium and large scale parallel simulations
* Projects move from Puhti to Mahti, once Puhti recources become limiting.

LUMI:
* Research + industry and SME access
* Users are mainly expected to install their own tools.

# Skills needed and how to get them

TODO




