# Parallel R
## Spatial libraries with parallel support

If starting from scratch with new code, the first option would be to look for spatial libraries that have parallelization already built in:

* `terra` has some functions in parallel for raster processing
* `gdalcubes` for multi-dimensional spatial data analysis
* `lidR` for lidar data analysis

## R parallel libraries

The parallel spatial libraries cover only very limited functionality, so often
these do not fit all requirements. They also cannot be used to easily
parallelize existing serial code. Then the next option is to write parallel
code yourself. 

R has many libraries to support parallelization:

   * Multi-core: `parallel`
   * Multi-core or multi-node: **`future`**, `snow`, `foreach`, `Rmpi`, `pbdMPI`.. 

If unsure, start with `future`. It is one of the newest, most versatile and most easy to use.

:::{admonition} Supercomputer usage
:class: warning

Some of the packages require specific settings in Puhti, see [CSC Docs, r-env, Parallel batch jobs](https://docs.csc.fi/apps/r-env/#parallel-batch-jobs) for details about some of these packages. These might differ from the package's general instructions.

:::

## future library
When using future, two main decisions have to be made for running code in parallel, which we will answer next:

* How to run the parallel code?
* How to make the code parallel?

### How to run the parallel code?
`future`-library supports both serial and parallel computing with different set-ups:

Name |	Description |
--- | --- |
sequential	|	serial, in the current R process
multisession |	multi-core, background R sessions, limited to one node
multicore	|	multi-core, forked R processes, limited to one node, not in Windows nor in RStudio
cluster	|	multi-node, external R sessions

While developing the code, it might be good to start with `multisession` or `multicore` parallelization and then if needed change it to `cluster`. The required changes to code are small when changing the parallelization set-up.

```
# Multi-core, use one of them
plan(multicore)
plan(multisession)

# Multi-node
cl<-getMPIcluster()
plan(cluster, workers = cl)
```

### How to make the code parallel?

The basic R code runs in serial mode, so usually some changes to code are needed to benefit from parallel computing. The changes to code are exactly the same for all parallization set-ups.

The most simple changes could be:

* For-loops:
  * Change to `furrr's future_map()`,
  * If you have several rows of code in your for-loop, make it to a function.
  * If your function needs more than one input variable, see [furrr, Map over multiple inputs simultaneously via futures](https://furrr.futureverse.org/reference/future_map2.html)
* `purrr's map()` -> `furrr's future_map()`
* `*apply()` -> `future.apply` functions

```
# Example of chaning for-loop and purrr's map() to furrr's future_map()
# Just a slow demo function that waits for 5 seconds
slow_function<-function(i) {
  Sys.sleep(5) 
  return(i)
}
# Input data vector. The slow function is run for each element.
input = 1:7

# SERIAL options
# Basic FOR loop
a <- 0
for(i in input) {  
  a[i] <- slow_function(i)
}

# purrr, map
library(purrr) 
a <- map(input, slow_function)

# PARALLEL, furrr future_map
library(furrr)
plan(multisession)

a <- future_map(input, slow_function)
```

If you have used `*apply()`-functions, `future.apply` library provides replacements for these.

```
# Example of chaning lapply() to future.apply's future_lapply()
# Basic lapply
b <- lapply(input, slow_function)

# Parallel future.apply lapply
library(future.apply) 
d <- future_lapply(input, slow_function)
```



:::{admonition} variables with `future`
:class: tip

* `future` exports needed variables and libraries automatically to the parallel processes
* The variables must be serializable. Terra's raster objects are not serializable, see [Terra library's recommendations](https://github.com/rspatial/terra/issues/36)
* Avoid moving variables that refer to large objects from the serial main process to a parallel process. Spatial data analysis often involves significant amounts of data. It is better to read the data inside the parallel function. Give the file name as input, compute area coordinates, etc. 

:::

* [CRAN, future: Unified Parallel and Distributed Processing in R for Everyone](https://cran.r-project.org/web/packages/future/index.html)
* [CRAN, furrr: Apply Mapping Functions in Parallel using Futures](https://cloud.r-project.org/web/packages/furrr/index.html)
* [CRAN, future.apply: Apply Function to Elements in Parallel using Futures](https://cran.r-project.org/web/packages/future.apply/index.html)

### Batch job scripts
#### Multi-core jobs
`multicore` or `multisession` parallization:
```
#SBATCH --nodes=1
#SBATCH --ntasks=4  # Number of tasks. Upper limit depends on number of CPUs per node.

(...)

srun apptainer_wrapper exec Rscript --no-save Calc_contours_future_multicore.R
```

#### Multi-node jobs
`cluster` parallelization:
```
#SBATCH --nodes=2 #For cluster usage to make sense, this should be more than 1.
#SBATCH --ntasks=40  # Number of tasks. Upper limit depends on number of CPUs per node.

(...)

srun apptainer_wrapper exec RMPISNOW --no-save --slave -f Calc_contours_future_cluster.R
```

Further reading:
* [CSC Docs, r-env, Parallel batch jobs](https://docs.csc.fi/apps/r-env/#parallel-batch-jobs)
* [CSC Geocomputing examples for R in Puhti](https://github.com/csc-training/geocomputing/tree/master/R/puhti): `future`, `snow`, `foreach`.
  * [`lidr`-example ](https://github.com/csc-training/geocomputing/tree/master/R/R_LiDAR/R_lidar_course_exercises)
  * [STAC-example](https://github.com/csc-training/geocomputing/tree/master/R/STAC): `gdalcubes`
  * [`raster::predict`-example](https://github.com/csc-training/geocomputing/tree/master/R/raster_predict)
