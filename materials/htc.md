# Parallizable processes

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
* And what if you are cooking with the help of a friend help? Is the soup done any faster?


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
Parallel programs are typically parallelized with the MPI and/or OpenMP standards or using GPUs. In this course we are focusing on making use of multiple CPUs and dealing with so called "embarrasingly/naturally/delightfully parallel" tasks. If you are interested in more advanced topics, please check our [CSC training calender](https://www.csc.fi/en/training#training-calendar).
:::

## Using multiple cores

### In-built multi core support

First thing to check, is if the software you are using has built-in support for using multiple CPUs/cores. For command line tools, look for `-n(umber of)_cores`, `-c(ores/pu)`, `-j(obs)`, `-t(hreads)` or similar .

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

### External tools for running scripts/tools at the same time 

Apart from in- built features, there is also ways to running scripts at the same time for tools without multi-core support or adapting your own code. Any program may be run in parallel with these tools. This way of running programs is also called task farming or high throughput computing.

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



:::{admonition} Things to consider in task farming
:class: warning

- In a big allocation, each computing core should have work to do
   - If the separate tasks are different, some might finish before the others, leaving some cores idle &rarr; waste of resources
   - Consider combining small and numerous jobs into fewer and bigger ones
- Try to estimate as accurately as possible the required memory and the time it takes for the separate tasks to finish

:::

### Workflow tools

If running your jobs gets more complex, requiring _e.g._ dependencies between subtasks, workflow tools can be a another or additional option. Workflow tools also help with making your work more reproducible by recording the computational steps and data. You can find some guidelines and suggestions in [CSC Docs: High Throughput Computing page](https://docs.csc.fi/computing/running/throughput/).
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
