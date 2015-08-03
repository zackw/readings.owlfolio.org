---
title: "Defending Tor from Network Adversaries:
        A Case Study of Network Path Prediction"
tags: [tor, routing, autonomous systems, traffic analysis, traceroute, anonymity]
authors:
 - Juen, Joshua
 - Das, Anupam
 - Johnson, Aaron
 - Borisov, Nikita
 - Caesar, Matthew
year: 2015
venue: preprint
eprints:
  arxiv: "1410.1823 [cs.CR]"
...

In a similar vein as [Tuesday's paper](/2014/anonymity-quicksand/),
this is an investigation of how practical it might be to _avoid_
exposing Tor circuits to traffic analysis by an adversary who controls
an Autonomous System.  Unlike Tuesday's paper, they assume that the
adversary does _not_ manipulate BGP to observe traffic that they
"shouldn't have" seen, so the concern is simply to ensure that the two
most sensitive links in the circuit---from client to entry, and from
exit to destination---do not pass through the same AS.  Previous
papers have suggested that the Tor client should predict the AS-level
paths involved in these links, and select entries and exits
accordingly [[1]][] [[2]][]. This paper observes that AS path
prediction is itself a difficult problem, and that different
techniques can give substantially different results.  Therefore, they
collected `traceroute` data from 28 Tor relays and compared AS paths
inferred from these traces with those predicted from BGP monitoring
(using the algorithm of "On AS-Level Path Inference" [[3]][]).

The core finding is that `traceroute`-based AS path inference does
indeed give substantially different results from BGP-based path
prediction.  The authors assume that `traceroute` is more accurate;
the discrepancy is consistently described as an _error_ in the
BGP-based prediction, and (since BGP-based prediction tends to
indicate exposure to more different ASes) as _overstating_ the risk
exposure of any given Tor link.  This seems unjustified to me.  The
standard `traceroute` algorithm is known to become confused in the
presence of load-balancing routers, which are extremely common in the
backbone [[4]][]; refinements have been proposed (and implemented in
the `scamper` tool used in this paper) but have problems themselves
[[5]][] [[6]][].  More elementally, `traceroute` produces a snapshot:
these UDP packets did take this route just now.  Tor links are
relatively long-lived TCP connections (tens of minutes) which could
easily be rerouted among several different paths over their lifetime.
I think it would be better to say that BGP path prediction produces a
_more conservative_ estimate of the ASes to which a Tor link could be
exposed, and highlight figuring out which one is more _accurate_ as
future work.

A secondary finding is that AS-aware path selection by the Tor client
interacts poorly with the "guard" policy, in which each Tor client
selects a small number of entry nodes to use for an extended period.
These nodes must be reliable and high-bandwidth; the economics of
running a reliable, high-bandwidth Internet server mean that they are
concentrated in a small number of ASes.  Similar economics apply to
the operation of exit nodes, plus additional legal headaches; as a
result, it may not be possible to find _any_ end-to-end path that
obeys both the guard policy and the AS-selection policy.  This
situation is, of course, worsened if you take the more conservative,
BGP-based estimation of AS exposure.

I've been concerned for some time that guards might actually be worse
for anonymity than the problem they are trying to solve.  The original
problem statement [[7]][] is that if you select an entry node at
random for each circuit, and some fraction of entry nodes are
malicious, with high probability you _will_ eventually run at least
one circuit through a malicious entry.  With guards, either _all_ your
circuits pass through a malicious entry for an extended period of
time, or _none_ do.  My fundamental concern with this is, first,
having all your traffic exposed to a malicious entry for an extended
period is probably _much worse_ for your anonymity than having one
circuit exposed every now and then; second, the hypothetical Tor
adversary has deep pockets and can easily operate reliable
high-bandwidth nodes, which are disproportionately likely to get
picked as guards.  Concentration of guards in a small number of ASes
only makes this easier for the adversary; concentration of guards
_together with exits_ in a small number of ASes makes it even easier.
It's tempting to suggest a complete about-face, preferentially
choosing entry nodes from the low-bandwidth, short-lived population
and using them only for a short time; this would also mean that entry
nodes could be taken from a much broader pool of ASes, and it would be
easier to avoid overlap with the AS-path from exit to destination.

[[1]]: http://freehaven.net/anonbib/cache/oakland2012-lastor.pdf
[[2]]: http://freehaven.net/anonbib/cache/DBLP:conf/ccs/EdmanS09.pdf
[[3]]: http://web.eecs.umich.edu/~zmao/Papers/routescope.pdf
[[4]]: https://hal.inria.fr/hal-01097553/document
[[5]]: http://pam2011.gatech.edu/papers/pam2011--Cunha.pdf
[[6]]: http://researchcommons.waikato.ac.nz/bitstream/handle/10289/5018/Measured%20impact.pdf
[[7]]: https://www.torproject.org/docs/faq#EntryGuards
