---
title: "The Declining Half-Life of Secrets and the Future of Signals Intelligence"
tags: [policy, surveillance]
authors:
 - Swire, Peter
year: 2015
venue: na.cyber.pol
url: https://www.newamerica.org/new-america/the-declining-half-life-of-secrets/
...

Today we're going to look at a position paper from the "[New America][]"
think tank's "[Cybersecurity Initiative][]."  If you're someone like me,
that descriptor probably raises at least four red flags: regarding
anything to do with Internet security, there's a _tremendous_ gulf in
groupthink between people associated with the US government, and
people associated with commercial or _pro bono_ development of
computer stuff.  Which is precisely why it's useful to read papers
from the other side of the gulf, like this one.   (This particular
think tank appears to be more on the "left" as that term is used in US
politics.  I haven't dug into their other position papers.)

Swire starts by pointing out that the government's understanding of
secrecy was developed during the Cold War, when it was, frankly, _much
easier_ to keep secrets.  Paper documents in an archive, which readers
must physically visit, and demonstrate their need-to-know to the man
with a gun at the entrance, are inherently difficult to duplicate.
But that entire archive probably fits on a $50 thumbdrive today.  In a
similar vein, regular readers will recall the "standard military
teletype" with its data transfer rate of 75 bits per second, from
"[Limitations of End-to-End Encryption][]" (1978).

Also, once data has been exfiltrated, it's much easier to broadcast
it, because there are lots more news organizations who might take an
interest---or you can just post it online yourself and rely on the
tremendously accelerated speed of gossip.  These things together are
what Swire means by the "declining half-life of secrets:" secrets have
always been expected to get out _eventually_, but the time scale is no
longer decades.  The metaphor of a reduced [half-life][] seems spot on
to me: leakage of secrets is inherently probabilistic, so exponential
decay is the simplest model, and should give people the right
first-order intuition.

Swire then moves on to discussing the effects of that groupthink gulf
I mentioned.  This bit is weaker, because it's plain that he doesn't
understand _why_ people might prefer the "world-view of [EFF][]."  But
it's accurate as far as it goes.  People associated with the
government are starting from the premise that revealing a secret,
regardless of its contents, is the worst possible thing anyone can do.
(I confess to not understanding how one comes to think _this_, myself.
It probably has to do with one's "default" idea of a secret being
something that really could get someone killed if it were revealed,
never mind that only a tiny fraction of all classified information is
that dangerous.)  In contrast, the "world-view of EFF" begins with the
premise that most information _should_ be published, and that an
organization doing something in secret from the general public
probably means it _knows_, institutionally, that the general public
would not approve.  And, therefore, that it shouldn't be doing it in
the first place.  Since most of the technology community takes this
position, the government has an increasingly large problem trying to
persuade that community to cooperate with its own attitude, and (Swire
says) this will only get worse.

The paper concludes with some fairly weaksauce recommendations: plan
for the possibility of disclosure; take the impact on public opinion
(should the secret be revealed) into account when planning secret
operations; put more effort into arguing _for_ surveillance.
Basically, business as usual but with more media savvy.  This may be
the best one can hope for in the short term, but I have some policy
suggestions of my own:

* Apply [Kerckhoffs' Principle][] to all surveillance programs.  The
  overall design of the system, its budget, the nature of the data
  collected, all relevant policies and procedures, everything except
  the collected data should be public knowledge, subject to normal
  public oversight (e.g. any Congressional hearings on the topic
  should be conducted in public and on the record), and debated in
  public prior to implementation---just like any other government
  program.  If that would render the surveillance useless, the logic
  of Kerckhoffs' principle says _it was already useless_.  (I've made
  this point before, [on my main blog][].)

* Abandon the desire for "exceptional access."  The technology
  community has spent 20+ years explaining over and over and over
  again why [exceptional access is impractical and makes security
  worse for everyone][keys under doormats].  Government agencies
  refusing to accept that message is probably the single strongest
  reason why the groupthink gulf is as wide as it is.

* More generally, whenever there is a tradeoff between offense and
  defense in computer security, choose defense.  Design cryptographic
  standards that are secure for _everyone_, even if they happen to be
  enemies of the USA right now (or might be at some time in the
  future).  Disclose all security-critical bugs to the vendors, so
  they get fixed, even if this means not being able to pull off
  another [Stuxnet][].  Think of this as the Internet analogue of the
  [SALT and START][] treaties.

* Split the [NSA][] in half.  Merge the offensive signals intelligence
  mission into the CIA, or scrap it, I don't care.  Merge the
  defensive cryptographic and cryptanalytic mission into NIST,
  declassify and publish _everything_, and do all future work in
  public (Kerckhoffs' Principle again).  Make it a bedrock policy that
  this organization only does offensive research in support of
  defensive programs (e.g. to demonstrate the (un)soundness of a cipher).

I'm willing to listen to reasons not to do these things, as long as
they do not boil down to "we're scared of hypothetical enemy X."

[New America]: https://www.newamerica.org/
[Cybersecurity Initiative]: https://www.newamerica.org/cybersecurity-initiative/
[Limitations of End-to-End Encryption]: /1978/limitations-end-to-end-encryption/
[half-life]: https://en.wikipedia.org/wiki/Half-life
[EFF]: https://www.eff.org/
[Kerckhoffs' Principle]: http://en.citizendium.org/wiki/Kerckhoffs'_Principle
[on my main blog]: https://www.owlfolio.org/research/institutional-secrecy-culture-is-antidemocratic/
[keys under doormats]: /2015/keys-under-doormats/
[Stuxnet]: http://www.wired.com/2014/11/countdown-to-zero-day-stuxnet/
[SALT and START]: https://en.wikipedia.org/wiki/Strategic_Arms_Limitation_Talks
[NSA]: https://en.wikipedia.org/wiki/National_Security_Agency
