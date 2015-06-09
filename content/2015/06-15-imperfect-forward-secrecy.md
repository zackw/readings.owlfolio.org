---
title: "Imperfect Forward Secrecy: How Diffie-Hellman Fails in Practice"
tags: [applied cryptography, complexity theory, diffie-hellman,
       backward compatibility, discrete logarithms]
authors:
 - Adrian, David
 - Bhargavan, Karthikeyan
 - Durumeric, Zakir
 - Gaudry, Pierrick
 - Green, Matthew
 - Halderman, J. Alex
 - Heninger, Nadia
 - Springall, Drew
 - Thorne, Emmanuel
 - Valenta, Luke
 - VanderSloot, Benjamin
 - Wustrow, Eric
 - Zanella-Béguelin, Santiago
 - Zimmermann, Paul
year: 2015
venue: preprint
url: https://weakdh.org/imperfect-forward-secrecy.pdf
...

[Diffie-Hellman key exchange][dh] is a cryptographic primitive used
in nearly all modern security protocols.  Like many cryptographic
primitives, it is difficult to break because it is difficult to solve
a particular mathematical problem; in this case, the
"[discrete logarithm problem][dlog]."  Generally, when people try to
break a security protocol, they either look at the pure math of
it---searching for an easier way to solve discrete logarithms---or
they look for mistakes in how the protocol is implemented---something
that will mean you don't _have_ to solve a discrete logarithm to break
the protocol.

This paper does a bit of both.  It observes something about the way
Diffie-Hellman is _used_ in Internet security protocols that makes it
unusually easy to solve the discrete logarithms that will break the
protocol.  Concretely: to break an instance of Diffie-Hellman as
studied in this paper, you have to solve for $x$ in the equation

$$g^x \equiv y \;(\text{mod}\,p)$$

where all numbers are positive integers, $g$ and $p$ are fixed in
advance, and $y$ is visible on the wire.  The trouble is with the
"fixed in advance" part.  It turns out that the most efficient known
way to solve this kind of equation, the
"[general number field sieve][nfs]," can be broken into two stages.
The first stage is much more expensive than the second, and it depends
only on $g$ and $p$.  So if the *same* $g$
and $p$ were reused for many communications, an eavesdropper could do
the first stage in advance, and then breaking individual
communications would be much easier---perhaps easy enough to do on the
fly, as needed.

At least three common Internet security protocols (TLS, IPsec, and SSH) do
reuse $g$ and $p$, if they are not specifically configured otherwise.
As the paper puts it, "if the attacker can precompute for one 1024-bit
group, they can compromise 37% of HTTPS servers in the Alexa Top 1
million, 66% of all probeable IPsec servers, and 26% of all probeable
SSH servers."  A "group" is a specific pair of values for $g$ and $p$,
and the number of bits essentially refers to how large $p$ is.  1024
bits is the smallest size that was previously considered secure; this
paper demonstrates that the precomputation for one such group would
cost only a little less than a billion dollars, most of which goes to
constructing the necessary supercomputer---the incremental cost for
more groups is much smaller.  As such we have to move 1024 bits onto
the "not secure anymore" pile.  (There's an entire section devoted to
the possibility that the [NSA][] might _already have done this._)

(Another section of the paper demonstrates that 512-bit groups can be
precomputed by a small compute cluster, and 768-bit groups by a
substantial (but not enormous) cluster: 110 and 36,500 core-years of
computation, respectively.  The former took one week of wall-clock
time with the equipment available to the authors.  We already knew
those groups were insecure; unfortunately, they are still accepted by
~10% of servers.)

What do we do about it?  If you're running a server, the thing you
should do right now is jump to a 2048-bit group;
[the authors have instructions for common TLS servers and SSH][weakdh-sysadmin],
and generic security configuration guidelines for
[HTTPS servers][moz-https] and [SSH][stribka-ssh] also cover this
topic.  (If you know where to find instructions for IPsec,
please let me know.)  2048 bits is big enough that you probably don't
need to worry about using the same group as anyone else, but
generating your own groups is also not difficult.  It is also
important to make sure that you have
completely disabled support for "[export ciphersuites][]."
This eliminates the 512- and 768-bit groups and also several other
primitives that we know are insecure.

At the same time, it would be a good idea turn *on* support for
TLSv1.2 and modern ciphersuites, including
"[elliptic curve Diffie-Hellman][ecdh]," which requires an attacker to
solve a more complicated equation and is therefore *much* harder to
break.  It's still a discrete logarithm problem, but in a different
"finite field" that is harder to work with.  I don't understand the
details myself, but an elliptic curve group only needs 256 bits to
provide the same security as a 2048-bit group for ordinary
Diffie-Hellman.  There is a catch: the general number field sieve
works for elliptic curves, too.  I'm not aware of any reason why the
precomputation attack in this paper wouldn't apply, and I wish the
authors had estimated how big your curve group needs to be for it to
be infeasible.  256 bits is almost certainly big enough; but how about
128 bits, which is usually considered equivalent to 1024 bits for
ordinary DH?

In the longer timeframe, where we think about swapping out algorithms
entirely, I'm going to say this paper means cryptographers should take
"precomputation should not help the attacker" as a design principle.
We already do this for passwords, where the whole point of "salt" is
to make precomputation not help; it's time to start thinking about
that in a larger context.

Also in the longer timeframe, this is yet another paper demonstrating
that old clients and servers, that only support old primitives that
are now insecure, hurt everyone's security.  Just about every time one
peer continues to support a broken primitive "for backward
compatibility," it has turned out that a man in the middle can
_downgrade_ it---trick it into communicating insecurely even with
counterparties that do support good primitives.  (There's a downgrade
attack to 512-bit Diffie-Hellman groups in this paper.)  This is one
of those thorny operational/incentive alignment problems that hasn't
been solved to anyone's satisfaction.  Windows XP makes an instructive
example: it would have been technically possible for Microsoft to
backport basically all of the security improvements (and other
user-invisible improvements) in later versions of Windows, and there
are an enormous number of people who would have benefited from that
approach.  But it wouldn't have been in Microsoft's own best interest,
so instead they did things geared to force people onto newer versions
of the OS even at the expense of security for people who didn't want
to budge, and people who needed to continue interoperating with people
who didn't want to budge (`schannel.dll` in XP *still* doesn't support
TLS 1.2).  I could spin a similar story for basically every major
player in the industry.


[dh]: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
[dlog]: https://en.wikipedia.org/wiki/Discrete_logarithm
[nfs]: https://en.wikipedia.org/wiki/General_number_field_sieve
[NSA]: https://en.wikipedia.org/wiki/National_Security_Agency
[weakdh-sysadmin]: https://weakdh.org/sysadmin.html
[moz-https]: https://wiki.mozilla.org/Security/Server_Side_TLS
[stribka-ssh]: https://stribika.github.io/2015/01/04/secure-secure-shell.html
[export ciphersuites]: https://security.stackexchange.com/questions/67902/ssl-cipher-suite-what-does-export-mean
[ecdh]: https://en.wikipedia.org/wiki/Elliptic_curve_cryptography
