# Parallel processes

Typically, large computers like those at CSC are not much faster than personal ones -- they are simply bigger. For fast computation, they utilize parallelism (and typically have special disk, memory and network solutions, too). Parallelism simplified: You use hundreds of ordinary computers simultaneously to solve a single problem.

:::{admonition} A small thought example
:class: tip

Let's make some pea soup following this recipe:

* (1 min) Pour water into a soup pan, add the split peas and bring it to boil.
* (60 min) Let it simmer under a lid for about 60 minutes.
* (15 min) Clean and chop the leek, celeriac, onion, carrot and potato.
* (20 min) Add the vegetables and simmer for 20 more minutes. Stir the soup occasionally.
* (1 day) Leave the soup for one day. Reheat before serving and add a sliced smoked sausage (vegetarian options are also welcome). Season with pepper and salt.

Imagine you’re cooking alone.

* How many workers does this process need?
* Can you identify potential for parallelisation in this recipe?
* And what if you are cooking with the help of a friend? Is the soup done any faster?


Adjusted from [Introduction to parallel programming in Python by the Carpentries](https://carpentries-incubator.github.io/lesson-parallel-python)

:::{admonition} Solution
:class: dropdown 

* There are two ‘workers’: the cook and the stove. 
* You can cut vegetables while simmering the split peas.
* If you have help, you can parallelize cutting vegetables further.
* The main part of the process (waiting) is not parallelizable, so we have to consider if it is worth the effort.
:::

:::

&rarr; Not everything can be parallelized. Identify serial and parallelizable parts of your code early on.

So what options do we have to run things at the same time?

:::{admonition} Parallel programming
:class: warning
Parallel programs are typically parallelized with the MPI and/or OpenMP standards or using GPUs. In this course we are focusing on making use of multiple CPUs and dealing with so called "embarrasingly/naturally/delightfully parallel" tasks. If you are interested in more advanced topics, please check our [CSC training calendar](https://www.csc.fi/en/training#training-calendar).
:::

## Using multiple cores

### In-built multi core support

First thing to check, is if the software you are using has built-in support for using multiple CPUs/cores. For command line tools, look for `-n(umber of)_cores`, `-c(ores/pu)`, `-j(obs)`, `-t(hreads)` or similar.

Some example geospatial tools with built-in multi CPU support: 
* GDAL, e.g. `gdalwarp -multi -wo NUM_THREADS=val/ALL_CPUS ...`
* Orfeo ToolBox; no extra action needed
* Whiteboxtools; many tools support parallel execution without extra action
* Lastools; many tools support parallel execution by setting `-cores`
* PDAL-wrench (not on Puhti);  many tools support parallel execution without extra action

For your own scripts, do you have **for-loops** or similar that you could replace by using multiple cores instead?
Many programming languages have packages that support this: 
* Python: `multiprocessing`, `joblib` and `dask`
* R:  `snow`, `parallel` and `future`
* Julia: built in [multi-threading](https://docs.julialang.org/en/v1/manual/multi-threading/#man-multithreading)

### Tools for running scripts/tools at the same time 

Apart from in-built features, there is also ways of running scripts at the same time for tools without multi-core support or adapting your own code. Any program may be run in parallel with these tools. This way of running programs is also called task farming or high throughput computing.

#### GNU Parallel

GNU parallel is a shell tool for executing jobs in parallel using one or more computers or cores. A job can be a single command or a small script that has to be run for each of the lines in the input. The typical input is a list of files, a list of hosts, a list of users, a list of URLs, or a list of tables. Tasks that are not run immediately due to space restrictions are queued and are automatically executed as space becomes available.

From [GNU Parallel documentation](https://www.gnu.org/software/parallel/)
See also [CSC Docs: GNU Parallel tutorial](https://docs.csc.fi/support/tutorials/many/)

#### Array jobs

Array jobs are another way of how you can run multiple independent jobs at the same time. They are a structure of SLURM, enabling users to run multiple instances of the same batch script as independent jobs.

See also [CSC Docs: Array jobs](https://docs.csc.fi/computing/running/array-jobs/)

:::{admonition} GNU parallel or array jobs?
:class: seealso

Array jobs are only a good option , if the independent jobs are "large" enough, so that the batch system overhead is not relevant (more than 30 minutes per job, for example), and the total number of independent jobs is not huge (less than 1000 per month, for example).

:::

:::{admonition} Things to consider in task farming
:class: warning

- In a big allocation, each computing core should have work to do
   - If the separate tasks are different, some might finish before the others, leaving some cores idle &rarr; waste of resources
   - Consider combining small and numerous jobs into fewer and bigger ones
- Try to estimate as accurately as possible the required memory and the time it takes for the separate tasks to finish

:::

#### HyperQueue

Instead of submitting each of your computational tasks as separate Slurm jobs or job steps, you can also allocate a large resource block and then use HyperQueue to submit your tasks to this allocation.

See also [CSC Docs: HyperQueue](https://docs.csc.fi/apps/hyperqueue/)


### Workflow tools

If running your jobs gets more complex, requiring _e.g._ dependencies between subtasks, workflow tools can be another or additional option. Workflow tools also help with making your work more reproducible by recording the computational steps and data. You can find some guidelines and suggestions in [CSC Docs: High Throughput Computing page](https://docs.csc.fi/computing/running/throughput/).
Many tools available:
- [Make](https://www.gnu.org/software/make/)
- [Snakemake](https://snakemake.github.io/)
- [FireWorks](https://docs.csc.fi/computing/running/fireworks/)
- [Nextflow](https://docs.csc.fi/support/tutorials/nextflow-puhti/)
- [Common Workflow Language](https://www.commonwl.org/)

:::{admonition} Think about your own work
:class: tip

Do you need to run a lot of steps one after another? Or few steps that need a lot of memory? Do steps depend on each other? Which steps could be run in parallel? Which steps cannot be run in parallel?

:::

:::{admonition} How many jobs is too many?
:class: seealso, dropdown

We mention in documentation and guidelines that users shouldn’t send too many jobs, but how many is too many?

Unfortunately it’s impossible to give any exact numbers because both Slurm and Lustre are shared resources.
* It’s possible to give better limits for global usage of the system.
* When system total load is low, it may be ok to run something that is problematic when system is full.

**How many jobs is too many?**

* SHOULD BE OK to run tens of jobs
* PAY ATTENTION if you run hundreds of jobs
* DON’T RUN several thousands of jobs

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

**I have lots of small tasks for Slurm**

* Regroup your tasks and execute larger group of tasks in single job.
    * Manual or automatic (if feature is present in your tool)
    * Horizontal and vertical packing
    * Tradeoff (redundancy, parallelism, utilization)
* Do a larger job and use another scheduler (HyperQueue, flux).
    * Integration for Nextflow and Snakemake already exists
    * CSC has some tools for farming type jobs
    * Not all or nothing

:::

For more advanced usage, there are two major parallelization schemes: [OpenMP](https://en.wikipedia.org/wiki/OpenMP) and [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface). 

:::{admonition} Advanced topics - MPI/OpenMP
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
#SBATCH --cpus-per-task=1
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

