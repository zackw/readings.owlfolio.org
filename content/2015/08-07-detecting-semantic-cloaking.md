---
title: "Detecting Semantic Cloaking on the Web"
tags: [web, spam, machine learning]
authors:
 - Wu, Baoning
 - Davison, Brian D.
year: 2006
venue: WWW
eprints:
 doi: 10.1145/1135777.1135901
url: http://wwwconference.org/www2006/programme/files/pdf/6014.pdf
...

Now for something a little different: today's paper is about detecting
search engine spam.  Specifically, it's about detecting when a Web
site presents different content to a search engine's "crawler" than it
does to human visitors.  As the article points out, this can happen
for benign or even virtuous reasons: a college's front page might
rotate through a selection of faculty profiles, or a site might strip
out advertising and other material that is only relevant to human
visitors when it knows it's talking to a crawler.  However, it also
happens when someone wants to fool the search engine into ranking
their site highly for searches where they don't actually have relevant
material.

To detect such misbehavior, obviously one should record each webpage
as presented to the crawler, and then again as presented to a human
visitor, and compare them.  The paper is about two of the technical
challenges which arise when you try to execute this plan.  (They do
not claim to have solved _all_ of the technical challenges in this
area.)  The first of these is, of course, "how do you program a
computer to tell when a detected difference is spam, versus when it is
benign?" and here they have done something straightforward: supervised
machine classification.  You could read this paper just as a case
study in semi-automated feature selection for a machine classifier,
and you would learn something.  (Feature selection is somewhat of a
black art---features that appear to be highly predictive may be
accidents of your sample, and features that logically _should_ be
predictive might not work out at all.  In this case, the "positive
features" they list seem plausibly motivated, but several of the
"negative features" (features which are anticorrelated with spamming)
seem likely to be accidental.  I would have liked to see more analysis
of _why_ each feature is predictive.)

The second technical challenge is less obvious: sites are updated
frequently.  You don't want to mistake an update for any kind of
variation between the crawl result and the human-visitor result.  But
it's not practical to visit a site simultaneously as the crawler and
as the human, just because of how many sites a crawl has to touch (and
if you did, the spammers might be able to figure out that your "human"
visit was an audit).  Instead, you could visit the site repeatedly as
each and see if the changes match, but this is expensive.  The paper
proposes to weed out sites that *don't* change at all between the
crawler visit and the "human" visit, and do the more expensive check
only to the sites that do.  A refinement is to use a heuristic to pick
out changes that are more likely to be spam: presence of *additional*
keywords or links in the crawler version, relative to the human
version.  In their tests, this cuts the number of sites that have to
be investigated in detail by a factor of 10 (and could do better by
refining the heuristic further).  These kinds of manual filter
heuristics are immensely valuable in classification problems when one
of the categories (no cloaking) is much larger than the other(s), both
because it reduces the cost of running the classifier (and, in this
case, the cost of data collection), and because machine-learning
classifiers often do better when the categories all have roughly the
same number of examples.

This paper shouldn't be taken as the last word in this area: it's ten
years old, its data set is respectable for an experiment but tiny
compared to the global 'net, and false positive and negative rates of
7% and 15% (respectively) are much too large for production use.  The
[false positive paradox][] is your nemesis when you are trying to weed
spammers out of an index of 10^9^ websites.  We know from what little
they've said about it in public (e.g. [[1]][] [[2]][]) that Google does
something much more sophisticated.  But it is still valuable as a
starting point if you want to learn how to do this kind of research
yourself.

[false positive paradox]: https://en.wikipedia.org/wiki/False_positive_paradox
[[1]]: http://googlewebmastercentral.blogspot.com/2010/11/how-to-help-google-identify-web-spam.html
[[2]]: http://googlewebmastercentral.blogspot.com/2012/04/another-step-to-reward-high-quality.html
