#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Uncomment to disable caching temporarily (for heavy theme/plugin development)
#CACHE_CONTENT = False

AUTHOR              = u'Zack Weinberg'
SITENAME            = u'Readings in Information Security'
SITEURL             = ''
TIMEZONE            = 'America/New_York'
DEFAULT_DATE        = 'fs'
DEFAULT_DATE_FORMAT = '%-d %B %Y'
DEFAULT_LANG        = u'en'
DEFAULT_PAGINATION  = 10
RELATIVE_URLS       = True

PATH                = 'content'
PAGE_PATHS          = ['pages']
STATIC_PATHS        = ['',]
IGNORE_FILES        = ['.#*', '*~', '#*#']
ARTICLE_EXCLUDES    = []

THEME               = '../style'
THEME_STATIC_DIR    = 's'

ARTICLE_URL         = '{category}/{slug}/'
ARTICLE_SAVE_AS     = '{category}/{slug}/index.html'
PAGE_URL            = '{slug}/'
PAGE_SAVE_AS        = '{slug}/index.html'
CATEGORY_URL        = '{slug}/'
CATEGORY_SAVE_AS    = '{slug}/index.html'
TAG_URL             = 't/{slug}/'
TAG_SAVE_AS         = 't/{slug}/index.html'

AUTHOR_SAVE_AS      = ''
ARCHIVES_SAVE_AS    = ''
AUTHORS_SAVE_AS     = ''
CATEGORIES_SAVE_AS  = ''
TAGS_SAVE_AS        = 't/index.html'

PAGINATION_PATTERNS = [
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
]

PLUGIN_PATHS        = ['plugins']
PLUGINS             = ['assets',
                       'neighbors',
                       'sitemap',
                       'summary',
                       'read_more_link',
                       'category_meta',
                       'pandoc_reader']

PANDOC_ARGS         = ['--smart', '--normalize', '--html-q-tags', '--mathml']
PANDOC_EXTENSIONS   = ['-citations']

# Setting SUMMARY_MAX_LENGTH to None breaks read_more_link.
# The <span> around the space and link is necessary because
# read_more_link will only insert _one element_.
SUMMARY_MAX_LENGTH    = 1e10
SUMMARY_END_MARKER    = '<!--more-->'
READ_MORE_LINK        = '(Continued…)'
READ_MORE_LINK_FORMAT = '<span> <a class="read-more" href="/{url}">{text}</a></span>'

# This is the default, but it complains if you don't set it explicitly.
SITEMAP             = { 'format': 'xml' }

# Outbound top-menu links.
MENUITEMS = [
    ('Contact',         'https://www.owlfolio.org/contact/',    'left'),
    ('Owl’s Portfolio', 'https://www.owlfolio.org/',            'left'),
    ('Hacks',           'https://hacks.owlfolio.org/',          'right'),
    ('Publications',    'https://hacks.owlfolio.org/pubs/',     'right'),
    ('Photography',     'https://www.flickr.com/zackw/photos/', 'right')
]

# Tag cloud
TAG_CLOUD_STEPS     = 4
TAG_CLOUD_MAX_ITEMS = 20
TAGS_UPPERCASE      = ['pki', 'https', 'bgp']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Most extra-path objects are not useful when developing, but the favicon is,
# if only to stop 404 log spam from SimpleHTTPServer.
EXTRA_PATH_METADATA = {
    '../meta/favicon.ico' : { 'path': 'favicon.ico' },
}

# If assets is allowed to run in debug mode, it puts the CSS files in
# the wrong place, breaking links to subresources.
ASSET_DEBUG = False
