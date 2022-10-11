project = "Hello Sphinx"
copyright= "2022, Alexander Mann-Wahrenberg (basejumpa)"
release = "0.1.0"

html_theme = "sphinx_material"

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# Hide hyper link which leeds to the source of page displayed
html_show_sourcelink = True

html_theme_options = {
    'nav_title'    : f"Write like an Egyptian",
    'color_primary': 'teal',
    'color_accent' : 'yellow',

    'globaltoc_depth'        : 3,
    'globaltoc_collapse'     : 'true',
    'globaltoc_includehidden': 'true',
}
