---
title: "Automated Experiments on Ad Privacy Settings"
tags: [advertising, machine learning, privacy]
authors:
 - Datta, Amit
 - Tschantz, Michael Carl
 - Datta, Anupam
year: 2015
venue: PETS
eprints:
 doi: 10.1515/popets-2015-0007
url: https://www.petsymposium.org/2015/papers/18_Datta.pdf
...

You've probably noticed the creepy effect where you consider buying
something online, or maybe just look at a page for something that
happens to be for sale, and for weeks afterward you get ads on totally
unrelated websites for that thing or similar things.  The more
reputable online ad brokerages offer a degree of control over this
effect (e.g.: [Google][g-ad-settings], [Microsoft][m-ad-settings]).
This study investigates exactly what effect those settings have on the
ads observed by automated browsing "agents."  The basic idea is to set
some of the knobs, visit websites that will tell the ad provider
something about the simulated customer's preferences, possibly adjust
the knobs again, and finally record what is being advertised on a
general-interest website.

A great deal of the paper is devoted to statistical methodology.
Because the ad provider is a stateful "[black box][]," and one whose
behavior may depend on uncontrollable external factors (e.g. "that
advertiser has exhausted their budget for the month"), it's vital to
avoid as many statistical assumptions as possible.  They use
[permutation tests][] and supervised classification (logistic
regression), both of which make minimal assumptions.  They're also
very careful about drawing conclusions from their results.  I'm not
much of a statistician, but it all *sounds* carefully thought out and
plausible, with one exception: heavy reliance on
'[significance testing][p-values],' which has come in for serious
criticism [[1]][] to the point where some journals no longer accept
its use at all [[2]][].  This is exactly the sort of research where
*p*-values can mislead; if I were reviewing this prior to publication
I would have encouraged the authors to think about how they could
present the same conclusions without using significance testing.

Now, the actual conclusions.  Only Google's ads were tested.
(Expanding the tests to additional ad brokers is listed as future
work.)  They confirm that turning a particular topic (dating) off in
the preferences does cause those ads to go away.  They observe that
two highly sensitive topics (substance abuse, disability) that do
trigger targeted ads are *not* controllable via the preferences; in
fact, they are completely invisible on that screen.  And the most
interesting case is when they set the ad preferences to explicitly
reveal a gender (man or woman) then browsed a bunch of sites related
to job searching.  Simulated customers who claimed to be men got ads
for a "career coaching" service which promised better odds of being
hired into "$200K+" executive positions; those who claimed to be women
did not see these ads.

This last example clearly reflects the well-known "[glass ceiling][]"
which affects business in general, but (as the authors point out) it's
impossible to tell, from outside the black box, _why_ it shows up in
this case.  The career-coaching service could have chosen to advertise
only to men.  Google's ad-targeting algorithm could have been coded
with (likely unconscious) bias in its category structure, or---this is
the most probable explanation---its feedback mechanism could have
detected that men are more likely to click on ads with those keywords,
so it makes that even more likely by showing them preferentially to
men. There's a telling comment at the very end of the paper:

> ... We consider it more likely that Google has lost control over its
> massive, automated advertising system.  Even without advertisers
> placing inappropriate bids, large-scale machine learning can behave
> in unexpected ways.

There's a lesson here for all the "big data" companies: the best an
"unbiased" machine learning system can hope to do is produce an
accurate reflection of the training set---including whatever biases
are in there.  If you want to avoid reduplicating all the systemic
biases of the offline world, you will have to write code to that
effect.

[g-ad-settings]: https://www.google.com/settings/ads/anonymous
[m-ad-settings]: https://choice.microsoft.com/en-US
[black box]: https://en.wikipedia.org/wiki/Black_box
[permutation tests]: https://en.wikipedia.org/wiki/Resampling_%28statistics%29#Permutation_tests
[p-values]: https://en.wikipedia.org/wiki/P-value
[[1]]: http://www.nature.com/news/scientific-method-statistical-errors-1.14700
[[2]]: http://www.tandfonline.com/doi/pdf/10.1080/01973533.2015.1012991
[glass ceiling]: https://en.wikipedia.org/wiki/Glass_ceiling
