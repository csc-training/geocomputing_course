# Materials for CSC Geocomputing course

> Course materials for Geocomputing course 2023

## View rendered version

Materials are build to [Geocomputing course main page](https://csc-training.github.io/geocomputing_course).

## Contributing

### Styling

See [MyST-parser](https://myst-parser.readthedocs.io/en/latest/index.html) and [sphinx book theme guide](https://sphinx-book-theme.readthedocs.io).

#### Images 

```{figure} images/imagename.png
:alt: Alt text
:width: 700px
:align: center
Caption here
```

#### Admonition usage

* Keypoints: important (yellow)
* Objectives/Timing/etc: note (blue)
* Note!: caution (orange)
* info: seealso (green)
* Tasks/Questions/Exercises: tip (green)

### Local build of materials

Materials are build to [Geocomputing course main page](https://csc-training.github.io/geocomputing_course) upon push to main (via PR).

Local testing can be done by installing [Sphinx](https://www.sphinx-doc.org/en/master/) and some extensions with for example pip:

`pip install sphinx sphinx-book-theme myst_parser sphinx-togglebutton colon-fence`

Then clone this repository and run 

`sphinx-build . _build` 

from within the repository directory.

> Note that `_build` directory should not be part of the github repository.

### Contributing changes

Please send a pull request, explainaing your changes. The changes should be refelcted in commit messages. If not, please provide a list of "bigger changes" (i.e. no need to report each sentence structure,typo change) and their motivation. For additional lessons it might be good to create an issue first. Please also add yourself to the authors as part of your pull request. 

## Contributors

These lesson materials are based on previous geocomputing materials by Kylli Ek, Johannes Hiekkasaari and Eduardo Gonzales. 

Some lessons are partly based on other CSC course materials by Maria Lehtivaara, Rasmus Kronberg, Ari-Matti Saren, Atte Sillanpää, Kimmo Mattila, Laxmana Yetukuri, Maria Dimitrova, Xavier Anthony Raj,  Jesse Harrison, Sami Ilvonen.

New edits and materials by Samantha Wittke, Kylli Ek. Review by Eetu Huusko, Rasmus Kronberg, Antoni Golos, Katri Tegel, Juha Lento.

## Other resources and further reading

[Aalto Scientific Computing Triton tutorial and HPC kickstart materials](https://scicomp.aalto.fi)
[Sigma2 HPC Onboarding materials](https://documentation.sigma2.no/training/events/2023-10-hpc-on-boarding.html)

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). 

## Citation

Citation info coming soon; with first release.

## Acknowledgement

This work is supported by CSC - IT center for Science and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513).

