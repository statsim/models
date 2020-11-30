#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican_jupyter import markup as nb_markup

#AUTHOR = u'Anton Zemlyansky'
SITENAME = u'StatSim Models'
DESCRIPTION = 'List of deterministic and probabilistic models you can run and fit in StatSim'

SITEURL = ''
BASEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs'
STATIC_PATHS = (['images'])

TIMEZONE = 'Europe/Paris'
LOCALE = 'en_US.UTF-8'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
# LINKS = (
#   ('StatSim', 'https://statsim.com/'),
#   ('Analyze.li', 'https://analyze.li')
# )

# Social widget
SOCIAL = (
 ('Twitter', 'https://twitter.com/statsimcom'),
 ('Facebook', 'https://www.facebook.com/statsim'),
 ('Github', 'https://github.com/statsim')
)

PLUGIN_PATHS = ['/home/anton/tools/pelican-plugins']

MARKUP = ("md", "ipynb")
PLUGINS = ['i18n_subsites', nb_markup]

I18N_SUBSITES = {
  'ru': {
    'SITENAME': 'Модели StatSim'
  }
}

IGNORE_FILES = ['.ipynb_checkpoints', '*-checkpoint.ipynb', '*.js', '*.py', '__pycache__', '*.pyc']

THEME = 'theme'
DISPLAY_FOOTER = False
DISPLAY_SUMMARY = True
ARTICLE_ORDER_BY = 'reversed-date'
DEFAULT_PAGINATION = False

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'category/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'author/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tag/index.html'

DELETE_OUTPUT_DIRECTORY = True

# TWITTER_USERNAME = 'statsimcom'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
