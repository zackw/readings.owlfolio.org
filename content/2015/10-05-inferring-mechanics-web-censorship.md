---
title: "Inferring Mechanics of Web Censorship Around the World"
tags: [censorship, web, methodology]
authors:
 - Verkamp, John-Paul
 - Gupta, Minaxi
year: 2012
venue: FOCI
...

I've talked a bunch about papers that investigate *what* is being
censored online in various countries, but you might also want to know
*how* it's done.  There are only a few ways it *could* be done, and
this paper does a good job of laying them out:

* By DNS name: intercept DNS queries either at the router or the local
  DNS relay, return either "no such host" or a server that will hand
  out errors for everything.

* By IP address: in an intermediate router, discard packets intended
  for particular servers, and/or respond with TCP RST packets (which
  make the client disconnect) or forged responses.  (In principle, an
  intermediate router could pretend to be the remote host for an
  entire TCP session, but it doesn't seem that anyone does.)

* By data transferred in cleartext: again in an intermediate router,
  allow the initial connection to go through, but if blacklisted
  keywords are detected then forge a TCP RST.

There are a few elaborations and variations, but those are the basic
options if you are implementing censorship in the "backbone" of the
network.  The paper demonstrates that all are used.  It could also, of
course, be done at either endpoint, but that is much less common
(though not unheard of) and the authors of this paper ruled it out of
scope.  It's important to understand that the usual modes of
encryption used on the 'net today (e.g. HTTPS) do not conceal either
the DNS name or the IP address of the remote host, but *do* conceal
the remainder of an HTTP request.  Pages of an HTTPS-only website
cannot be censored individually, but the entire site *can* be censored
by its DNS name or server IP address.  This is why Github was being
DDoSed a few months ago to try to get them to delete repositories
being used to host circumvention tools [[1]][]: Chinese censors cannot
afford to block the entire site, as it is too valuable to their
software industry, but they have no way to block access to the
specific repositories they don't like.

Now, if you want to find out which of these scenarios is being carried
out by any given censorious country, you need to do detailed network
traffic logging, because at the application level, several of them are
indistinguishable from the site being down or the network unreliable.
This also means that the censor could choose to be stealthy: if
Internet users in a particular country expect to see an explicit
message when they try to load a blocked page, they might assume that a
page that always times out is just broken.  [[2]][] The *research*
contribution of this paper is in demonstrating how you do that,
through a combination of packet logging and carefully tailored probes
from hosts in-country.  They could have explained themselves a bit
better: I'm not sure they bothered to try to discriminate "packets are
being dropped at the border router" from "packets are being dropped by
a misconfigured firewall on the site itself", for instance.  Also, I'm
not sure whether it's worth going to the trouble of packet logging,
frankly.  You should be able to get the same high-level information by
comparing the results you get from country A with those you get from
country B.

Another common headache in this context is knowing whether the results
you got from your measurement host truly reflect what a "normal"
Internet user in the country would see.  After all, you are probably
using a commercial data center or academic network that may be under
fewer restrictions.  This problem is one of the major rationales for
Encore, which I discussed a couple weeks ago [[3]][].  This paper nods
at that problem but doesn't really dig into it.  To be fair, they
*did* use "personal contacts" to make some of their measurements, so
those may have involved residential ISPs, but they are
(understandably) vague about the details.

[[1]]: https://citizenlab.org/2015/04/chinas-great-cannon/
[[2]]: https://www3.cs.stonybrook.edu/~phillipa/papers/TWeb.pdf
[[3]]: /2015/encore-lightweight-measurement-web-censorship/
