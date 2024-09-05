# Job monitoring

* Check the status of your job: `squeue --me`

## Job output
By default, the standard output (e.g. things that you print as part of your script) and standard error (e.g. error messages from Slurm, your tool or package) are written to the file `slurm-jobid.out` in the same folder as the batch job script. You can change the defaults in the batch job script:

```
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
```

:::{admonition} What to do if a job fails?
:class: seealso

Does `sacct` show you that your job failed? Or did your job not do what you expected (e.g. write some files, etc)? 
Some things to check:

1. Did the job run out of time?
2. Did the job run out of memory?
3. Did the job actually use the resources you specified?
   - Problems in the batch job script can cause parameters to be ignored and default values are used instead
4. Did it fail immediately or did it run for some time?
   - Jobs failing immediately are often due to something like typos, missing inputs, bad parameters _etc_.
5. Check the error file captured by the batch job script (default name `slurm-jobid.out`)
6. Check any other error files and logs your program may have produced
7. Error messages can sometimes be long, cryptic and a bit intimidating, but ...
   - Try skimming through them and see if you can spot something "human-readable"
   - Often you can spot the actual problem, if you go through the whole message. Something like "required input file so-and-so missing" or "parameter X out of range" _etc_.
8. Consult the [FAQ on common Slurm issues](https://docs.csc.fi/support/faq/why-does-my-batch-job-fail/) in the CSC Docs
:::

## Testing
- Before large runs, it's a good idea to do a smaller trial run
- Start simple and gradually use more complex approaches if needed
   - Try first running interactively (**not** on a login node) to check how the tool performs on actual input data
   - Check that results are as expected
   - Check the resource usage after the test run and adjust accordingly
   - If developers provide some test or example data, run it first and make sure results are correct
- You can use the `test`-partition to check that your batch job script is correct and everything is interpreted correctly
   - Limits : 15 min, 2 nodes
   - Job turnaround usually very fast even if machine is "full"
   - Can be useful to spot typos, missing files, _etc_. before submitting a job that might stay waiting in the queue

## Resource monitoring
See the resource usage after job has finished: `seff jobid`

More detailed queries can be tailored with `sacct`
- Job with ID: `sacct -j jobid -o jobid,partition,state,reqmem,maxrss,averss,elapsed`
- All jobs started after some date: `sacct -S 2024-08-01 -o jobid,partition,state,reqmem,maxrss,averss,elapsed` 

**Note!** Querying data from the Slurm accounting database with `sacct` can be a very heavy operation. **Don't** query long time intervals or run `sacct` in a loop/using `watch` as this will degrade the performance of the system for all users.

Important aspects to monitor are:
- Memory efficiency
     - If low memory usage: too much memory requested?
     - If a lot of memory needed, think how to re-write your analysis to use less memory
     - [CSC Docs: How to estimate how much memory my batch job needs?](https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/)
- CPU efficiency
    - Parallel jobs must always benefit from all requested resources.
    - Low CPU Efficiency:
         - Too many cores requested?
         - Cores waiting for other processes?
         - Cores waiting for data from disk?
         - Cores spread over too many nodes?
         - Perform a scaling test. 
- GPU efficiency
   - If low GPU usage: better to use CPUs? Is disk I/O the bottleneck?
- Disk workload
-    If a lot of I/0, use [local disks on compute nodes](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage)

:::{admonition} Monitoring interactive jobs
:class: tip
If you want to monitor real-time resource usage:
   - Open a new terminal on the same compute node as where the tool/script is running:
      - Jupyter and RStudio have Terminal windows.
      - If it is some other tool, open another terminal to the copmpute node:
         - Find out the compute node name from the prompt of the interactive job, something like: `r18c02`
         - Open a new terminal to login node login node,
         - Connect to compute node, for example: `ssh r18c02`
   - Use Linux `top -u $USER` command, it gives rough estimate of memory and CPU usage. 
:::


## Optimizing the performance of your own code

You can use profiling tools to find out how much time is spent in different parts of the code
- [CSC Docs: Performance analysis](https://docs.csc.fi/computing/performance/)
- [LUMI Docs: Profiling on LUMI](https://docs.lumi-supercomputer.eu/development/profiling/strategies/)
When the computing bottlenecks are identified, try to figure out ways to improve the code.
