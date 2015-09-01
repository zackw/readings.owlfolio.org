---
title: "Detecting Internet Filtering from Geographic Time Series"
tags: [machine learning, censorship, tor, time series, anomaly detection]
authors:
 - Wright, Joss
 - Darer, Alexander
 - Farnan, Oliver
year: 2015
venue: preprint
eprints:
 arxiv: 1507.05819 [cs.CY]
...

We're picking back up with a paper that's brand new---so new that it
exists only as an [arXiv][] preprint and I don't know if it is planned
to be published anywhere.  It probably hasn't gone through formal peer
review yet.

Wright and colleagues observe that because [Tor][] is commonly used to
evade censorship, changes in the
[number of people using Tor from any given country][metrics-direct-users]
are a signal of a change in the censorship régime in that country.
This isn't a new idea: the Tor project itself has been
[doing something similar since 2011][tr-detector].  What this paper
does is present an improved algorithm for detecting such changes.  It
uses [<abbr title="principal components analysis">PCA</abbr>][pca] to
compare the time series of Tor active users across countries.  The
idea is that if there's a change in Tor usage worldwide, that probably
doesn't indicate censorship, but a change in just a few countries is
suspicious.  To model this using PCA, they tune the number of
"principal components" so that the projected data matrix is
well-divided into what they call "normal" and "anomalous" subspaces;
large components in the anomalous subspace for any data vector
indicate that that country at that time is not well-predicted by all
the other countries, i.e. something fishy is going on.

They show that their algorithm can pick out previously
known cases where a change in Tor usage is correlated with a change in
censorship, and that its top ten "most anomalous" countries are mostly
the countries one would expect to be suspicious by this metric---but
also a couple that nobody had previously suspected, which they
highlight as a matter needing further attention.

PCA used as an anomaly detector is a new idea on me.  It seems like
they could be extracting more information from it than they are.  The
graphs in this paper show what's probably a _global_ jump in Tor usage
in mid-2013; this has a [clear explanation][], and they show that
their detector _ignores_ it (as it's supposed to), but can they make
their detector call it out _separately_ from country-specific events?
PCA should be able to do that.  Similarly, it seems quite probable
that the ongoing revolutions and wars in the Levant and North Africa
are causing _correlated_ changes to degree of censorship region-wide;
PCA should be able to pull that out as a separate explanatory
variable.  These would both involve taking a closer look at the
"normal subspace" and what each of its dimensions mean.

It also seems to me that a bit of preprocessing, using standard
[time series decomposition][] techniques, would "clean up" the
analysis and make its results easier to interpret.  There's not one
word about that possibility in the paper, which seems like a major
omission; decomposition is the first thing that anyone who knows
anything about time series analysis would think of.  In this case, I
think seasonal variation should definitely be factored out, and
removing _linear_ per-country trends might also helpful.

[arXiv]: https://arxiv.org/
[Tor]: https://www.torproject.org/
[metrics-direct-users]: https://metrics.torproject.org/userstats-relay-country.html
[tr-detector]: https://research.torproject.org/techreports/detector-2011-09-09.pdf
[pca]: https://en.wikipedia.org/wiki/Principal_components_analysis
[clear explanation]: http://www.theguardian.com/world/series/the-snowden-files
[time series decomposition]: https://www.otexts.org/fpp/6
