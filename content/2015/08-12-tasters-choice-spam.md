---
title: "Taster's Choice: A Comparative Analysis of Spam Feeds"
tags: [spam, large sample, methodology]
authors:
 - Pitsillidis, Andreas
 - Kanich, Chris
 - Voelker, Geoffrey
 - Levchenko, Kirill
 - Savage, Stefan
year: 2012
venue: IMC
url: https://cseweb.ucsd.edu/~klevchen/pkvls-imc12.pdf
...

Here's another paper about spam; this time it's email spam, and they
are interested not so much in the spam itself, but in the differences
between *collections* of spam ("feeds") as used in research.  They
have ten different feeds, and they compare them to each other looking
only at the domain names that appear in each.  The goal is to figure
out whether or not each feed is an unbiased sample of all the spam
being sent at any given time, and whether some types of feed are
better at detecting particular sorts of spam.  (Given this goal,
looking only at the domain names is probably the most serious
limitation of the paper, despite being brushed off with a footnote.
It means they can't say anything about spam that *doesn't* contain any
domain names, which may be rare, but is interesting *because* it's
rare and different from all the rest.  They should have at least
analyzed the proportion of it that appeared in each feed.)

The spam feeds differ primarily in how they collect their samples.
There's one source consisting exclusively of manually labeled spam
(from a "major email provider"); two DNS blacklists (these provide
*only* domain names, and are somehow derived from other types of
feed); three MX honeypots (registered domains that accept email to any
address, but are never used for legitimate mail); two seeded honey
accounts (like honeypots, but a few addresses are made visible to
attract more spam); one botnet-monitoring system; and one "hybrid."
They don't have full details on exactly how they all work, which is
probably the second most serious limitation.

The actual results of the analysis are basically what you would
expect: manually labeled spam is lower-volume but has more unique
examples in it, botnet spam is very high volume but has lots of
duplication, everything else is somewhere in between.  They made an
attempt to associate spam domains with "affiliate networks" (the
business of spamming nowadays is structured as a multi-level marketing
scheme) but they didn't otherwise try to categorize the spam itself.
I can think of plenty of additional things to do with the data
set---which is the point: it says right in the abstract 'most studies
[of email spam] use a single "spam feed" and there has been little
examination of how such feeds may differ in content.'  They're not
trying so much to produce a comprehensive analysis *themselves* as to
alert people working in this subfield that they might be missing stuff
by looking at only one data source.
