# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Geocomputing course'
copyright = '2023, CSC - IT center for Science'
author = 'CSC - IT center for Science'
release = '0.1'

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
html_title = "CSC Geocomputing course"

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_theme_options = {
  "repository_url": "https://github.com/csc-training/geocomputing_course",
  "announcement": 'Psst, remember the <a href="https://csc-training.github.io/geocomputing_course/materials/cheatsheet.html">cheatsheet</a>!',
  "use_repository_button": True,
}




