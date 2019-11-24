#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ben Hanna'
SITENAME = u'Farmadeus'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Etc/UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

#Static
STATIC_PATHS = [
    'extra',
    'images'
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True