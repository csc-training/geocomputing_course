# Starting a new project

## Administrative
Get [CSC user account and project](account_project.md) with access Puhti (and Allas).

## Analysis tool
- Choose the [tool for your analysis](software.md).
   - Which tools are able to solve the kind of task you have?
   - Look for tools, that have parallel computing support built in.
   - Fastest vs. ease-of-use
- When you've found the software you want to use, check if it is available at CSC as a [pre-installed application](https://docs.csc.fi/apps/)

   - Also check that all used packages are available on the supercomputer, on Puhti, e.g. within the [geoconda module](https://docs.csc.fi/apps/geoconda) or the [r-env module](https://docs.csc.fi/apps/r-env). 
- If the tool is not provided by CSC, you can [install it yourself](installations.md) or ask <servicedesk@csc.fi> for help.

## Parallelisation
- Start simple and gradually use more complex approaches if needed
   - Try first running interactively (**not** on a login node) to check how the tool performs on actual input data
   - Use the `top` command to get rough estimate of memory use, _etc_.
   - 
## Batch job
   - If it is, check if it has an example batch script 
   - Otherwise, use a [general batch job script template](https://docs.csc.fi/computing/running/example-job-scripts-puhti/)
- How many cores and memory to allocate?

## Data

## Testing
   - Before large runs, it's a good idea to do a smaller trial run
      - Check that results are as expected
      - Check the resource usage after the test run and adjust accordingly
      - If developers provide some test or example data, run it first and make sure results are correct
   - You can use the `--partition=test` to check that your batch job script is correct and everything is interpreted correctly
      - Limits : 15 min, 2 nodes
      - Job turnaround usually very fast even if machine is "full"
      - Can be useful to spot typos, missing files, _etc_. before submitting a job that migh stay waiting in the queue
Keep track of your script versions by using a version control system, like Git(Hub). This also simplifies collaboration and synchronising your scripts on different computers.

:::{admonition} Reminder for  Puhti 
:class: seealso

* Keep scripts in `/projappl/project_200xxxx/`
* Keep data in `/scratch/project_200xxxx/` during processing, Allas for longer term storage
* Keep personal configuration scripts in `/users/cscusername/`
:::

When moving a script from your own computer to Puhti, take care of any hard-coded file dependencies (e.g. `/my/home/dir/file.txt` ). It is not recommended to have hard-coded file paths in your scripts, instead, provide them as command line input to your script or make use of configuration files. No matter where you input your file paths, always make sure that you have the actual data files also available on the supercomputer. 







