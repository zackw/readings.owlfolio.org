---
title: "Scandinista! Analyzing TLS Handshake Scans and HTTPS Browsing
by Website Category"
tags: [https, large sample]
authors:
 - Andrew Hills
year: 2015
venue: SATS
url: https://satsymposium.org/papers/scandanista.pdf
...

Today's paper is a pilot study, looking into differences in adoption
rate of HTTPS between various broad categories of websites (as defined
by [Alexa][]).  They looked at raw availabilty of TLS service on port
443, and they also checked whether an HTTP request for the front page
of each Alexa domain would redirect to HTTPS or vice versa.  This test
was conducted only once, and supplemented with historical data from
the University of Michigan's [HTTPS Ecosystem][] project.

As you would expect, there is a significant difference in the current
level of HTTPS availability from one category to another.  They only
show this information for a few categories, but the pattern is not
terribly surprising: shopping 82%, business 70%, advertisers 45%,
adult 36%, news 30%, arts 26%.  (They say "The relatively low score
for Adult sites is surprising given that the industry has a large
amount of paid content", but I suspect this is explained by that
industry's habit of outsourcing payment processing, plus the
ubiquitous (not just in the adult category) misapprehension that
*only* payment processing is worth bothering to encrypt.)  It is also
not surprising to find that more popular sites are more likely to
support HTTPS.  And the enormous number of sites that redirect their
front page *away from* HTTPS is depressing, but again, not surprising.

What's more interesting to me is the trendlines, which show a steady,
slow, category-independent, linear uptake rate.  There's a little bit
of a bump in adult and news around 2013 but I suspect it's just noise.
(The "response growth over time" figure (number 2), which appears to
show a category dependence, is improperly normalized and therefore
misleading. You want to look only at figure 1.)  The paper looks for a
correlation with the "Snowden revelations"; I'd personally expect that
the dominant causal factor here is the difficulty of setting up TLS,
and I'd like to see them look for correlations with major changes in
*that:* for instance, Cloudflare's offering no-extra-cost HTTPS
support [[1]][], Mozilla publishing a server configuration guide
[[2]][], or the upcoming "Let's Encrypt" no-hassle CA [[3]][].  It
might also be interesting to look at uptake rate as a function of
ranking, rather than category; it *seems* like the big names are
flocking to HTTPS lately, it would be nice to know for sure.

The study has a number of methodological problems, which is OK for a
pilot, but they need to get fixed before drawing serious conclusions.
I already mentioned the normalization problem in figure 2: I think
they took percentages _of percentages_, which doesn't make sense.  The
right thing would've been to just subtract the initial level seen in
figure 1 from each line, which (eyeballing figure 1) would have
demonstrated an increase of about 5% in each category over the time
period shown, with no evidence for a difference between categories.
But before we even get that far, there's a question of the difference
between an IP address (the unit of the UMich scans), a website (the
unit of TLS certificates), and a domain (the unit of Alexa ranking).
To take some obvious examples: There are hundreds, if not thousands,
of IP addresses that will all answer to the name of `www.google.com`.
Conversely, [Server Name Indication][] permits _one_ IP address to
answer for dozens or even hundreds of encrypted websites, and that
practice is even more common over unencrypted HTTP.  And hovering
around #150 in the Alexa rankings is `amazonaws.com`, which is the
backing store for at least tens of thousands of different websites,
each of which has its own subdomain and may or may not have configured
TLS.  The correct primary data sources for this experiment are not
Alexa and IPv4 scanning, but DNS scanning and
[certificate transparency][] logs.  (A major search engine's crawl
logs would also be useful, if you could get your hands on them.)
Finally, they should pick one set of 10-20 mutually exclusive,
exhaustive categories (one of which would have to be "Other") and
_consistently use them throughout the paper_.

[Alexa]: http://alexa.com/topsites/category
[HTTPS Ecosystem]: https://scans.io/study/umich-https
[[1]]: https://blog.cloudflare.com/introducing-universal-ssl/
[[2]]: https://wiki.mozilla.org/Security/Server_Side_TLS
[[3]]: https://letsencrypt.org/
[Server Name Indication]: https://en.wikipedia.org/wiki/Server_Name_Indication
[certificate transparency]: https://certificate-transparency.org/
