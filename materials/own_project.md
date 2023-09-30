# Own project hints

No matter if you are just starting a new project or already have found suitable tools for your task or maybe even written your own tools.

## Making use of HPC resources

Just moving your workflow or script to the supercomputer does not make it run faster. But there is some things that you can do.

## New project hints

When you start a new project and don't yet know how you are going to approach the task, spend a little time to investigate:
- Which tools are able to solve the kind of task you have?
   - Google your task
   - Ask experienced colleagues or <servicedesk@csc.fi> for guidance
   - Once you found some, if it comes with tutorials, do at least one
      - This will likely be the fastest way forward
      - Naturally, read the manual/instructions
         - It is not only how your software is constructed and compiled that affects performance
         - It may also be run in different ways
- Consider:
   - The software that solves your problem fastest might not always be the best
   - Issues like ease-of-use and compute power/memory/disk demands are also highly relevant
- When you've found the software you want to use, check if it is available at CSC as a [pre-installed optimized version](https://docs.csc.fi/apps/)
   - If it is, use the batch script example from _there_
   - Otherwise, use a [general template](https://docs.csc.fi/computing/running/example-job-scripts-puhti/)
   - If it is not, check if you can install it yourself using [Tykky](https://docs.csc.fi/computing/containers/tykky/) or ask <servicedesk@csc.fi> for help.
- Quite often it is useful to start simple and gradually use more complex approaches if needed
   - Try first running interactively (**not** on a login node)
   - Use the `top` command to get rough estimate of memory use, _etc_.
   - If developers provide some test or example data, run it first and make sure results are correct
   - Before large runs, it's a good idea to do a smaller trial run
      - Check that results are as expected
      - Check the resource usage after the test run and adjust accordingly
   - You can use the _test_ queue to check that your batch job script is correct
      - Limits : 15 min, 2 nodes
      - Job turnaround usually very fast even if machine is "full"
      - Can be useful to spot typos, missing files, _etc_. before submitting a job that will idle in the queue
- How many cores to allocate?
   - This depends on many things, so you have to try, see our [instructions about a scaling test](https://docs.csc.fi/support/tutorials/cmdline-handson/#scaling-test-for-an-mpi-parallel-job)
- If you can't find suitable software, consider writing your own code


## Running your own scripts

To keep track of your script versions by using a version control system, like Git(Hub). This also simplifies collaboration and synchronising your scripts on different computers.

:::{admonition} Reminder for  Puhti 
:class: tip,

* Keep scripts in `/projappl/project_200xxxx/your_groupname/`
* Keep data in `/scratch/project_200xxxx/your_groupname/` during processing, Allas for longer term storage
* Keep personal configuration scripts in `/users/your_username/`
* Puhti webinterface / `scp` for data transfer: own computer - Puhti
* `wget` for data transfer:  internet - Puhti

:::

## FAIR research code

!()[./images/fair-principles.svg]
The Turing Way project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: 10.5281/zenodo.3332807.

Following "good enough" practices for FAIR research code will not only help you rerunning your code again when reviewers would like you to "just run XX again" half a year after you moved on to the next project. It will also make your code more reproducible for others:
* Version control
* Clean directory structure
* Reproducible computing environment
   * Use existing modules
   * Know your dependencies 
   * Containers
* Documentation with code, minimum: README
* Modularity -> simplifies reusability and making things parallel
* License
* Share your code, data, results

You can find self-study materials on these topics from the [CodeRefinery project lessons](https://coderefinery.org/lessons/core/).

Eliminate all hardcoded filepaths in your scripts. Instead read from `stdin` or a configuration file instead.

## Optimizing the performance of your own code


You can use profiling tools to find out how much time is spent in different parts of the code
- Docs CSC: [Performance analysis](https://docs.csc.fi/computing/performance/)
- [Profiling on LUMI](https://docs.lumi-supercomputer.eu/development/profiling/strategies/)
When the computing bottlenecks are identified, try to figure out ways to improve the code
- Again, [servicedesk@csc.fi](mailto:servicedesk@csc.fi) is a channel to ask for help
   - [The more concrete the problem is described, the better](https://docs.csc.fi/support/support-howto/)
- If your issue concerns LUMI, contact the [LUMI User Support Team](https://lumi-supercomputer.eu/user-support/need-help/)


:::{admonition} Advanced topic: Developing scripts remotely
:class: tip, dropdown

Instead of developing code on your local machine (e.g. laptop) and moving it to the supercomputer for testing, you can also consider to use a local editor and push edited files directly into the remote system via SSH. This works for example with an IDE like _Visual Studio Code_ or a text editor like _Notepad++_. Follow these [detailed instructions to set them up](https://docs.csc.fi/support/tutorials/remote-dev/). Note that [Visual Studio Code](https://docs.csc.fi/computing/webinterface/vscode/) and [Jupyter Notebooks](https://docs.csc.fi/computing/webinterface/jupyter/) are also available through the Puhti web interface

:::