# Terminology


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

:::{admonition} Login node etiquette
:class: tip
Which of the following tasks would suit to run on the login node?


1. `python join_dataframes.py`
2. `make`
3. `create_directories.sh`
4. `qgis`
5. `tar -xzf mytool.tar.gz`

:::{admonition} Solution
:class: tip, dropdown


 Options #2 Building software  (make), #3 creating directories (mkdir), and #5 unpacking software (tar) are common and acceptable tasks for the login node. 
 
 >Note that script names do not always reflect their contents: before launching #3, please less create_directories.sh and make sure it does what the name suggests.

Running resource-intensive applications is frowned upon. Unless you are sure it will not affect other users, do not run jobs like #1 (python) or #4 (a software). You will anyway want more resources for these, than the login node can provide.

:::
:::

# Available batch job partitions

- [The available batch job partitions](https://docs.csc.fi/computing/running/batch-job-partitions/) are listed in docs.csc.fi
- In order to use the resources in an efficient way, it is important to estimate the request as accurately as possible
- By avoiding an excessive "just-in-case" request, the job will start earlier

# Interactive jobs

- When you login to CSC's supercomputers, you end up in one of the login nodes of the computer
    - These login nodes are shared by all users and they are [not intended for heavy computing.](https://docs.csc.fi/computing/overview/#usage-policy)
- You already got to know the [interactive web interface for Puhti](https://docs.csc.fi/computing/webinterface/)
- If you have a heavier job that still requires interactive response (_e.g._ testing, prototyping)
    - Allocate the resource via the the [interactive partition](https://docs.csc.fi/computing/running/interactive-usage/)
    - This way your work is performed in a compute node, not on the login node

# Different type of HPC jobs

- Apart from interactive jobs, an HPC job can be classified as serial, parallel or GPU, depending on the main requested resource 
- A serial job is the simplest type of job whereas parallel and GPU jobs may require some advanced methods to fully utilise their capacity

# HPC serial jobs

- Serial jobs only use one core (so don't reserve more)!
- Why could your serial job benefit from being executed using CSC's resources instead of on your own computer? 

    - Part of a larger workflow
    - Avoid data transfer between CSC and your own computer
    - Data sharing among other project members
    - Readily configured environment / dependencies (e.g. R environment on Puhti)
    - Memory and/or disk demands

# HPC parallel jobs

- A parallel job distributes the calculation over several cores in order to achieve a shorter wall time (and/or a larger allocatable memory)   
- There are two major parallelization schemes: [OpenMP](https://en.wikipedia.org/wiki/OpenMP) and [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface)
   - Note, depending on the parallellization scheme there is a slight difference between _how_ the resource reservation is done  
- Batch job script [how-to create](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/) and [examples](https://docs.csc.fi/computing/running/example-job-scripts-puhti/) for Puhti
- **The best starting point:** [Software specific batch scripts in docs](https://docs.csc.fi/apps/)


# HPC GPU jobs 

- A graphics processing unit (GPU, a video card), is capable of doing certain type of simultaneous calculations very efficiently
- In order to take advantage of this power, a computer program must be reprogrammed to adapt on how GPU handles data   
- CSC's GPU resources are relatively scarce and hence should be used with [particular care](https://docs.csc.fi/computing/overview/#gpu-nodes)
    - A GPU uses 60 times more billing units than a single CPU core - see above for performance requirements
    - In practice, 1-10 CPU cores (but not more) should be allocated per GPU on Puhti


# Running multiple serial jobs using job arrays

- [Job arrays](https://docs.csc.fi/computing/running/array-jobs/) can be used to simultaneously run multiple serial jobs
- Useful for so-called *embarrassingly parallel* analyses (many identical but separate tasks, e.g. repeating same steps for multiple data sets)


