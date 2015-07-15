---
title: "An Automated Approach for Complementing Ad Blockers' Blacklists"
tags: [privacy, machine learning, web]
authors:
 - Gugelmann, David
 - Happe, Markus
 - Ager, Bernhard
 - Lenders, Vincent
year: 2015
venue: PETS
eprints:
 doi: 10.1515/popets-2015-0018
url: https://petsymposium.org/2015/papers/19_Gugelmann.pdf
...

Last week's long PETS paper was very abstract; this week's paper is
very concrete.  The authors are concerned that manually-curated
blacklists, as currently used by most ad-blocking software, cannot
hope to keep up with the churn in the online ad industry.  (I saw a
very similar talk at WPES back in 2012 [[1]][] which quoted the
statistic that the default AdBlock Plus filter list contains 18,000
unique URLS, with new ones added at a rate of five to 15 every week.)
They propose to train a machine classifier on *network-level*
characteristics that differ between ad services and "normal" web
sites, to automate detection of new ad providers and/or third-party
privacy-invasive analytics services.  (This is the key difference from
the paper at WPES 2012: that project used static analysis of
JavaScript delivered by third-party services to extract features for
their classifier.)

They find that a set of five features provides a reasonably effective
classification: proportion of requests that are 'third-party'
(for transclusion into another website), number of unique referrers,
ratio of received to sent bytes, and proportion of requests including
cookies.  For the training set they used, they achieve 83% precision
and 85% recall, which is reasonable for a system that will be used
to identify candidates for manual inspection and addition to blacklists.

There are several methodological bits in here which I liked.  They use
[entropy-based discretization][] and [information gain][] to identify
valuable features and discard unhelpful ones.  They compare a
classifier trained on manually-labeled data (from a large HTTP traffic
trace) with a classifier trained on the default AdBlock Plus filter
list; both find similar features, but the ABP filter list has better
coverage of *infrequently used* ads or analytics services, whereas the
manually labeled training set catches a bunch of *common* ads and
analytics services that ABP missed.

One fairly significant gap is that the training set is limited to
cleartext HTTP.  There's a strong trend nowadays toward HTTPS for
everything, including ads, but established ad providers are finding it
difficult to cut all their services over efficiently, which might
provide an opportunity for new providers---and thus cause a shift
toward providers that have been missed by the blacklists.

There's almost no discussion of false positives.  Toward the end there
is a brief mention of third-party services like Gravatar and Flattr,
that share a usage pattern with ads/analytics and showed up as false
positives.  But it's possible to enumerate common types of third-party
services (other than ads and analytics) _a priori:_ outsourced
commenting (Disqus, hypothes.is), social media "share buttons"
(Facebook, Twitter), shared hosting of resources (jQuery, Google
Fonts), static-content CDNs, etc.  Probably, most of these are weeded
out by the "ratio of received to sent bytes" check, but I would still
have liked to see an explicit check of at least a few of these.

And finally, nobody seems to have bothered talking to the people who
actually maintain the ABP filter lists to find out how _they_ do it.
(I suspect it relies strongly on manual, informal reporting to a forum
or something.)  If this is to turn into anything more than an
experiment, people need to be thinking about integration and
operationalization.

[[1]]: https://www.cs.indiana.edu/~minaxi/pubs/wpes12.pdf
[entropy-based discretization]: https://www.aaai.org/Papers/KDD/1996/KDD96-019.pdf
[information gain]: http://www.autonlab.org/tutorials/infogain.html
