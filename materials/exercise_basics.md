# Exercise - basics

:::{admonition} Timing
:class: note

45 min

:::

:::{admonition} Goals
:class: note

* Get more familiar with command line
* Get to know sbatch script
* Get to know job submission
* Interactive -> non interactive

:::


:::{admonition} Prerequisites
:class: important

* Access to Puhti webinterface
* Own directory within the course directory `/scratch/project_200xxxx/students/cscusername`

:::


## Batch job tutorial - Interactive jobs

These examples are done on Puhti. When using the web interface, you can open a compute node shell directly.

In an interactive batch job, an interactive shell session is launched on a compute node, for which one can request specific resources (time, memory, cores, disk).

### Launching an interactive job / compute node shell

Observe how now you need to define the resources you want to reserve now. 
Let's reserve 10 minutes. 

:::{admonition} Other ways of starting an interactive session
:class: seealso

On the login node: Start an interactive job with `srun`, e.g.:

```bash
srun  --time=00:10:00 --pty --account=project_200xxxx --partition=interactive bash
```
or on Puhti you can also use `sinteractive` wrapper, which simplifies the call and asks you for the resources step by step: 

```bash
sinteractive
```
or directly: 

```bash
sinteractive --account project_200xxxx --time 00:10:00         # replace <project> with your CSC project, e.g. project_2001234
```
:::

:::{admonition} Need your project number?
:class: seealso
You can check [my.csc.fi](https://my.csc.fi/) or list your projects with `csc-projects` in a login node shell.
:::

Observe how the command prompt (initial text on each row on the command-line) looks now compared to a login node shell e.g. `r07c51`,which refers to a compute node, as opposed to e.g. `puhti-login11` .

1. Once on the compute node, you can run commands directly from the command-line. You can e.g. load the `geoconda` module:

```bash
module load geoconda
```

2. Then we can use for example `gdalinfo` to check the details of some rasterfile.

```bash
gdalinfo /appl/data/geo/luke/forest_wind_damage_sensitivity/2017/windmap2017_int1k_metsamaa2_cog.tif
```

:::{admonition} Task
:class: tip

Try out some other command line tool, or maybe even start a `python` or `R` session. What modules do you need to load? Check the [CSC Docs pages about "geo" applications](https://docs.csc.fi/apps/by_discipline/#geosciences).

:::


3. Quit the interactive batch job with `exit`. 

-> This way you can work interactively for an extended period, using e.g. lots of memory without creating load on the login nodes. 

Note that above we only asked for 10 minutes of time. Once that is up, you will be automatically logged out from the compute node.

Running `exit` on the login node will log you out from Puhti.


:::{admonition} More information on interactive jobs
:class: seealso

Documentation at [Docs CSC: Interactive usage](https://docs.csc.fi/computing/running/interactive-usage/) and 
[CSC Docs: FAQ on CSC batch jobs](https://docs.csc.fi/support/faq/#batch-jobs)

:::


## Batch job tutorial - Serial jobs

Examples are done on Puhti. If using the web interface, open a login node shell.

:::{admonition} Remember
:class: seealso
A serial program can only use one core (CPU)

- One should request only a single core from SLURM
- The job does not benefit from additional cores
- Excess cores are wasted since they will not be available to other users
:::

If you use a software that is pre-installed by CSC, please [check its documentation page](https://docs.csc.fi/apps/); it might have a batch job example with useful default settings.

### Launching a serial job

1. Go to your own directory in the `/scratch` directory of your project:

```bash
cd /scratch/project_200xxxx/students/cscusername      # replace xxxx with your CSC project number
```

2. Create a file called `my_serial.bash` e.g. with the `nano` text editor:

```bash
nano my_serial.bash
```

3. Copy the following **batch script** there and change `<project>` to the CSC project you actually want to use:

```bash
#!/bin/bash
#SBATCH --account=<project>      # Choose the billing project. Has to be defined!
#SBATCH --time=00:02:00          # Maximum duration of the job. Upper limit depends on the partition. 
#SBATCH --partition=test         # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --ntasks=1               # Number of tasks. Upper limit depends on partition. For a serial job this should be set 1!

echo -n "We are running on"
hostname                    # Run hostname-command, that will print the name of the Puhti compute node that has been allocated for this particular job
sleep 60                    # Run sleep-command, to keep the job running for an additional 60 seconds, in order to have time to monitor the job
echo "This job has finished"
```

In the batch job example above we are requesting

- one core (`--ntasks=1`)
- for two minutes (`--time=00:02:00`)
- from the test queue (`--partition=test`)  

4. Submit the job to the batch queue and check its status with the commands:

```bash
sbatch my_serial.bash
squeue -u $USER
```

5. Once the job is done, check how much of the resources have been used with `seff <jobid>`.

:::{admonition} Additional exercises
:class: tip

1. Where can you find the hostname print?
2. How could you add a name to the job for easier identification?
3. What happens if you run the same script from above, but we request only one minute, and sleep for 2 minutes?
4. Can you run the gdalinfo command from the interactive job above via a non interactive job? What do you need to change in the sbatch job script?


:::{admonition} Solution
:class: dropdown

1. `slurm-<jobid>.out` in the directory from where you submitted the batch job. You can also change that location by specifying it in your batch job script with `#SBATCH --output=/your/path/slurm-%j.out`.
2. Add `#SBATCH --job-name=<myname>` to the resource request in the top of your sbatch script.
3. After the job finished, check the log file with `cat slurm-<jobid>.out`. You should see an an error in the end `slurmstepd: error: *** JOB xxx ON xxx CANCELLED AT xDATE-TIMEx DUE TO TIME LIMIT ***`. This means that our job was killed for exceeding the amount of resources requested. Although this appears harsh, this is actually a feature. Strict adherence to resource requests allows the scheduler to find the best possible place for your jobs. It also ensures the fair share of use of the computing resources.
4. Since gdalinfo is quite a fast command to run, you will only need to change the script part of your sbatch script, the resources request can stay the same. First we will need to make `gdal` available within the job with `module load geoconda`, then we can run the `gdalinfo` command. After the job is done, you can find the information again in the `slurm-<jobid>.out` file. 

```bash
#!/bin/bash
#SBATCH --account=<project>      # Choose the billing project. Has to be defined!
#SBATCH --time=00:02:00          # Maximum duration of the job. Upper limit depends on the partition. 
#SBATCH --partition=test         # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --ntasks=1               # Number of tasks. Upper limit depends on partition. For a serial job this should be set 1!

module load geoconda

gdalinfo /appl/data/geo/luke/forest_wind_damage_sensitivity/2017/windmap2017_int1k_metsamaa2_cog.tif
```

:::

:::{admonition} Key points
:class: important

* A batch job script combines resource estimates and computation steps
    * Resource request lines start with `#SBATCH`
* You can find the jobs output, errors and prints in `slurm-<jobid>.out`


:::