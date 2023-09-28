

# Jobs 

![](./images/puhti_overview.png)

## Jobs and queueing 

* **Batch** jobs
	* resource request
	* computing step(s)
* Queue for resource management system to grant resources
* All heavy computing must be done via batch jobs!

## Serial vs array vs parallel

> TODO: image here

## Example sbatch script

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

## Monitoring jobs

* Standard output in file: slurm-<jobid>.out
* `squeue -u $USER`
* `seff <jobid>`
* `scancel <jobid>`


# What if your job fails? Troubleshooting checklist 1/2

1. Did the job run out of time?
2. Did the job run out of memory?
3. Did the job actually use the resources you specified?
   - Problems in the batch job script can cause parameters to be ignored and default values are used instead
4. Did it fail immediately or did it run for some time?
   - Jobs failing immediately are often due to something simple like typos, missing inputs, bad parameters, _etc_.

# What if your job fails? Troubleshooting checklist 2/2

5. Check the error file captured by the batch job script
6. Check any other error files and logs the your program may have produced
7. Error messaged can sometimes be long, cryptic and a bit intimidating, but ...
   - Try skimming through them and see if you can spot something "human-readable"
   - Often you can spot the actual problem easily if you go through the whole message. Something like "required input file so-and-so missing" or "parameter X out of range", _etc_.
8. Consult the [FAQ on common Slurm issues](https://docs.csc.fi/support/faq/why-does-my-batch-job-fail/) in the CSC Docs
