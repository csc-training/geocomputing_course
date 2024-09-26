# Exercise: Python

:::{admonition} Timing
:class: note

75 min

:::

:::{admonition} Goals
:class: note

* Get to know geoconda Python environment on Puhti
* Try out different ways of parallelizing Python code
* Understand when to go for internal vs external parallelization

:::

:::{admonition} Prerequisites
:class: important

* Access to Puhti web interface
* Some experience with Python and GIS Python tools

:::


[Python exercise materials in Geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/puhti)

Check out at least the sections about [serial jobs](https://github.com/csc-training/geocomputing/blob/master/python/puhti/README.md#serial-job) and [parallelizing within Python](https://github.com/csc-training/geocomputing/blob/master/python/puhti/README.md#internal-parallelization).

Additional, you can also check out some of the other Python examples in [CSC geocomputing repository](https://github.com/csc-training/geocomputing/blob/master/python).

:::{admonition} Key points
:class: important

* GNU parallel for embarassingly parallel tasks, without changing the Python code
* `dask.delayed` or `multiprocessing` can be used to parallelize for-loops

:::
