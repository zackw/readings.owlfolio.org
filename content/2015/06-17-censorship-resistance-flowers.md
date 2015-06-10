---
title: "Censorship Resistance: Let a Thousand Flowers Bloom?"
tags: [censorship, circumvention, steganography, game theory]
authors:
 - Elahi, Tariq
 - Murdoch, Steven J.
 - Goldberg, Ian
year: 2014
venue: preprint
eprints:
  arxiv: "1412.1859 [cs.CR]"
...

This short paper presents a simple game-theoretic analysis of a late
stage of the arms race between a censorious national government and
the developers of tools for circumventing that censorship.  Keyword
blocking, IP-address blocking, and protocol blocking for known
circumvention protocols have all been insitituted and then evaded.
The circumvention tool is now steganographically masking its traffic
so it is indistinguishable from some commonly-used, innocuous "cover"
protocol or protocols; the censor, having no way to unmask this
traffic, must either block _all_ use of the cover protocol, or give
up.

The game-theoretic question is, _how many_ cover protocols should the
circumvention tool implement?  Obviously, if there are several
protocols, then the tool is resilient as long as not all of them are
blocked.  On the other hand, implementing more cover protocols
requires more development effort, and increases the probability that
some of them will be imperfectly mimicked, making the tool
detectable. [[1]][] This might seem like an intractable question, but
the lovely thing about game theory is it lets you demonstrate that
nearly all the fine details of each player's utility function are
irrelevant.  The answer: if there's good reason to believe that
protocol X will never be blocked, then the tool should only implement
protocol X.  Otherwise, it should implement several protocols, based
on some assessment of how likely each protocol is to be blocked.

In real life there probably won't be a clear answer to "will protocol
X ever be blocked?"  As the authors themselves point out, the censors
can change their minds about that quite abruptly, in response to
political conditions.  So, in real life several protocols will be
needed, and that part of the analysis in this paper is not complete
enough to give concrete advice.  Specifically, it offers a stable
strategy for the [Nash equilibrium][] (that is, neither party can
improve their outcome by changing the strategy) but, again, the
censors might abruptly change their utility function in response to
political conditions, disrupting the equilibrium.  (The circumvention
tool's designers are probably philosophically committed to free
expression, so their utility function can be assumed to be stable.)
This requires an adaptive strategy.  The obvious adaptive strategy is
for the tool to use only one or two protocols at any given time (using
more than one protocol may also improve verisimilitude of the overall
traffic being surveilled by the censors) but *implement* several
others, and be able to activate them if one of the others stops
working.  The catch here is that the *change in behavior* may itself
reveal the tool to the censor.  Also, it requires all the engineering
effort of implementing multiple protocols, but some fraction of that
may go to waste.

The paper also doesn't consider what happens if the censor is capable
of disrupting a protocol in a way that only mildly inconveniences
normal users of that protocol, but renders the circumvention tool
unusable.  (For instance, the censor could be able to remove the
steganography without necessarily knowing that it is there. [[2]][])
I *think* this winds up being equivalent to the censor being able to
block that protocol without downside, but I'm not sure.

[[1]]: http://freehaven.net/anonbib/cache/oakland2013-parrot.pdf
[Nash equilibrium]: https://en.wikipedia.org/wiki/Nash_equilibrium
[[2]]: http://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1095&context=computerelectronicfacpub
