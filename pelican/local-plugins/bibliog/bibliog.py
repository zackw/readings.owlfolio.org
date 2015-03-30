"""Bibliographic metadata handling for readings.owlfolio.org.
   Probably not useful on any other site.
"""

from __future__ import absolute_import, unicode_literals

import logging
logger = logging.getLogger(__name__)

from pelican import signals
from pelican.contents import Article, Category
from pelican.contents import Author as stock_Author
from pelican.contents import Tag as stock_Tag
from pelican.utils import slugify, strftime

from .venues import VENUES, EPRINTS

import lxml.etree
import lxml.html
from lxml.html import builder as H

# HTML5 elements not in lxml.html.builder as of this writing
if not hasattr(H, 'HEADER'):
    H.HEADER = H.E.header
    H.TIME = H.E.time

def as_html(tree):
    return lxml.html.tostring(tree, encoding="unicode")
def as_text(tree):
    return lxml.etree.tostring(tree, encoding="unicode", method="text")

#
# Metadata preprocessing
#

# Note: These classes' __name__s must be 'Author' and 'Tag'
# respectively, otherwise URLWrapper._from_settings will malfunction.
class Author(stock_Author):
    """Subclass Author to provide both 'last, first' and 'first last'
       names; requires 'last, first' name input.  The slug, and the
       default print format, are based on the 'first last' name.
    """
    def __init__(self, name, settings):
        last, _, first = name.partition(", ")
        # Don't allow word-wrapping between components of the first
        # and last names.
        first = first.strip().replace(" ", "\u00a0")
        last  = last.strip().replace(" ", "\u00a0")
        if not first:
            fl_name = last
            lf_name = last
        else:
            fl_name = first + " " + last
            lf_name = last + ", " + first

        stock_Author.__init__(self, fl_name, settings)
        self.lf_name = lf_name
        self.lf_slug = slugify(lf_name,
                               self.settings.get('SLUG_SUBSTITUTIONS', ()))

class Tag(stock_Tag):
    """Subclass Tag to honor TAG_CAPITALIZATION when printed.
       (tag.name is unaffected, because overriding just the getter
       is Too Hard)"""

    def __str__(self):
        name = self.name
        cap = self.settings.get('TAG_CAPITALIZATION', {})
        if name in cap:
            return cap[name]
        else:
            return name.capitalize()

def adjust_metadata(generator, metadata):
    # The publication year becomes the category.  This is a kludge-around
    # the absence of indices on arbitrary metadata columns (and the
    # requirement to have _some_ category).
    metadata['category'] = Category(str(metadata['year']), generator.settings)

    # The 'url' field is renamed 'fulltext_url', if present.
    # (We use it for a non-systematic URL of the full text of a paper,
    # Pelican wants to use it for the site-relative permalink.)
    if 'url' in metadata:
        metadata['fulltext_url'] = metadata['url']
        del metadata['url']

    # Convert all authors to our custom Author class, and all
    # tags to our custom Tag class.
    if 'authors' in metadata:
        metadata['authors'] = [Author(a.name, a.settings)
                               for a in metadata['authors']]
    if 'author' in metadata:
        a = metadata['author']
        metadata['author'] = Author(a.name, a.settings)
    if 'tags' in metadata:
        metadata['tags'] = [Tag(t.name, t.settings)
                            for t in metadata['tags']]

    # Articles are always published at PUBLICATION_TIME; the date in
    # the metadata is just the _date_. Pelican wants a full datetime
    # (because RSS).
    pubtime = generator.settings.get('PUBLICATION_TIME', {})
    if 'date' in metadata:
        metadata['date'] = metadata['date'].replace(**pubtime)

#
# Header rendering
#

def time_tag(dt, dformat, *, cls=None, prefix=None, suffix=None):
    isotime    = dt.isoformat()
    localized  = strftime(dt, dformat)
    attrs      = { 'datetime': isotime }
    if cls: attrs['class'] = cls
    text = ""
    if prefix: text += prefix
    text += localized
    if suffix: text += suffix
    return H.TIME(attrs, text)

def entry_title(article, is_article_page):
    if is_article_page:
        h_tag = lxml.html.fragment_fromstring(article.title, create_parent='h1')
    else:
        a_tag = lxml.html.fragment_fromstring(article.title, create_parent='a')
        a_tag.set("href",  "/"+article.url)
        a_tag.set("rel",   "bookmark")
        a_tag.set("title", "Permalink to " + as_text(a_tag))
        h_tag = H.H2(a_tag)
    h_tag.set("class", "entry-title")
    return h_tag

def entry_tags(article):
    elements = [ H.A(str(tag).replace(" ", "\u00a0"), href="/"+tag.url)
                 for tag in sorted(article.tags) ]
    for i in range(len(elements)-1):
        elements[i].tail = ", "
    return H.DIV(H.CLASS("tags"), *elements)

def entry_authors(article):
    elements = [ H.A(str(author), href="/"+author.url)
                 for author in article.authors ]
    for i in range(len(elements)-1):
        elements[i].tail = ", "
    return H.DIV(H.CLASS("authors"), *elements)

def review_meta(article):
    elements = []
    elements.append(time_tag(article.date, article.date_format,
                             cls="published", prefix="Reviewed "))
    if hasattr(article, 'modified'):
        elements.append(time_tag(article.modified, article.date_format,
                                 cls="modified", prefix="Review edited "))
    elements.append(entry_tags(article))
    return H.DIV(H.CLASS("review-meta"), *elements)

def paper_meta_abbrv(article):
    elements = [entry_authors(article)]
    if hasattr(article, 'venue'):
        venue = VENUES.get(article.venue, None)
        if venue:
            venue_link = venue.get_link(article.year)
            if venue_link is not None:
                elements.append(H.DIV(H.CLASS("venue"), venue_link))
        else:
            logger.warning('unrecognized venue ' + repr(article.venue) +
                           ' for article ' + article.slug)
    else:
        logger.warning('no venue for article ' + article.slug)

    return H.DIV(H.CLASS("paper-meta"), *elements)

def paper_meta_full(article):
    div = paper_meta_abbrv(article)
    if hasattr(article, 'eprints'):
        for ep_type, ep_data in sorted(article.eprints.items(),
                                       # DOIs go last
                                       key = lambda kv: (kv[0]=='doi', kv[0])):
            if ep_type not in EPRINTS:
                logger.warning('unrecognized eprint type ' + repr(ep_type) +
                               ' for article ' + article.slug)
                continue
            div.append(EPRINTS[ep_type].get_link(ep_data))

    if hasattr(article, 'fulltext_url'):
        div.append(H.DIV(H.CLASS("eprint misc"),
                         H.A("full text", href=article.fulltext_url)))
    return div

def render_article_header_abbrv(article):
    return as_html(H.HEADER(H.CLASS("post-header"),
                            entry_title(article, False),
                            H.DIV(H.CLASS("entry-meta"),
                                  review_meta(article),
                                  paper_meta_abbrv(article))))

def render_article_header_full(article):
    return as_html(H.HEADER(H.CLASS("post-header"),
                            entry_title(article, True),
                            H.DIV(H.CLASS("entry-meta"),
                                  review_meta(article),
                                  paper_meta_full(article))))

#
# Plugin glue
#

def add_template_callbacks(generator):
    generator.env.globals.update({
        'article_header_abbrv': render_article_header_abbrv,
        'article_header_full':  render_article_header_full
    })

def register():
    signals.generator_init.connect(add_template_callbacks)
    signals.article_generator_context.connect(adjust_metadata)
