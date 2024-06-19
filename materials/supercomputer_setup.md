# Supercomputer setup

![](./images/puhti_overview.png)

Typical physical parts of a supercomputer:
* Login-nodes
* Compute nodes
* Storage
* High-speed networks between these

## Login-nodes
- Login nodes are used for moving data and scripts, script editing and for starting jobs.
- When you login to CSC's supercomputers, you enter one of the login nodes of the computer
- There is only a few login-nodes and they are shared by all users, so they are [not intended for heavy computing.](https://docs.csc.fi/computing/overview/#usage-policy)
 
## Compute-nodes
- The heavy computing should be done on compute-nodes. 
- One compute node has similar components as your laptop: processors, memory and sometimes also local disk space.
- Each node has **memory**, which is used for storing information about a current task.
- Some nodes might have also **local disk space**. 
- Compute nodes have 2 main types: 
  * **CPU-nodes** have only CPU (central processing unit). One CPU-node includes 40 cores in Puhti and 128 in Mahti and LUMI.
  * **GPU-nodes** have both GPU (graphical processing unit) and CPU. GPUs are widely used for deep learning.
  * It depends on the used software, if it benefits from GPU or not. Most GIS-tools can not use GPUs.
  * GPUs are more expensive, so in general the software should run at least 3x faster on GPU, that it would be reasonable to use GPU-nodes.
- While using compute nodes the compute resources have to be defined in advance, and specified if CPU, GPU or local is needed, how many cores or nodes and how much memory.
- Specifics of [Puhti](https://docs.csc.fi/computing/systems-puhti/#nodes), [Mahti](https://docs.csc.fi/computing/systems-mahti/) and [LUMI](https://docs.lumi-supercomputer.eu/hardware/lumic/) compute nodes.

## Storage
- **Disk** refers to all storage that can be accessed like a file system. This is generally storage that can hold data permanently, i.e. data is still there even if the computer has been restarted.
- CSC supercomputers use Lustre as the **parallel distributed file system**


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

:::{admonition} Exploring the login node(s)
:class: tip

Let's start a login shell from the Puhti webinterface. Which login node are you on?

`username@puhti-loginXX`

Close the shell and open another one, which login node are you on now? puhti-loginXX is also called the hostname which you can also retrieve using the `hostname` command.

-> Every time you login, you will get to a random login node. This usually does not matter, but has some side effects in more advanced topics, so it is good to always be aware where you are within the supercomputer.

:::
