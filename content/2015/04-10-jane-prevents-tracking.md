---
title: "What Deters Jane from Preventing Identification and Tracking
        on the Web?"
tags: [usable security, anonymity, surveillance, user tracking]
authors:
 - Shirazi, Fatemeh
 - Volkamer, Melanie
year: 2014
venue: WPES
pages: 107--116
eprints:
 doi: 10.1145/2665943.2665963
...

If you do a survey, large majorities of average people will say they
don't like the idea of other people snooping on what they do online.
[[1]][] [[2]][] Yet, the existing bolt-on software that can prevent
such snooping (at least somewhat) doesn't get used by nearly as many
people.  The default explanation for this is that it's because the
software is hard to install and use correctly. [[3]][] [[4]][]

This paper presents a complementary answer: maybe people don't realize
just how ubiquitous or invasive online snooping is, so the benefit
seems not worth the hassle.  The authors interviewed a small group
about their beliefs concerning "identification and tracking."  (They
admit that the study group skews young and technical, and plan to
broaden the study in the future.)  Highlights include: People are
primarily concerned about data they explicitly provide to some
service---social network posts, bank account data, buying habits---and
may not even be aware that ad networks and the like can build up
comprehensive profiles of online activity even if all they do is
"browse."  They often have heard a bunch of fragmentary information
about "cookies" and "supercookies" and "IP addresses" and so on, and
don't know how this all fits together or which bits of it to worry
about.  Some people thought that tracking was only possible for
services with which they have an account, while they are logged in (so
they log out as soon as they're done with the service).  There is also
general confusion about which security threats qualify as
"identification and tracking"---to be fair, just about all of them
_can_ include some identification or tracking component.  The
consequences of being tracked online are unclear, leading people to
underestimate the potential harm.  And finally, many of the
respondents assume they are not important people and therefore no one
would _bother_ tracking them.  All of these observations are
consistent with earlier studies in the same vein, e.g. Rick Wash's
"[Folk Models of Home Computer Security][folk-models]."

The authors argue that this means maybe the usability problems of the
bolt-on privacy software are overstated, and user education about
online security threats (and the mechanism of the Internet in general)
should have higher priority.  I think this goes too far.  It seems
more likely to me that _because_ people underestimate the risk and
don't particularly understand how the privacy software would help,
they are not motivated to overcome the usability problems.  I am also
skeptical of the effectiveness of user education.  The mythical
average users may well feel, and understandably so, that they should
not _need_ to know exactly what a cookie is, or exactly what data gets
sent back and forth between their computers and the "cloud," or the
internal structure of that "cloud."  Why is it that the device that
they own is not acting in their best interest in the first place?

[[1]]: http://www.pewinternet.org/2013/09/05/anonymity-privacy-and-security-online/
[[2]]: https://epic.org/privacy/survey/
[[3]]: http://cs.berkeley.edu/~tygar/papers/Why_Johnny_Cant_Encrypt/OReilly.pdf
[[4]]: https://www.privacyassociation.org/media/pdf/knowledge_center/Why_Johnny_Can%E2%80%99t_Opt_Out.pdf
[folk-models]: http://www.rickwash.com/papers/rwash-homesec-soups10-final.pdf
