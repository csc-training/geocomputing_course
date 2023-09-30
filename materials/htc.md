# Parallizable processes

Typically, large computers like those at CSC are not much faster than personal ones -- they are simply bigger. For fast computation, they utilize parallelism (and typically have special disk, memory and network solutions, too). Parallelism simplified: You use hundreds of ordinary computers simultaneously to solve a single problem

:::{admonition} A small thought example
:class: tip

What of the following is a task, that can be parallelized in real life:

1. Manually copying a book and producing a clone
2. Clearing the table after dinner
3. Rinsing the dishes with one sink
4. A family getting dressed to leave the apartment for a birthday party.

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

So what options do we have to run things at the same time?

:::{admonition} Parallel programming
:class: warning
Parallel programs are typically parallelized with the MPI and/or OpenMP standards or using GPUs. In this course we are focusing on making use of multiple CPUs and dealing with so called "embarrasingly parallel" tasks. If you are interested in more advanced topics, please check our [CSC training calender](https://www.csc.fi/en/training#training-calendar).
:::

## Using multiple CPUs

### In-built

First thing to check, is if the software you are using has built-in support for using multiple CPUs/cores. For command line tools, look for `-n(umber of)_cores`, `-c(ores/pu)`, `-j(obs)`, `-t(hreads)` or similar.

Some example geospatial tools with built-in multi CPU support: 
* GDAL, e.g. `gdalwarp -multi -wo NUM_THREADS=val/ALL_CPUS ...`
* Orfeo ToolBox; no extra action needed
* Whiteboxtools; many tools support parallel execution without extra action
* Lastools; many tools support parallel execution by setting `-cores`
* PDAL-wrench;  many tools support parallel execution without extra action


For your own scripts, do you have **for-loops** or similar that you could replace by using multiple cores instead?
Many programming languages have packages that support this: 
* Python: `multiprocessing`, `joblib` and `dask`
* R:  `snow`, `parallel` and `future`
* Julia: built in [multi-threading](https://docs.julialang.org/en/v1/manual/multi-threading/#man-multithreading)

### From the outside

Task farming means running many similar independent jobs simultaneously.

If subtasks are few (<100), an easy solution is [array jobs](https://docs.csc.fi/computing/running/array-jobs/)
   - Individual tasks should run >30 minutes. Otherwise, you're generating too much overhead &rarr; consider another solution
   - Array jobs create _job steps_ and for 1000s of tasks Slurm database will get overloaded &rarr; consider another solution

You can also run multiple tasks on a single node without using an array job. Tasks that are not run immediately due to space restrictions are queued and are automatically executed as space becomes available. One tool to achieve this is [GNU Parallel](https://docs.csc.fi/support/tutorials/many/).

:::{admonition} Things to consider in task farming
:class: warning

- In a big allocation, each computing core should have work to do
   - If the separate tasks are different, some might finish before the others, leaving some cores idle &rarr; waste of resources
   - Consider combining small and numerous jobs into fewer and bigger ones
- Try to estimate as accurately as possible the required memory and the time it takes for the separate tasks to finish

:::

### Workflow tools

If running your jobs gets more complex, requiring _e.g._ dependencies between subtasks, workflow tools can be used
- Guidelines and solutions are suggested in [Docs CSC](https://docs.csc.fi/computing/running/throughput/)
- Many options:  [Snakemake](https://snakemake.github.io/), [FireWorks](https://docs.csc.fi/computing/running/fireworks/), [Nextflow](https://docs.csc.fi/support/tutorials/nextflow-puhti/), [Knime](https://www.knime.com/), [BioBB](http://mmb.irbbarcelona.org/biobb/), ...



:::{admonition} Think about your own work
:class: tip

Do you need to run a lot of steps one after another? Or few steps that need a lot of memory? Do steps depend on each other? Which steps could be run in parallel? Which steps cannot be run in parallel?

:::


:::{admonition} Computations as part of the scientific workflow
:class: seealso

Try to formulate your scientific results when you have a minimum amount of computational results. This helps to clarify what you still need to compute, what computations would be redundant and what data you need to store.

:::

:::{admonition} Avoid unneccesary reading and writing
:class: seealso
Avoid unnecessary reads and writes of data and containerize Conda environments to improve I/O performance
- Read and write in big chunks and avoid reading/writing lots of small files
   - If unavoidable, use [fast local NVMe disk](https://docs.csc.fi/computing/disk/#compute-nodes-with-local-ssd-nvme-disks), not Lustre (i.e. `/scratch`)
:::

## Before starting large-scale calculations

- Check how the software performs on actual input data
    - Common job errors are caused by typos in batch/input scripts
- Use short runs in the queue `--partition=test` to check that the input works and that the resource requests are interpreted correctly
- Check the output of the `seff` command to ensure that CPU and memory efficiencies are as high as possible
    - It's OK if a job is (occasionally) killed due to insufficient resource requests: just adjust and rerun/restart
    - It's _much worse_ to always run with excessively large requests "just in case"
