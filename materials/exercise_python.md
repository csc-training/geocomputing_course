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

* Access to Puhti webinterface
* Some experience with Python and GIS Python tools

:::


[Python exercise materials in Geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/puhti)

Check out at least the sections about [serial jobs](https://github.com/csc-training/geocomputing/blob/master/python/puhti/README.md#serial-job) and [parallelizing within Python](https://github.com/csc-training/geocomputing/blob/master/python/puhti/README.md#internal-parallelization).

Additional example to check out from Jupyter application in the webinterface: [https://github.com/csc-training/geocomputing/blob/dask_stac_example/python/STAC/stac_dask_download_data_example.ipynb]

:::{admonition} Key points
:class: important

* GNU parallel for embarassingly parallel tasks, without changing the Python code
* `dask.delayed` or `multiprocessing` can be used to parallelize for loop

:::
