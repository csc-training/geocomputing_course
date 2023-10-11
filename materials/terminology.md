
# Fundamentals and Terminology

:::{admonition} HPC?
:class: seealso
While for some there might be differences, the terms "computing cluster", "High Performance Computer (HPC)" and "supercomputer" are also often used interchangeably.
:::

The term **HPC system** is a stand-alone resource for computationally intensive workloads. 
They are typically comprised of a multitude of integrated processing and
storage elements, designed to handle high volumes of data and/or large numbers of floating-point
operations ([FLOPS](https://en.wikipedia.org/wiki/FLOPS)) with the highest possible performance. 

To support these constraints, an HPC resource must exist in a specific, fixed location: networking
cables can only stretch so far, and electrical and optical signals can travel only so fast.

**CPUs** (central processing unit) are a computer’s processors for actually running programs and calculations. 

A Graphical Processing Units (**GPU**) does certain linear algebra operations extremely efficiently, such as those encountered when processing computer graphics.

Both CPUs and GPUs contain many **cores** plus shared memory.

Information about a current task is stored in the computer’s **memory**. 

**Disk** refers to all storage that can be accessed like a file system. This is generally storage that can hold data permanently, i.e. data is still there even if the computer has been restarted. While this storage can be local (a hard drive installed inside of it), it is more common for nodes to connect to a shared, remote fileserver or cluster of servers. 

A **cluster** is all resources wired together for the purpose of high performance computing, which includes computational devices, networking devices (switches) and storage devices combined.

When you want to execute a program on the supercomputer, it has to be boxed into an abstraction layer called **job**.

Adapted from [ODU Research Computing Wiki](https://wiki.hpc.odu.edu/) and [NRIS](https://training.pages.sigma2.no).


:::{admonition} Difference between an HPC system and the cloud
:class: seealso, dropdown


  * All computers involved are located in the same location (e.g. in the same room)
  * All computers are connected to each other with very fast local area network (LAN)
  * All computers involved are architecturally identical and run the same operating system
  * A set of optimised software installed and accessible from all computers
  * All computers have access to shared storage, if you place a file on one machine you 
    can access it from all the other machines
  * All computers have a synchronised clock.
  * A scheduler is involved (latter lesson)

A cloud service could have access to an HPC system as part of the service as well.

From [NRIS](https://training.pages.sigma2.no).
:::
