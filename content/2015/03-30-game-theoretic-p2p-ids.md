---
title: "Game-theoretic Patrolling Strategies for Intrusion Detection
        in Collaborative Peer-to-Peer Networks"
tags: [theory, game theory, intrusion detection, peer to peer]
authors:
 - Narang, Pratik
 - Mehta, Kunal
 - Hota, Chittaranjan
year: 2014
bibtex_type: unpublished
doi: 10.13140/2.1.2533.2804
url: http://www.bits-pilani.ac.in/uploads/Hyderabad/hota/Pratik-hota.pdf
...

Commercial intrusion detection systems are designed for corporate
networks; they almost always assume a small number of choke points
between internal and external networks, and often they also assume
centralized control of all the devices on the internal network.
Neither assumption is valid for a peer-to-peer "overlay" network,
where there are typically a large number of mutually distrusting human
agencies operating a small number of network peers each, and the
routes between them are diverse.

It might seem that in the peer-to-peer environment, each node would
have no choice but to run its own IDS.  However, if we are willing to
assume _some_ degree of trust vested in other node operators, perhaps
the task could be delegated.  That's the germ of this paper.  For an
idealized peer-to-peer network, they derive a game-theoretically
optimal strategy for rotating the job of running the IDS around all
the "super-peers" (long-lived nodes with extra responsibilities; many
real P2P networks have such nodes).

I like the concept, but the idealized scenario they used may be _too_
idealized to be applicable in real life.  Key assumptions which
probably don't hold include:

 * The attacker does not already control any super-peers.
 * The IDS is perfect: that is, if attack traffic passes through a
   node running an IDS, the attack _will_ be detected and blocked.
 * The attacker's goal is to take control of, or deny availability of,
   a specific set of super-peers.
 * The defender can predict in advance which nodes will be attacked.
   (I would accept this if it were probabilistic, e.g. assuming that
   the attacker is more likely to target nodes that contribute more to
   to the overall network capacity.)

I think a more realistic model would go something like this: The
attacker is assumed already to control some fraction of the
super-peers.  (The attacker may _also_ mount attacks from other
computers, either independently or in collaboration with malicious
super-peers.)  The attacker seeks to avoid detection, and so does not
mount overt attacks on other super-peers; instead, it has some
strategy for violating the _protocol_ to achieve an adversarial goal
(e.g. forging blockchain transactions, deanonymizing users, delivering
false data to users) The malicious peers execute the protocol honestly
_most_ of the time, but sometimes break the rules.  The defender's
goal is to detect peers that are violating the protocol often enough
that this can't be an accident, while not wasting too many resources
on monitoring overhead.

> Note: This paper is said to have been published in the
> "[International Conference on Secure Knowledge Management in Big-data era, 2014](https://web.archive.org/web/20140829073258/http://www.bits-dubai.ac.ae/skm2014/)"
> but I cannot confirm this, as the conference website no longer
> exists and the Internet Archive's copy does not include a program.
