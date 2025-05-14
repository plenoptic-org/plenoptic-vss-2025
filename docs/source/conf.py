# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

project = 'plenoptic satellite event, VSS, 2025'
copyright = '2025, Billy Broderick'
author = 'Billy Broderick'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_nb',
    'sphinx_copybutton',
    'sphinx_togglebutton',
    'sphinx_design',
    'sphinx.ext.intersphinx'
]

intersphinx_mapping = {'plenoptic': ("https://docs.plenoptic.org/docs/branch/main/", None)}

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# max time (in secs) per notebook cell. here, we disable this
nb_execution_timeout = -1
# we have two versions of each notebook, one with explanatory text and one without
# (which ends in `-stripped.md`). we don't need to run both of them
nb_execution_excludepatterns = ["*-users*", "*-presenters*"]
nb_execution_mode = "cache"
nb_execution_raise_on_error = True
# on Jenkins, always want to use kernel called "python3" (otherwise, it's system specific)
if os.environ.get("JENKINS"):
    nb_kernel_rgx_aliases = {".*": "python3"}
else:
    nb_kernel_rgx_aliases = {}
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_favicon = '_static/plenoptic.ico'
html_sourcelink_suffix = ""
myst_enable_extensions = ["colon_fence", "dollarmath"]
html_theme_options = {
    "home_page_in_toc": True,
    "github_url": "https://github.com/plenoptic-org/plenoptic-vss-2025",
    "repository_url": "https://github.com/plenoptic-org/plenoptic-vss-2025",
    "logo": {
        "alt_text": "Home",
        "image_light": "_static/plenoptic.svg",
        "image_dark": "_static/plenoptic_darkmode.svg",
    },
    "use_download_button": True,
    "use_repository_button": True,
    "icon_links": [
        {
            "name": "Workshops home",
            "url": "https://workshops.plenoptic.org/",
            "type": "fontawesome",
            "icon": "fa-solid fa-house",
        },
        {
            "name": "Binder",
            "url": "https://binder.flatironinstitute.org/v2/user/wbroderick/vss2025?filepath=introduction-stripped.ipynb",
            "type": "url",
            "icon": "https://mybinder.org/badge_logo.svg",
        },
    ],
}
