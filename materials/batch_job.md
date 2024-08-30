# Batch jobs

On our own computer, we are used to start a program (job) and the program starts instantly. In an supercomputing environment, the computer is **shared among hundreds of other users**.  All heavy computing must be done on compute nodes, see [Usage policy](https://docs.csc.fi/computing/overview/#usage-policy). For using compute nodes, the user first asks for the computing resources, then waits to have access to the requested resources and first then the job starts. 

## SLURM - job management system
A job management system keeps track of the available and requested computing resources. It aims to share the resources in an efficient and fair way among all users. It optimizes resource usage by filling the compute nodes so that there will be as little idling resources as possible. CSC uses a job management system called SLURM.

```{figure} images/slurm-sketch.svg
:alt: How batch jobs are distributed on compute nodes in terms of number of CPU cores, time and memory
:width: 700px
:align: center
SLURM job allocations
```


It is important to request only the resources you need and ensure that the resources are used efficiently. Resources allocated to a job are not available for others to use. If a job is _not_ using the cores or memory it reserved, resources are wasted. 

## Batch job script

A **batch job script** is used to request resources for a job. It consists of two parts:

* The resource request: computing time, number of cores, amount of memory and other resources like GPUs, local disk, etc.
* Instructions for computing: what tool or script to run.

Example minimal batch script:

```bash title="simple.sh"
#!/bin/bash
#SBATCH --account=project_200xxxx   # Your CSC project. Mandatory.
#SBATCH --partition=test            # Partition, see section below
#SBATCH --time=00:02:00             # Maximum duration of the job. 
#SBATCH --ntasks=1                  # How many cores?
#SBATCH --mem=2G                    # How much memory

srun python myscript.py             # The script to run  
``` 

To submit the job for computation: `sbatch simple.sh`

When we submit a batch job script, the job is not started directly, but is sent into a **queue**. Depending on the requested resources and load, the job may need to wait to get started. 

:::{admonition} How many resources to request?
:class: seealso

* You can use your workstation / laptop as a base measuring stick: If the code runs on your machine, as a first guess you can reserve the same amount of CPUs & memory as your machine has.
* Before reserving multiple CPUs, check if your code can make use them.
* You can also check more closely what resources are used with `top` on Mac and Linux or `task manager` on Windows when running on your machine
* Similarly for running time: if you have run it on your machine, you should reserve similar time in the cluster.
* If your program does the same thing more than once, you can estimate that the `total run time is number of steps times time taken by each step`.
* Likewise, if your program runs multiple parameters, the `total time needed is number of parameters times the time needed to run the program with one/some parameters`.
* You can also run a smaller version of the problem and try to estimate how the program will scale when you make the problem bigger.
* You should always monitor jobs to find out what were the actual resources you requested.

Adapted from [Aalto Scientific Computing](https://scicomp.aalto.fi/triton/usage/program-size/)
:::

## Partitions

A **partition** is a set of compute nodes, grouped logically. Resource limitations for a job are defined by the partition (or queue) the job is submitted to. The limitations affect the **maximum run time, available memory and the number of  CPU/GPU cores**. Jobs should be submitted to the smallest partition that matches the required resources. 

- [CSC Docs: Available batch job partitions](https://docs.csc.fi/computing/running/batch-job-partitions/)
- [LUMI Docs: Slurm particions](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/)


:::{admonition} Which partition to choose?
:class: tip

Check [CSC Docs: Available batch job partitions](https://docs.csc.fi/computing/running/batch-job-partitions/) and find suitable partitions for these tasks:

1. Through trial and error Anna has determined that her image processing process takes about 60 min, 16 GB of memory on a single CPU. 
2. Laura has profiled her code, and determined that it can run efficiently on 20 cores with 12 GB of memory each. The complete process should be done within 4 days.
3. Ben wants to visualize a 2 GB file in QGIS.
4. Neha has written and run some Python code on her own machine. She now wants to move to Puhti and, before running her full pipeline, test that her code executes correctly with a minimal dataset.
5. Josh wants to run 4 memory heavy tasks (100GB) in parallel. Each job takes about 30 minutes to execute.

:::{admonition} Solution
:class: dropdown

1. She does not need interactive access to her process, so `small` suits best.
2. She needs to choose `longrun` or adapt her code to get under 3 days runtime (which she might want to do in order to avoid exessively long queueing times).
3. For the webinterface,`interactive` suits best and should be the first choice. 
4. This is a very good idea and should always be done first. Neha can get the best and fast experience using `test` partition. This means to keep the runtime under 15 min and the memory needs below 190 GiB at a maximum of 80 tasks.
5. 400GB memory in total is more than most partitions can take. If this is the least memory possible for the jobs, it has to be run on `hugemem`.
:::
:::


:::

More information:
* [CSC Dosc: Running jobs, Getting started](https://docs.csc.fi/computing/running/getting-started/) for Puhti and Mahti
* [LUMI Docs: Run jobs](https://docs.lumi-supercomputer.eu/runjobs/)
* [CSC Docs: Software specific example batch scripts](https://docs.csc.fi/apps/)
* [SLURM documentation](https://slurm.schedmd.com/sbatch.html)
