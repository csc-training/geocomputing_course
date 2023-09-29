# High Throughput Computing (HTC) and parallelization

TODO: fix texts and reorder

## Parallizable processes


:::{admonition} A small thought example
:class: tip

What of the following is a task, that can be parallelized in real life:

1. Manually copying a book and producing a clone
2. Clearing the table after dinner
3. Rinsing the dishes with one sink
4. A family getting dressed to leave the apartment for a birthday party*

Think about what the inputs are to the task at hand. Can individual items of the inputs be processed independent of each other?

From [HPC-Carpentry](http://www.hpc-carpentry.org/hpc-parallel-novice/02-parallel-estimate/index.html)

:::{admonition} Solution
:class: tip, dropdown 

1. not parallel typically - as we have to start with one book and only have one reader/writer
2. parallel, the more people help, the better
3. not parallel, every piece of cutlery and dishes needs to go through one sink
4. parallel, each family member can get dressed independent of each other
:::

:::

&rarr; Not everything can be parallelized. Identify serial and parallelizable parts of your code early on.

# The purpose of large computers

- Typically, large computers like those at CSC are not much faster than personal ones -- they are simply bigger
   - For fast computation, they utilize parallelism (and typically have special disk, memory and network solutions, too)
- Parallelism simplified:
   - You use hundreds of ordinary computers simultaneously to solve a single problem

## Parallelizing your workflow

- There are multiple ways to parallelize your workflow
   - Maybe several smaller jobs are better than one large (task farming)?
   - Is there a more efficient code or algorithm?
   - Is the file I/O slowing you down (lots of read/write operations)?
- Optimize usage considering single job wall-time, overall used CPU time, I/O
- [Docs CSC: Guidelines for high-throughput computing](https://docs.csc.fi/computing/running/throughput/)

# Running your software

- It is not only how your software is constructed and compiled that affects performance
- It may also be run in different ways

# HPC parallel jobs

- A parallel job distributes the calculation over several cores in order to achieve a shorter wall-time (and/or a larger allocatable memory)
- Examples of batch job scripts for [Puhti](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/) and [Mahti](https://docs.csc.fi/computing/running/example-job-scripts-mahti/)
- Examples of batch job scripts for [LUMI-C](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumic-job/) and [LUMI-G](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/)
- **The best starting point:** [Software-specific batch scripts in Docs CSC](https://docs.csc.fi/apps/)

# Running in parallel

- Parallel programs are typically parallelized with the MPI and/or OpenMP standards
- Further parallelization possible if you can split your whole workflow into smaller independent tasks and run them simultaneously
   - [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) or [Slurm array jobs](https://docs.csc.fi/computing/running/array-jobs/)
   - More details about high-throughput computing and workflow automation in [Docs CSC](https://docs.csc.fi/computing/running/throughput/)


:::{admonition} More advanced topics - MPI/OpenMP
:class: dropdown, tip

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

**Self study materials for OpenMP and MPI**

- There are many tutorials available online
   - Look with simple searches for _e.g._ "MPI tutorial"
- Check the documented exercise material and model answers from the CSC course "Introduction to Parallel Programming"
   - Available on [GitHub](https://github.com/csc-training/parallel-prog/)
   - See also the [materials of CSC Summer School in HPC](https://github.com/csc-training/summerschool)

:::

:::{admonition} More advanced topics - GPU
:class: dropdown, tip

# GPUs can speed up jobs

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

:::{admonition} A small thought example
:class: tip

Think about your work, do you need to run a lot of steps one after another?



:::

# Task farming -- running multiple independent jobs simultaneously

- Task farming == running many similar independent jobs simultaneously
- If subtasks are few (<100), an easy solution is [array jobs](https://docs.csc.fi/computing/running/array-jobs/)
   - Individual tasks should run >30 minutes. Otherwise, you're generating too much overhead &rarr; consider another solution
   - Array jobs create _job steps_ and for 1000s of tasks Slurm database will get overloaded &rarr; consider another solution
- If running your jobs gets more complex, requiring _e.g._ dependencies between subtasks, workflow tools can be used
   - Guidelines and solutions are suggested in [Docs CSC](https://docs.csc.fi/computing/running/throughput/)
   - Many options: [FireWorks](https://docs.csc.fi/computing/running/fireworks/), [Nextflow](https://docs.csc.fi/support/tutorials/nextflow-puhti/), [Snakemake](https://snakemake.github.io/), [Knime](https://www.knime.com/), [BioBB](http://mmb.irbbarcelona.org/biobb/), ...

- Before opting for a workflow manager, check if the code you run has built-in high-throughput features
  - Many chemistry software ([CP2K](https://docs.csc.fi/apps/cp2k/#high-throughput-computing-with-cp2k), [GROMACS](https://docs.csc.fi/apps/gromacs/#high-throughput-computing-with-gromacs), [Amber](https://docs.csc.fi/apps/amber/#high-throughput-computing-with-amber), _etc._) provide methods for efficient task farming
  - Also [Python](https://docs.csc.fi/apps/python/#python-parallel-jobs) and [R](https://docs.csc.fi/support/tutorials/parallel-r/), if you write your own code
- Task farming can be combined with _e.g._ OpenMP to accelerate sub-jobs
  - [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) is the best option for sub-node task scheduling (non-MPI)
- Finally, MPI can be used to run several jobs in parallel
   - Three levels of parallelism, requires skill and time to set up
   - Always test before scaling up -- a small mistake can result in lots of wasted resources!

# Things to consider in task farming

- In a big allocation, each computing core should have work to do
   - If the separate tasks are different, some might finish before the others, leaving some cores idle &rarr; waste of resources
   - Try combining small and numerous jobs into fewer and bigger ones
- As always, try to estimate as accurately as possible the required memory and the time it takes for the separate tasks to finish
   - Consult _e.g._ this [bio job tutorial with examples](https://docs.csc.fi/support/tutorials/biojobs-on-puhti/)



# Tricks of the trade

- Although it is reasonable to try to achieve best performance by using the fastest computers available, it is not the only important issue
- Different codes may give very different performance for a given use case
    - Compare the options you have in [CSC's software selection](https://docs.csc.fi/apps/)
- Before launching massive simulations, look for the most efficient algorithms to get the job done
- Well-known boosters are:
    - Enhanced sampling methods _vs._ brute force molecular dynamics
    - Machine learning methods
      - _E.g._ Bayesian optimization structure search ([BOSS](https://cest-group.gitlab.io/boss/), potential energy maps)
    - Start with coarser models and gradually increase precision (if needed)
      - _E.g._ pre-optimize molecular geometries using a small basis set
    - When starting a new project, begin with small/fast tests before scaling up
      - Don't submit large jobs before knowing that the setup works as intended
    - When using separate runs to scan a parameter space, start with a coarse scan, and improve resolution where needed
      - Be mindful of the number of jobs/job steps, use meta-schedulers if needed
    - Try to use or implement checkpoints/restarts in your software, and _check results between restarts_
- Try to formulate your scientific results when you have a minimum amount of computational results
    - Helps to clarify what you still need to compute, what computations would be redundant and what data you need to store
- Reserving more memory and/or more compute cores does not necessary equal faster computations
    - Check with `seff`, `sacct` and from software-specific log files if the memory was used and whether the job ran faster
    - Testing for optimal amount of cores and memory is advised before performing massive computations
- If possible, running the same job on a laptop may be useful for comparison
- Avoid unnecessary reads and writes of data and containerize Conda environments to improve I/O performance
    - Read and write in big chunks and avoid reading/writing lots of small files
       - If unavoidable, use [fast local NVMe disk](https://docs.csc.fi/computing/disk/#compute-nodes-with-local-ssd-nvme-disks), not Lustre (i.e. `/scratch`)
- Don't run too short jobs to minimize queuing and scheduling overhead
    - There's a time overhead in setting up a batch job, aim for >30 minute jobs
    - Don't run too many/short _job steps_ -- they will bloat Slurm accounting
- Don't run too long jobs without a restart option
    - Increased risk of something going wrong, resulting in lost time/results








## Running things at same time

* within batch script 
<p>&rarr; array job, GNU parallel </p>
* within python script
<p>&rarr; multiprocessing, joblib, dask </p>
* within R script
<p>&rarr; future, foreach, snow </p>