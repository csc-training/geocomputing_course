# Exercise: R

## R in supercomputers
* `r-env` is the only R module in Roihu. It has ~1300 packages for all fields of science.
* LUMI has only [EasyBuild recipe for R](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/r/R/)
* [CSC Docs: r-env](https://docs.csc.fi/apps/r-env/)
* [CSC Docs: R for GIS](https://docs.csc.fi/apps/r-env-for-gis/)

:::{admonition} Timing
:class: note

45 min

:::

:::{admonition} Goals
:class: note

* Get to know the `r-env` R environment on Roihu
* Running R code interactively and as a batch job
* Try out different ways of parallelizing R code


:::

:::{admonition} Prerequisites
:class: important

* [CSC user account](https://docs.csc.fi/accounts/how-to-create-new-user-account/) and [project](https://docs.csc.fi/accounts/how-to-create-new-project/) with [access to Roihu](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/)
* Some experience with R spatial
* Basic Linux skills

:::


  
[R exercise materials in Geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/R/roihu)

* Interactive working
* Simple batch job
* Parallel job with `future` library
* Additionally, you can check out some of the other R examples in [CSC geocomputing repository](https://github.com/csc-training/geocomputing/blob/master/R).

:::{admonition} Key points
:class: important

* Roihu web interface enables working with RStudio interactively
* `future` can be used for parallelization

:::
