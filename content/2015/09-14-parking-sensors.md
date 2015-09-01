---
title: "Parking Sensors: Analyzing and Detecting Parked Domains"
tags: [advertising, malware, machine learning, software ecology, web]
authors:
 - Vissers, Thomas
 - Joosen, Wouter
 - Nikiforakis, Nick
year: 2015
venue: NDSS
eprints:
 doi: 10.14722/ndss.2015.23053
...

In the same vein as the [ecological study of ad injectors][ad-inj] I
reviewed back in June, this paper does an ecological analysis of
[domain parking][].  Domain parking is the industry term of art for
the practice of registering a whole bunch of domain names you don't
have any particular use for but hope someone will buy, and while you
wait for the buyer, sticking a website consisting entirely of ads in
the space, usually with "This domain is for sale!" at the top in big
friendly letters.  Like many ad-driven online business models, domain
parking can be mostly harmless or it can be a lead-in to outright
scamming people and infesting their computers with malware, and the
research question in this paper is, how bad does it get?

In order to answer that question, the authors carried out a
modest-sized survey of 3000 parked domains, identified by trawling the
DNS for name servers associated with 15 known parking services.  (Also
like many other online businesses, domain parking runs on an affiliate
marketing basis: lots of small fry register the domains and then hand
the keys over to big services that do the actual work of maintaining
the websites with the ads.)  All of these services engage in all of
the abusive behavior one would expect: [typosquatting][], aggressive
behavioral ad targeting, drive-by malware infection, and feeding
visitors to scam artists and phishers.  I do not come away with a
clear sense of _how common_ any of these attacks are relative to the
"default" parking page of advertisements and links---they have
numbers, but they're not very well organized, and different sets of
parking pages were used in each section (discussing a different type
of abuse) which makes it hard to compare across sections.

I'm most interested in the last section of the paper, in which they
develop a machine classifier that can distinguish parking pages from
"normal" webpages, based on things like the amount of text that is and
isn't a hyperlink, number of external links, total volume of resources
drawn from third-party sources, and so on.  The bulk of this section
is devoted to enumerating all of the features that they _tested_, but
doesn't do a terribly good job of explaining which features wound up
being _predictive_.  Algorithmic choices also seem a little arbitrary.
They got 97.9% true positive rate and 0.5% false positive rate out of
it, though, which says to me that this isn't a terribly challenging
classification problem and probably most anything would have worked.
(This is consistent with the intuitive observation that you, a human,
can tell at a glance when you've hit a parking page.)

[ad-inj]: /2015/ad-injection-at-scale/
[domain parking]: https://en.wikipedia.org/wiki/Domain_parking
[typosquatting]: https://en.wikipedia.org/wiki/Typosquatting
