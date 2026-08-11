# Installing own tools

## Adding some packages to existing modules

* Generally the easiest option.
* [CSC Docs: Installing **Python** packages to existing modules](https://docs.csc.fi/support/tutorials/python-usage-guide/#installing-python-packages-to-existing-modules)
  * python-geo, tensorflow, pytorch, python-data etc.
  * The added package must be available via `pip`.
* [CSC Docs: **R** package installations](https://docs.csc.fi/apps/r-env/#r-package-installations) 
* [CSC Docs: **Julia**, adding packages to an environment](https://docs.csc.fi/apps/julia/#adding-packages-to-an-environment)

## Tykky

* The easiest way to create a custom installation is with Tykky
* Tykky has 3 options, new installation based on:
  * `conda` .yml file
  * `pip` requirement file
  * Existing Docker image
* [CSC Docs: Tykky](https://docs.csc.fi/computing/containers/tykky)
* [LUMI Docs: container-wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/) is the same as Tykky

:::{admonition} Do not use "normal" conda installations
:class: important

* "Normal" conda installations create a lot of files - up to hundreds of thousands
* Supercomputers do not like too many files
* Use Tykky to create containerized conda installation

:::

## Other
* [CSC Docs: Installing software](https://docs.csc.fi/computing/installing/), inc installing from source, Spack
* [LUMI Docs: Installing additional software](https://docs.lumi-supercomputer.eu/software/#installing-additional-software), inc installing from source, EasyBuild
* Generally useful? -> ask from servicedesk to install
