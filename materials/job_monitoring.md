# Job monitoring

By default, the standard output (e.g. things that you print as part of your script) and standard error (e.g. error messages from Slurm, your tool or package) are written to the file `slurm-jobid.out`. 

You can check the status of your job and follow its progress with the `sacct` or `squeue --me` command (see also [Slurm documentation of job code states](https://slurm.schedmd.com/squeue.html#SECTION_JOB-STATE-CODES))
Resource usage while the job runs, can be queried with `seff jobid` (note that `seff` output can only be trusted after a job has finished).

If you would like to cancel a job after job submission or during runtime, you can do so with `scancel jobid`.

## Resource monitoring

**Important resource requests that should be monitored with `seff` are:**
- [Memory requirements](https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/)  
- [Disk workload](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage)
- [GPU efficiency](https://docs.csc.fi/computing/usage-policy/#gpu-nodes)
- [Scaling of a job over several cores and nodes](https://docs.csc.fi/computing/running/performance-checklist/#perform-a-scaling-test)
    - Parallel jobs must always benefit from all requested resources
    - **When you double the number of cores, the job should run _at least_ 1.5x faster**

:::{admonition} Troubleshooting resource usage
:class: seealso

Points to pay attention to:
- Low CPU Efficiency:
   - Too many cores requested?
   - Cores waiting for other processes?
   - Cores waiting for data from disk?
   - Cores spread over too many nodes?
- Low Memory Efficiency:
   - Too much memory requested?
   - Lots of caveats here
- Low GPU efficiency:
   - Better to use CPUs? Disk I/O?

:::

:::{admonition} `sacct`
:class: warning
More detailed queries can be tailored with `sacct`
- `sacct -j jobid -o jobid,partition,state,elapsed,start,end`
- `sacct -S 2022-08-01` will show all jobs started after that date
**Note!** Querying data from the Slurm accounting database with `sacct` can be a very heavy operation. **Don't** query long time intervals or run `sacct` in a loop/using `watch` as this will degrade the performance of the system for all users.
:::

:::{admonition} What to do if a job fails?
:class: warning

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
