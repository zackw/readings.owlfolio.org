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

    def get_link(self, citation):
        return None

class Conference(Venue):
    def __init__(self, *, name, organization=None, urls=None):
        Venue.__init__(self, name=name)
        self.urls = urls or {}
        self.organization = organization
        self.bibtex_type = 'inproceedings'

    def get_link(self, citation):
        year = str(citation.get('year', '')).strip()
        url = self.urls.get(year, None)

        name = H.EM(self.name)
        if url is None:
            if year == '':
                return name
            else:
                return H.SPAN(name, " " + year)
        else:
            if year == '':
                return H.A(name, href=url)
            else:
                return H.A(H.EM(self.name), " " + year, href=url)

class Journal(Venue):
    def __init__(self, *, name,
                 url=None, url_vol=None, url_iss=None, url_vol_iss=None):
        Venue.__init__(self, name=name)
        self.url         = url
        self.url_vol     = url_vol
        self.url_iss     = url_iss
        self.url_vol_iss = url_vol_iss
        self.bibtex_type = 'article'

    def get_link(self, citation):
        volume = str(citation.get('volume', '')).strip()
        issue  = str(citation.get('issue', '')).strip()
        year   = str(citation.get('year', '')).strip()

        name = H.EM(self.name)

        if volume and issue and self.url_vol_iss:
            url = self.url_vol_iss.format(volume=volume, issue=issue)
            linkto = 'all'

        elif issue and self.url_iss:
            url = self.url_iss.format(issue=issue)
            linkto = 'all'

        elif volume and self.url_vol:
            url = self.url_vol.format(volume=volume)
            linkto = 'volume'

        elif self.url:
            url = self.url
            linkto = 'name'

        else:
            url = None
            linkto = None

        if url:
            link = H.A(name, href=url)
            is_A = True
        else:
            link = H.SPAN(name)
            is_A = False

        if volume:
            if is_A and linkto != 'volume' and linkto != 'all':
                link = H.SPAN(link)
                is_A = False

            addText(link, " " + volume)

        if issue:
            if is_A and linkto != 'all':
                link = H.SPAN(link)
                is_A = False

            if volume:
                addText(link, "(" + issue + ")")
            else:
                addText(link, " iss.\u2009" + issue)

        # The year never goes inside the hyperlink.
        if year:
            if is_A:
                link = H.SPAN(link)
                is_A = False

            addText(link, "; " + year)

        return link


class Preprint(Venue):
    def __init__(self):
        Venue.__init__(self, name='Preprint')
        self.bibtex_type = 'unpublished'

VENUES = {
    # Conferences, alpha by tag
    'ATIS': Conference(
        name = 'Applications and Techniques in Information Security',
        urls = {
            '2014': 'http://atis2014.tulip.org.au/',
        }
    ),
    'CCS': Conference(
        name = 'Computer and Communications Security',
        organization = 'ACM SIGSAC',
        urls = {
            '2013': 'http://www.sigsac.org/ccs/CCS2013/',
        }
    ),
    'HotNets': Conference(
        name = 'Hot Topics in Networks',
        organization = 'ACM SIGCOMM',
        urls = {
            '2014': 'http://conferences.sigcomm.org/hotnets/2014/',
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
    'MoST': Conference(
        name = 'Mobile Security Technologies',
        organization = 'IEEE',
        urls = {
            '2015': 'http://www.ieee-security.org/TC/SPW2015/MoST/',
        }
    ),
    'Oakland': Conference(
        name = 'Symposium on Security and Privacy',
        organization = 'IEEE',
        urls = {
            '2015': 'http://www.ieee-security.org/TC/SP2015/',
        }
    ),
    'PETS': Conference(
        name = 'Privacy Enhancing Technologies',
        urls = {
            '2014': 'https://petsymposium.org/2014/',
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
    'WWW': Conference(
        name = 'International World Wide Web Conference',
        urls = {
            '2015': 'http://www2015.wwwconference.org/',
        }
    ),

    # Journals, alpha by tag
    'J.ComNet': Journal(
        name = 'Computer Networks',
        url = 'http://www.sciencedirect.com/science/journal/13891286/',
        url_vol =
            'http://www.sciencedirect.com/science/journal/13891286/{volume}/'
    ),

    'j.ics': Journal(
        name = 'Information, Communication & Society',
        url = 'http://www.tandfonline.com/loi/rics20',
        url_vol_iss =
            'http://www.tandfonline.com/toc/rics20/{volume}/{issue}'
    ),

    'PNAS': Journal(
        name = 'Proc Nat Acad Sci',
        url = 'http://www.pnas.org/',
        url_vol_iss = 'http://www.pnas.org/content/{volume}/{issue}.toc'
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
        data = str(data).strip()
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
