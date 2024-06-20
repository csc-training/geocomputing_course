# CSC Supercomputers

![](./images/lumi2.jpg)

Name | CPUs | GPUs | Pre-installed GIS tools | Finnish spatial data locally | Scope |
--- | --- | --- | --- | --- | --- |
**Puhti** | 28 000 | 240 Nvidia V100 | **20** | **Yes** | Finland |
**Mahti** | 90 000 | 96 Nvidia A100 | 1 | No | Finland |
**LUMI** | **100 000** | **10 000** AMD MI250X | 5 | No | EU |

Puhti:
* From interactive single core to medium scale parallel analysis
* **The first option to consider for Finnish academic projects**
* [CSC Docs: Technical details about Puhti](https://docs.csc.fi/computing/systems-puhti/)

Mahti:
* For medium and large scale parallel analysis
* Projects move from Puhti to Mahti, once Puhti recources become limiting.
* [CSC Docs: Technical details about Mahti](https://docs.csc.fi/computing/systems-mahti/)

LUMI:
* Owned by LUMI consortium: 11 countries + EU
* For very large scale analysis
* Mainly GPU-machine -> for deep learning projects
* **For companies and international projects**
* [LUMI Docs: Hardware overview](https://docs.lumi-supercomputer.eu/hardware/)


## Puhti compared to other options

|  | Puhti supercomputer| cPouta virtual machine| my laptop |
|---|---| ---|---|
|Max per job: CPU | **4000** | 48 | 4 |
|Max per job: memory, Gb | **1500** | 240 | 18 |
|Max per job: GPU | **80** | 4 | 1 |
|Pre-installed GIS tools | **Yes** | No | No |
|Main Finnish datasets  | **Yes** | No | No |
|Admin rights | No | **Yes** | Yes |
