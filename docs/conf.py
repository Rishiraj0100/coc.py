# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import pathlib
import sys
import os


root_project = pathlib.Path(__file__).parents[1].resolve()
sys.path.insert(0, root_project.as_posix())
sys.path.append((root_project / "docs").as_posix())
sys.path.append(os.path.abspath('extensions'))

project = 'coc'
copyright = '2022, mathsman5133'
author = 'mathsman5133'
release = '3.6.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "builder",
    "sphinx.ext.duration",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "attributetable",
    "resourcelinks"
]

templates_path = ['_templates']
html_static_path = ['_static']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_js_files = [
  'custom.js',
  'settings.js',
  'copy.js',
  'sidebar.js'
]
