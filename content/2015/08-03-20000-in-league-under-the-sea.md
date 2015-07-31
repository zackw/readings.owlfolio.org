---
title: "20,000 In League Under The Sea: Anonymous Communication,
        Trust, MLATs, and Undersea Cables"
tags: [anonymity, autonomous systems, bgp, routing, tor, theory,
       threat modeling, belief networks]
authors:
 - Jaggard, Aaron D.
 - Johnson, Aaron
 - Cortes, Sarah
 - Syverson, Paul
 - Feigenbaum, Joan
year: 2015
venue: PETS
eprints:
 doi: 10.1515/popets-2015-0002
url: https://www.petsymposium.org/2015/papers/04_Jaggard.pdf
...

Today's paper takes another shot at modeling how the physical topology
of the Internet affects the security of Tor against passive
adversaries with the ability to snoop on a lot of traffic.  It's by
some of the same people who wrote
"[Defending Tor from Network Adversaries](/2015/network-path-prediction/)"
and is quite closely related.

Most of the work of this paper goes into building a flexible, formal
threat model, which Tor client software could (in principle) use to
inform its routing decisions.  Acknowledging that there's always going
to be a good deal of uncertainty about what adversaries are out there
and what they are capable of, they make two key design decisions.  The
model is probabilistic (based on a Bayesian belief network), and it
takes user input.  For instance, if you have reason to think the
government of Transbelvia has it in for you, you can instruct Tor to
avoid paths that Transbelvia might be able to snoop on, and the model
will expand that out to all the ways they might do that.  Conversely,
if you trust a particular organization you might like to
preferentially use its guards or exit nodes, and it can do that too.

The model is very thorough about different ways a government might be
able to snoop on network traffic---not just relays physically hosted
in the country, but [AS][]es and [IXP][]s (Transbelvia hosts a major
IXP for Eastern Europe), submarine cable landing sites (not relevant
for a landlocked country), "mutual legal assistance treaties" (MLATs)
which might be used to have another country do some snooping on
Transbelvia's behalf, and even hacking into and subverting routers
at interesting points in the connectivity graph.  (The pun in the
title refers to their analysis of how MLATs could allow several of the
usual suspects to snoop on 90+% of *all* submarine cable traffic, even
though they host hardly any cable landings themselves.)  Equally
important, it can be expanded at need when new techniques for spying
are revealed.

I think something like this is going to be an essential building block
if we want to add any spy-aware routing algorithm to Tor, but I have
two serious reservations.  First, simplest, but less important, right
now all Tor clients make routing decisions more-or-less the same way
(there have been small changes to the algorithm over time, but
everyone is strongly encouraged to stay close to the latest client
release anyway, just because of bugs).  If clients *don't* all make
routing decisions the same way, then that by itself might be usable to
fingerprint them, and thus cut down the number of people who might've
taken some action, from "all Tor users" to "all Tor users who make
routing decisions like THIS."  If highly personalized threat models
are allowed, the latter group might be just one person.

Second, and rather more serious, the user-input aspect of this system
is going to require *major* user experience research and design to
have any hope of not being worse than the problem it's trying to
solve.  It's not just a matter of putting a friendly face on the
"belief language" (although that does need to happen)---the system
will need to educate its users in the meaning of what it is telling
them, and it will need to walk them through the consequences of their
choices.  And it might need to provide nudges if there's a good reason
to think the user's assessment of their threat model is flat-out wrong
(even just making that judgement automatically is fraught with
peril---but so is *not* making that judgement).

[AS]: https://en.wikipedia.org/wiki/Autonomous_system
[IXP]: https://en.wikipedia.org/wiki/Internet_Exchange_Point
