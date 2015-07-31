---
title: "Automated Detection and Fingerprinting of Censorship Block Pages"
tags: [censorship, web, machine learning]
authors:
 - Jones, Ben
 - Lee, Tzu-Wen
 - Feamster, Nick
 - Gill, Phillipa
year: 2014
venue: IMC
eprints:
 doi: 10.1145/2663716.2663722
url: http://conferences.sigcomm.org/imc/2014/papers/p299.pdf
...

This short paper, from IMC last year, presents a re-analysis of data
collected by the [OpenNet Initiative][] on overt censorship of the Web
by a wide variety of countries.  "Overt" means that when a webpage is
censored, the user sees an error message which unambiguously informs
them that it's censored.  (A censor can also act "deniably", giving
the user no proof that censorship is going on---the webpage just
appears to be broken.)  The goal of this reanalysis is to identify
"block pages" (the error messages) automatically, distinguish them from
normal pages, and distinguish them from _each other_---a new,
unfamiliar format of block page may indicate a new piece of software
is in use to do the censoring.

The chief finding is that block pages can be reliably distinguished
from normal pages just by looking at their length: block pages are
typically much shorter than normal.  This is to be expected, seeing
that they are just an error message.  What's interesting, though, is
that this technique works _better_ than techniques that look in more
detail at the contents of the page.  I'd have liked to see some
discussion of what kinds of misidentification appear for each
technique, but there probably wasn't room for that. Length is _not_ an
effective tactic for distinguishing block pages from each other, but
"term frequency" is (they don't go into much detail about that).

One thing that's really not clear is how they distinguish block pages
from ordinary HTTP error pages.  They mention that ordinary errors
introduce "significant noise" in term-frequency clustering, but they
don't explain how they weeded them out.  It might have been done
manually; if so, that's a major hole in the overall automated-ness of
this process.

[OpenNet Initiative]: https://opennet.net/
