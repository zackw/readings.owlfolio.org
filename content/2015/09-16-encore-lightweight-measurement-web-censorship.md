---
title: "Encore: Lightweight Measurement of Web Censorship with Cross-Origin Requests"
tags: [web, censorship, surveillance, ethics, methodology]
authors:
 - Burnett, Sam
 - Feamster, Nick
year: 2015
venue: SIGCOMM
eprints:
 doi: 10.1145/2785956.2787485
url: http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p653.pdf
...

As I've mentioned a few times here before, one of the biggest problems
in measurement studies of Web censorship is taking the measurement
from the right place.  The easiest thing (and this may still be
difficult) is to get access to a commercial VPN exit or university
server inside each country of interest.  But commercial data centers
and universities have ISPs that are often somewhat less aggressive
about censorship than residential and mobile ISPs in the same
country---we think. [[1]][] And, if the country is big enough,
it probably has more than one residential ISP, and there's no reason
to think they behave exactly the same. [[2]][] [[3]][]  What we'd
*really* like is to enlist spare CPU cycles on a horde of residential
computers across all of the countries we're interested in.

This paper proposes a way to do just that.  The authors propose to add
a script to globally popular websites which, when the browser is idle,
runs tests of censorship.  Thus, anyone who visits the website will be
enlisted.  The first half of the paper is a technical demonstration
that this is possible, and that you get enough information out of it
to be useful.  Browsers put a bunch of restrictions on what network
requests a script can make---you *can* load an arbitrary webpage in an
invisible `<iframe>`, but you don't get notified of errors and the
script can't see the content of the page; conversely, `<img>` can only
load images, but a script *can* ask to be notified of errors.
Everything else is somewhere in between.  Nonetheless, the authors
make a compelling case for being able to detect censorship of entire
websites with high accuracy and minimal overhead, and a somewhat less
convincing case for being able to detect censorship of individual
pages (with lower accuracy and higher overhead).  You only get a
yes-or-no answer for each thing probed, but that is enough for many
research questions that we can't answer right now.  Deployment is made
very easy, a simple matter of adding an additional third-party script
to websites that want to participate.

The *second* half of the paper is devoted to ethical and practical
considerations.  Doing this at all is controversial---in a box on the
first page, above the title of the paper, there's a statement from the
SIGCOMM 2015 program committee, saying the paper almost got rejected
because some reviewers felt it shouldn't be done.  SIGCOMM also
published a [page-length review][] by John Byers, saying much the same
thing.  George Danezis wrote a [rebuttal][] arguing that the
reviewers' concerns are based on a superficial understanding of what
ethical research in this area looks like.  I am largely in agreement
with Danezis, although I would add that this does not mean I think
Encore should go ahead as is.  Rather, we need to look past the
superficial notions that (a) informed consent is the gold standard for
all research involving people in some way, (b) harm is binary---an
experiment either does or does not harm each person involved in the
study, (c) anyone interacting with an ethical problem is directly
responsible for the entire scope of the problem.

Let's be concrete about the risks involved.  Encore modifies a webpage
such that web browsers accessing it will, automatically and invisibly
to the *user*, also access a number of unrelated webpages (or
resources).  By design, those unrelated webpages contain material
which is considered unacceptable, perhaps to the point of illegality,
in at least some countries.  Moreover, it is known that these
countries mount active <abbr title="man in the middle">MITM</abbr>
attacks on much of the network traffic exiting the country, precisely
to detect and block access to unacceptable material.  Indeed, the
whole point of the exercise is to provoke an observable response from
the MITM, in order to discover what it will and won't respond to.

The MITM has the power to do more than just block access.  It almost
certainly records the client IP address of each browser that accesses
undesirable material, and since it's operated by a state, those logs
could be used to arrest and indict people for accessing illegal
material.  Or perhaps the state would just cut off their Internet
access, which would be a lesser harm but still a punishment.  It could
also send back malware instead of the expected content (we don't know
if that has ever happened in real life, but very similar things have
[[4]][]), or turn around and mount an attack on the site hosting the
material (this definitely _has_ happened [[5]][]).  It could also
figure out that certain accesses to undesirable material are caused by
Encore and _ignore_ them, causing the data collected to be junk, or it
could use Encore itself as an attack vector (i.e. replacing the Encore
program with malware).

In addition to the state MITM, we might also want to worry about other
adversaries in a position to monitor user behavior online, such as
employers, compromised coffee shop WiFi routers, and user-tracking
software.  Employers may have their own list of material that people
aren't supposed to access using corporate resources.  Coffee shop WiFi
is probably interested in finding a way to turn your laptop into a
botnet zombie; any unencrypted network access is a chance to inject
some malware.  User-tracking software might become very confused about
what someone's demographic is, and start hitting them with ads that
relate to whatever controversial topic Encore is looking for
censorship of.  (This last might actually be a Good Thing, considering
the enormous harms behavioral targeting can do. [[6]][])

All of these are harm to someone.  It's important to keep in mind that
except for poisoning the data collected by Encore (harm to the
research itself) all of them can happen in the absence of Encore.
Malware, ad networks, embedded videos, embedded "like" buttons,
third-party resources of any kind: all of these can and do cause a
client computer to access material without its human operator's
knowledge or consent, including accesses to material that some
countries consider undesirable.  Many of them also offer an active
MITM the opportunity to inject malware.

The ethical debate over this paper has largely focused on increased
risk of legal, or quasilegal, sanctions taken against people whose
browsers were enlisted to run Encore tests.  I have two things to say
about that.  First, informed consent would actually make that risk
**worse**.  Because there are so many reasons a computer might contact
a network server without its owner's knowledge, people already have
plausible deniability regarding accesses to controversial material
(i.e. "I never did that, it must have been a virus or something").  If
Encore told its enlistees what it was doing and gave them a chance to
opt out, it would take that away.  Second, I didn't see one word---in
the paper, or in the reviews and rebuttals and ongoing discussion---to
suggest that *anyone* has bothered to talk to lawyers and activists
from the actual countries of interest to find out how serious this
risk is.  The organizations that the authors *are* talking to
([Citizen Lab][], [Oxford Internet Institute][], the
[Berkman Center][]) should have appropriate contacts already or be
able to find them reasonably quickly.

In the absence of expert opinions from people who would know, I'm
inclined to think the non-legal risks involved here are more of a
concern than the legal risks.  We do know, after all, that many of the
countries involved are not nearly as aggressive about filtering the
Internet as they could be, [[7]][] and that makes me think they also
probably can't be bothered to prosecute people just for an occasional
attempt to access stuff that is blocked.  It could still be that they
do prosecute people for *bulk* attempts to access stuff that is
blocked, but Encore's approach---many people doing a few tests---would
tend to avoid that.  There's enough uncertainty that I think
researchers *should* talk to people in a position to know for real,
but meanwhile, all the worry over legal risks has distracted from
worrying about the non-legal risks.  Encore itself has, as far as I
can tell, *no* hardening against MITM manipulation of its own code or
the results sent back---that should be priority number one.  If I were
trying to collect this type of data, I would be more inclined to the
[Herdict][] approach, where people opt in to collection of data about
sites they were going to visit anyway.  That gets around many of the
ethical issues and addresses several technical problems as well, but
does have its own issues, such as revealing people's full browsing
histories to the researchers.

In closing, I think the controversy over this paper is more about the
community not having come to an agreement about its own research
ethics than it is about the paper itself.  If you read the paper
carefully, the
[<abbr title="Institutional Review Board: university committee responsible for protecting human subjects of research">IRB</abbr>][IRB]
at each author's institution did *not* review this research.  They
declined to engage with it.  This was probably a correct decision from
the board's point of view, because an IRB's core competency is medical
and psychological research.  (They've come in for criticism in the
past for reviewing sociological studies as if they were clinical
trials.)  They do not, in general, have the background or expertise to
review this kind of research.  There are efforts underway to change
that: for instance, there was a
[Workshop on Ethics in Networked Systems Research][ws-ethics] at the
very same conference that presented this paper.  (I wish I could have
attended.)  Development of a community consensus here will, hopefully,
lead to better handling of future, similar papers.

[[1]]: /2014/inconsistencies-worlds-largest-firewall/
[[2]]: http://pam2011.gatech.edu/papers/pam2011--Xu.pdf
[[3]]: /2014/regional-variation-chinese-internet-filtering/
[page-length review]: http://conferences.sigcomm.org/sigcomm/2015/pdf/reviews/226pr.pdf
[rebuttal]: https://conspicuouschatter.wordpress.com/2015/08/20/on-the-morals-of-network-research-and-beyond/
[[4]]: http://www.leviathansecurity.com/blog/the-case-of-the-modified-binaries/
[[5]]: https://citizenlab.org/2015/04/chinas-great-cannon/
[[6]]: https://medium.com/@Kendra_Serra/but-what-did-the-daughter-think-8d9233789b4f
[Citizen Lab]: https://citizenlab.org/
[Oxford Internet Institute]: http://www.oii.ox.ac.uk/
[Berkman Center]: https://cyber.law.harvard.edu/
[[7]]: /2012/whiskey-weed-wukan/
[Herdict]: https://www.herdict.org/
[IRB]: https://en.wikipedia.org/wiki/Institutional_review_board
[ws-ethics]: http://conferences.sigcomm.org/sigcomm/2015/netethics.php
