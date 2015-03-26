"""
Generate an embedded BibTeX entry from article metadata, and munge the
article metadata for Pelican consumption.

With this plugin in use, all top-level metadata keys are translated
directly to BibTeX field tags, with the following exceptions:

 * `date`, `category`, `tags` - ignored
 * `authors` - converted to "and"-separated list, used as the 'author' value

 * `<field>_url` - not visible, but `field`'s value will be made into
                   a hyperlink to this
 * `_type` - Value is used as the BibTeX entry type.  Default: 'article'
 * `_label` - Value is used as the entry label (the thing you put in a
              \cite{}). Default: the first author's last name + '.' +
              the 'year'.

Some keys have special semantics:

 * `doi`, `url`, `eprint`: automatically hyperlinked
 * `editor`: if there is no `author` or `authors`, will be copied to `authors`
 * `year`: becomes the `category` if there is none

You can get @STRING-like replacements using a `BIBLIOG_SHORTHAND` dictionary
in the configuration.  Replacements are only considered if they are the
*entire* value of a metadata key.

    BIBLIOG_SHORTHAND = {
        "CCS":      "Computer and Communications Security",
        "Oakland":  "Symposium on Security and Privacy",
        # ...
    }

"""

import re
import six
import textwrap

#
# BibTeX output
#
# The quoting rules for BibTeX are poorly documented and unpleasant to
# work with.  This is my best guess at a safe set of rules.  We assume
# that Unicode is used instead of diacritic escape sequences.  We also
# assume 
#


def bibtex_quote(text, protect_uppercase=False):
    output = []
    brace_depth = 0
    need_outer_braces = False
    quote_backslash

    if not isinstance(text, six.text_type):
        if isinstance(text, six.string_types):
            text = text.decode("utf-8")
        else:
            text = str(text)

def register():
    pass
