# Job types

## Interactive jobs


You already got to know the [interactive web interface for Puhti](https://docs.csc.fi/computing/webinterface/)
- If you have a heavier job that still requires interactive response (_e.g._ testing, prototyping)
    - Allocate the resource via the the [interactive partition](https://docs.csc.fi/computing/running/interactive-usage/)
    - This way your work is performed in a compute node, not on the login node

:::{admonition} Exploring the compute node(s)
:class: tip

This time, let's start a compute shell from the Puhti webinterface. What is different from starting a login node shell?
What is your hostname? 
-> You are now in an interactive job.

:::

Apart from interactive jobs, an HPC job can be classified as **serial, parallel or GPU**, depending on the main requested resource. A serial job is the simplest type of job whereas parallel and GPU jobs may require some advanced methods to fully utilise their capacity

## Serial jobs

Serial jobs only use one core -> so don't reserve more.

Why could your serial job benefit from being executed using CSC's resources instead of on your own computer? 
- Part of a larger workflow
- Avoid data transfer between CSC and your own computer
- Data sharing among other project members
- Readily configured environment / dependencies (e.g. R environment on Puhti)
- Memory and/or disk demands

## Parallel jobs

A parallel job distributes the calculation over several cores in order to achieve a shorter wall time (and/or a larger allocatable memory). There are two major parallelization schemes: [OpenMP](https://en.wikipedia.org/wiki/OpenMP) and [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface). Depending on the parallellization scheme there is a slight difference between _how_ the resource reservation is done.

:::{admonition} More advanced topics - MPI/OpenMP
:class: dropdown, seealso

**What is MPI?**

- MPI (Message Passing Interface) is a widely used standard for writing software that runs in parallel
- MPI utilizes parallel **processes** that _do not share memory_
   - To exchange information, processes pass data messages back and forth between the cores
   - Communication can be a performance bottleneck
- MPI is required when running on multiple nodes

**What is OpenMP?**

- OpenMP (Open Multi-Processing) is a standard that utilizes compute cores that share memory, i.e. **threads**
   - They do not need to send messages between each other
- OpenMP is easier for beginners, but problems quickly arise with so-called _race conditions_
   - This appears when different compute cores process and update the same data without proper synchronization
- OpenMP is restricted to a single node

**Batch job examples**

- Multicore OpenMP job


```bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=X
```

- Multicore MPI job

```bash
#SBATCH --nodes=X
#SBATCH --ntasks-per-node=Y
#SBATCH --cpus-per-task=Z
```

- `--cpus-per-task` is typically used for OpenMP jobs
- `--ntasks` is typically used for MPI jobs
    - A task cannot be split between nodes, but tasks can be on different nodes
    - `--ntasks-per-node` can be used for finer control

**Self study materials for OpenMP and MPI**

- There are many tutorials available online
   - Look with simple searches for _e.g._ "MPI tutorial"
- Check the documented exercise material and model answers from the CSC course "Introduction to Parallel Programming"
   - Available on [GitHub](https://github.com/csc-training/parallel-prog/)
   - See also the [materials of CSC Summer School in HPC](https://github.com/csc-training/summerschool)

:::

## GPU jobs 

A graphics processing unit (GPU, a video card), is capable of doing certain type of simultaneous calculations very efficiently. In order to take advantage of this power, a computer program must be reprogrammed to adapt on how GPU handles data. CSC's GPU resources are relatively scarce and hence should be used with [particular care](https://docs.csc.fi/computing/overview/#gpu-nodes). A GPU uses 60 times more billing units than a single CPU core. In practice, 1-10 CPU cores (but not more) should be allocated per GPU on Puhti.

:::{admonition} More advanced topics - GPU
:class: dropdown, seealso

**GPUs can speed up jobs**

- GPUs, or Graphics Processing Units, are extremely powerful processors developed for graphics and gaming
- They can be used for science, but are often challenging to program
   - Not all algorithms can use the full power of GPUs
- Check the manual if the software can utilize GPUs, don't use GPUs if you're unsure
   - Consult [how to check if your batch job used GPU](https://docs.csc.fi/support/tutorials/gpu-ml/#gpu-utilization)
   - The [CSC usage policy](https://docs.csc.fi/computing/usage-policy/#gpu-nodes) limits GPU usage to where it is most efficient
   - Also, if you process lots of data, make sure you [use the disk efficiently](https://docs.csc.fi/support/tutorials/ml-data/#using-the-shared-file-system-efficiently)
- Does your code run on AMD GPUs? [LUMI](https://docs.lumi-supercomputer.eu/hardware/compute/lumig/) has a massive GPU capacity!

- Can your software utilize GPUs?
   - [GPUs in Puhti batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#gpus)
   - [GPUs in Mahti batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-mahti/#gpu-batch-jobs)
   - [GPUs in LUMI batch jobs](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/)

:::

## Array jobs

[Array jobs](https://docs.csc.fi/computing/running/array-jobs/) can be used to simultaneously run multiple serial jobs. These are useful for so-called *embarrassingly parallel* analyses (many identical but separate tasks, e.g. repeating same steps for multiple data sets). 


:::{admonition} Check your understanding
:class: tip

TODO: come up with some usecases, also some that are not parallelizable

:::

