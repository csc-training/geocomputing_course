# Supercomputing 

## Why use a supercomputer?

<p style="font-size:40px;">&#8987; Resource needs (time, memory, storage, GPU)</p>
<p style="font-size:40px;">&#128126; “Outsource” heavy computations, keep own computer free</p>
<p style="font-size:40px;">&#127960; Prebuilt environments, application availability</p>
<p style="font-size:40px;">&#128202; Run many experiments at same time</p>
<p style="font-size:40px;">&#127760; Data availability</p>
<p style="font-size:40px;">&#128101; Collaboration possibility</p>
<p style="font-size:40px;">&#10067; CSC specialist support</p>
<p style="font-size:40px;">&#128184; Free of charge for open science at Finnish universities and research institutes.</p>

## Supercomputer

Main differences to own computer:
<br><br>

* Not faster, but bigger
* For speed up: parallelism
* Memory and CPU(/GPU) availability (application needs to make use of this!)
* Non-interactive for heavy computations
* Resource knowledge

## Possibilities

* Use more memory/CPU/GPU than your own computer has available <br>
<br>
<p>&rarr; analyse large files, Machine learning model training </p>
<br>
* Speed up so called *embarrassingly parallel* analyses (many identical, but separate tasks) <br><br>
<p>&rarr; doing same thing to multiple map tiles/ data chunks </p>


## CSC Supercomputers

<br><br><br>

<p align="center">
<b>Puhti - Mahti - LUMI</b>
</p>

## Puhti

<div class="column">

<p align="center">
  <img src="../images/puhti_a4.jpg" width="55%">
</p>

</div>

<div class="column" >

<br>

* Use cases from interactive single core data processing to medium scale parallel simulations
* `~28 000` Intel CPUs 
* `240` Nvidia V100 GPUs 
* Wide stack of pre-installed software
</div>

## Mahti

<div class="column">

<p align="center">
  <img src="../images/mahti_a4.jpg" width="55%">
</p>

</div>

<div class="column">

<br>

* Geared towards medium and large scale parallel simulations
* `~90 000` Intel CPUs
* `96` Nvidia A100 GPUs 
* Some pre-installed software

</div>

## LUMI

<div class="column">

<p align="center">
  <img src="../images/lumi2.jpg" width="95%">
</p>
</div>

<div class="column">

<br>

* Research + industry and SME access
* `~100 000`  AMD EPYK CPUs
* `~10 000` AMD MI250X GPUs
* Some pre-installed software
</div>

## Modules

Applications in Puhti are provided in modules. Use

<br>

`module load <modulename>`

<br>

before every application use to make application available.

Check [`https://docs.csc.fi/apps`](https://docs.csc.fi/apps) for module names and versions.

## Directories

<br>

* HOME – user specific; personal configuration files
* PROJAPPL – project specific; your installations and shared binaries
* SCRATCH – project specific; main working area


# Puhti 

<p align="center">
  <img src="images/puhti_overview.png" width="50%">
</p>



## Jobs and queueing 

* **Batch** jobs
	* resource request
	* computing step(s)
* Queue for resource management system to grant resources
* All heavy computing must be done via batch jobs!

## Serial vs array vs parallel

> TODO: image here

## Example sbatch script

```
#!/bin/bash
#SBATCH --account=<project>      # Choose the billing project. Has to be defined!
#SBATCH --time=00:02:00          # Maximum duration of the job. Upper limit depends on the partition. 
#SBATCH --partition=test         # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --ntasks=1               # Number of tasks. Upper limit depends on partition. For a serial job this should be set 1!

srun hostname                    # Print compute node name that has been allocated

``` 

<br>
<p>&rarr; File `simple.bash` </p> <br>
<p>&rarr; Submit for computation with `sbatch simple.bash` </p>

## Monitoring jobs

* Standard output in file: slurm-<jobid>.out
* `squeue -u $USER`
* `seff <jobid>`
* `scancel <jobid>`


## Applications available on Puhti

<div class="column">
* CloudCompare
* FORCE 
* GDAL/OGR
* GRASS GIS
* LasTools
* MatLab 
* OpenDroneMap
* Orfeo Toolbox
* PCL
* PDAL
</div>

<div class="column">
* Python geospatial packages: geoconda
* QGIS
* R geospatial packages: r-env
* SagaGIS
* SNAP, Sen2cor, sen2mosaic
* WhiteboxTools
* Zonation
* Deep learning: pytorch, tensorflow

 Something missing?
      Ask us :)
      servicedesk@csc.fi
</div>