---
title: Regional Variation in Chinese Internet Filtering
tags: [censorship, china, dns, field observations]
authors:
 - Joss Wright
year: 2014
volume: 17
issue: 1
pages: 121--141
venue: j.ics
doi: 10.1080/1369118X.2013.853818
url: http://ssrn.com/abstract=2265775
...

This is one of the earlier papers that looked specifically for
regional variation in China's internet censorship; as I mentioned when
reviewing
"[Large-scale Spatiotemporal Characterization of Inconsistencies in the World’s Largest Firewall][[1]],"
assuming that censorship is monolithic is unwise in general and
especially so for a country as large, diverse, and technically
sophisticated as China.  This paper concentrates on variation in
DNS-based blockade: they probed 187 DNS servers in 29 Chinese cities
(concentrated, like the population, toward the east of the country)
for a relatively small number of sites, both highly likely and highly
unlikely to be censored within China.

The results reported are maybe better described as "inconsistencies
among DNS servers" than "regional variation".  For instance, there are
no sites called out as accessible from one province but not another.
Rather, roughly the same set of sites is blocked in all locales, but
all of the blocking is somewhat leaky, and some DNS servers are more
likely to leak---regardless of the site---than others.  The type of
DNS response when a site is blocked also varies from server to server
and site to site; observed behaviors include no response at all, an
error response, or (most frequently) a success response with an
incorrect IP address.  Newer papers (e.g. [[1]][] [[2]][]) have
attempted to explain some of this in terms of the large-scale network
topology within China, plus periodic "outages" when nothing is
filtered at all, but I'm not aware of any wholly compelling analysis
(and short of a major leak of internal policy documents, I doubt
we can ever have one).

There's also an excellent discussion of the practical and ethical
problems with this class of research.  I suspect this was largely
included to justify the author's choice to only look at DNS filtering,
despite its being well-known that China also uses several other
techniques for online censorship.  It nonetheless provides valuable
background for anyone wondering about methodological choices in this
kind of paper.  To summarize:

 * Many DNS servers accept queries from the whole world, so they can
   be probed directly from a researcher's computer; however, they
   might vary their response depending on the apparent location of the
   querent, their use of UDP means it's hard to tell censorship by the
   server itself from censorship by an intermediate DPI router, and
   there's no way to know the geographic distribution of their
   intended clientele.

 * Studying most other forms of filtering requires measurement clients
   within the country of interest.  These can be dedicated proxy
   servers of various types, or computers volunteered for the
   purpose.  Regardless, the researcher risks inflicting legal
   penalties (or worse) on the operators of the measurement clients;
   even if the censorship authority normally takes no direct action
   against people who merely try to access blocked material, they
   might respond to a sufficiently high volume of such attempts.

 * Dedicated proxy servers are often blacklisted by sites seeking to
   reduce their exposure to spammers, scrapers, trolls, and DDoS
   attacks; a study relying exclusively on such servers will therefore
   tend to overestimate censorship.

 * Even in countries with a strong political commitment to free
   expression, there are some things that are illegal to download or
   store; researchers must take care not to do so, and the simplest
   way to do that is to avoid retrieving anything other than text.

[[1]]: /2014/inconsistencies-worlds-largest-firewall/
[[2]]: http://arxiv.org/pdf/1410.0735
