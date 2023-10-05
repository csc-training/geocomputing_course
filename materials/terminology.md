
# Fundamentals and Terminology

:::{admonition} HPC?
:class: seealso
While for some there might be differences, the terms **computing cluster", "High Performance Computer (HPC)" and "supercomputer" are also often used interchangeably.
:::

**Cluster**
A cluster is all resources wired together for the purpose of high performance computing, which includes computational devices (servers), networking devices (switches) and storage devices combined.

**Node**
You can roughly think that one **node** is a single computer.

**Core**
A node contains one or more central processing units (**CPUs**) with many **cores** plus shared memory.

**Job**
When you want the scheduler to execute a program, performing a computation on your behalf, it has to be boxed into an abstraction layer called "job".

**Partition**
A partition is a set of compute nodes, grouped logically. We separate our computational resources base on the features of their hardware and the nature of the job.
For instance, there is an interactive computation partition called `interactive` and a CUDA enabled GPU based partition `gpu``.

**Task**
It maybe confusing, but tasks in Slurm means processor resource. By default, 1 task uses 1 core. However, this behavior can be altered.

Adapted from [ODU Research Computing Wiki](https://wiki.hpc.odu.edu/)


All of the nodes in an HPC (High Performance Computing) system have the same components as your own laptop or desktop: CPUs (sometimes also called processors or cores), memory (or RAM), and disk space. CPUs are a computer’s tool for actually running programs and calculations. Information about a current task is stored in the computer’s memory. Disk refers to all storage that can be accessed like a file system. This is generally storage that can hold data permanently, i.e. data is still there even if the computer has been restarted. While this storage can be local (a hard drive installed inside of it), it is more common for nodes to connect to a shared, remote fileserver or cluster of servers.


:::{admonition} What is an HPC system?
:class: seealso

The term *HPC system* is a stand-alone resource for computationally intensive workloads. 
They are typically comprised of a multitude of integrated processing and
storage elements, designed to handle high volumes of data and/or large numbers of floating-point
operations ([FLOPS](https://en.wikipedia.org/wiki/FLOPS)) with the highest possible performance.
For example, all the machines on the [Top-500](https://www.top500.org) list are HPC systems. To
support these constraints, an HPC resource must exist in a specific, fixed location: networking
cables can only stretch so far, and electrical and optical signals can travel only so fast.

The word `cluster` is often used for small to moderate scale HPC resources. Clusters are often maintained in computing centers that support several such systems, all sharing common networking and storage to support common compute intensive
tasks.

From [NRIS](https://training.pages.sigma2.no).

:::

:::{admonition} Difference between a HPC computing cluster and the cloud
:class: seealso, dropdown


  * All computers involved are located in same location (e.g. in the same room)
  * All computers are connected to each other with very fast local area network(LAN)
  * All computers involved are architecturally identical and runs the same operating system
  * A set of optimised software installed and accessible from all computers
  * All computers have access to shared storage, if you place a file on one machine you 
    can access it from all the other machines
  * All computers have a synchronised clock.
  * A scheduler is involved (latter lesson)

*A cloud service could have access to a HPC cluster as part of the service as well*

From [NRIS](https://training.pages.sigma2.no).
:::
