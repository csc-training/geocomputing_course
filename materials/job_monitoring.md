# Job monitoring

By default, the standard output (e.g. things that you print as part of your script) and standard error (e.g. error messages from SLURM, your tool or package) are written to files `slurm-jobid.out` and `slurm-jobid.err` respectively. The file names can be changed from batch job script.

You can check the status of your job and follow its progress with the `squeue --me` command.
Resource usage while the job runs, can be queried with `seff jobid` (note that `seff` output can only be trusted after a job has finished).

If after job submission or during runtime you would like to cancel a job, you can do so with `scancel jobid`.


## Resource monitoring

**Important resource requests that should be monitored with `seff` are:**
- [Memory requirements](https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/)  
- [Disk workload](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage)
- [GPU efficiency](https://docs.csc.fi/computing/usage-policy/#gpu-nodes)
- [Scaling of a job over several cores and nodes](https://docs.csc.fi/computing/running/performance-checklist/#perform-a-scaling-test)
    - Parallel jobs must always benefit from all requested resources
    - When you double the number of cores, the job should run _at least_ 1.5x faster

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
