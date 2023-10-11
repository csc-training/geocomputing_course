
# Fundamentals and Terminology

:::{admonition} HPC?
:class: seealso
While for some there might be differences, the terms "computing cluster", "High Performance Computing (HPC) system" and "supercomputer" are also often used interchangeably. We use supercomputer.
:::

Supercomputers are for computationally intensive workloads with the highest possible performance, designed to handle big volumes of data. It typically includes computational, networking and storage devices. 
This also means that a supercomputer must exist in a specific, fixed location: networking cables can only stretch so far, and electrical and optical signals can travel only so fast.

Typical parts of a supercomputer:

* **CPUs** (central processing unit) are a computer’s processors for actually running programs and calculations. 
* **GPU** (graphical processing unit) does certain linear algebra operations extremely efficiently, such as those encountered when processing computer graphics. Widely used also for speeding up model training in deep learning.
* Both CPUs and GPUs contain many **cores** plus shared memory.
* Information about a current task is stored in the computer’s **memory**. 
* **Disk** refers to all storage that can be accessed like a file system. This is generally storage that can hold data permanently, i.e. data is still there even if the computer has been restarted. While this storage can be local (a hard drive installed inside of it), it is more common for nodes to connect to a shared, remote fileserver or cluster of servers. 

Text adapted from [ODU Research Computing Wiki](https://wiki.hpc.odu.edu/) and [NRIS](https://training.pages.sigma2.no).


:::{admonition} Difference between a supercomputer and the cloud
:class: seealso


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
