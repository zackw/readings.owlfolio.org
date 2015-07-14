---
title: "Cache Timing Attacks Revisited: Efficient and Repeatable
        Browser History, OS, and Network Sniffing"
tags: [privacy, information leakage, fingerprinting, web]
authors:
 - Bansal, Chetan
 - Preibusch, Sören
 - Milic-Frayling, Natasa
year: 2015
venue: IFIP SEC
eprints:
 doi: 10.1007/978-3-319-18467-8_7
...

"Cache timing attacks" use the time some operation takes to learn
whether or not a datum is in a cache.  They're inherently hard to fix,
because the entire *point* of a cache is to speed up access to data
that was used recently.  They've been studied as far back as Multics.
[[1]][] In the context of the Web, the cache in question (usually) is
the browser's cache of resources retrieved from the network, and the
attacker (usually) is a malicious website that wants to discover
something about the victim's activity on *other* websites. [[2]][]
[[3]][] This paper gives examples of using cache timing to learn
information needed for phishing, discover the victim's location, and
monitor the victim's search queries.  It's also known to be possible
to use the victim's browsing habits as an identifying fingerprint
[[4]][].

The *possibility* of this attack is well-known, but to date it has
been dismissed as an actual risk for two reasons: it was slow, and
probing the cache was a destructive operation, i.e. the attacker could
only probe any given resource once, after which it would be cached
whether or not the victim had ever loaded it.  This paper overcomes
both of those limitations.  It uses [Web Workers][] to parallelize
cache probing, and it sets a very short timeout on all its background
network requests---so short that the request can only succeed if it's
cached.  Otherwise, it will be cancelled and the cache will not be
perturbed.  (Network requests will always take at least a few tens of
milliseconds, whereas the cache can respond in less than a
millisecond.)  In combination, these achieve two orders of magnitude
speedup over the best previous approach, and, more importantly, they
render the attack repeatable.

What do we do about it?  Individual sites can mark highly sensitive
data not to be cached at all, but this slows the web down, and you'll
never get *everyone* to do it for *everything* that could be relevant.
Browsers aren't about to disable caching; it's too valuable.  A
possibility (not in this paper) is that we could notice the first time
a resource was loaded from a new domain, and deliberately delay
satisfying it from the cache by approximately the amount of time it
took to load off the network originally.  I'd want to implement and
test that to make sure it didn't leave a hole, but it seems like it
would allow us to have the cake and eat it.

In closing, I want to point out that this is a beautiful example of
the maxim that "[attacks always get better][]."  Cryptographers have
been banging that drum for decades, trying to get people to move away
from cipher primitives that are only a *little* weak before it's too
late, without much impact.  The same, it seems, goes for information
leaks.

[[1]]: http://www.multicians.org/timing-chn.html
[[2]]: http://web.stanford.edu/~jcm/papers/sameorigin.pdf
[[3]]: http://w2spconf.com/2014/papers/geo_inference.pdf
[[4]]: https://hal.inria.fr/hal-00747841/document
[Web Workers]: https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers
[attacks always get better]: https://tools.ietf.org/html/rfc4270#section-6
