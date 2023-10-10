# Partitions

Partitions are logical sets of nodes. Resource limitations for a job are defined by the partition (or queue) the job is submitted to. The limitations affect the maximum run time, the amount of memory, and the number of available CPU cores (which are called CPUs in Slurm). In addition, partitions may also define default resources that are automatically allocated for jobs if nothing has been specified.

Jobs should be submitted to the partition that best matches the required resources. That way, as few resources as possible are blocked and another user with a higher demand in RAM can run a job earlier. Of course, other considerations may also influence the choice of a partition. 

- [CSC Docs: Available batch job partitions](https://docs.csc.fi/computing/running/batch-job-partitions/) 
- In order to use the resources in an efficient way, it is important to estimate the request as accurately as possible
- By avoiding an excessive "just-in-case" request, the job will start earlier

:::{admonition} Which partition to choose?
:class: tip

1. Through trial and error Anna has determined that her image processing process takes about 60 min, 16 GB of memory on a single CPU. 
2. Kalika has profiled her code, and determined that it can run efficiently on 20 cores with 12 GB of memory each. The complete process should be done within 4 days.
3. Ben wants to visualize a 80 GB file in QGIS.
4. Neha has written and run some Python code on her own machine. She now wants to move to Puhti and, before running her full pipeline, test that her code executes correctly with a minimal dataset.
5. Josh wants to run 4 memory heavy tasks (100GB) in parallel. Each job takes about 30 minutes to execute.

:::{admonition} Solution
:class: dropdown

1. Based on the requirements, she has a few choices,except `test`, `gpu` and `gputest`. She does not need interactive access to her process, so in order to not block any unnecessary resources, Anna chooses `small` partition.
2. Based on the requirements, Kalika needs to choose `longrun` or adapt her code to get under 3 days runtime (which she might want to do in order to avoid exessively long queueing times).
3. For the webinterface, only `test`, `small` or `interactive` can be used. According to the resource needs (> 80GB of memory), he needs to use `small` partition. 
4. This is a very good idea and should always be done first. Neha can get the best and fast experience using `test` partition. This means to keep the runtime under 15 min and the memory needs below 190 GiB at a maximum of 80 tasks.
5. 400GB memory in total is more than most partitions can take. If this is the least memory possible for the jobs, it has to be run on `hugemem`.
:::
:::
