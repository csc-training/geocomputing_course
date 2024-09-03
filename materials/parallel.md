# Parallel computing

For fast computation, supercomputers utilize parallelism. 

![](./images/parallel.png)

For doing analysis in parallel there are four main options:

1) Tools with built-in parallel support
2) Python, R or Julia parallel libaries
3) External tools to run the scripts in parallel
4) Write your own parallel code

From practival point of view in supercomptuers, it is also important to understand, if the the tool supports:
* **Multi-core** - it runs in parallel only inside one node of the supercomputer. Currently in Puhti there is 40 cores in a node and in Mahti and LUMI 128.
* **Multi-node** - it can distribute the work to several nodes of the supercomputer.

For multi-core there is clearly more options. The number of cores in a single node has been recently been increasing, so also multi-core tools can be very useful. 

:::{admonition} Think about your own work
:class: tip

Do you need to run a lot of steps one after another? Or few steps that need a lot of memory? Do steps depend on each other? Which steps could be run in parallel? Which steps cannot be run in parallel?

:::

## Tools with built-in parallel support

Look from the tool's manual, if it has built-in support for using multiple CPUs/cores. For command line tools, look for `-n(umber of)_cores`, `-c(ores/pu)`, `-j(obs)`, `-t(hreads)` or similar. Unfortunatelly not many GIS-tools have such option.

Some example geospatial tools with built-in parallel support: 
* GDAL, some commands e.g. `gdalwarp -multi -wo NUM_THREADS=val/ALL_CPUS ...`
* FORCE
* OpenDronemap
* OrfeoToolBox
* Whiteboxtools; many tools support parallel execution without extra action
* Lastools; many tools support parallel execution by setting `-cores`
* [PDAL-wrench](https://github.com/PDAL/wrench?tab=readme-ov-file#parallel-processing)
* SNAP with [Graph Processing Tool](https://docs.csc.fi/apps/snap/#using-snap-with-graph-processing-tool-gpt-command)
* Zonation
* Python libraries: osmnx, xarray, dask-geopandas
* R libraries: raster, terra, lidR

All of these tools are multi-core, but not multi-node.

The deep learning libraries have options for [Multi-GPU and multi-node machine learning](https://docs.csc.fi/support/tutorials/ml-multi/).

## Python, R or Julia parallel libaries

Many programming languages have packages for parallel computing: 
* Python:
   * Multi-core: `multiprocessing` and `joblib`
   * Multi-core or multi-node: `dask`
* R:
   * Multi-core: `parallel`
   * Multi-core or multi-node: `snow` and `future`
* Julia:
   * Multi-core: [multi-threading](https://docs.julialang.org/en/v1/manual/multi-threading/#man-multithreading)

If you have for-loops`, `map()`/`*apply()-functions or similar in your scripts, it can be rather easy to make the scripts running in parallel.

## External tools to run the scripts in parallel

The external tools enable running the scripts in parallel. This way of running programs is also called task farming or high throughput computing. The tools have different complexity and different features. The simpler of these tools are for running same script with different input paramaters, for example different input files, scenarios, time frames etc. More complicated tools support managing the whole workflow with several steps and with dependecies between steps. Workflow tools also help with making your work more reproducible by recording the computational steps and data. See [CSC Docs: High-throughput computing and workflows](https://docs.csc.fi/computing/running/throughput/) for more information.

### GNU Parallel

GNU parallel is a general Linux tool for executing commands or scripts in parallel in one node. It iterates over an input list, which can be a list of files or list of input parameters. The number of tasks may be higher than number of cores, it waits with execution as resources become available. GNU Parellel does not support dependecies between the tasks.

* From [GNU Parallel documentation](https://www.gnu.org/software/parallel/)
* Geocomputing examples: [GDAL with GNU-parallel](https://github.com/csc-training/geocomputing/tree/master/gdal) and [PDAL with GNU-parallel](https://github.com/csc-training/geocomputing/tree/master/pdal)
* A more advanced example for using [GNU-parallel for multi-node](https://docs.csc.fi/support/tutorials/many/) together with another tool.

### Snakemake

Snakemake is a scientific workflow management system, that supports running for example R, bash and Python scripts. It can handle dependecies between the tasks and can be used both multi-core and multi-node set-ups. Snakemake is one of the easiest tools for workflow management.

* [CSC Docs: Running Snakemake workflow on Puhti](https://docs.csc.fi/support/tutorials/snakemake-puhti/)



## Write your own parallel code

Parallel programs are typically parallelized with the [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) and/or [OpenMP](https://en.wikipedia.org/wiki/OpenMP) standards or using GPUs, but in this course we are not going to these topics.

* [CSC training calendar](https://www.csc.fi/en/training#training-calendar), look for advanced coding courses.
* [CSC Computing Environment, How to speed up jobs](https://a3s.fi/CSC_training/11_speed_up_jobs.html#/how-to-speed-up-jobs)


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

:::

