

# Jobs 

![](../images/puhti_overview.png)

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