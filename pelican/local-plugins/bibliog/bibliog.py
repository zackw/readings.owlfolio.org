
import logging
logger = logging.getLogger(__name__)

from pelican import signals
from pelican.contents import Article, Category
from pelican.contents import Author as stock_Author
from pelican.utils import slugify

# Note: This class's __name__ must be 'Author', otherwise
# URLWrapper._from_settings will malfunction.
class Author(stock_Author):
    """Subclass Author to provide both 'last, first' and 'first last'
       names; requires 'last, first' name input.  The slug, and the
       default print format, are based on the 'first last' name.
    """
    def __init__(self, name, settings):
        last, _, first = name.partition(", ")
        stock_Author.__init__(self, first + " " + last, settings)
        self.lf_name = name
        self.lf_slug = slugify(name, self.settings.get('SLUG_SUBSTITUTIONS',
                                                       ()))

def augment_metadata(generator, metadata):
    # The publication year becomes the category.  This is a kludge-around
    # the absence of indices on arbitrary metadata columns (and the
    # requirement to have _some_ category).
    metadata['category'] = Category(metadata['year'], generator.settings)

    # Convert all authors to our custom Author class.
    if 'authors' in metadata:
        metadata['authors'] = [Author(a.name, a.settings)
                               for a in metadata['authors']]
    if 'author' in metadata:
        a = metadata['author']
        metadata['author'] = Author(a.name, a.settings)

def register():
    signals.article_generator_context.connect(augment_metadata)
