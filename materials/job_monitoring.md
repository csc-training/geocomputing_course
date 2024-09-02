# Job monitoring

* Check the status of your job: `squeue --me`
* Cancel a job after job submission or during runtime: `scancel jobid`.

More detailed queries can be tailored with `sacct`
- `sacct -j jobid -o jobid,partition,state,reqmem,maxrss,averss,elapsed`
- `sacct -S 2024-08-01 -o jobid,partition,state,reqmem,maxrss,averss,elapsed` will show all jobs started after that date

**Note!** Querying data from the Slurm accounting database with `sacct` can be a very heavy operation. **Don't** query long time intervals or run `sacct` in a loop/using `watch` as this will degrade the performance of the system for all users.

## Job output
By default, the standard output (e.g. things that you print as part of your script) and standard error (e.g. error messages from Slurm, your tool or package) are written to the file `slurm-jobid.out`. You can change the default in the batch job script:

#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt

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
:::

## Resource monitoring
See the resource usage after job has finished: `seff jobid`

Important aspects to monitor are:
- [Memory requirements](https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/)
- [CPU usage](https://docs.csc.fi/computing/running/performance-checklist/#perform-a-scaling-test)
    - Parallel jobs must always benefit from all requested resources
    - **When you double the number of cores, the job should run _at least_ 1.5x faster**
- [Disk workload](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage)
- [GPU efficiency](https://docs.csc.fi/computing/usage-policy/#gpu-nodes)

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




