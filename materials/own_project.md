# Own project hints

TODO: fix texts and reorder

# First steps for fast jobs 

- Spend a little time to investigate:
   - Which of the available software would be the best to solve the kind of problem you have?
      - Ask experienced colleagues or <servicedesk@csc.fi> for guidance
- Consider:
   - The software that solves your problem fastest might not always be the best
      - Issues like ease-of-use and compute power/memory/disk demands are also highly relevant
   - Quite often it is useful to start simple and gradually use more complex approaches if needed
- When you've found the software you want to use, check if it is available at CSC as a [pre-installed optimized version](https://docs.csc.fi/apps/)
   - Familiarize yourself with the software manual, if available
- If you need to install a software package distributed through Conda, [you need to containerize it](https://docs.csc.fi/computing/usage-policy/#conda-installations)
   - Containerizing greatly speeds up performance at startup and can be done easily with the [Tykky wrapper](https://docs.csc.fi/computing/containers/tykky/)
- If you can't find suitable software, consider writing your own code



* keep scripts under version control (also simplifies collaboration and synchronising different computers, e.g. git(hub))
* on Puhti: 
    * scripts in `/projappl/project_200xxxx/your_groupname/`
    * data in `/scratch/project_200xxxx/your_groupname/` -> raw data, intermediate and final results
    * personal configuration scripts in `/users/your_username/`
    * Puhti webinterface / `scp` for data transfer: own computer - Puhti
    * `wget` for data transfer:  internet - Puhti

On project organization: [CodeRefinery lesson - Reproducible research](https://coderefinery.github.io/reproducible-research/organizing-projects/)<br>
[CodeRefinery lesson - Modular code development](https://coderefinery.github.io/modular-type-along/instructor-guide/)

## Making use of HPC resources

* Just moving a script to HPC does not make it run faster
* 

## Moving from GUI to CLI/scripts

Some GUI tools provide the commands that correspond to GUI tool either in documentation or as part of the tool.
> Show QGIS -> GDAL commands

Google the toolname from eg QGIS and the desired scripting language to get some ideas.


## Moving from own computer to HPC

Think about Git* for sharing your scripts instead of moving them around.

### Your own scripts

* no hard coded filepaths such as `/my/home/dir/file.txt`
  * read from stdin or config file instead
* modular code
  * easier to parallelize, if needed
* know your dependencies
* know your resources
* make sure your code works as expected before moving to HPC

## Before starting large-scale calculations

- Check how the software and your actual input performs
    - Common job errors are caused by typos in batch/input scripts
- Use short runs in the queue `--partition=test` to check that the input works and that the resource requests are interpreted correctly
- Check the output of the `seff` command to ensure that CPU and memory efficiencies are as high as possible
    - It's OK if a job is (occasionally) killed due to insufficient resource requests: just adjust and rerun/restart
    - It's _much worse_ to always run with excessively large requests "just in case"


## Running a new application in Puhti 

- If it comes with tutorials, do at least one
   - This will likely be the fastest way forward
   - Naturally, read the manual/instructions
- Check if there's a page about it in [Docs CSC](https://docs.csc.fi/apps/)
   - If there is, use the batch script example from _there_
   - Otherwise, use a [general template](https://docs.csc.fi/computing/running/example-job-scripts-puhti/)
- Try first running interactively (**not** on a login node)
   - Perhaps it is easier to find the correct command line options
   - Use the `top` command to get rough estimate of memory use, _etc_.
   - If developers provide some test or example data, run it first and make sure results are correct
- You can use the _test_ queue to check that your batch job script is correct
   - Limits : 15 min, 2 nodes
   - Job turnaround usually very fast even if machine is "full"
   - Can be useful to spot typos, missing files, _etc_. before submitting a job that will idle in the queue
- Before large runs, it's a good idea to do a smaller trial run
   - Check that results are as expected
   - Check the resource usage after the test run and adjust accordingly
- How many cores to allocate?
   - This depends on many things, so you have to try, see our [instructions about a scaling test](https://docs.csc.fi/support/tutorials/cmdline-handson/#scaling-test-for-an-mpi-parallel-job)


# Optimize the performance of your own code

- If you have written your own code, compile it with optimizing compiler options
   - Docs CSC: compiling on [Puhti](https://docs.csc.fi/computing/compiling-puhti/) and [Mahti](https://docs.csc.fi/computing/compiling-mahti/)
   - [Compiling on LUMI](https://docs.lumi-supercomputer.eu/development/)
- Construct a small and quick test case and run it in the test queue
   - Docs CSC: [Queue options](https://docs.csc.fi/computing/running/batch-job-partitions/)
   - [Available partitions on LUMI](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/)
   - Use the test case to optimize computations before starting massive ones
- Use profiling tools to find out how much time is spent in different parts of the code
   - Docs CSC: [Performance analysis](https://docs.csc.fi/computing/performance/)
   - [Profiling on LUMI](https://docs.lumi-supercomputer.eu/development/profiling/strategies/)
- When the computing bottlenecks are identified, try to figure out ways to improve the code
   - Again, [servicedesk@csc.fi](mailto:servicedesk@csc.fi) is a channel to ask for help
      - [The more concrete the problem is described, the better](https://docs.csc.fi/support/support-howto/)
   - If your issue concerns LUMI, contact the [LUMI User Support Team](https://lumi-supercomputer.eu/user-support/need-help/)




