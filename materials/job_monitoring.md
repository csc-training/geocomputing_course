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

## Resource monitoring
See the resource usage after job has finished: `seff jobid`

More detailed queries can be tailored with `sacct`
- Job with ID: `sacct -j jobid -o jobid,partition,state,reqmem,maxrss,averss,elapsed`
- All jobs started after some date: `sacct -S 2024-08-01 -o jobid,partition,state,reqmem,maxrss,averss,elapsed` 

**Note!** Querying data from the Slurm accounting database with `sacct` can be a very heavy operation. **Don't** query long time intervals or run `sacct` in a loop/using `watch` as this will degrade the performance of the system for all users.

Important aspects to monitor are:
- [Memory efficiency](https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/)
     - If low memory usage: too much memory requested?
     - If a lot of memory needed, think how to re-write your analysis to use less memory
- [CPU efficiency](https://docs.csc.fi/computing/running/performance-checklist/#perform-a-scaling-test)
    - Parallel jobs must always benefit from all requested resources.
    - **When you double the number of cores, the job should run at least 1.5x faster.**
    - Low CPU Efficiency:
         - Too many cores requested?
         - Cores waiting for other processes?
         - Cores waiting for data from disk?
         - Cores spread over too many nodes?
- [GPU efficiency](https://docs.csc.fi/computing/usage-policy/#gpu-nodes)
   - If low GPU usage: better to use CPUs? Is disk I/O the bottleneck?
- [Disk workload](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage)
