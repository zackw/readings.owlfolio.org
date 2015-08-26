---
title: "Folk Models of Home Computer Security"
tags: [usable security, threat modeling]
authors:
 - Wash, Rick
year: 2010
venue: SOUPS
url: https://cups.cs.cmu.edu/soups/2010/proceedings/a11_Walsh.pdf
...

It is well known that people who aren't computer security experts tend
to ignore expert advice on computer security, and (to some extent as a
consequence) get exploited.  This paper is not the first, or the last,
to investigate why; see also the "What Deters Jane" papers [[1]][]
[[2]][],
"[So Long and No Thanks for the Externalities][externalities]," and
"[Users Are Not the Enemy][users-not-enemy]."
However, this paper provides a much more compelling explanation than
anything earlier (that I have read), and a lens through which to view
everything since.  It's plainly written and requires almost no
specialized background knowledge; you should just go ahead and read
the whole thing.

For those not in the mood to read the whole thing right now, I will
summarize.  Wash conducted "semi-structured, qualitative" interviews
of 33 home computer users, who were selected to maximize sample
diversity, and specifically to exclude security experts.  From these,
he extracted a number of what he calls "folk models"---qualitative,
brief descriptions of how these people understand various threats to
their computer security.  The term "folk" is used to describe a model
which accurately reflects users' understanding of a system, and is
broadly shared among a user population, but might not accurately
reflect the true behavior of that system. [[3]][]  In this case, that
means the models reflect what the interviewees _think_ are the threats
to their home computers, even if those aren't accurate.  Indeed, it is
precisely where the model is inaccurate to the real threats that it
provides an explanation of the phenomenon (i.e. users not bothering to
follow well-publicized security advice).

A key aspect of all the models presented is a division of security
threats into "viruses" and "hackers."  "Virus" is used by the
interviewees as an umbrella term, corresponding most closely to what
experts call "malware"---any piece of software which is unwanted and
has harmful effects.  (One model expands this category even further,
to include programs which are _unintentionally_ harmful, i.e. they
have bugs.)  The models differ primarily in users' understanding of
how "viruses" get into the computer, and what they are programmed to
do once there.  This can be very vague (e.g. 'viruses are bad software
you don't want on your computer') or quite specific (e.g. 'viruses are
deliberately programmed by hackers as an act of vandalism; they cause
annoying problems with the computer; you get them passively by
visiting sketchy websites'---an expert will acknowledge this as
true-but-incomplete).

"Hackers" on the other hand are people who are actively seeking to
exploit computers; most interviewees share the understanding that this
involves "taking control" of a computer remotely, thus allowing it to
be manipulated as if the hacker were physically present at its
console.  (Many of them hedge that they do not know _how_ this is
done, but they are sure that it is possible.)  The models here differ
primarily in the motives ascribed to the hackers, which are:
vandalism, identity theft, or _targeted_ identity theft and financial
fraud.  This last is one of the most telling observations in the
entire paper: a significant number of people believe that they are
safe from hackers because they have nothing worth stealing or
exposing.  (Again, an expert would recognize this as
true-but-incomplete: there really is a subpopulation of black-hat
actors who specialize in going after the "big fish."  The catch, of
course, is that the data exfiltrated from a "big fish" might include
[millions of people's personal credit card numbers][target-breach]...)

Having presented these models, Wash runs down a list of standard items
of home computer security advice (drawn from [Microsoft][], [CERT][],
and [US-CERT][]'s guides on the topic) and points out how many of them
are either useless or unimportant according to these models: for
instance, if you think you can't get viruses without actively
downloading software, then antivirus software is pointless, and
patching only valuable if it eliminates bugs you trip over yourself;
if you think hackers rarely, if ever, vandalize a computer, then
backups are not necessary to protect against that risk.  He closes by
comparing the novel-at-the-time threat of botnets to all the models,
observing that none of them account for the possibility that an
attacker might subvert computers indiscriminately and automatically,
then use them only for their Internet connection.  In particular, all
of the "hacker" models assume that computers are attacked in order to
do something to _that_ computer, rather than as a means to an
unrelated goal (sending spam, enlarging the botnet, executing DDoS
attacks, ...) and that the hacker must be doing something manually at
the time of the attack.

The landscape of security threats has changed quite a bit since this
paper was published.  I would be curious to know whether
[ransomware][], [RATs][], third-party data breaches, and so on have
penetrated the public consciousness enough to change any of the
models.  I'd also like to know whether and how much people's
understanding of the threats to a mobile phone is different.  And,
although Wash did make an effort to cover a broad variety of
non-expert home computer users, they are all from the general
population near his Midwestern university, hence mostly [WEIRDos][].
I'm not aware of any studies of this type conducted anywhere but North
America and Europe, but I bet it's not quite the same elsewhere...

[[1]]: /2014/jane-protects-privacy/
[[2]]: /2014/jane-prevents-tracking/
[externalities]: http://research.microsoft.com/en-us/um/people/cormac/papers/2009/solongandnothanks.pdf
[users-not-enemy]: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.465.6547&rep=rep1&type=pdf
[[3]]: http://csjarchive.cogsci.rpi.edu/1986v10/i01/p0075p0090/MAIN.PDF
[target-breach]: http://www.forbes.com/sites/paularosenblum/2014/01/17/the-target-data-breach-is-becoming-a-nightmare/
[Microsoft]: https://www.microsoft.com/security/default.aspx
[CERT]: https://web.archive.org/web/20100107080747/http://www.cert.org/homeusers/HomeComputerSecurity/
[US-CERT]: http://www.us-cert.gov/cas/tips/
[ransomware]: https://www.microsoft.com/security/portal/mmpc/shared/ransomware.aspx
[RATs]: http://arstechnica.com/tech-policy/2013/03/rat-breeders-meet-the-men-who-spy-on-women-through-their-webcams/
[WEIRDos]: http://neuroanthropology.net/2010/07/10/we-agree-its-weird-but-is-it-weird-enough/
