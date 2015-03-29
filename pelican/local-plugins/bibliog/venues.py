# This module contains a big table of places where things have been
# published ('venues'), with metadata that doesn't change from paper
# to paper within a venue, thus reducing the amount of repetition and
# potential error in the bibliographic database.
#
# It also contains classes for each _type_ of venue which handle some
# of the formatting details for HTML and BibTeX.

from lxml.html import builder as H

# From http://infohost.nmt.edu/tcc/help/pubs/pylxml/web/builder-addText.html
# Why did anyone think the tail representation was a good idea, anyway?
def addText(node, s):
    """Add text content to an element."""
    if not s:
        return
    if len(node) == 0:
        node.text = (node.text or "") + s
    else:
        lastChild = node[-1]
        lastChild.tail = (lastChild.tail or "") + s

class Venue:
    def __init__(self, *, name):
        self.name = name

    def __str__(self):
        return 'Venue(' + repr(self.name) + ')'

    def get_link(self, year):
        return None

class Conference(Venue):
    def __init__(self, *, name, organization, urls):
        Venue.__init__(self, name=name)
        self.urls = urls
        self.organization = organization
        self.bibtex_type = 'inproceedings'

    def get_link(self, year):
        year = str(year)
        url = self.urls.get(year, None)
        if url is None: return None
        return H.A(H.EM(self.name), " " + year,
                   href=url)

class Preprint(Venue):
    def __init__(self):
        Venue.__init__(self, name='Preprint')
        self.bibtex_type = 'unpublished'

VENUES = {
    # Conferences
    'CCS': Conference(
        name = 'Computer and Communications Security',
        organization = 'ACM SIGSAC',
        urls = {
            '2013': 'http://www.sigsac.org/ccs/CCS2013/',
        }
    ),
    'IMC': Conference(
        name = 'Internet Measurement Conference',
        organization = 'ACM SIGCOMM',
        urls = {
            '2013': 'http://conferences.sigcomm.org/imc/2013/',
        }
    ),
    'LangSec': Conference(
        name = 'Workshop on Language-Theoretic Security',
        organization = 'IEEE',
        urls = {
            '2015': 'http://spw15.langsec.org/index.html',
        }
    ),
    'HotNets': Conference(
        name = 'Hot Topics in Networks',
        organization = 'ACM SIGCOMM',
        urls = {
            '2014': 'http://conferences.sigcomm.org/hotnets/2014/',
        }
    ),
    'WOOT': Conference(
        name = 'Workshop on Offensive Technologies',
        organization = 'USENIX',
        urls = {
            '2014': 'https://www.usenix.org/conference/woot14',
        }
    ),
    'WPES': Conference(
        name = 'Workshop on Privacy in the Electronic Society',
        organization = 'ACM SIGSAC',
        urls = {
            '2014': 'https://www.cylab.cmu.edu/news_events/events/wpes2014/',
        }
    ),

    # Preprints
    'preprint': Preprint()
}


# EPrints operate separately from venues, because any paper may have _both_
# been published in a traditional venue, and appear in one or more online
# archives.  The EPrint class handles DOIs as well.

class EPrint:
    def __init__(self, name, base_url, colon=True):
        self.name     = name
        self.base_url = base_url
        self.colon    = colon

    def get_url(self, data):
        return self.base_url + data.strip()

    def _build_link(self, data, url):
        return H.DIV(H.CLASS("eprint " + self.name.lower()),
                     self.name + (": " if self.colon else " "),
                     H.A(data, href=url))

    def get_link(self, data):
        data = data.strip()
        url = self.get_url(data)
        return self._build_link(data, url)

class Arxiv(EPrint):
    def __init__(self):
        EPrint.__init__(self, 'arXiv', 'http://arxiv.org/abs/')

    def get_url(self, data):
        serial, _, category = data.partition(" ")
        return EPrint.get_url(self, serial)

    def get_link(self, data):
        serial, _, category = data.partition(" ")
        url = EPrint.get_url(self, serial)
        link = self._build_link(serial, url)
        if category:
            addText(link, " " + category)
        return link

EPRINTS = {
    'arxiv': Arxiv(),
    'iacr':  EPrint('IACR', 'http://eprint.iacr.org/'),
    'rfc':   EPrint('RFC',  'https://tools.ietf.org/html/rfc', colon=False),
    'doi':   EPrint('DOI',  'http://dx.doi.org/')
}
