# Exercise - basics

Goals:
* get to know the command line
* get to know sbatch script
* get to know job submission
* interactive -> non interactive

TODO: update to fit here; current texts from env eff course

## Interactive

# Batch job tutorial - Interactive jobs

> In this tutorial we'll get familiar with the basic usage of the Slurm batch queue system at CSC
- The goal is to learn how to request resources that **match** the needs of a job

💬 A job consists of two parts: resource requests and the job step(s)

☝🏻 Examples are done on Puhti. If using the web interface, you can either open a login node shell and follow the steps below or, even better, open a compute node shell directly and skip to step 3.

💡 The benefit of running an interactive session through the Puhti web interface is that the shell is *persistent*, i.e. the session will stay open and any programs started there will keep running even if you would happen to lose internet connection or close the browser tab.

## Interactive jobs

💬 In an interactive batch job, an interactive shell session is launched on a compute node.

- For heavy interactive tasks one can request specific resources (time, memory, cores, disk).

💡 You can also use tools with graphical user interfaces in an interactive shell session.

- For such usage the [Puhti web interface](https://www.puhti.csc.fi/) remote desktop often provides an improved experience.
- Check also [how to use RStudio and Jupyter Notebooks in Puhti](https://docs.csc.fi/support/tutorials/rstudio-or-jupyter-notebooks/)

### A simple interactive job

1. Start an interactive job using one core for ten minutes:

```bash
sinteractive --account <project> --time 00:10:00         # replace <project> with your CSC project, e.g. project_2001234
```

💡 You can list your projects with `csc-projects`

{:start="2"}
2. You should see that the command prompt (initial text on each row on the command-line) has changed from e.g. `puhti-login11` to e.g. `r07c51` which refers to a compute node.
3. Once on the compute node, you can run commands directly from the command-line without `srun`. You can e.g. load the `python-data` module (e.g. for running Python scripts interactively on Puhti):

```bash
module load python-data
```

{:start="4"}
4. Quit the interactive batch job with `exit`.

💬 This way you can work interactively for an extended period, using e.g. lots of memory without creating load on the login nodes. Running heavy/long tasks on the login nodes is forbidden according to our [Usage Policy](https://docs.csc.fi/computing/usage-policy/).

‼️ Note that above you asked only for 10 minutes of time.

- Once that is up, you will be automatically logged out from the compute node.

💡 From the command-line prompt you can see whether you're on a compute node (e.g. `r07c51`) or on the login node (e.g. `puhti-login12`).

- Running `exit` on the login node will log you out from Puhti.

## More information

💡 Documentation at Docs CSC on [Interactive usage](https://docs.csc.fi/computing/running/interactive-usage/)

💡 [FAQ on CSC batch jobs](https://docs.csc.fi/support/faq/#batch-jobs) in Docs CSC



# Batch job tutorial - Serial jobs

> In this tutorial we'll get familiar with the basic usage of the Slurm batch queue system at CSC
- The goal is to learn how to request resources that **match** the needs of a job

💬 A batch job consists of two parts: resource requests and the job step(s)

☝🏻 Examples are done on Puhti. If using the web interface, open a login node shell.

## Serial jobs

💬 A serial program can only use one core (CPU)

- One should request only a single core from Slurm
- The job does not benefit from additional cores
- Excess cores are wasted since they will not be available to other users

💬 Within the job (or allocation), the actual program is launched using the command `srun`

☝🏻 If you use a software that is pre-installed by CSC, please [check its documentation page](https://docs.csc.fi/apps/); it might have a batch job example with useful default settings.

### Launching a serial job

1. Go to the `/scratch` directory of your project:

```bash
cd /scratch/<project>      # replace <project> with your CSC project, e.g. project_2001234
```

- Now your input (and output) will be on a shared disk that is accessible to the compute nodes.

💡 You can list your projects with `csc-projects`

💡 Note! If you're using a project with other members (like the course project), first make a subdirectory for yourself (e.g. `mkdir $USER` and then move there (`cd $USER`) to not clutter the `/scratch` root of your project)

{:start="2"}
2. Create a file called `my_serial.bash` e.g. with the `nano` text editor:

```bash
nano my_serial.bash
```

{:start="3"}
3. Copy the following **batch script** there and change `<project>` to the CSC project you actually want to use:

```bash
#!/bin/bash
#SBATCH --account=<project>      # Choose the billing project. Has to be defined!
#SBATCH --time=00:02:00          # Maximum duration of the job. Upper limit depends on the partition. 
#SBATCH --partition=test         # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --ntasks=1               # Number of tasks. Upper limit depends on partition. For a serial job this should be set 1!

srun hostname                    # Run hostname-command
srun sleep 60                    # Run sleep-command
```

{:start="4"}
4. Submit the job to the batch queue and check its status with the commands:

```bash
sbatch my_serial.bash
squeue -u $USER
```

💬 In the batch job example above we are requesting

- one core (`--ntasks=1`)
- for two minutes (`--time=00:02:00`)
- from the test queue (`--partition=test`)  

💬 We want to run the program `hostname` that will print the name of the Puhti compute node that has been allocated for this particular job

💬 In addition, we are running the `sleep` program to keep the job running for an additional 60 seconds, in order to have time to monitor the job

#### Checking the output and the efficiency

- By default, the output is written to a file named `slurm-<jobid>.out` where `<jobid>` is a unique job ID assigned to the job by Slurm
- Check the efficiency of the job compared to the reserved resources by issuing the command `seff <jobid>` (replace `<jobid>` with the actual Slurm job ID)

💭 You can get a list of all your jobs that are running or queuing with the command `squeue -u $USER`

🗯 A submitted job can be cancelled using the command `scancel <jobid>`

## More information

💡 [FAQ on CSC batch jobs](https://docs.csc.fi/support/faq/#batch-jobs) in Docs CSC


