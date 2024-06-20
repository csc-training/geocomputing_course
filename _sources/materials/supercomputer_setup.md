# Supercomputer setup

![](./images/HPC_basic.png)

Typical physical parts of a supercomputer:
* Login-nodes
* Compute-nodes
* Storage
* High-speed networks between these

## Login-nodes
- Login nodes are used for moving data and scripts, script editing and for starting jobs.
- When you login to CSC's supercomputers, you enter one of the login nodes of the computer
- There is only a few login-nodes and they are shared by all users, so they are [not intended for heavy computing.](https://docs.csc.fi/computing/overview/#usage-policy)

![](./images/HPC_nodes.png)
 
## Compute-nodes
- The heavy computing should be done on compute-nodes. 
- One compute node has similar components as your laptop: processors, memory and sometimes also local disk space.
- Each node has **memory**, which is used for storing information about a current task.
- Some nodes might have also **local disk space**. 
- Compute nodes have 2 main types: 
  * **CPU-nodes** have only CPUs (central processing unit).
  * **GPU-nodes** have both GPUs (graphical processing unit) and CPUs. GPUs are widely used for deep learning.
  * Each CPU-node includes **cores**, which are the basic computing. There are 40 cores in Puhti and 128 in Mahti and LUMI CPU-nodes.
  * It depends on the used software, if it benefits from GPU or not. Most GIS-tools can not use GPUs.
  * GPUs are more expensive, so in general the software should run at least 3x faster on GPU, that it would be reasonable to use GPU-nodes.
- While using compute nodes the compute resources have to be defined in advance, and specified if CPU, GPU or local is needed, how many cores or nodes and how much memory.
- Specifics of [Puhti](https://docs.csc.fi/computing/systems-puhti/#nodes), [Mahti](https://docs.csc.fi/computing/systems-mahti/) and [LUMI](https://docs.lumi-supercomputer.eu/hardware/lumic/) compute nodes.


## Storage
![](./images/HPC_disks.png)

- **Disk** refers to all storage that can be accessed like a file system. This is generally storage that can hold data permanently, i.e. data is still there even if the computer has been restarted.
- CSC supercomputers use Lustre as the **parallel distributed file system**

### Puhti disk areas

| Name     |Access   |Path                 |Cleaning      |Capacity|Number of files| Use |
|------------|--------|--------------------|---------------------|--------------|----------------|----------------|
|**[home](https://docs.csc.fi/computing/disk/#home-directory)**    |Personal|`/users/cscusername` |No            |10 GiB              |100 000 files  | personal settings and files |
|**[projappl](https://docs.csc.fi/computing/disk/#projappl-directory)**|Project |`/projappl/project_200xxxx`|No            |50 GiB              |100 000 files  | installation files |
|**[scratch](https://docs.csc.fi/computing/disk/#scratch-directory)** |Project |`/scratch/project_200xxxx` |**180 days**      |**1 TiB**              |1 000 000 files  | main working area |

* `scratch` space can be extended, but it would use billing units then.

#### Temporary fast disks 

- [CSC Docs: Login node local tmp](https://docs.csc.fi/computing/disk/#login-nodes)  `$TMPDIR` for compiling, cleaned frequently.
	
- [CSC Docs: NVMe](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage) - `$LOCAL_SCRATCH` in batch jobs, 
    - NVMe is accessible only during your job allocation, inc. interactive job
	- You must copy data in and out during your batch job
    - If your job reads or writes a lot of small files, using this can give 10x performance boost

:::{admonition} Avoid unneccesary reading and writing
:class: seealso
Avoid unnecessary reads and writes of data to improve I/O performance
- Read and write in big chunks and avoid reading/writing lots of small files
   - If unavoidable, use [fast local NVMe disk](https://docs.csc.fi/computing/disk/#compute-nodes-with-local-ssd-nvme-disks), not Lustre (i.e. `/scratch`)
:::

### LUMI disk areas
- [LUMI docs: storage](https://docs.lumi-supercomputer.eu/storage/)
- LUMI has similar main disks, but different temporary disks.

:::{admonition} Login node etiquette
:class: tip
Which of the following tasks would suit to run on the login node?


1. `python join_dataframes.py`
2. `make`
3. `create_directories.sh`
4. `qgis`
5. `tar -xzf mytool.tar.gz`

:::{admonition} Solution
:class: dropdown


 Options #3 creating directories (mkdir), and #5 unpacking software (tar) are common and acceptable tasks for the login node. Option #2 Building software (make) can be done on the login node, but ideally one would use a compute node with local scratch to avoid stressing the filesystem in the process.
 
 >Note that script names do not always reflect their contents: before launching #3, please check what is inside create_directories.sh and make sure it does what the name suggests.

Running resource-intensive applications on the login node are forbidden. Unless you are sure it will not affect other users, do not run jobs like #1 (python) or #4 (a software). You will anyway want more resources for these, than the login node can provide.

:::
:::
