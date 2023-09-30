# Batch jobs

**Batch** jobs consist of resource request and computing step(s). These requests are submitted from the login node. Every batch job will sit in queue for resource management system to grant resources according to the request. All heavy computing must be done via batch jobs!

## Example sbatch script

Batch job script [how-to create](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/) and [examples](https://docs.csc.fi/computing/running/example-job-scripts-puhti/) for Puhti.

```
#!/bin/bash
#SBATCH --account=<project>      # Choose the billing project. Has to be defined!
#SBATCH --time=00:02:00          # Maximum duration of the job. Upper limit depends on the partition. 
#SBATCH --partition=test         # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --ntasks=1               # Number of tasks. Upper limit depends on partition. For a serial job this should be set 1!

srun hostname                    # Print compute node name that has been allocated

``` 

<p>&rarr; File `simple.bash` </p> 
<p>&rarr; Submit for computation with `sbatch simple.bash` </p>

**The best starting point for writing batch job scripts:** [Software specific batch scripts in docs](https://docs.csc.fi/apps/)




:::{admonition} Batch job troubleshooting checklist
:class: tip

What to do if a job fails?

1. Did the job run out of time?
2. Did the job run out of memory?
3. Did the job actually use the resources you specified?
   - Problems in the batch job script can cause parameters to be ignored and default values are used instead
4. Did it fail immediately or did it run for some time?
   - Jobs failing immediately are often due to something simple like typos, missing inputs, bad parameters, _etc_.
5. Check the error file captured by the batch job script (default name `slurm-<jobid>.out`)
6. Check any other error files and logs the your program may have produced
7. Error messages can sometimes be long, cryptic and a bit intimidating, but ...
   - Try skimming through them and see if you can spot something "human-readable"
   - Often you can spot the actual problem, if you go through the whole message. Something like "required input file so-and-so missing" or "parameter X out of range", _etc_.
8. Consult the [FAQ on common Slurm issues](https://docs.csc.fi/support/faq/why-does-my-batch-job-fail/) in the CSC Docs

:::
