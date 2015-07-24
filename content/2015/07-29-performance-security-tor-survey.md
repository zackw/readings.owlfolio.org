---
title: "Performance and Security Improvements for Tor: A Survey"
tags: [survey paper, privacy, anonymity, traffic analysis, protocol design, tor]
authors:
 - AlSabah, Mashael
 - Goldberg, Ian
year: 2015
venue: preprint
eprints:
 iacr: 2015/235
...

This week's non-PETS paper is a broad survey of research into
improving either the security, or the performance, or both, of
low-latency anonymity networks such as Tor.  Nearly all of the
research used Tor itself as a testbed, and the presentation here
assumes Tor, but most of the work could be generalized to other
designs.

There's been a lot of work on this sort of thing in the eleven years
since Tor was first introduced, and this paper does a generally good
job of categorizing it, laying out lines of research, indicating which
proposals have been integrated into Tor and which haven't, etc.  (I
particularly liked the mindmap diagram near the beginning, and the
discussion near the end of which problems still need to get solved.)
One notable exception is the section on improved cryptography, where
you need to have a solid cryptography background to get any idea of
what the proposals are, let alone whether they worked.  There are also
a couple of places where connections to the larger literature of
network protocol engineering would have been helpful: for instance,
there's not a single mention of [bufferbloat][], even though that is
clearly an aspect of the congestion problems that one line of research
aims to solve.  And because it's not mentioned, it's not clear whether
the researchers doing that work knew about it.

Tor is a difficult case in protocol design because its security goals
are---as acknowledged in the original paper describing its design
[[1]][]---directly in conflict with its performance goals.
Improvements in end-to-end latency, for instance, may make a
[traffic correlation][] attack easier.  Improvements in queueing
fairness or traffic prioritization may introduce inter-circuit
"crosstalk" enabling an attacker to learn something about the
traffic passing through a relay.  Preferring to use high-bandwidth
relays improves efficiency but reduces the number of possible paths
that traffic can take.  And so on.  It is striking, reading through
this survey, to see how often an apparently good idea for performance
was discovered to have unacceptable consequences for anonymity.

[bufferbloat]: http://www.bufferbloat.net/projects/bloat/wiki/Introduction
[[1]]: https://svn.torproject.org/svn/projects/design-paper/tor-design.pdf
[traffic correlation]: http://www.ohmygodel.com/publications/usersrouted-ccs13.pdf
