# Connecting to supercomputer
## Web interface

* [Roihu web interface](https://roihu.csc.fi)
* [LUMI web interface](https://www.lumi.csc.fi)
* [CSC Docs: web interface](https://docs.csc.fi/computing/webinterface/)

## Tools in web interface:
- View, download and upload files, only for small amounts of data
- **Terminal to login node** for starting batch jobs and moving data
- **Terminal to compute node** for heavier computing
- Info: running jobs, disk usage, project status and supercomputer's general status
- Interactive apps:
    - Desktop with apps: **QGIS**, CloudCompare, GRASS, SagaGIS, SNAP, Zonation etc
    - **Jupyter**
    - Marimo
    - TensorBoard, MLFlow
    - **Visual Studio Code**
    - **RStudio**
    - MATLAB
    - Interactive apps have limited resources -> suitable for **developing code and small analysis tasks**
    - Run bigger analysis tasks via batch jobs

 ![Roihu web interface](images/ood_main.png)

## Connecting to the supercomputer via SSH

During the course we will access the supercomputer via the web interface in
order to not overwhelm you with setups before the course. However, this way
may not always be the most convenient. You can also connect to the
supercomputer via SSH.

:::{admonition} Connecting with SSH clients
:class: seealso, dropdown

- SSH clients give command-line access to a supercomputer or any other Linux server.
- SSH clients:
   - Mac and Linux have Terminal for SSH connections.
   - In Windows:
      - `Command Prompt` or `Powershell` are always available and can be used for basic connections.
      - Special tools like [PuTTY](https://www.putty.org/) or [MobaXterm](https://mobaxterm.mobatek.net/) provide more options, inc possibility to save settings, but need installation.
- Requires setting up [SSH-keys](https://docs.csc.fi/computing/connecting/ssh-keys/) and for Roihu downloading daily SSH certifacate.
- [CSC Docs: Connecting to CSC supercomputers](https://docs.csc.fi/computing/connecting/)
- [LUMI Docs: Get started](https://docs.lumi-supercomputer.eu/firststeps/).

:::
