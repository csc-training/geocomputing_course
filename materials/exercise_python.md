# Exercise: Python

:::{admonition} Timing
:class: note

75 min

:::

:::{admonition} Goals
:class: note

* 

:::

Shared memory programming

Shared memory programming means using the resources on a single computer, and having multiple threads or processes work together on a single copy of a dataset in memory. This is the most common form of parallel programming and is relatively easy to do. -> multiprocessing.

Python does not thread very well. Specifically, Python has a very nasty drawback known as a Global Interpreter Lock (GIL). The GIL ensures that only one compute thread can run at a time. This makes multithreaded processing very difficult. Instead, the best way to go about doing things is to use multiple independent processes to perform the computations. This method skips the GIL, as each individual process has it’s own GIL that does not block the others. This is typically done using the multiprocessing module.

Before we start, we will need the number of CPU cores in our computer. To get the number of cores in our computer, we can use the psutil module. We are using psutil instead of multiprocessing because psutil counts cores instead of threads. Long story short, cores are the actual computation units, threads allow additional multitasking using the cores you have. For heavy compute jobs, you are generally interested in cores.

import psutil
# logical=True counts threads, but we are interested in cores
psutil.cpu_count(logical=False)

The multiprocessing module has a major limitation: it only accepts certain functions, and in certain situations. For instance any class methods, lambdas, or functions defined in __main__ wont’ work. This is due to the way Python “pickles” (read: serialises) data and sends it to the worker processes. “Pickling” simply can’t handle a lot of different types of Python objects.

Fortunately, there is a fork of the multiprocessing module called multiprocess that works just fine (pip install --user multiprocess). multiprocess uses dill instead of pickle to serialise Python objects (read: send your data and functions to the Python workers), and does not suffer the same issues. Usage is identical.

Parallel workers (with their own copy of everything) are created, data are sent to these workers, and then results are combined back together again. There is also an optional chunksize argument (for pool.map()) that lets you control how big each chunk of data is before it’s sent off to each worker. A larger chunk size means that less time is spent shuttling data to and from workers, and will be more useful if you have a large number of very fast computations to perform. When each iteration takes a very long time to run, you will want to use a smaller chunk size.

From [HPC Carpentry](http://www.hpc-carpentry.org/hpc-python/06-parallel).

[Python exercise materials in Geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/puhti)


