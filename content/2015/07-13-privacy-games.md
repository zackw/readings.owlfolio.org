---
title: "Privacy Games: Optimal User-Centric Data Obfuscation"
tags: [privacy, differential privacy, distortion privacy, game theory,
       adversarial optimization, theory]
authors:
 - Shokri, Reza
year: 2015
venue: PETS
eprints:
 doi: 10.1515/popets-2015-0024
url: https://www.petsymposium.org/2015/papers/20_Shokri.pdf
...

I attended this year's <a
href="https://www.petsymposium.org/2015/program.php"><abbr
title="Privacy Enhancing Technologies Symposium">PETS</abbr></a>
conference a couple weeks ago, and for the next several weeks I'm
going to be focusing on highlights from there.  For variety's sake,
there will be one unrelated thing each week.

I'm starting with a paper which is heavier mathematical going than I
usually pick.  The author claims to have developed an optimal
(meta-)strategy for obfuscating a person's location before revealing
it to some sort of service.  The person wants to reveal enough
information to get whatever utility the service provides, while not
telling it _exactly_ where they are, because they don't entirely trust
the service.  The service, meanwhile, wants to learn as much as
possible about the person's location---it doesn't matter why.

There are two standard mathematical techniques for obfuscating a
location: [differential privacy][] and [distortion privacy][].  They
both work by adding noise to a location value, but they use different
metrics for how much the adversary can learn given the noisy value.
The paper asserts: "[differential privacy] is sensitive to the
likelihood of observation given data, [distortion privacy] is
sensitive to the joint probability of observation given data.  Thus,
by guaranteeing both, we encompass all the defense that is
theoretically possible."  (This is a bold claim and I don't know
enough about this subfield to verify it.)  The paper proceeds to
demonstrate, first, that you can construct a [linear-programming][]
problem whose solution gives an appropriate amount of noise to add to
a location value, and second, that this solution is game-theoretically
optimal, even against an adversary who knows your strategy and can
adapt to it.  Then they analyze the degree to which the data has to be
obfuscated, comparing this with more limited algorithms from previous
literature.

I unfortunately couldn't make any sense of the comparisons, because
the figures are poorly labeled and explained.  And the bulk of the
paper is just mathematical derivations, to which I have nothing to
add.  But there is an important point I want to highlight.  The
game-theoretic analysis only works if everything the adversary
_already_ knows (before they learn the obfuscated location) is
captured by a distance metric which defines "how far" the obfuscated
location has been displaced.  Mathematically, this is fine; any given
fact that the adversary might know about the person revealing their
location _can_ be modeled by adjusting the metric.  (Person is in a
city, so their path is constrained to the street grid.  Person just
left a large park, there is only one coffee shop within radius X of
that park.  Person never goes to that restaurant.)  However, the
system doing the obfuscation might not be able to predict all of those
factors, and if it distorts the metric _too_ much it might contradict
itself (person cannot possibly have walked from A to B in the time
available).  In the future I'd like to see some analysis of this.
What is it plausible for the adversary to know?  At what point does
the obfuscation break down because it can't cover all the known facts
without contradicting itself?

[differential privacy]: https://en.wikipedia.org/wiki/Differential_privacy
[distortion privacy]: http://icapeople.epfl.ch/rshokri/papers/09WPES.pdf
[linear-programming]: https://en.wikipedia.org/wiki/Linear_programming
