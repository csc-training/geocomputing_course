# Fair share of use

TODO: fix texts and reorder
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


## Queueing 

- A job is queued and starts when the requested resources become available
- The order in which the queued jobs start depends on their priority and currently available resources
- At CSC, the priority is configured to use "fair share"
   - The _initial_ priority of a job _decreases_ if the user has recently run lots of jobs
   - Over time (while queueing) its priority _increases_ and eventually it will run
   - Some queues have a lower priority (e.g. _longrun_ -- use shorter if you can!)
- See our documentation for more information on [Getting started with running batch jobs on Puhti/Mahti](https://docs.csc.fi/computing/running/getting-started/) and [LUMI](https://docs.lumi-supercomputer.eu/runjobs/).

### Optimal usage on multi-user computing platforms

- The computing resources are shared among hundreds of your colleagues, who all have different resource needs
- Resources allocated to your job are not available for others to use
   - Important to request only the resources you need and ensure that the resources are used efficiently
- Even if you _can_ use more resources, should you?

### One resource type will be a bottleneck

<div class="column">
- A single node can host many jobs from different users
- Different jobs need different resources
- Typically, the cores run out before the memory does
- Sometimes a job uses only one core, but will consume all memory
   - No further jobs will fit in the node
   - If the job is _not_ using the memory (just reserving it), resources are wasted
</div>
<div class="column">
![](img/node-cpu-full.svg "Node cpu full"){width=45%}
![](img/node-mem-full.svg "Node memory full from one job"){width=45%}
</div>

# Schema of how the batch job scheduler works

![](./images/slurm-sketch.svg)