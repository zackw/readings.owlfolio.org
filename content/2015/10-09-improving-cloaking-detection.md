---
title: "Improving Cloaking Detection Using Search Query Popularity and Monetizability"
tags: [web, spam, machine learning, adversarial optimization, economics]
authors:
 - Chellapilla, Kumar
 - Chickering, David Maxwell
year: 2006
venue: AIRWeb
url: http://chickeringfamily.org/publications/airweb2006.pdf
...

Here's another paper about detecting search engine spam, contemporary
with "[Detecting Semantic Cloaking on the Web][]" and, in fact,
presented as a refinement to that paper.  They don't make any changes
to the "is this page spamming the search engine" algorithm itself;
rather, they optimize the *scan* for pages that are spamming the
search engine, by looking at the spammers' economic incentives.

It obviously does no good to make your site a prominent search hit for
keywords that nobody ever searches for.  Less obviously, since search
engine spammers are trying to make money by sucking people into
linkfarms full of ads, they should be focusing on keywords that lots
of advertisers are interested in ("monetizability" in the paper's
jargon).  Therefore, the search engine operator should focus its
spam-detection efforts on the most-searched and most-advertised
keywords.  Once you identify a linkfarm, you can weed it out of *all*
your keyword indexes, so this improves search results in the "long
tail" as well as the popular case.

They performed a quick verification of this hypothesis with the help
of logs of the 5000 most popular and 5000 most advertised search
keywords, from the MSN search engine (now Bing).  Indeed, the spam was
strongly skewed toward both high ends---somewhat more toward
monetizability than popularity.

That's really all there is to say about this paper.  They had a good
hypothesis, they tested it, and the hypothesis was confirmed.  I'll
add that this is an additional reason (besides just making money) for
search engines to run their own ad brokerages, and a great example of
the value of applying economic reasoning to security research.

[Detecting Semantic Cloaking on the Web]: /2006/detecting-semantic-cloaking/
