---
title: "Tor's Usability for Censorship Circumvention"
tags: [usable security, tor, circumvention]
authors:
 - Fifield, David
 - Lee, Linda N.
 - Egelman, Serge
 - Wagner, David
year: 2015
venue: HotPETS
url: https://petsymposium.org/2015/papers/fifield-tor-censorship-usability-hotpets2015.pdf
...

This is a report on a pilot usability study.  The authors ran five
"journalists" (there aren't any more details than that) through the
process of installing, activating, and using the [Tor Browser][]
for a small number of canned tasks, identifying a number of problems:

> ... people did have difficulty with installing Tor Browser
> (principally because of the Gatekeeper code-signing feature
> on OS X), did not understand what many of the many options
> meant, and were confused about why certain things were happening.

They are going to do a much larger study, and were soliciting feedback
on experimental design.  I have only two things to say.  First, the
proposal is to do a large test of 200 users and then, presumably,
start making changes to the software to improve usability.  The
problem with this is, it is very likely that subtle (yet serious) UX
issues are being _masked out_ by the more blatant ones: no matter how
many people you experiment on, you won't detect the subtle problems
until the blatant ones are fixed.  Therefore, it would be far more
valuable to do a _series_ of smaller user studies, improving the
software based on the results of each study before doing the next one.
This strategy also ensures that the research results do get
incorporated into the product, rather than being lost in the shuffle
once the paper is published.

The other point is more of a hypothesis about what would be good to
aim for.  To use Tor in a way that genuinely improves your security
outcomes, you need to understand what it is doing and why, and to do
that you have to wrap your head around some concepts that may be
unfamiliar---especially if you haven't previously needed to understand
the Internet itself in any kind of detail.  (For instance, the fact
that every IP packet is labeled with its source and destination is
"obvious once you think about it, but I never thought about it" to a
lot of people.)  There probably needs to be a training manual, and
this manual needs to take the attitude that yeah, this is a little
tricky, and you have to think about it some, but don't panic, you
_can_ understand it.  Shoot for the
["we understand" tone said to characterize Rust compiler errors][rust-reddit]
(warning: Reddit).  The place I've seen this done best, personally,
was the ["tutorial and concepts guide" for GnuCash][gnucash-tut],
which took just this tone with regard to
[double-entry bookkeeping][]---also somewhat notorious for its
inscrutability.  (Note: I read this quite time ago, and I don't know
whether its current edition is still like that.)

[Tor Browser]: https://www.torproject.org/projects/torbrowser.html.en
[rust-reddit]: https://www.reddit.com/r/rust/comments/3cl12r/is_rust_too_complicated/csxp7xa
[gnucash-tut]: http://www.gnucash.org/viewdoc.phtml?doc=guide
[double-entry bookkeeping]: https://en.wikipedia.org/wiki/Double-entry_bookkeeping_system
