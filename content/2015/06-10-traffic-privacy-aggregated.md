---
title: "Protecting traffic privacy for massive aggregated traffic"
tags: [traffic analysis, overlay networks, privacy]
authors:
 - Iacovassi, Alfonso
 - Baiocchi, Andrea
year: 2015
venue: J.ComNet
volume: 77
pages: 1--17
eprints:
 doi: 10.1016/j.comnet.2014.11.019
...

Nowadays we are pretty darn sure we know how to encrypt network
packets in transit such that there's no realistic way to decrypt them.
There are a whole host of second-order problems that are not as well
solved, but basic message confidentiality is done---except for one
thing: the length and timing of each packet are still visible to
anyone who can monitor the "wire."  It turns out that this enables
eavesdroppers to extract a frightening amount of information from
those encrypted packets, such as which page of a medical-advice website you
are reading [[1]][], the language of your VoIP phone call [[2]][], or
even a *transcript* of your VoIP phone call [[3]][].

In principle, we know how to close this information leak.  It is
simply necessary for Alice to send Bob a continuous stream of
fixed-size packets, at a fixed rate, forever, whether or not she has
anything useful to say.  (When she doesn't have anything useful to
say, she can encrypt an endless stream of binary zeroes.)  This is
obviously a non-starter in any context where Alice cares about power
consumption, shared channel capacity, or communicating with more than
one Bob.  Even when none of these is a concern---for instance,
high-volume VPN links between data centers, which are running at
significant utilization 24x7x365 anyway---forcing all traffic to fit
the constant packet length and transmission schedule adds significant
overhead.  Thus, there's a whole line of research trying to minimize
that overhead, and/or see how far we can back down from the
ideal-in-principle case without revealing too much.

Today's paper offers a theoretical model and test framework that
should make it easier to experiment with the high-volume-VPN-link
case.  I like it for its concreteness---often theoretical modeling
papers feel so divorced from practice that it's hard to see how to do
anything constructive with them.  It is also easy to see how the model
could be extended to more sophisticated traffic-shaping techniques,
which would be the obvious next step.  The big downside, though, is
that it only considers a fixed network topology: Alice talking to Bob
and no one else, ever.  Even for inter-data-center links, topologies
can change on quite short notice, and a topology-change event might be
exactly what Eve is listening for (perhaps it gives her advance notice
of some corporate organizational change).  To be fair, the "continuous
stream of fixed size packets" scheme does completely solve the
length-and-timing issue in principle; we do not have nearly as good
schemes for concealing who is talking to whom, even in principle.
Which is unfortunate, because you can do *even more terrifying* things
with knowledge only of who is talking to whom. [[4]][]


[[1]]: http://research.microsoft.com/pubs/119060/webappsidechannel-final.pdf
[[2]]: http://static.usenix.org/events/sec07/tech/full_papers/wright/wright_html/
[[3]]: https://www.ieee-security.org/TC/SP2011/PAPERS/2011/paper001.pdf
[[4]]: http://www.slate.com/articles/health_and_science/science/2013/06/prism_metadata_analysis_paul_revere_identified_by_his_connections_to_other.single.html
