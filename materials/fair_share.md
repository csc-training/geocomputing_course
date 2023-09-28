# Fair share of use

TODO: restaurant analogy?


* A resource management system that keeps track of all jobs that use, or would like to use, the computing resources
* Aims to share the resources in an efficient and fair way among all users
* Optimizes resource usage by filling the compute nodes so that there will be as little idling resources as possible

## Slurm


* CSC uses a batch job system called Slurm to manage resources
* Slurm is used to control how the overall computing resources are shared among all jobs in an efficient and fair manner
* Slurm controls how a single job request is allocated resources, such as:
    * computing time
    * number of cores
    * amount of memory
    * other resources like GPUs, local disk, etc.
* Getting started with Slurm batch jobs on Puhti/Mahti and LUMI


## Queing 

- A job is queued and starts when the requested resources become available
- The order in which the queued jobs start depends on their priority and currently available resources
- At CSC, the priority is configured to use "fair share"
   - The _initial_ priority of a job _decreases_ if the user has recently run lots of jobs
   - Over time (while queueing) its priority _increases_ and eventually it will run
   - Some queues have a lower priority (e.g. _longrun_ -- use shorter if you can!)
- See our documentation for more information on [Getting started with running batch jobs on Puhti/Mahti](https://docs.csc.fi/computing/running/getting-started/) and [LUMI](https://docs.lumi-supercomputer.eu/runjobs/).

# Schema of how the batch job scheduler works

![](./images/slurm-sketch.svg)