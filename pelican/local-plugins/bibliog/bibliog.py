
import logging
logger = logging.getLogger(__name__)

from pelican import signals
from pelican.contents import Category, Article

def augment_metadata(generator, metadata):
    # The publication year becomes the category.  This is a kludge-around
    # the absence of indices on arbitrary metadata columns (and the
    # requirement to have _some_ category).
    metadata['category'] = Category(metadata['year'], generator.settings)

def register():
    signals.article_generator_context.connect(augment_metadata)
