# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'plenoptic tutorial, CSHL Vision Course, 2024'
copyright = '2024, Billy Broderick'
author = 'Billy Broderick'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_nb',
    'sphinx_copybutton',
    'sphinx_togglebutton',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# max time (in secs) per notebook cell. here, we disable this
nb_execution_timeout = -1
# we have two versions of each notebook, one with explanatory text and one without
# (which ends in `-stripped.md`). we don't need to run both of them
nb_execution_excludepatterns = ['*stripped*']
nb_execution_raise_on_error = True
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_favicon = '_static/plenoptic.ico'
html_sourcelink_suffix = ""
myst_enable_extensions = ["colon_fence"]
html_theme_options = {
    "home_page_in_toc": True,
    "github_url": "https://github.com/plenoptic-org/plenoptic-cshl-vision-2024",
    "repository_url": "https://github.com/plenoptic-org/plenoptic-cshl-vision-2024",
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
            "url": "https://binder.flatironinstitute.org/v2/user/wbroderick/cshl2024?filepath=introduction-stripped.ipynb",
            "type": "url",
            "icon": "https://mybinder.org/badge_logo.svg",
        },
    ],
}
