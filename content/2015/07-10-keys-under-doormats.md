---
title: "Keys Under Doormats: Mandating insecurity by requiring
        government access to all data and communications"
tags: [surveillance, key escrow, policy, philosophy of security]
authors:
 - Abelson, Harold
 - Anderson, Ross
 - Bellovin, Steven M.
 - Benaloh, Josh
 - Blaze, Matthew
 - Diffie, Whitfield
 - Gilmore, John
 - Green, Matthew
 - Neumann, Peter G.
 - Landau, Susan
 - Rivest, Ronald L.
 - Schiller, Jeffrey I.
 - Schneier, Bruce
 - Specter, Michael
 - Weitzner, Daniel J.
year: 2015
venue: preprint
url: https://dspace.mit.edu/bitstream/handle/1721.1/97690/MIT-CSAIL-TR-2015-026.pdf
...

Today's paper is not primary research, but an expert opinion on a
matter of public policy; three of its authors have posted their own
summaries [[1]][] [[2]][] [[3]][], the general press has picked it up
[[4]][] [[5]][] [[6]][] [[7]][] [[8]][], and it was mentioned during
Congressional hearings on the topic [[9]][].  I will, therefore, only
briefly summarize it, before moving on to some editorializing of my
own.  I encourage all of you to read the paper itself; it's clearly
written, for a general audience, and you can probably learn something
about how to argue a position from it.

The paper is a direct response to FBI Director [James Comey][], who
has for some time been arguing that "data storage and communications
systems must be designed for *exceptional access* by law enforcement
agencies" (quote from paper); his [recent Lawfare editorial][] can be
taken as representative.  British politicians have also been making
similar noises (see the above general-press articles).  The paper, in
short, says that this would cause much worse technical problems than
it solves, and that *even if, by some magic, those problems could be
avoided*, it would still be a terrible idea for political reasons.

At slightly more length, "exceptional access" means: law enforcement
agencies (like the FBI) and espionage agencies (like the NSA) want to
be able to [wiretap][] all communications on the 'net, even if those
communications are encrypted.  This is a bad idea technically for the
same reasons that master-key systems for doors can be more trouble
than they're worth.  The locks are more complicated, and easier to
pick than they would be otherwise.  If the master key falls into the
wrong hands you have to change *all* the locks.  Whoever has access to
the master keys can misuse them---which makes the keys, and the people
who control them, a target.  And it's a bad idea politically because,
if the USA gets this capability, every other sovereign nation gets it
too, and a universal wiretapping capability is *more* useful to a
totalitarian state that wants to suppress the political opposition,
than it is to a detective who wants to arrest murderers.
[I went into this in more detail toward the end of my review of RFC 3514][rfc-3514].

I am certain that James Comey knows all of this, in at least as much
detail as it is explained in the paper.  Moreover, he knows that the
"robust democratic debate" he calls for *already happened*, in the
1990s, and wiretapping lost. [[10]][] [[11]][] [[12]][] Why, then, is he trying
to relitigate it?  Why does he keep insisting that it must *somehow*
be both technically and politically feasible, against all evidence to
the contrary?  Perhaps most important of all, why does he keep
insisting that it's desperately important for his agency to be able to
break encryption, when it was only an obstacle nine times in all of
2013? [[13]][]

On one level, I think it's a failure to understand the scale of the
problems with the idea.  On the technical side, if you don't live your
life down in the gears it's hard to bellyfeel the extent to which
[everything is broken][] and therefore any sort of wiretap requirement
cannot help but make the situation worse.  And it doesn't help, I'm
sure, that Comey has heard (correctly) that what he wants is
_mathematically_ possible, so he thinks everyone saying "this is
impossible" is trying to put one over on him, rather than just
communicate "this isn't _practically_ possible."

The geopolitical problems with the idea are perhaps even harder to
convey, because the Director of the FBI wrestles with geopolitical
problems every day, so he thinks he _does_ know the scale there.  For
instance, the paper spends quite some time on a discussion of the
jurisdictional conflict that would naturally come up in an
investigation where the suspect is a citizen of country A, the crime
was committed in B, and the computers involved are physically in C but
communicate with the whole world---and it elaborates from there.  But
we already _have_ treaties to cover that sort of investigation.  Comey
probably figures they can be bent to fit, or at worst, we'll have to
negotiate some new ones.

If so, what he's missing is that he's imagining too small a group of
wiretappers: law enforcement and espionage agencies from countries
that are on reasonably good terms with the USA.  He probably thinks
export control can keep the technology out of the hands of countries
that _aren't_ on good terms with the USA (it can't) and hasn't even
considered non-national actors: local law enforcement, corporations
engaged in industrial espionage, _narcotraficantes_, mafiosi, bored
teenagers, Anonymous, religious apocalypse-seekers, and corrupt
insiders in all the above.  People the USA can't negotiate treaties
with.  People who would already have been thrown in jail if anyone
could make charges stick.  People who may not even share premises like
what "good governance" or "due process of law" or "basic human
decency" mean.  There are a bit more than seven billion people on the
planet today, and this is the true horror of the Internet: roughly 40%
of those people [[14]][] could, if they wanted, ruin your life, right
now.  It's not hard.  [[15]][] (The other 60% could too, if they could
afford to buy a mobile, or at worst a satellite phone.)

But these points, too, have already been made, repeatedly.  Why does
none of it get through?  I am only guessing, but my best guess is: the
War On Some Drugs [[16]][] and the aftermath of 9/11 [[17]][]
(paywalled, sorry; please let me know if you have a better cite) have
both saddled the American "homeland security" complex with impossible,
Sisyphean labors.  In an environment where failure is politically
unacceptable, yet inevitable, the loss of any tool---even if it's only
marginally helpful---must seem like an existential threat.  To get
past that, we would have to be prepared to back off on the "must never
happen again" / "must be stopped at all cost" posturing; the good news
is, that has an excellent chance of delivering better, cheaper law
enforcement results overall. [[18]][]

[[1]]: https://www.lightbluetouchpaper.org/2015/07/07/crypto-wars-2-0/
[[2]]: http://www.lawfareblog.com/keys-under-doormats-mandating-insecurity
[[3]]: https://www.cs.columbia.edu/~smb/blog/2015-07/2015-07-07.html
[[4]]: http://www.theguardian.com/world/2015/jul/07/uk-and-us-demands-to-access-encrypted-data-are-unprincipled-and-unworkable
[[5]]: http://www.theregister.co.uk/2015/07/08/security_giants_publish_paper_destroying_government_encryption_plans/
[[6]]: http://www.nytimes.com/2015/07/08/technology/code-specialists-oppose-us-and-british-government-access-to-encrypted-communication.html?_r=0
[[7]]: http://takingnote.blogs.nytimes.com/2015/07/07/why-a-back-door-to-the-internet-is-a-bad-idea/
[[8]]: https://www.techdirt.com/articles/20150709/00441731596/fbi-bring-us-unicorn-techies-they-dont-exist-senator-stop-complaining-tell-us-where-unicorn-is.shtml
[[9]]: https://www.eff.org/deeplinks/2015/07/top-five-takeaways-todays-hearings-encryption
[James Comey]: https://en.wikipedia.org/wiki/James_Comey
[recent Lawfare editorial]: http://www.lawfareblog.com/encryption-public-safety-and-going-dark
[wiretap]: https://en.wikipedia.org/wiki/Telephone_tapping
[rfc-3514]: https://readings.owlfolio.org/2003/ipv4-security-flag/
[[10]]: https://www.schneier.com/blog/archives/2014/10/iphone_encrypti_1.html
[[11]]: http://archive.wired.com/wired/archive/1.02/crypto.rebels_pr.html
[[12]]: http://justsecurity.org/24483/end-debate-encryption-backdoors/
[[13]]: http://www.wired.com/2014/07/rising-use-of-encryption-foiled-the-cops-a-record-9-times-in-2013/
[everything is broken]: https://medium.com/message/everything-is-broken-81e5f33a24e1
[[14]]: http://www.internetworldstats.com/stats.htm
[[15]]: https://theconversation.com/doxxing-swatting-and-the-new-trends-in-online-harassment-40234
[[16]]: http://www.politico.com/magazine/story/2015/01/war-on-drugs-a-century-of-failure-113936.html
[[17]]: http://www.palgrave-journals.com/sj/journal/v24/n1/full/sj20097a.html
[[18]]: http://blog.mpp.org/prohibition/prohibitionists-hold-anti-reform-campaign-event-on-public-dime/5112010/
