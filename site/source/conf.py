import datetime

# -- Project information -----------------------------------------------------
# -- Citations order and reversal --------------------------------------------
 
# spent too much time on this, but pretty cool in the end
# started from issue:
# https://github.com/mcmtroffaes/sphinxcontrib-bibtex/issues/272#issuecomment-1932497783
import pybtex.plugin
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.labels import BaseLabelStyle
from pybtex.style.sorting.author_year_title import SortingStyle

class ChronoSortingStyle(SortingStyle):
    def sorting_key(self, entry):
        year_key = self.year_key(entry)
        return (year_key)
    def year_key(self, entry):
        return entry.fields.get('year', '')
    # need to check if overriding the default sort function is ok
    def sort(self, entries):
        return sorted(entries, key=self.year_key, reverse=True)

pybtex.plugin.register_plugin("pybtex.style.sorting", "year", ChronoSortingStyle)


class ReverseLabelStyle(BaseLabelStyle):
    def format_labels(self, sorted_entries):
        for i, entry in enumerate(sorted_entries):
            yield str(len(sorted_entries) - i)

class ChronoSortedReverseLabelStyle(UnsrtStyle):
    default_label_style = ReverseLabelStyle
    default_sorting_style = 'year'

pybtex.plugin.register_plugin("pybtex.style.formatting", "chronosortedreverselabelstyle", ChronoSortedReverseLabelStyle)



# -- Project information -----------------------------------------------------
year = datetime.date.today().year
month = datetime.date.today().month
project = 'Carlos A. R.'
copyright = '{:d}'.format(year)
author = 'Carlos A. Ruvalcaba'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        "ablog",
        "myst_nb",
        "sphinxcontrib.bibtex",
        "sphinxcontrib.youtube",
        "sphinx_togglebutton",
        "sphinx_tabs.tabs",
        "sphinx_design",
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

bibtex_bibfiles = [
    "research/references/conf.bib",
    "research/references/papers.bib"]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    # "html_admonition",
    # "html_image",
    "colon_fence",
    # "smartquotes",
    # "replacements",
    # "linkify",
    # "substitution",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_title = "Carlos-AR"
html_copy_source = True
html_favicon = "_static/logo-dark.svg"
html_last_updated_fmt = ""

html_context = {
    "last_updated": str(datetime.date.today()),
}

html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]

# Book theme options
html_theme_options = {
    "show_prev_next": False,
    "show_navbar_depth": 1,
    "show_toc_level": 2,
    "home_page_in_toc": True,
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/carlos-ar",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
   ],
   "logo": {
        "text": "Carlos A. Ruvalcaba",
        "image_light": "_static/logo-light.svg",
        "image_dark": "_static/logo-dark.svg",
   }
}