---
title: "Anonymity on QuickSand: Using BGP to Compromise Tor"
tags: [bgp, tor, traffic analysis, autonomous systems, routing]
authors:
 - Vanbever, Laurent
 - Li, Oscar
 - Rexford, Jennifer
 - Mittal, Prateek
year: 2014
venue: HotNets
pages: 14:1--14:7
eprints:
  doi: 10.1145/2670518.2673869
pdf_url: http://conferences.sigcomm.org/hotnets/2014/papers/hotnets-XIII-final80.pdf
...

One of the oldest research threads regarding [Tor][] is trying to
figure out how close you could get in real life to the "global passive
adversary" that's known to be able to deanonymize all communications.
This is a new entry in that line of research, from [HotNets 2014][].

At the largest scale, the global Internet is administratively divided
into "[autonomous systems][]" (ASes) that exchange traffic, using
[BGP][] for configuration.  Any given AS can only communicate with a
small number of direct "peers", so a stream of packets will normally
pass through many different ASes on the way to its destination.  It's
well-known that AS-operated backbone routers are in an excellent
position to mount traffic-correlation attacks on Tor, particularly if
they collude [[1]][] [[2]][].  The key observation in *this* paper is
that, by manipulating BGP, a malicious AS can observe traffic that
wouldn't naturally flow through it.

BGP is an old protocol, originally specified in 1989; like most of our
older protocols, it assumes that all participants are cooperative and
honest.  Any backbone router can "announce" that it is now capable of
forwarding packets to a "prefix" (set of IP addresses) and the rest of
the network will believe it.  Incidents where traffic is temporarily
redirected to an AS that either can't get it to the destination at
all, or can only do so suboptimally, are commonplace, and people argue
about how malicious these are. [[3]][] [[4]][] [[5]][] Suppose an
adversary can observe one end of a Tor circuit---perhaps they control
the ISP for a Tor client.  They also have some reason to suspect a
particular destination for the traffic.  They use BGP to hijack
traffic to the suspected destination, passing it on so that the client
doesn't notice anything.  They can now observe both ends of the
circuit and confirm their suspicions.  They might not get to see
traffic in both directions, but the authors also demonstrate that a
traffic-correlation attack works in principle even if you can only see
the packet flow in one direction, thanks to TCP acknowledgments.

Making this worse, high-bandwidth, long-lived Tor relays (which are
disproportionately likely to be used for either end of a circuit) are
clustered in a small number of ASes worldwide.  This means an
adversary can do "dragnet" surveillance by hijacking all traffic to
some of those ASes; depending on its own position in the network, this
might not even appear abnormal.  The adversary might even *be* one of
those ASes, or an agency in a position to lean on its operators.

The countermeasures proposed in this paper are pretty weak; they would
only operate on a timescale of hours to days, whereas a BGP hijack can
happen, and stop happening, in a matter of minutes.  I don't see a
*good* fix happening anywhere but in the routing protocol itself.
Unfortunately, routing protocols that do *not* assume honest
participants are still a topic of basic research.  (I may get to some
of those papers eventually.)  There are proposals for adding a notion
of "this AS is authorized to announce this prefix" to BGP [[6]][] but
those have all the usual problems with substituting "I trust this
organization" for "I have verified that this data is accurate".

[Tor]: https://www.torproject.org/about/overview.html
[HotNets 2014]: http://conferences.sigcomm.org/hotnets/2014/index.html
[autonomous systems]: https://en.wikipedia.org/wiki/Autonomous_system_%28Internet%29
[BGP]: https://en.wikipedia.org/wiki/Border_Gateway_Protocol
[[1]]: http://freehaven.net/anonbib/full/topic.html#feamster:wpes2004
[[2]]: http://freehaven.net/anonbib/full/topic.html#ccs2013-usersrouted
[[3]]: http://www.arbornetworks.com/asert/2008/02/internet-routing-insecuritypakistan-nukes-youtube/
[[4]]: http://www.arbornetworks.com/asert/2010/11/china-hijacks-15-of-internet-traffic/
[[5]]: http://www.bgpmon.net/bgp-routing-incidents-in-2014-malicious-or-not/
[[6]]: http://www.bgpmon.net/securing-bgp-routing-with-rpki-and-roas/
