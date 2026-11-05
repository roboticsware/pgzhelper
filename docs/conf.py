import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath('..'))
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

MY_DOC_LANG = os.environ.get('MY_DOC_LANG', 'ko')

# Mock out GUI/display-dependent modules on RTD if needed
class Mock:
    __all__ = []
    def __init__(self, *args, **kw): pass
    def __call__(self, *args, **kw): return Mock()
    def __getattr__(self, name): return Mock()

# Set dummy video driver for headless pygame in doc builds
os.environ['SDL_VIDEODRIVER'] = 'dummy'

# -- Project information -----------------------------------------------------
project = 'pgzhelper'
copyright = '2024, Roboticsware'
author = 'Roboticsware'
release = '1.0.13'

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

if MY_DOC_LANG == 'ko':
    exclude_patterns.extend(['uz/**', 'en/**']) 
    language = 'ko'
elif MY_DOC_LANG == 'uz':
    exclude_patterns.extend(['ko/**', 'en/**'])
    language = 'uz'
else:
    exclude_patterns.extend(['ko/**', 'uz/**'])
    language = 'en'

# -- Options for HTML output -------------------------------------------------
if on_rtd:
    html_theme = "sphinx_rtd_theme"
    html_sidebars = {
        "**": [
            "globaltoc.html",
            "relations.html",
            "searchbox.html",
        ],
    }
else:
    html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]

# -- Autodoc configuration ------------------------------------------------
autodoc_member_order = "bysource"
autodoc_mock_imports = []
