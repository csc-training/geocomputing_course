# Terminology

TODO: clean up and texts

- You can roughly think that one **node** is a single computer
- A node on a supercomputer contains:
  - One or more central processing units (**CPUs**) with many **cores**
  - Shared **memory**
- Some nodes may also have:
  - **Local storage**
  - Graphics processing units (**GPUs**)


- Login nodes are used to set up jobs (and to launch them)
- Jobs are run on the compute nodes
- A batch job system (scheduler) is used to run and manage the jobs
  - On CSC machines, we use Slurm

![](./images/puhti_overview.png){width=80%} 


# Available batch job partitions

- [The available batch job partitions](https://docs.csc.fi/computing/running/batch-job-partitions/) are listed in docs.csc.fi
- In order to use the resources in an efficient way, it is important to estimate the request as accurately as possible
- By avoiding an excessive "just-in-case" request, the job will start earlier

# Different type of HPC jobs

- Typically an HPC job can be classified as serial, parallel or GPU, depending on the main requested resource 
- The following slides will provide you with an overview of different job types
- A serial job is the simplest type of job whereas parallel and GPU jobs may require some advanced methods to fully utilise their capacity
- R jobs are typically serial or parallel (few R packages exist with GPU support)
   - We will cover R-specific topics later during the workshop

# HPC serial jobs

- Serial jobs only use one core (so don't reserve more)!
- Why could your serial job benefit from being executed using CSC's resources instead of on your own computer? 

    - Part of a larger workflow
    - Avoid data transfer between CSC and your own computer
    - Data sharing among other project members
    - Readily configured environment / dependencies (e.g. R environment on Puhti)
    - Memory and/or disk demands

# Running multiple serial jobs using job arrays
- [Job arrays](https://docs.csc.fi/computing/running/array-jobs/) can be used to simultaneously run multiple serial jobs
- Useful for so-called *embarrassingly parallel* analyses (many identical but separate tasks, e.g. repeating same steps for multiple data sets)

# HPC parallel jobs

- A parallel job distributes the calculation over several cores in order to achieve a shorter wall time (and/or a larger allocatable memory)   
- There are two major parallelization schemes: [OpenMP](https://en.wikipedia.org/wiki/OpenMP) and [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface)
   - Note, depending on the parallellization scheme there is a slight difference between _how_ the resource reservation is done  
- Batch job script [how-to create](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/) and [examples](https://docs.csc.fi/computing/running/example-job-scripts-puhti/) for Puhti
- **The best starting point:** [Software specific batch scripts in docs](https://docs.csc.fi/apps/)

# Parallel resource reservation: a couple of examples

- Multicore OpenMP job

<font size="6">
```bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=X
```
</font>

- Multicore MPI job

<font size="6">
```bash
#SBATCH --nodes=X
#SBATCH --ntasks-per-node=Y
#SBATCH --cpus-per-task=Z
```
</font>

- `--cpus-per-task` is typically used for OpenMP jobs
- `--ntasks` is typically used for MPI jobs
    - A task cannot be split between nodes, but tasks can be on different nodes
    - `--ntasks-per-node` can be used for finer control

# HPC GPU jobs 

- A graphics processing unit (GPU, a video card), is capable of doing certain type of simultaneous calculations very efficiently
- In order to take advantage of this power, a computer program must be reprogrammed to adapt on how GPU handles data   
- CSC's GPU resources are relatively scarce and hence should be used with [particular care](https://docs.csc.fi/computing/overview/#gpu-nodes)
    - A GPU uses 60 times more billing units than a single CPU core - see above for performance requirements
    - In practice, 1-10 CPU cores (but not more) should be allocated per GPU on Puhti

# Interactive jobs

- When you login to CSC's supercomputers, you end up in one of the login nodes of the computer
    - These login nodes are shared by all users and they are [not intended for heavy computing.](https://docs.csc.fi/computing/overview/#usage-policy)
- If you have a heavier job that still requires interactive response (_e.g._ a graphical user interface)
    - Allocate the resource via the the [interactive partition](https://docs.csc.fi/computing/running/interactive-usage/)
    - This way your work is performed in a compute node, not on the login node
- We have recently launched an easy-to-use [interactive web interface for Puhti](https://docs.csc.fi/computing/webinterface/)




