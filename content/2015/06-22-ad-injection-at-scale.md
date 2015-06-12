---
title: "Ad Injection at Scale: Assessing Deceptive Advertisement Modifications"
tags: [advertising, web, malware, software ecology, field observations]
authors:
 - Thomas, Kurt
 - Burzstein, Elie
 - Grier, Chris
 - Ho, Grant
 - Jagpal, Nav
 - Kapravelos, Alexandros
 - McCoy, Damon
 - Nappa, Antonio
 - Paxson, Vern
 - Pearce, Paul
 - Provos, Niels
 - Abu Rajab, Moheeb
year: 2015
venue: Oakland
url: http://www.ieee-security.org/TC/SP2015/papers-archived/6949a151.pdf
...

Today we have a study of "ad injection" software, which runs on your
computer and inserts ads into websites that didn't already have them,
or replaces the website's ads with their own.  (The authors
concentrate on browser extensions, but there are several other places
where such programs could be installed with the same effect.)  Such
software is, in 98 out of 100 cases (figure taken from paper), not
intentionally installed; instead it is a "side-load", packaged
together with something else that the user intended to install, or
else it is loaded onto the computer by malware.

The injected ads cannot easily be distinguished from ads that a
website intended to run, by the person viewing the ads _or_ by the
advertisers.  A website subjected to ad injection, however, can figure
it out, because it knows what its HTML page structure is supposed to
look like.  This is how the authors detected injected ads on a variety
of Google sites; they say that they developed software that can be
reused by anyone, but I haven't been able to find it.  They say that
[`Content-Security-Policy`][csp] should also work, but that doesn't
seem right to me, because page modifications made by a browser
extension _should_, in general, be exempt from CSP.

The bulk of the paper is devoted to characterizing the ecosystem of
ad-injection software: who makes it, how does it get onto people's
computers, what does it do?  Like the malware ecosystem [[1]][]
[[2]][], the core structure of this ecosystem is a layered affiliate
network, in which a small number of vendors market ad-injection
modules which are added to a wide variety of extension modules, and
broker ad delivery and clicks from established advertising exchanges.
Browser extensions are in an ideal position to surveil the browser
user and build up an ad-targeting profile, and indeed, all of the
injectors do just that.  Ad injection is often observed in conjunction
with other malicious behaviors, such as search engine hijacking,
affiliate link hijacking, social network spamming, and preventing
uninstallation, but it's not clear whether the ad injectors themselves
are responsible for that (it could equally be that the extension
developer is trying to monetize by every possible means).  There is no
mention of click-fraud; it is easy for an extension to forge clicks,
so I'm a little surprised the authors did not discuss the possibility.

An interesting tidbit, not followed up on, is that ad injection is
much more common in South America, parts of Africa, South Asia, and
Southeast Asia than in Europe, North America, Japan, or South Korea.
(They don't have data for China, North Korea, or all of Africa.)  This
could be because Internet users in the latter countries are more
likely to know how to avoid deceptive software installers and
malicious extensions, or, perhaps, just less likely to click on ads in
general.

----

Up to this point I have followed the authors' characterization of
ad-injection software as not _necessarily_ malware, just frequently
installed via deceptive means and/or doing some of the same things
that malware is known to do.  In my actual opinion, though, it _is_
automatically malware, and the authors' reluctance to declare it so is
why their proposed solutions are inadequate.  In particular, because
they think ad injection _can_ be legitimate, it does not occur to them
to ask whether extension authors have any viable alternatives if they
want to get paid for their work.  Relatedly, I would have liked to see
some analysis of what the problematic extensions' overt functions
were.  There are legitimate reasons for an extension to add content to
all webpages, e.g. [[3]][] [[4]][], but extension repositories could
reasonably require more careful scrutiny of an extension that asks for
that privilege.

It would also help if the authors acknowledged that the _only_
difference between an ad injector and a "legitimate" ad provider is
that the latter only runs ads on sites with the _site's_ consent.  All
of the negative impact to end users---behavioral tracking, pushing
"organic" content below the fold or under interstitials, slowing down
page loads, and so on---is present with site-solicited advertising.

[[1]]: https://www.usenix.org/legacy/events/sec11/tech/full_papers/Caballero.pdf
[[2]]: https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/40669.pdf
[csp]: http://www.html5rocks.com/en/tutorials/security/content-security-policy/
[[3]]: https://hypothes.is/
[[4]]: http://thenethernet.com/

