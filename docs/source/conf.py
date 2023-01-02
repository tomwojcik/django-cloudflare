# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import pathlib
import sys

import toml

ROOT_DIR = pathlib.Path(__file__).parents[2].resolve()
sys.path.append(ROOT_DIR.as_posix())

pyproject = toml.load((ROOT_DIR / "pyproject.toml").as_posix())
poetry = pyproject["tool"]["poetry"]

project = poetry["name"]
copyright = "2022, Tom Wojcik"
author = poetry["authors"][0]
release = poetry["version"]


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.


extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
