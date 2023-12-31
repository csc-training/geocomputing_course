# Supercomputer setup

![](./images/puhti_overview.png)


A supercomputer has a lot of **nodes** which have the same components as your laptop or desktop computer: CPUs (sometimes also called processors or cores), memory (or RAM), and disk space. However, the supercomputer has some additional/specialized components:

- When you want to execute a program on the supercomputer, it has to be boxed into an abstraction layer called **job**.
- **Login nodes** are used to set up jobs (and to launch them)
- Jobs are run on the **compute nodes**
- A **batch job system (scheduler)** is used to run and manage the jobs
  - On CSC supercomputers, we use Slurm
- CSC supercomputers use Lustre as the **parallel distributed file system**

- When you login to CSC's supercomputers, you enter one of the login nodes of the computer
    - These login nodes are shared by all users and they are [not intended for heavy computing.](https://docs.csc.fi/computing/overview/#usage-policy)

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