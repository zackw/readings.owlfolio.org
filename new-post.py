"""Create a new scheduled post.

Starting with the calendar week after the current one and moving
forward, test M, W, F, Tu, Th in that order for an existing post.
The first date not already occupied is assigned.

Command line arguments are used for the slug part of the name.

This program hardwires the location of existing posts and the format
of their names (content/YYYY/MM-DD-slug.md, relative to the directory
containing __file__)

"""

import datetime
import os
import re
import stat
import sys
import textwrap
import unicodedata
import unidecode

CONTENT_BASE = os.path.join(os.path.dirname(__file__), "content")

def raise_NotADirectoryError(filename):
    """Yes, this is the only way to initialize a manual NotADirectoryError
       correctly."""
    import errno
    raise NotADirectoryError(errno.ENOTDIR,
                             os.strerror(errno.ENOTDIR),
                             filename)

def posting_date_sequence(start_date):
    """Generate a sequence of dates that may be used for a post composed
       on START_DATE, which is expected to be a datetime.date object;
       values yielded are also datetime.date objects.
    """
    day  = datetime.timedelta(days=1)
    week = datetime.timedelta(days=7)

    # Align to next Monday.
    # date.weekday() 0 is Monday
    d = start_date + day
    while d.weekday():
        d += day

    while True:
        yield d         # Monday
        yield d + 2*day # Wednesday
        yield d + 4*day # Friday
        yield d +   day # Tuesday
        yield d + 3*day # Thursday
        d += week

def dates_already_used(year):
    yeardir = os.path.join(CONTENT_BASE, str(year))
    try:
        st = os.stat(yeardir)
    except FileNotFoundError:
        return set()

    if not stat.S_ISDIR(st.st_mode):
        raise_NotADirectoryError(yeardir)

    dates_used = set()
    for fname in os.listdir(yeardir):
        if fname == '' or fname[0] == '.': continue
        try:
            month, day, rest = fname.split('-', 2)
            month = int(month)
            day = int(day)
            dates_used.add(datetime.date(year=year, month=month, day=day))
        except ValueError:
            continue

    return dates_used

def find_next_posting_date(start_date):
    current_year = None
    current_year_used = None
    for candidate in posting_date_sequence(start_date):
        if candidate.year != current_year:
            current_year = candidate.year
            current_year_used = dates_already_used(candidate.year)

        if candidate not in current_year_used:
            return candidate

def slugify(words):
    # more-or-less compatible with what pelican.utils.slugify does
    text = unicodedata.normalize('NFKD', "-".join(words))
    text = unidecode.unidecode(text).lower()
    text = re.sub('[^\w\s-]', '', text).strip()
    text = re.sub('[-\s]+', '-', text)

    # this step may be unnecessary; does unidecode guarantee to emit only ASCII?
    text = text.encode('ascii', 'ignore').decode('ascii')
    return text

def main(argv, stdout):
    date = find_next_posting_date(datetime.date.today())
    if len(argv) == 1:
        stdout.write("Next posting date {}\n"
                     .format(date.strftime("%Y-%m-%d")))
    else:
        path = date.strftime("%Y/%m-%d-") + slugify(argv[1:]) + ".md"
        with open(os.path.join(CONTENT_BASE, path), "xt") as f:
            f.write(textwrap.dedent("""\
            ---
            title:
            tags:
            authors:
             -
            year:
            venue:
            ...
            """))

        stdout.write("Created content/{}\n".format(path))

main(sys.argv, sys.stdout)
