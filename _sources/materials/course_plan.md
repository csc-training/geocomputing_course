# Geocomputing course plan

* CSC 
* CSC services
* CSC support

* Start with GUI via webinterface, no in depth info on resources, start QGIS or SNAP
    * talk about usecases
* basics of supercomputing, mainly resources
    * resource knowledge
    * fair share
* supercomputer setup
    * Puhti overview
    * login vs compute node
* compute node: interactive usage of some gdal/pdal/ogr command (show how to get it from QGIS)
    * running into limits of interactiveness
* the sbatch script
    * resource + command (same as above just together in one)
    * many commands in script -> python/R/bash script
* calling it "serial"
* now parallel; harnessing the power
    * external vs internal
    * external
        * script as usual
        * GNU parallel
        * array job
    * internal
        * depends on tool, does it have multi cpu option (multi, cores, n_cores or similar?)
        * R/Python: use dedicated packages 
* own project hints
    * script and tools
        * from script that runs on your computer to hpc enabled 
        * available tools
    * data
        * storage (directories and Allas)
        * transfer
        * strategies




:::{admonition} Painter analogy
:class: tip

Suppose that we want to paint the four walls in a room. This is our problem. We can divide our problem in 4 different tasks: paint each of the walls. In principle, our 4 tasks are independent from each other in the sense that we don’t need to finish one to start another. However, this does not mean that the tasks can be executed simultaneously or in parallel. It all depends on the amount of resources that we have for the tasks.
Concurrent vs. parallel execution

If there is only one painter, they could work for a while in one wall, then start painting another one, then work for a little bit in the third one, and so on. The tasks are being executed concurrently but not in parallel. Only one task is being performed at a time. If we have 2 or more painters for the job, then the tasks can be performed in parallel.

In our analogy, the painters represent CPU cores in your computer. The number of CPU cores available determines the maximum number of tasks that can be performed in parallel. The number of concurrent tasks that can be started at the same time, however, is unlimited.
Synchronous vs. asynchronous execution

Now imagine that all workers have to obtain their paint form a central dispenser located at the middle of the room. If each worker is using a different colour, then they can work asynchronously. However, if they use the same colour, and two of them run out of paint at the same time, then they have to synchronise to use the dispenser — one should wait while the other is being serviced.

In our analogy, the paint dispenser represents access to the memory in your computer. Depending on how a program is written, access to data in memory can be synchronous or asynchronous.
Distributed vs. shared memory

Finally, imagine that we have 4 paint dispensers, one for each worker. In this scenario, each worker can complete its task totally on their own. They don’t even have to be in the same room, they could be painting walls of different rooms in the house, on different houses in the city, and different cities in the country. In many cases, however, we need a communication system in place. Suppose that worker A, needs a colour that is only available in the dispenser of worker B — worker A should request the paint to worker B, and worker B should respond by sending the required colour.

Think of the memory distributed on each node/computer of a cluster as the different dispensers for your workers. A fine-grained parallel program needs lots of communication/synchronisation between tasks, in contrast with a course-grained one that barely communicates at all. An embarrassingly/massively parallel problem is one where all tasks can be executed completely independent from each other (no communications required).
Processes vs. threads

Our example painters have two arms, and could potentially paint with both arms at the same time. Technically, the work being done by each arm is the work of a single painter.

In this example, each painter would be a process (an individual instance of a program). The painters’ arms represent a “thread” of a program. Threads are separate points of execution within a single program, and can be executed either synchronously or asynchronously.

From [HPC Carpentry](http://www.hpc-carpentry.org/hpc-python/06-parallel).
:::



