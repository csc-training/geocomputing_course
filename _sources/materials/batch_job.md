# Batch jobs

On our own computer, we are used to a started program (job) starting
instantly. In a supercomputing environment, the computer is **shared among
hundreds of users**. All heavy computing must be done on compute nodes
(see [Usage policy](https://docs.csc.fi/computing/overview/#usage-policy)). To
use compute nodes, the user first asks for the computing resources and then
waits for the job to start when the requested resources become available.

## SLURM - job management system
A job management system keeps track of the available and requested computing
resources. It aims to share the resources in an efficient and fair way among
all users. It optimizes resource usage by filling the compute nodes so that
there will be as little idling resources as possible. CSC uses a job
management system called SLURM.

```{figure} images/slurm-sketch.svg
:alt: How batch jobs are distributed on compute nodes in terms of number of CPU cores, time and memory
:width: 700px
:align: center
SLURM job allocations
```

It is important to request only the resources you need and ensure that the
resources are used efficiently. Resources allocated to a job are not available
for others to use. If a job is _not_ using the cores or memory it reserved,
resources are wasted. 

## Batch job script

A **batch job script** is used to request resources for a job. It consists of two parts:

* The resource request: computing time, number of cores, amount of memory and
  other resources like GPUs, local disk, etc.
* Instructions for computing: what tool or script to run.

Minimal example of batch script:

```bash title="simple.sh"
#!/bin/bash
#SBATCH --account=project_2015299   # Your CSC project. Mandatory.
#SBATCH --partition=test            # Partition, see section below
#SBATCH --time=00:02:00             # Maximum duration of the job. 
#SBATCH --ntasks=1                  # How many cores?
#SBATCH --mem=2G                    # How much memory

srun python myscript.py             # The script to run  
``` 

* Submit the job for computation: `sbatch simple.sh`
* Cancel a job after job submission during queueing or runtime: `scancel jobid`.

When we submit a batch job script, the job is not started directly, but is
sent into a **queue**. Depending on the requested resources and load, the job
may need to wait to get started. 

:::{admonition} How many resources to request?
:class: seealso

* If you have run the code on some other machine (your laptop?), as a first
  guess, you can reserve the same amount of CPUs and memory as on that
  machine.
* You can also monitor resource usage more closely with `top` on Mac and Linux
  or `task manager` on Windows when running on the other machine.
* If your program does the same thing (or similar things) more than once, you
  can estimate the total run time by multiplying the duration of one run with
  the total number of runs.
* An initial resource reservation on a supercomputer is often a guess, do not
  worry too much, just adjust it later.
* Before reserving multiple CPUs, check if your code can make use of them.
* Before reserving multiple nodes, check if your code can make use of them.
  Most GIS tools can not.
* When you double the number of cores, the job should run at least 1.5x
  faster.
* Some tools run on both CPU and GPU. If unsure which to use, a good rule of
  thumb is to compare the billing unit (BU) usage and select the one consuming
  fewer units. A GPU uses 60 times more billing units than a single CPU core.
* You should always monitor jobs to find out what were the actual resources
  you requested.

Partly adapted from [Aalto Scientific Computing](https://scicomp.aalto.fi/triton/usage/program-size/)
:::

## Partitions

A **partition** is a logically grouped set of compute nodes. Resource
limitations for a job are defined by the partition (or queue) the job is
submitted to. The limitations affect the **maximum run time, available memory
and the number of  CPU/GPU cores**. Jobs should be submitted to the smallest
partition that matches the required resources. 

- [CSC Docs: Available batch job partitions](https://docs.csc.fi/computing/running/batch-job-partitions/)
- [LUMI Docs: Slurm particions](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/)

## Job types

* **Interactive jobs** are used for e.g. working interactively with
  tools that have a graphical UI, writing code (using graphical development
  environments) and testing whether a program runs as intended. For
  interactive jobs, allocate the resources from the
  [interactive partition](https://docs.csc.fi/computing/running/interactive-usage/).
  This way your work is performed on a compute node, not on the login node.
  The interactive partition is often used for applications in the web interface.
  The resources are limited on this partition, but it should have very
  short queuing times.
* **Serial jobs** work on only one task at a time following a sequence of
  instructions and only using one core.
* **Parallel jobs** distribute the work over several cores or nodes in order
  to achieve a shorter wall time (and/or more allocatable memory). 
* **GPU jobs** for tools that can benefit from running on GPUs. In a spatial
  analysis context, GPUs are most often used for deep learning.

:::{admonition} Which partition to choose?
:class: tip

Check [CSC Docs: Available batch job partitions](https://docs.csc.fi/computing/running/batch-job-partitions/) and find suitable partitions for these tasks:

1. Through trial and error, Anna has determined that her image processing task
   takes about 60 min and 16 GB of memory. 
2. Laura has profiled her code, and determined that it can run efficiently on
   20 cores with 12 GB of memory each. The complete process should be done
   within 4 days.
3. Ben wants to visualize a 2 GB file in QGIS.
4. Neha has written and run some Python code on her own machine. She now wants
   to move to Puhti and, before running her full pipeline, test that her code
   executes correctly with a minimal dataset.
5. Josh wants to run 4 memory heavy tasks (100GB) in parallel. Each job takes
   about 30 minutes to execute.

:::{admonition} Solution
:class: dropdown

1. She does not need interactive access to her process, so `small` suits best.
2. She needs to choose `longrun` or adapt her code to get under 3 days runtime
   (which she might want to do in order to avoid excessively long queueing
   times).
3. For the web interface, `interactive` suits best and should be the first
   choice. 
4. This is a very good idea and should always be done first. Neha can get the
   testing done quickly (= with limited queuing overhead) using the `test`
   partition. This means to keep the runtime under 15 min and the memory needs
   below 190 GiB at a maximum of 80 tasks.
5. 400GB memory in total is more than most partitions can provide. If this is the
   least memory possible for the jobs, it has to be run on `hugemem`.
:::
:::

More information:
* [CSC Dosc: Running jobs, Getting started](https://docs.csc.fi/computing/running/getting-started/) for Puhti and Mahti
* [LUMI Docs: Run jobs](https://docs.lumi-supercomputer.eu/runjobs/)
* [CSC Docs: Software specific example batch scripts](https://docs.csc.fi/apps/)
* [SLURM documentation](https://slurm.schedmd.com/sbatch.html)
