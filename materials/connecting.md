# Connecting to supercomputer
## Web interface

* **For lightweight entry to supercomputers**
* In web interface the resources are limited -> suitable for **developing code and small analysis tasks**
* Bigger analysis tasks should be run via batch jobs
    * Web interface can be used for starting batch jobs 
* [Puhti web interface](https://puhti.csc.fi)
* [LUMI web interface](https://www.lumi.csc.fi,)
* [CSC Docs: web interface](https://docs.csc.fi/computing/webinterface/)

## Tools in web interface:
- View, download and upload files
- **Terminal to login-node**
- **Terminal to compute-node**
- Info: running jobs, disk usage, project status and supercomputer's general status
- Launch interactive apps and open them directly from the browser:
    - Desktop with apps: **QGIS**, GRASS, SagaGIS, SNAP, Zonation etc
    - **Jupyter**
    - TensorBoard, MLFlow
    - **Visual Studio Code**
    - **RStudio**
    - MATLAB

 ![Puhti web interface](images/ood_main.png)

## Connecting to the supercomputer via SSH

During the course we will access the supercomputer via the web interface in
order to not overwhelm you with setups before the course. However, this way
may not always be the most convenient. You can also connect to the
supercomputer via SSH.

:::{admonition} Connecting with SSH clients
:class: seealso, dropdown

- SSH clients give command-line access to a supercomputer or any other Linux server.
- Basic SSH connection will not allow displaying remote graphics, but it is possible to set up with extra settings.
- SSH clients:
   - Mac and Linux have Terminal for SSH connections.
   - In Windows:
      - `Command Prompt` or `Powershell` are always avaialbe and can be used for basic connections.
      - Special tools like [PuTTY](https://www.putty.org/) or [MobaXterm](https://mobaxterm.mobatek.net/) provide more options, inc possibility to save settings, but need installation.
- To avoid typing your password every time again and to make your connection more secure, you can [set up SSH-keys](https://docs.csc.fi/computing/connecting/ssh-keys/).
- [CSC Docs: Connecting to CSC supercomputers](https://docs.csc.fi/computing/connecting/)
- [LUMI Docs: Get started](https://docs.lumi-supercomputer.eu/firststeps/).

:::

## Developing scripts remotely

Instead of developing code on your local machine and moving it as files to the
supercomputer for testing, you can also consider to use a local editor and
push edited files directly to the supercomputer.  This works for example
with **Visual Studio Code** or **Notepad++**. Note that [Visual Studio
Code](https://docs.csc.fi/computing/webinterface/vscode/) is also available
through the Puhti web interface.

- [CSC Docs: Developing scripts remotely](https://docs.csc.fi/support/tutorials/remote-dev/)
