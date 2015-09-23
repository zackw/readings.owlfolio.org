---
title: "RAPPOR: Randomized Aggregatable Privacy-Preserving Ordinal Response"
tags: [privacy, differential privacy, statistics, data collection]
authors:
 - Erlingsson, Úlfar
 - Pihur, Vasyl
 - Korolova, Aleksandra
year: 2014
venue: CCS
eprints:
 arxiv: 1407.6981 [cs.CR]
 doi: 10.1145/2660267.2660348
...

Lots of software developers would love to know in detail how people
use their work, and to that end, there's an increasing number of
programs that "[phone home][]" with crash reports, [heat maps][] of
which UI elements get used, and even [detailed logs][] of every
interaction.  The problem, of course, is how to collect as much useful
information as possible without infringing on user privacy.  Usually,
what the developers want are aggregate statistics---how often does
this widget get used by _everyone_, that sort of thing---so the
logical method to apply is [differential privacy][].  However, stock
differential privacy algorithms assume a central, trusted database,
and in this case, the only people who could run the database are the
developers---the very same people against whom individual responses
should be protected.  Also, differential privacy's mathematical
guarantees are eroded if you repeatedly ask the same survey questions
of the same population---which is exactly what you want to do to
understand how user behavior changes over time.

This paper solves both problems with a combination of
[randomized response][] and [Bloom filters][].  Randomized response is
an old, ingenious idea for asking sensitive yes-no survey questions
such that any one person has plausible deniability, but the true
aggregate number of "yes" responses is still known: each survey
participant secretly flips a coin before answering, and if it comes up
heads they answer "yes" whether or not that's true.  Otherwise they
answer honestly.  After the fact, everyone can _claim_ to have
answered "yes" because of the coin flip, but to recover the true
population statistic one simply doubles the number of "no" answers.
Bloom filters (which I'm not going to try to explain) are used to
extend this from yes-no to reporting sets of strings.  Finally, there
are two stages of randomization.  Given a set of survey questions, the
system computes a "Permanent randomized response" which is, as the
name implies, reused until either the answers or the questions change.
This prevents privacy erosion, because each user is _always_ either
answering honestly or falsely to any given question; a nosy server
cannot average out the coin tosses.  Additional "instantaneous"
randomness is added each time a report is submitted, to prevent the
report being a fingerprint for that user.  The system is said to be in
use for telemetry from the Chrome browser, and they give several
examples of data collected in practice.

The Permanent randomized responses illustrate a basic tension in
security design: you can often get better security outcomes versus a
remote attacker if you keep local state, but that local state is
probably high-value information for a _local_ attacker.  For example,
any system involving [trust on first use][] will store a list of
frequently contacted remote peers, with credentials, on the local
machine; tampering with that can destroy the system's security
guarantees, and simply _reading_ it tells you, at a minimum, which
remote peers you regularly connect to.  The [TAILS][] live-CD is
intended to "leave no trace" on the system it's run on, which means it
changes its [entry guards][] on every reboot, increasing the chance of
picking a malicious guard.  In this case, a local adversary who can
read a Chrome browser profile has access to much higher-value data
than the Permanent responses, but a cautious user who erases their
browser profile on every shutdown, to protect against that local
adversary, is harming their own security against the Chrome
developers.  (This might be the right tradeoff, of course.)

I also wonder what a network eavesdropper learns from the telemetry
reports.  Presumably they are conveyed over a secure channel, but at a
minimum, that still reveals that the client software is installed, and
the size of the upload might reveal things.  A crash report, for
instance, is probably much bulkier than a statistics ping, and is
likely to be submitted immediately rather than on a schedule.

[phone home]: http://www.imdb.com/title/tt0083866/quotes?item=qt0474627
[heat maps]: http://www.ridgehead.com/heat-maps-and-user-interface-design/
[detailed logs]: https://www.reddit.com/r/baww/comments/1wiybg/the_woman_who_talked_to_clippy/
[differential privacy]: https://en.wikipedia.org/wiki/Differential_privacy
[randomized response]: https://en.wikipedia.org/wiki/Randomized_response
[Bloom filters]: https://en.wikipedia.org/wiki/Bloom_filter
[trust on first use]: https://en.wikipedia.org/wiki/Trust_on_first_use
[TAILS]: https://tails.boum.org/about/index.en.html
[entry guards]: https://blog.torproject.org/blog/improving-tors-anonymity-changing-guard-parameters
