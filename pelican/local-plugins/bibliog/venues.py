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

class InBook(Venue):
    def __init__(self):
        Venue.__init__(self, name='InBook')
        self.bibtex_type = 'inbook'

    def get_link(self, citation):
        year = str(citation.get('year', '')).strip()
        booktitle = str(citation.get('booktitle', '')).strip()
        isbn = str(citation.get('isbn', '')).strip()
        editors = citation.get('editors', [])

        if booktitle:
            link = H.I(booktitle)
        else:
            link = H.I("BOOK TITLE MISSING")

        if isbn:
            link = H.A(link,
                       href=
                       "https://www.worldcat.org/search?q=isbn%3A"
                       + isbn.replace("-", ""))

        link = H.SPAN("In ", link)

        if editors:
            ed_adj = []
            #XXX Duplicates code in bibliog.py
            for ed in editors:
                last, _, first = ed.partition(", ")
                # Don't allow word-wrapping between components of the first
                # and last names.
                first = first.strip().replace(" ", "\u00a0")
                last  = last.strip().replace(" ", "\u00a0")
                if not first:
                    ed = last
                else:
                    ed = first + " " + last
                ed_adj.append(ed)
            if len(ed_adj) == 1:
                ed_credit = "(" + ed_adj[0] + ", ed.)"
            else:
                ed_credit = " (" + ", ".join(ed_adj) + ", eds.)"
            addText(link, ed_credit)

        if year:
            addText(link, ", " + year)

        return link


class Preprint(Venue):
    def __init__(self):
        Venue.__init__(self, name='Preprint')
        self.bibtex_type = 'unpublished'

    def get_link(self, citation):
        year = str(citation.get('year', '')).strip()
        if year:
            return H.SPAN(year)
        return None

VENUES = {
    # Conferences, alpha by tag
    'ACL-IJCNLP': Conference(
        name = 'Association for Computational Linguistics',
        urls = {
            '2015': 'http://acl2015.org/'
        }
    ),
    'AIRWeb': Conference(
        name = 'Adversarial Information Retrieval on the Web',
        organization = 'ACM SIGIR',
        urls = {
            '2006': 'http://airweb.cse.lehigh.edu/2006/',
        }
    ),
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
            '2001': 'http://www.sigsac.org/ccs/ccs-history.html#8th',
            '2013': 'http://www.sigsac.org/ccs/CCS2013/',
            '2014': 'http://www.sigsac.org/ccs/CCS2014/',
            '2015': 'http://www.sigsac.org/ccs/CCS2015/',
        }
    ),
    'CHES': Conference(
        name = 'Cryptographic Hardware and Embedded Systems',
        organization = 'IACR',
        urls = {
            '2013': 'http://www.chesworkshop.org/ches2013/'
        }
    ),
    'CSET': Conference(
        name = 'Cyber Security Experimentation and Test',
        organization = 'USENIX',
        urls = {
            '2012': 'https://www.usenix.org/conference/cset12',
        }
    ),
    'FOCI': Conference(
        name = 'Free and Open Communications on the Internet',
        organization = 'USENIX',
        urls = {
            '2012': 'https://www.usenix.org/conference/foci12',
        }
    ),
    'HotNets': Conference(
        name = 'Hot Topics in Networks',
        organization = 'ACM SIGCOMM',
        urls = {
            '2014': 'http://conferences.sigcomm.org/hotnets/2014/',
        }
    ),
    'HotPETS': Conference(
        name = 'Hot Topics in Privacy Enhancing Technologies',
        urls = {
            '2015': 'https://www.petsymposium.org/2015/hotpets.php'
        }
    ),
    'IFIP SEC': Conference(
        name = 'International Information Security and Privacy Conference',
        organization = 'International Federation for Information Processing',
        urls = {
            '2015': 'https://ifipsec.org/2015/',
        }
    ),
    'IMC': Conference(
        name = 'Internet Measurement Conference',
        organization = 'ACM SIGCOMM',
        urls = {
            '2012': 'http://conferences.sigcomm.org/imc/2012/',
            '2013': 'http://conferences.sigcomm.org/imc/2013/',
            '2014': 'http://conferences.sigcomm.org/imc/2014/',
            '2015': 'http://conferences.sigcomm.org/imc/2015/',
        }
    ),
    'ISCA': Conference(
        name = 'International Symposium on Computer Architecture',
        organization = 'ACM SIGARCH',
        urls = {
            '2014': 'http://cag.engr.uconn.edu/isca2014/'
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
    'NDSS': Conference(
        name = 'Network and Distributed System Security Symposium',
        organization = 'Internet Society',
        urls = {
            '2015': 'https://www.internetsociety.org/events/ndss-symposium-2015',
        }
    ),
    'Oakland': Conference(
        name = 'Symposium on Security and Privacy',
        organization = 'IEEE',
        urls = {
            '2003': 'http://www.ieee-security.org/TC/SP2003/sp03prelimprogram.html',
            '2015': 'http://www.ieee-security.org/TC/SP2015/',
        }
    ),
    'PETS': Conference(
        name = 'Privacy Enhancing Technologies',
        urls = {
            '2012': 'https://petsymposium.org/2012/',
            '2013': 'https://petsymposium.org/2013/',
            '2014': 'https://petsymposium.org/2014/',
            '2015': 'https://petsymposium.org/2015/',
        }
    ),
    'SATS': Conference(
        name = 'Workshop on Surveillance & Technology',
        urls = {
            '2015': 'https://satsymposium.org/',
        }
    ),
    'SIGCOMM': Conference(
        name = 'SIGCOMM',
        organization = 'ACM SIGCOMM',
        urls = {
            '2015': 'http://conferences.sigcomm.org/sigcomm/2015/'
        }
    ),
    'SOUPS': Conference(
        name = 'Symposium on Usable Privacy and Security',
        organization = 'ACM',
        urls = {
            '2010': 'https://cups.cs.cmu.edu/soups/2010/',
        }
    ),
    'USENIX Security': Conference(
        name = 'USENIX Security Symposium',
        organization = 'USENIX',
        urls = {
            '2015': 'https://www.usenix.org/conference/usenixsecurity15',
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
            '2006': 'http://www2006.wwwconference.org/',
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

    'na.cyber.pol': Journal(
        name = 'New America Cybersecurity Initiative Policy Papers',
        url = 'https://www.newamerica.org/tags/cybersecurity-initiative-policy-papers/'
    ),

    'PNAS': Journal(
        name = 'Proc Nat Acad Sci',
        url = 'http://www.pnas.org/',
        url_vol_iss = 'http://www.pnas.org/content/{volume}/{issue}.toc'
    ),

    # Other
    'inbook': InBook(),
    'preprint': Preprint(),
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
        data = data.strip()
        if '{}' in self.base_url:
            return self.base_url.format(data)
        else:
            return self.base_url + data

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
    'i-d':   EPrint('Internet-Draft',
                    'https://datatracker.ietf.org/doc/draft-{}/'),
    'rfc':   EPrint('RFC',  'https://tools.ietf.org/html/rfc', colon=False),
    'doi':   EPrint('DOI',  'http://dx.doi.org/')
}
