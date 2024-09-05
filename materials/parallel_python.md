# Parellel Python

If starting with a new code, the first option could be to look for spatial libraries that have parallelization already built in:

* [Dask-geopandas](https://dask-geopandas.readthedocs.io/) for vector data analysis, still a lot more limited than `geopandas`
* [xarray](http://xarray.pydata.org/) for basic raster data analysis with Dask
  * The [STAC exercise](exercise_stac.md) is using Dask with `xarray`.
* [xarray-spatial](https://xarray-spatial.readthedocs.io/en/stable/) for common raster analysis functions with Dask
* [rioxarray](https://corteva.github.io/rioxarray/stable/index.html) for reading data via GDAL-supported formats and basic merging, clipping etc with Dask
* [osmnx](https://osmnx.readthedocs.io/en/stable/index.html) for routing with `multiprocessing`
  
These libraries are still developing and do not support very wide range of functionality, so often these do not fit all requirements. Or if you are changing an existing serial code to parallel. Then the next option is to write parallel coude yourself. The basic Python code runs in serial mode, so usually some changes to code are needed to benefit from parallel computing. 

Python has many libraries to support parallelization:

   * Multi-core: `multiprocessing` and `joblib`
   * Multi-core or multi-node: **`dask`** and `mpi4py`

If unsure, start with Dask, it is one of the newest, most versatile and easy to use. But Dask has many options and alternatives, `multiprocessing` might be easier to learn as first.

:::{admonition} How many cores I can use?
:class: tip.

If you need to check in code, how many cores you can use, use:
```
len(os.sched_getaffinity(0))
```

Do not use `multiprocessing.cpu_count()`, that counts only hardware cores, but does not understand batch jobs.

:::

* [CSC Parallel Python course materials](https://github.com/csc-training/hpc-python/blob/master/docs/mooc/index.md), inc `mpi4py`
* [Geocomputing examples for Puhti](https://github.com/csc-training/geocomputing/tree/master/python/puhti), inc. `dask`, `multiprocessing` and `joblib`

## Dask

### Parallelization set-up
[Dask](https://docs.dask.org/en/stable/) supports different set-ups for parallel computing, from supercomptuers point of view, the main options are:

* [Default schedulers](https://docs.dask.org/en/stable/scheduler-overview.html) for multi-core jobs.
* [LocalCluster](https://distributed.dask.org/en/latest/index.html) for multi-core jobs.
* [SLURMCluster](https://jobqueue.dask.org/en/latest/index.html) for multi-node jobs.

While developing the code, it might be good to start with default scheduler or `LocalCluster` parallelization and then if needed change it to `SLURMCluster`. The required changes to code are small, when changing the parallelization set-up.

One of the advantages of using LocalCluster, is that then in Jupyter the [Dask-extension](https://github.com/dask/dask-labextension) is able to show progress and resource usage.

```
# Default scheduler is started automatically, when Dask objects or functions are used.

######################
# LOCALCLUSTER, with default settings.
from dask.distributed import Client
client = Client()

# With for example 30 cores available, Dask by default would likely create 6 workers.
# Depending on your analysis, it might be good or not.
# To select the number of workers explicitly:
no_of_workers = len(os.sched_getaffinity(0))
client = Client(n_workers=no_of_workers)


######################
# SLURMCLUSTER
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

### Changes to code
The changes to code are exactly the same for all parallization set-ups. The most simple changes could be:

* For-loops:
  * Change to `Dask's client.map()`,
  * If you have several rows of code in your for-loop, make it to a function.
* `map()` -> `Dask's client.map()`

```
# Example of changing for-loop and map() to client.map()
# Just a demo slow function, that waits for 5 seconds
def slow_functio(i):
  time.sleep(2) 
  return(i)
# Input data vector, the slow function is run for each element.
input = range(0, 7)

# SERIAL options:
# Basic FOR loop
a = []
for i in input: 
  a.append(slow_function(i))

print(a)

# Basic map
a = map(slow_function, input)
print(list(a))

# PARALLEL, with Dask futures with LocalCluster
# Could be used also with SLURMCluster
from dask.distributed import Client
client = Client() 
futures = client.map(slow_function, input)
a = client.gather(futures)
print(a)

# PARALLEL, with Dask delayed functions
# Can be used with default scheduler, LocalCluster or SLURMCluster
from dask import delayed
from dask import compute
list_of_delayed_functions = []
for i in input:
    list_of_delayed_functions.append(delayed(slow_function)(i))

### This starts the execution with the resources available
a = compute(list_of_delayed_functions)
print(a)
```

:::{admonition} variables with Dask
:class: tip

* Dask exports needed variables and libraries automatically to the parallel processes
* The variables must be serializable.
* Avoid moving big size variables from main to parallel process. Spatial data analysis often includes significant amounts of data. It is better to read the data inside the parallel function. Give as input the file name or compute area coordinates etc. 

:::


## Batch job file changes
### Multi-core jobs
Default schedulers or `LocalCluster` parallization:
```
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4  # Number of cores. Upper limit depends on number of CPUs per node.

(...)

srun python dask_singlenode.py
```

### Multi-node jobs
`SLURMCluster` parallelization:
```
#SBATCH --nodes=2 #For cluster usage to make sense, this should be more than 1.
#SBATCH --cpus-per-task=40  # Number of cores. Upper limit depends on number of CPUs per node.

(...)

srun python dask_multinode.py
```
