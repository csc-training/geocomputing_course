# Job types

## Interactive jobs

You already got to know the [interactive web interface for Puhti](https://docs.csc.fi/computing/webinterface/)
- If you have a heavier job that still requires interactive response (_e.g._ testing, prototyping)
    - Allocate the resource via the the [interactive partition](https://docs.csc.fi/computing/running/interactive-usage/)
    - This way your work is performed in a compute node, not on the login node

Disadvantages of interactive jobs: 
* Blocks your shell until it finishes
* Connection interruption means that job is gone.
     * Note: With persistent `compute node shell` from the web interface or using Linux tool [screen](https://www.geeksforgeeks.org/screen-command-in-linux-with-examples/) it is possible to keep a job running while closing the terminal.

Apart from interactive jobs, a job can be classified as **serial, parallel or GPU**, depending on the main requested resource. A serial job is the simplest type of job whereas parallel and GPU jobs may require some advanced methods to fully utilise their capacity. 

## Serial jobs

Serial job means that the computer works on only one task at a time following a sequence of instructions, while only using one core.

Why would your serial job benefit from being executed using CSC's resources instead of on your own computer? 
- Part of a larger workflow
- Avoid data transfer between CSC and your own computer
- Data sharing among other project members
- Readily configured environment / dependencies (e.g. R environment on Puhti)
- Memory and/or disk demands

## Parallel jobs

A parallel job distributes the work over several cores in order to achieve a shorter wall time (and/or a larger allocatable memory). 

In this course we will focus on **embarrassingly/naturally/delightfully parallel processes** with methods that are either built-in to the tools or tools that can start multiple jobs from one call. For more advanced usage, there are two major parallelization schemes: [OpenMP](https://en.wikipedia.org/wiki/OpenMP) and [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface). 

:::{admonition} Advanced topics - MPI/OpenMP
:class: dropdown, seealso

**What is MPI?**

- MPI (Message Passing Interface) is a widely used standard for writing software that runs in parallel
- MPI utilizes parallel **processes** that _do not share memory_
   - To exchange information, processes pass data messages back and forth between the cores
   - Communication can be a performance bottleneck
- MPI is required when running on multiple nodes

**What is OpenMP?**

- OpenMP (Open Multi-Processing) is a standard that utilizes compute cores that share memory, i.e. **threads**
   - They do not need to send messages between each other
- OpenMP is easier for beginners, but problems quickly arise with so-called _race conditions_
   - This appears when different compute cores process and update the same data without proper synchronization
- OpenMP is restricted to a single node

**Batch job examples**

- Multicore OpenMP job


```bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=X
```

- Multicore MPI job

```bash
#SBATCH --nodes=X
#SBATCH --ntasks-per-node=Y
#SBATCH --cpus-per-task=1
```

- `--cpus-per-task` is typically used for OpenMP jobs
- `--ntasks` is typically used for MPI jobs
    - A task cannot be split between nodes, but tasks can be on different nodes
    - `--ntasks-per-node` can be used for finer control

**Self study materials for OpenMP and MPI**

- There are many tutorials available online
   - Look with simple searches for _e.g._ "MPI tutorial"
- Check the documented exercise material and model answers from the CSC course "Introduction to Parallel Programming"
   - Available on [GitHub](https://github.com/csc-training/parallel-prog/)
   - See also the [materials of CSC Summer School in HPC](https://github.com/csc-training/summerschool)

:::

## Array jobs

[Array jobs](https://docs.csc.fi/computing/running/array-jobs/) are one way of taking advantage of Puhti's parallel processing capabilities for embarrassingly parallel tasks. Array jobs are useful when same code is executed many times for different datasets or with different parameters without the need to change your code. In GIS context, a typical use case would be to run some model on study area split into multiple files where output from one file doesn't have an impact on the result of another area. 

:::{admonition} Maximum job limits
:class: warning

Submitting an array job of 100 members counts the same as 100 individual jobs from the batch queue system's perspective. In Puhti, one can submit/run a maximum of 400/200 jobs at the same time (except for `interactive`, `test` and `gputest`, where the limits are one or two). The number of submitted jobs per user per month should be kept below one thousand. 

:::

## GPU jobs 

A GPU is capable of doing certain type of simultaneous calculations very efficiently. In order to take advantage of this power, a computer program must be programmed to adapt on how GPU handles data. For spatial computations on the GPU, check out for example [RAPIDS cuSpatial](https://docs.rapids.ai/api/cuspatial/stable/user_guide/cuspatial_api_examples/). [CSC's GPU resources](https://docs.csc.fi/computing/overview/#gpu-nodes) are relatively scarce and hence should be used with particular care. A GPU uses 60 times more billing units than a single CPU core. In practice, 1-10 CPU cores (but not more) should be allocated per GPU on Puhti.

:::{admonition} Advanced topics - GPU
:class: dropdown, seealso

**GPUs can speed up jobs**

- GPUs can be used for science, but are often challenging to program
   - Not all algorithms can use the full power of GPUs
- Check the manual if the software can utilize GPUs, don't use GPUs if you're unsure
   - See our [CSC Docs page on how to check if your batch job used GPU](https://docs.csc.fi/support/tutorials/gpu-ml/#gpu-utilization)
   - The [CSC usage policy](https://docs.csc.fi/computing/usage-policy/#gpu-nodes) limits GPU usage to where it is most efficient
   - Also, if you process lots of data, make sure you [use the disk efficiently](https://docs.csc.fi/support/tutorials/ml-data/#using-the-shared-file-system-efficiently)
- Does your code run on AMD GPUs? [LUMI](https://docs.lumi-supercomputer.eu/hardware/lumig/) has a massive GPU capacity!

- Can your software utilize GPUs?
   - [GPUs in Puhti batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#gpus)
   - [GPUs in Mahti batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-mahti/#gpu-batch-jobs)
   - [GPUs in LUMI batch jobs](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/)

:::


:::{admonition} Think about your work
:class: info

Which job type sounds like it could benefit your work? 

:::
