# Parallel Python
## Spatial libraries with parallel support
If starting from scratch with a new program, the first option would be to look for spatial libraries that have parallelization already built in:

* [Dask-geopandas](https://dask-geopandas.readthedocs.io/) for vector data analysis, still a lot more limited than `geopandas`
* [xarray](http://xarray.pydata.org/) for basic raster data analysis
  * The [STAC exercise](exercise_stac.md) is using Dask with `xarray`.
* [xarray-spatial](https://xarray-spatial.readthedocs.io/en/stable/) for common raster analysis functions
* [rioxarray](https://corteva.github.io/rioxarray/stable/index.html) for reading data via GDAL-supported formats and basic merging, clipping etc
* [osmnx](https://osmnx.readthedocs.io/en/stable/index.html) for routing 

## Python parallel libraries

The parallel spatial libraries are still developing and do not support a very
wide range of functionality, so often these do not fit all requirements. The
next option is to write parallel code yourself. The basic Python code runs in
serial mode, so usually some changes to code are needed to benefit from
parallel computing. 

Python has many libraries to support parallelization:

   * Multi-core: `multiprocessing` and `joblib`
   * Multi-core or multi-node: **`dask`** and `mpi4py`

If unsure, start with Dask, it is one of the newest, most versatile and most
easy to use. There are, of course, many options and alternatives to Dask.
`multiprocessing` might be the easiest to learn first. All of the
above-mentioned spatial libraries use Dask, except `osmnx`, which uses
`multiprocessing`.

:::{admonition} How many cores can I use?
:class: tip.

To check for the number of cores you can use in your Python code, run:
```
len(os.sched_getaffinity(0))
```

Do not use `multiprocessing.cpu_count()`, that counts only hardware cores, but does not understand batch jobs.

:::

## Dask

[Dask](https://dask.org/) is a versatile Python library for scalable analytics. 

:::{admonition} Delayed computing
:class: tip

One general feature of Dask is that it delays computing to the point when the result is actually needed, for example for plotting or saving to a file. So for example when running the code in Jupyter, cells that actually require a longer runtime may run instantly, but another cell may run much later.

:::

When using Dask, two main decisions have to be made for running code in parallel, which we will answer next. 

1. How to run the parallel code?
2. How to make the code parallel?

### How to run the parallel code?

[Dask](https://docs.dask.org/en/stable/) supports different set-ups for parallel computing, from a supercomputing point-of-view, the main options are:

* [Default schedulers](https://docs.dask.org/en/stable/scheduler-overview.html) for multi-core jobs.
* [LocalCluster](https://distributed.dask.org/en/latest/index.html) for multi-core jobs.
* [SLURMCluster](https://jobqueue.dask.org/en/latest/index.html) for multi-node jobs.

While developing the code, it might be good to start with the default scheduler or `LocalCluster` parallelization and then, if needed, change it to `SLURMCluster`. The required changes to code are small when changing the parallelization setup.

One of the advantages of using `LocalCluster`, is that the Jupyter [Dask-extension](https://github.com/dask/dask-labextension) is able to show progress and resource usage.

**Default scheduler** is started automatically, when Dask objects or functions are used.

**LocalCluster**
```
# With default settings
from dask.distributed import Client
client = Client()

# With for example 30 cores available, Dask by default would likely create 6 workers.
# Depending on your analysis, it might be good or not.
# To select the number of workers explicitly:
no_of_cores = len(os.sched_getaffinity(0))
client = Client(n_workers=no_of_cores)
```

**SLURMCluster**
```
from dask_jobqueue import SLURMCluster

cluster = SLURMCluster(
    queue="small",
    account=project_name,
    cores=no_of_cores,
    processes=no_of_cores,
    memory="12G",
    walltime="00:10:00",
    interface="ib0"
)

cluster.scale(number_of_jobs)
client = Client(cluster)
```

### How to make the code parallel?
Dask provides several options, inc [Dask DataFrames](https://docs.dask.org/en/stable/dataframe.html), [Dask Arrays](https://docs.dask.org/en/stable/array.html), [Dask Bags](https://docs.dask.org/en/stable/bag.html), [Dask Delayed](https://docs.dask.org/en/stable/delayed.html) and [Dask Futures](https://docs.dask.org/en/stable/futures.html). This decision depends on the type of analyzed data and already existing code. Additionally Dask has support for scalable machine learning with [DaskML](https://ml.dask.org/).

In this course we use delayed functions. Delayed functions are useful in parallelizing existing code. This approach delays function calls and creates a graph of the computing process. From the graph, Dask can then divide the work tasks to different workers whenever parallel computing is possible. Keep in mind that the other ways of code parallelization might suit you better in different use cases. 

The changes to code are exactly the same for all parallelization setups. The most simple changes could be:

* For-loops:
  * Change to Dask's delayed functions,
* `map()` -> `Dask's client.map()`

```
# Example of changing for-loop and map() to Dask
# Just a slow demo function that waits for 2 seconds
def slow_functio(i):
  time.sleep(2) 
  return(i)
# Input data vector. The slow function is run for each element.
input = range(0, 7)
```
**Serial**
```
# Basic FOR loop
a = []
for i in input: 
  a.append(slow_function(i))

print(a)

# Basic map
a = map(slow_function, input)
print(list(a))
```

**Parallel, Dask delayed functions**
```
from dask import delayed
from dask import compute
list_of_delayed_functions = []
for i in input:
    list_of_delayed_functions.append(delayed(slow_function)(i))

a = compute(list_of_delayed_functions)
print(a)
```

**Parallel, with Dask futures**
```
from dask.distributed import Client
client = Client() 
futures = client.map(slow_function, input)
a = client.gather(futures)
print(a)
```

:::{admonition} variables with Dask
:class: tip

* Dask exports needed variables and libraries automatically to the parallel processes
* The variables must be serializable.
* Avoid moving variables that refer to large objects from main the main serial
  process to a parallel process. Spatial data analysis often involves
  significant amounts of data. It is better to read the data inside the
  parallel function: give the file name as input, compute area coordinates,
  etc. 

:::


### Batch job scripts
In batch job scripts it is important to set correctly:

#### Default schedulers and `LocalCluster`
* `nodes` - 1
* `cpus-per-task` - How many cores to reserve? Depending on the task, something between 1 and the total number of available CPUs per node. 

```
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4  

(...)

srun python dask_script.py
```

#### `SLURMCluster`
The main batch job file reserves only resources for the **master job** of Dask, so 1 node and 1 core is enough. 

```
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1  

(...)

srun python dask_script.py
```

The worker jobs are reserved on inside Python code. Ideally each job should fill one node. The number of jobs is defined by `cluster.scale()`. `cores` defines how many cores should be reserved. `processes` sets the number of workers in one job.

```
cluster = SLURMCluster(
    queue="small",
    account=project_name,
    cores=no_of_cores,
    processes=no_of_cores,
    memory="12G",
    walltime="00:10:00",
    interface="ib0"
)

cluster.scale(number_of_jobs)
client = Client(cluster)
```

Further reading:
* [CSC Docs, Dask tutorial](https://docs.csc.fi/support/tutorials/dask-python)
* [CSC geocomputing Python examples](https://github.com/csc-training/geocomputing/tree/master/python/puhti), inc. `dask`, `multiprocessing` and `joblib`
  * Dask DataFrames: [CSC dask-geopandas example](https://github.com/csc-training/geocomputing/edit/master/python/dask_geopandas)
  * Dask Arrays [CSC STAC example with Xarray](https://github.com/csc-training/geocomputing/edit/master/python/STAC)
* [CSC Parallel Python course materials](https://github.com/csc-training/hpc-python/blob/master/docs/mooc/index.md), inc `mpi4py` and `cython`
