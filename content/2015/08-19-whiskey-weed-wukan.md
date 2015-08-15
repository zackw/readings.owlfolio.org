---
title: "Whiskey, Weed, and Wukan on the World Wide Web"
tags: [censorship, culture, economics, threat modeling]
authors:
 - Aase, Nicholas
 - Crandall, Jedidiah R.
 - Díaz, Álvaro
 - Knockel, Jeffrey
 - Molinero, Jorge Ocaña
 - Saia, Jared
 - Wallach, Dan
 - Zhu, Tao
year: 2012
venue: FOCI
url: https://www.usenix.org/system/files/conference/foci12/foci12-final17.pdf
...

The subtitle of today's paper is "On Measuring Censors' Resources and
Motivations."  It's a position paper, whose goal is to get other
researchers to start considering how economic constraints might affect
the much-hypothesized "arms race" or "tit-for-tat" behavior of censors
and people reacting to censorship: as they say,

> [...] the censor and censored have some level of motivation to
> accomplish various goals, some limited amount of resources to
> expend, and real-time deadlines that are due to the timeliness of
> the information that is being spread.

They back up their position by presenting a few pilot studies, of
which the most compelling is the investigation of keyword censorship
on Weibo (a Chinese microblogging service).  They observe that
searches are much more aggressively keyword-censored than posts---that
is, for "many examples" of known-censored keywords, one is permitted
to make a post on Weibo containing that keyword, but searches for that
keyword will produce either no results or very few results.  (They
don't say whether unrelated searches will turn up posts containing
censored keywords.)  They also observe that, for some keywords that
are *not* permitted to be posted, the server only bothers checking for
variations on the keyword if the user making the post has previously
tried to post the literal keyword.  (Again, the exact scope of the
phenomenon is unclear---does an attempt to post any blocked keyword
make the server check more aggressively for variations on *all*
blocked keywords, or just that one?  How long does this escalation
last?)  And finally, whoever is maintaining the keyword blacklists at
Weibo seems to care most about controlling the news cycle: terms
associated with breaking news that the government does not like are
immediately added to the blacklist, and removed again just as quickly
when the event falls out of the news cycle or is resolved positively.
They give detailed information about this phenomenon for one news
item, the [Wukan incident][], and cite several other keywords that
seem to have been treated the same.

They compare Weibo's behavior to similar keyword censorship by
chat programs popular in China, where the same patterns appear, but
whoever is maintaining the lists is sloppier and slower about it.
This is clear evidence that the lists are not maintained centrally (by
some government agency) and they suggest that many companies are not
trying very hard:

> At times, we often suspected that a keyword blacklist was being
> typed up by an over-worked college intern who was given vague
> instructions to filter out anything that might be against the law.

Sadly, I haven't seen much in the way of people stepping up to the
challenge presented, designing experiments to probe the economics of
censorship.  You can see similar data points in other studies of China
[[1]][] [[2]][] [[3]][] (it is still the case, as far as I know, that
ignoring spurious TCP RST packets is sufficient to evade several
aspects of the "Great Firewall"), and in reports from other countries.
It is telling, for instance, that Pakistani censors did not bother to
update their blacklist of porn sites to keep up with a shift in
viewing habits. [[4]][] George Danezis has been talking about the
economics of anonymity and surveillance for quite some time now
[[5]][] [[6]][] but that's not quite the same thing.  I mentioned
above some obvious follow-on research just for Weibo, and I don't
think anyone's done *that*.  Please tell me if I've missed something.

[Wukan incident]: https://en.wikipedia.org/wiki/Wukan_protests
[[1]]: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.97.7682&rep=rep1&type=pdf
[[2]]: http://sec.cs.ucl.ac.uk/users/smurdoch/papers/is07ignoring.pdf
[[3]]: http://www.pseudonymity.net/~joss/doc/papers/2012/wright12variation.pdf
[[4]]: /2014/consequences-censorship-isp-lens/
[[5]]: http://freehaven.net/anonbib/cache/redblue.pdf
[[6]]: http://freehaven.net/anonbib/cache/danezis:weis2006.pdf
