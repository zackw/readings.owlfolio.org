#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Uncomment to disable caching temporarily (for heavy theme/plugin development)
#CACHE_CONTENT = False

AUTHOR                 = 'Zack Weinberg'
SITENAME               = 'Readings in Information Security'
SITEURL                = ''
TIMEZONE               = 'America/New_York'
DEFAULT_DATE           = None
PUBLICATION_TIME       = { 'hour': 8, 'minute': 0, 'second': 0 }
PATH_METADATA          = '^(?P<date>\d{4}/\d{2}-\d{2})-(?P<slug>[^.]+)'
DEFAULT_DATE_FORMAT    = '%-d %B %Y'
DEFAULT_LANG           = 'en'
DEFAULT_PAGINATION     = 10
RELATIVE_URLS          = True
SUMMARY_MAX_LENGTH     = None
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY       = 'ERROR.CATEGORY.NOT.SET'
REVERSE_CATEGORY_ORDER = True

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
AUTHOR_URL          = 'a/{slug}/'
AUTHOR_SAVE_AS      = 'a/{slug}/index.html'

ARCHIVES_SAVE_AS    = ''
AUTHORS_SAVE_AS     = 'a/index.html'
CATEGORIES_SAVE_AS  = ''
TAGS_SAVE_AS        = 't/index.html'

TAG_CAPITALIZATION  = {
    'pki'   : 'PKI',
    'https' : 'HTTPS',
    'bgp'   : 'BGP',
    'ipv4'  : 'IPv4',
    'ipv6'  : 'IPv6'
}

PAGINATION_PATTERNS = [
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
]

PLUGIN_PATHS        = ['../../pelican-plugins', 'local-plugins']
PLUGINS             = ['assets',
                       'neighbors',
                       'sitemap',
                       'pandoc_reader',
                       'bibliog']

PANDOC_ARGS         = ['--smart', '--normalize', '--html-q-tags', '--mathml']
PANDOC_EXTENSIONS   = ['-citations', '-mmd_title_block']

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

# These properly belong to the bibliog extension, but have to be done
# here.  (Also, it's infuriating that jinja's builtin sort filter
# doesn't support key=.  Actually, it's infuriating that jinja
# expressions are *in any way* different from regular python
# expressions.  Thou shalt not reinvent the square wheel.)

def jf_sort_authors_by_lf_name(author_list):
    return sorted(author_list, key = lambda xy: xy[0].lf_name)

def jf_sort_by_article_count(articles_list):
    return sorted(articles_list, key = lambda xy: (-len(xy[1]), xy[0]))

JINJA_FILTERS = {
    'sort_authors_by_lf_name':  jf_sort_authors_by_lf_name,
    'sort_by_article_count':    jf_sort_by_article_count
}

JINJA_EXTENSIONS = ['jinja2.ext.loopcontrols']
