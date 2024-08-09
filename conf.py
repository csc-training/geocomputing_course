# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Geocomputing course'
#copyright = '2023, CSC - IT center for Science'
author = 'CSC - IT center for Science. This page is available under the Creative Commons 4.0 Share-Alike License.'
#release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_togglebutton']

myst_enable_extensions = ['colon_fence']

source_suffix = ['.rst','.md']
    

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# setting title in left panel (default is <projectname> documentation <release>)
#html_title = "Geocomputing with Puhti supercomputer course"
# setting upper left logo

html_logo = "materials/images/Geocomputing_on_supercomputer.png"
html_favicon = "materials/images/csc.png"

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files = ["custom.css"]


html_theme_options = {
  "repository_url": "https://github.com/csc-training/geocomputing_course",
  "announcement": 'Psst, remember the <a href="https://csc-training.github.io/geocomputing_course/materials/cheatsheet.html">cheatsheet</a>!',
  "use_repository_button": True,
  "show_toc_level": 3,
}




