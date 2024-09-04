# Parallel R

R has many libraries to support parallelization:

   * Multi-core: `parallel`
   * Multi-core or multi-node: **`future`**, `snow`, `foreach`, `Rmpi`, `pbdMPI`.. 

If unsure, start with future, it is one of the newest, most versatile and easy to use. 

:::{admonition} Define number of cores explicitly
:class: warning

Some of the packages require specific settings in Puhti, see [CSC Docs, r-env, Parallel batch jobs](https://docs.csc.fi/apps/r-env/#parallel-batch-jobs) for details. These might differ from package's general instructions.

:::

## future-library


### Parallelization options
`future`-library supports both serial and parallel computing with different set-ups:

Name |	Description |
--- | --- |
synchronous, non-parallel: |	
sequential	|	sequentially in the current R process
asynchronous, parallel:	|	
multisession	|	background R sessions (on current machine), limited to one node
multicore*	|	forked R processes (on current machine), limited to one node
cluster	|	external R sessions on current, local, and/or remote machines, multi-node possible

* not in Windows nor in RStudio

While developing the code, it might be good to start with  multisession or multicore parallelization and then if needed to change to cluster. The required changes to code are small, when changing the parallelization set-up.

```
# Just a demo slow function, that waits for 1 second
slow_function<-function(i) {
  Sys.sleep(1) 
  return(i)
}
# Input data vector, the slow function is run for each element.
input = 1:7

# SERIAL options
# Basic FOR loop
a <- 0
for(i in input) {  
  a[i] <- slow_function(i)
}

# Basic lapply
b <- lapply(input, slow_function)

# purrr, map
library(purrr) 
c <- map(input, slow_function)

# PARALLEL options with future
library(future.apply) 
plan(multisession)
#options(future.availableCores.methods = "Slurm")
future::availableCores()

# Parallel lapply
d <- future_lapply(input, slow_function)

# Parallel map
library(furrr) 
e <- future_map(input, slow_function)
```

* [CRAN, future: Unified Parallel and Distributed Processing in R for Everyone](https://cran.r-project.org/web/packages/future/index.html)
