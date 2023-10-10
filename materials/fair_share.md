
# Fair share of use on multi-user computing platforms

The computing resources are shared among hundreds of users, who all have different resource needs. Resources allocated to a job are not available for others to use. It is important to request only the resources you need and ensure that the resources are used efficiently. A resource/job management system keeps track of the computing resources. It aims to share the resources in an efficient and fair way among all users. It optimizes resource usage by filling the compute nodes so that there will be as little idling resources as possible.

:::{admonition} Resource bottleneck
:class: seealso

- A single node can host many jobs from different users
- Different jobs need different resources
- Typically, the cores run out before the memory does
- Sometimes a job uses only one core, but will consume all memory
   - No further jobs will fit in the node
   - If the job is _not_ using the memory (just reserving it), resources are wasted

:::

## SLURM

CSC uses a batch job system called SLURM to manage resources. SLURM is used to control how the overall computing resources are shared among all jobs and users in an efficient and fair manner.
SLURM controls how a single job request is allocated resources, such as:
* computing time
* number of cores
* amount of memory
* other resources like GPUs, local disk, etc.


```{figure} images/slurm-sketch.svg
:alt: How batch jobs are distributed on compute nodes in terms of number of CPU cores, time and memory
:width: 700px
:align: center
SLURM job allocations
```


## Queueing 

- A job is queued and starts when the requested resources become available
- The order in which the queued jobs start depends on their priority and currently available resources
- At CSC, the priority is configured to use "fair share"
   - The _initial_ priority of a job _decreases_ if the user has recently run lots of jobs
   - Over time (while queueing) its priority _increases_ and eventually it will run
   - Some queues have a lower priority (e.g. _longrun_ -- use shorter if you can!)
- See our documentation for more information on [Getting started with running batch jobs on Puhti/Mahti](https://docs.csc.fi/computing/running/getting-started/) and [LUMI](https://docs.lumi-supercomputer.eu/runjobs/).

:::{admonition} How many resources to request?
:class: seealso

* You can use your workstation / laptop as a base measuring stick: If the code runs on your machine, as a first guess you can reserve the same amount of CPUs & RAM as your machine has.
* You can also check more closely what resources are used with `top` when running on your machine
* Similarly for running time: if you have run it on your machine, you should reserve similar time in the cluster.
* If your program does the same thing more than once, you can estimate that the total run time is T≈n_steps⋅t_step, where tstep is the time taken by each step.
* Likewise, if your program runs multiple parameters, the total time needed is T_total≈n_parameters⋅T_single, where T_single is time needed to run the program with some parameters.
* You can also run a smaller version of the problem and try to estimate how the program will scale when you make the problem bigger.
* You should always monitor jobs to find out what were the actual resources you requested (seff JOBID).

Adapted from [Aalto Scientific Computing](https://scicomp.aalto.fi/triton/usage/program-size/)
:::

:::{admonition} How many jobs is too many?
:class: seealso, dropdown

We mention in documentation and guidelines that users shouldn’t send too many jobs, but how many is too many?
Unfortunately it’s impossible to give any exact numbers because both Slurm and Lustre are shared resources.
* It’s possible to give better limits for global usage of the system.
* When system total load is low, it may be ok to run something that is problematic when system is full.

**How many jobs/steps is too many?**

* SHOULD BE OK to run tens of jobs/steps
* PAY ATTENTION if you run hundreds of jobs/steps
* DON’T RUN several thousands of jobs*

**How many file operations is too many?**

* SHOULD BE OK to access hundreds of files
* PAY ATTENTION if you need several thousands of files
* DON’T USE hundreds of thoudsands of files

Note that these guideline numbers are for all operations on all jobs.

**I have lots of small files**

* Check the tool that you are using
    * There may be different options for data storage
* Tar/untar and compress your datasets.
* Use local disk (NVMe on Puhti, ramdisk on Mahti).
* Remove intermediate files if possible.
* Use squashfs for read-only datasets and containers.

**I have lots of small tasks for SLURM**

* Check the tool that you are using
    * There may already be support for multiple jobs in a single job 
* Regroup your tasks and execute larger group of tasks in single job/step.
    * Manual or automatic (if feature is present in your tool)
    * Horizontal and vertical packing
    * Tradeoff (redundancy, parallelism, utilization)
* Do a larger job and use another scheduler (hyperqueue, flux).
    * Integration for nextflow and snakemake already exists
    * CSC has some tools for farming type jobs
    * Not all or nothing

:::

