# Partitions

Partitions are logical collections of nodes that define limitations that restrict the resources that can be requested for a job submitted to that partition. The limitations affect the maximum run time, the amount of memory, and the number of available CPU cores (which are called CPUs in Slurm). In addition, partitions may also define default resources that are automatically allocated for jobs if nothing has been specified.

Jobs should be submitted to the partition that best matches the required resources. That way, as few resources as possible are blocked and another user with a higher demand in RAM can run a job earlier. Of course, other considerations may also influence the choice of a partition. 

- [The available batch job partitions](https://docs.csc.fi/computing/running/batch-job-partitions/) are listed in docs.csc.fi
- In order to use the resources in an efficient way, it is important to estimate the request as accurately as possible
- By avoiding an excessive "just-in-case" request, the job will start earlier

:::{admonition} Which partition to choose?
:class: tip

TODO: check solutions and more usecases

1. Through trial and error Anna has determined that her image processing process takes about 60 min, 16 GB of memory on a single CPU. 
2. Kalika has profiled her code, and determined that it can run efficiently on 20 cores with 12 GB of memory each. The complete process should be done within 4 days.
3. Ben wants to visualize a 80 GB file in QGIS.
4. Neha 

:::{admonition} Solution
:class: tip, dropdown

1. Based on the requirements, any partition would work for Anna, except `test`. She does not need interactive access to her process, so in order to not block any unnecessary resources, Anna chooses `small` partition.
2. Based on the requirements, Kalika need to choose `hugemem_longrun` or adapt her code to get under 3 days runtime.
3. For the webinterface, only `test`, `small` or `interactive` can be used. According to the resource needs (> 80GB of memory), he needs to use `small` partition. 
4. `test`
:::
:::