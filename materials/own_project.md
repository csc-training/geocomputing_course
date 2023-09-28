# Own project hints

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






