
# Parallizable processes

Typically, large computers like those at CSC are not much faster than personal ones -- they are simply bigger. For fast computation, they utilize parallelism (and typically have special disk, memory and network solutions, too). Parallelism simplified: You use hundreds of ordinary computers simultaneously to solve a single problem

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

## Parallelizing your workflow

Parallel programs are typically parallelized with the MPI and/or OpenMP standards (we do not talk about this here).

- Maybe several smaller jobs are better than one large (task farming)?
- Is there a more efficient code or algorithm?
- Is the file I/O slowing you down (lots of read/write operations)?

-> Optimize usage considering single job wall-time, overall used CPU time, I/O
-> [Docs CSC: Guidelines for high-throughput computing](https://docs.csc.fi/computing/running/throughput/)


:::{admonition} Think about your own work
:class: tip

Think about your work, do you need to run a lot of steps one after another? Or few steps that need a lot of memory? Do steps depend on each other? Which steps could be run in parallel? Which steps cannot be run in parallel?

:::

## Task farming 

Task farming means running many similar independent jobs simultaneously.

Check if the code you run has built-in high-throughput features
- Check for `n_cores`, `cpus` or similar
- Also [Python](https://docs.csc.fi/apps/python/#python-parallel-jobs) and [R](https://docs.csc.fi/support/tutorials/parallel-r/), if you write your own code


- If subtasks are few (<100), an easy solution is [array jobs](https://docs.csc.fi/computing/running/array-jobs/)
   - Individual tasks should run >30 minutes. Otherwise, you're generating too much overhead &rarr; consider another solution
   - Array jobs create _job steps_ and for 1000s of tasks Slurm database will get overloaded &rarr; consider another solution
- If running your jobs gets more complex, requiring _e.g._ dependencies between subtasks, workflow tools can be used
   - Guidelines and solutions are suggested in [Docs CSC](https://docs.csc.fi/computing/running/throughput/)
   - Many options: [FireWorks](https://docs.csc.fi/computing/running/fireworks/), [Nextflow](https://docs.csc.fi/support/tutorials/nextflow-puhti/), [Snakemake](https://snakemake.github.io/), [Knime](https://www.knime.com/), [BioBB](http://mmb.irbbarcelona.org/biobb/), ...

- Always test before scaling up -- a small mistake can result in lots of wasted resources!

:::{admonition} Things to consider in task farming
:class: tip

- In a big allocation, each computing core should have work to do
   - If the separate tasks are different, some might finish before the others, leaving some cores idle &rarr; waste of resources
   - Try combining small and numerous jobs into fewer and bigger ones
- Try to estimate as accurately as possible the required memory and the time it takes for the separate tasks to finish

:::

:::{admonition} Tricks of the trade
:class: tip, dropdown

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
:::

## Running things at same time

* within batch script &rarr; array job, GNU parallel 
* within python script &rarr; multiprocessing, joblib, dask 
* within R script &rarr; future, foreach, snow 

TODO image outside/inside