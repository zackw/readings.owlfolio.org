---
title: The Security Flag in the IPv4 Header
tags: [philosophy of security, coloured bits]
author: Bellovin, Steven M.
year: 2003
bibtex_type: misc
eprinttype: rfc
eprint: 3514
...

This post is going to be more general-audience-friendly than usual.
Today I propose to explain a classic joke---or perhaps I should call
it a parable instead.

[RFC 3514][] steals a bit from the IPv4 fragment offset field and
redefines it as the "evil bit": packets with malicious intent [MUST][]
set that bit, benign packets [MUST NOT][] set it.  It follows that a
firewall router can protect its network from all attacks by dropping
packets with the evil bit set (and the RFC requires them to do so).
Yay!  Network security is solved, we can all go home!

From the fact that we are all still chained to our desks twelve years
later, you may deduce that network security is *not* solved.  The flaw
is obvious, once pointed out: *nothing can force an attacker to set
the evil bit*.  Nonetheless, there are people who believe that
something resembling this *ought* to work; [Matthew Skala][] called
that belief the phenomenon of "Colour" back in 2004 [[1]][] [[2]][].
Bellovin did not intend his RFC to be implemented; he knew perfectly
well it would not help at all.  But by writing it out so baldly, he
gave us something to point at when people propose the same thing in
less obvious form, which happens *all the time*.  I'm going to give
three examples in increasing order of intractability; the first does
actually have a technical solution (sort of), the second is a
long-standing open problem which *could* have a technical solution
(but no one's thought of it yet), and the third is known to have no
solution at all.

The evil bit is the difference between a [cryptographic hash][] and a
[digital signature][].  A cryptographic hash is a large but
fixed-length number (usually written as a string of hexadecimal)
algorithmically derived from a document.  Many documents produce the
same hash, but it's computationally infeasible to *find* two documents
with the same hash---that is, nobody knows a better way to do it than
guess-and-check, which would take so long that the Sun would be burnt
out before you were done.  Lots of people *think* that this means:
when I give you a document and its hash, you can recompute the hash
and if you get the same thing, you must have the document I meant to
give you.  It is not so.  [Mallory][], the evil mastermind who can
tamper with everything I send you, can change the document, and then
*change the hash* to be the hash of Mallory's document, and you'll
never know the difference.  Mallory can't do this with a digital
signature, which is *also* a large but fixed-length number
algorithmically derived from a document, because---unlike a hash---the
algorithm depends on information that *only I have* (namely, my
signing key).  That you don't also need that information to *check*
the signature is the miracle of [public key cryptography][].

Public key cryptography isn't perfect.  The evil bit is also the
difference between *my* public key, truthfully labeled with my name
and address, and Mallory's public key, which is *also* labeled with my
name and address, because nothing stops Mallory from doing that if
Mallory wants.  How do you tell the difference?  Well, you can look at
https://www.owlfolio.org/contact/ where I have posted a string of
hexadecimal called the "fingerprint" of my public key, and
painstakingly compare that to the fingerprint of the key you just
pulled off the PGP keyservers, and---wait a minute, how do you know
that's *my* website you're looking at?  How do you know Mallory hasn't
modified the fingerprint, and carefully left everything else alone?

Well, it's an HTTPS website, so every page has a digital signature
that the browser verifies for you, and you can click on the lock icon
and observe that GeoTrust, Inc. assures you that you are talking to a
web server operated by the person who controls the domain name
`owlfolio.org`, and then you can consult [whois][] and learn that that
person is known only as "Domain Administrator" at a P.O. box in
Florida, because spam.  That didn't help much, did it?  Besides, why
should you believe GeoTrust, Inc. about this, and how do you know you
have *their* public key?  If you know anything about the
[certificate authority][] system you will know that it is, in fact,
turtles all the way down, and each one of those turtles could be
Mallory in disguise.  There are other ways you could attempt to decide
whose public key you have, but those are *also* turtles all the way
down.

Enough about Mallory, though; let's talk about Reyes.
[Special Agent Reyes][] of the F.B.I., that is.  Reyes' job is
tracking down murderers.  Sometimes Reyes could catch the murderers
faster if he could listen in on their telephone conversations;
sometimes this might, in fact, save someone's life.  The F.B.I. wants
Reyes to catch murderers as fast as possible, so they get Congress
to pass a law that requires
[telephone companies to facilitate wiretapping][CALEA].  Reyes knows
most of what people talk about on the phone is useless to him, even
when those people are murderers, so he only listens in when he's sure
he will hear something that will help one of his cases.

The F.B.I. also employs [Special Agent Sullivan][].  Sullivan does not
track down murderers, he monitors "extremist political groups."  The
Bureau uses a broad definition of extremism: if someone is even
slightly famous and has said something negative about the government
in the last 20 years, Sullivan has a file on them, and all their
friends too.  Sullivan's job is also made considerably easier if he
can listen in on these people's telephone conversations.  Unlike
Reyes, Sullivan records *all* their telephone conversations, all the
time, because Sullivan is looking for dirt.  Sullivan wants to be able
to publicly humiliate each and every one of those people, at a
moment's notice, should it become necessary.  Who decides if it's
necessary?  Sullivan.

The difference between Reyes and Sullivan is the evil bit.

[RFC 3514]: https://tools.ietf.org/html/rfc3514
[MUST]: https://tools.ietf.org/html/rfc2119
[MUST NOT]: https://tools.ietf.org/html/rfc2119
[cryptographic hash]: https://en.wikipedia.org/wiki/Cryptographic_hash_function
[digital signature]: https://en.wikipedia.org/wiki/Digital_signature
[Mallory]: https://en.wikipedia.org/wiki/Man-in-the-middle_attack
[public key cryptography]: https://en.wikipedia.org/wiki/Public-key_cryptography
[whois]: https://en.wikipedia.org/wiki/Whois
[certificate authority]: https://en.wikipedia.org/wiki/Certificate_authority
[Special Agent Reyes]: http://shadowunit.org/
[CALEA]: https://en.wikipedia.org/wiki/Communications_Assistance_for_Law_Enforcement_Act
[Special Agent Sullivan]: https://en.wikipedia.org/wiki/COINTELPRO
[Matthew Skala]: http://ansuz.sooke.bc.ca/
[[1]]: http://ansuz.sooke.bc.ca/entry/23
[[2]]: http://ansuz.sooke.bc.ca/entry/24
