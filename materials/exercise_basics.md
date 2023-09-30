# Exercise - basics

:::{admonition} Timing
:class: note

45 min

:::

:::{admonition} Goals
:class: note

* Get to know the command line
* Get to know sbatch script
* Get to know job submission
* Interactive -> non interactive

:::


:::{admonition} Prerequisites
:class: important

* Access to Puhti webinterface
* Own directory within the course directory `/scratch/project_200xxxx/$USER`

:::


## Batch job tutorial - Interactive jobs

These examples are done on Puhti. If using the web interface, you can either open a login node shell and follow the steps below or open a compute node shell directly and skip to step 2.

In an interactive batch job, an interactive shell session is launched on a compute node, for which one can request specific resources (time, memory, cores, disk).

### Launching an interactive job

1. Start an interactive job using one core for ten minutes:

```bash
sinteractive --account <project> --time 00:10:00         # replace <project> with your CSC project, e.g. project_2001234
```

:::{admonition} Need your project number?
:class: seealso
You can list your projects with `csc-projects`
:::

Observe that the command prompt (initial text on each row on the command-line) has changed from e.g. `puhti-login11` to e.g. `r07c51` which refers to a compute node.

2. Once on the compute node, you can run commands directly from the command-line. You can e.g. load the `geoconda` module:

```bash
module load geoconda
```

3. Then we can use for example `gdalinfo` to check the details of some rasterfile.

```bash
gdalinfo /appl/data/geo/luke/forest_wind_damage_sensitivity/2017/windmap2017_int1k_metsamaa2_cog.tif
```

4. Quit the interactive batch job with `exit`.

-> This way you can work interactively for an extended period, using e.g. lots of memory without creating load on the login nodes. Running heavy/long tasks on the login nodes is forbidden according to our [Usage Policy](https://docs.csc.fi/computing/usage-policy/).

Note that above we only asked for 10 minutes of time. Once that is up, you will be automatically logged out from the compute node.

Running `exit` on the login node will log you out from Puhti.


:::{admonition} More information on interactive jobs
:class: seealso

Documentation at Docs CSC on [Interactive usage](https://docs.csc.fi/computing/running/interactive-usage/)
[FAQ on CSC batch jobs](https://docs.csc.fi/support/faq/#batch-jobs) in Docs CSC

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

1. Go to the `/scratch` directory of your project:

```bash
cd /scratch/<project>/$USER      # replace <project> with your CSC project, e.g. project_2001234
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

srun hostname                    # Run hostname-command, that will print the name of the Puhti compute node that has been allocated for this particular job
srun sleep 60                    # Run sleep-command, to keep the job running for an additional 60 seconds, in order to have time to monitor the job
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


:::{admonition} Solution
:class: topic, dropdown

1. `slurm-<jobid>.out` in the directory from where you submitted the batch job. You can also change that location by specifying it with `#SBATCH --output=/your/path/slurm-%j.out`.
2. `#SBATCH --job-name=<myname>`

:::

:::{admonition} Key points
:class: important

* A batch job script combines resource estimates and computation steps
    * Resource request lines start with `#SBATCH`
* You can find the jobs output, errors and prints in `slurm-<jobid>.out`


:::