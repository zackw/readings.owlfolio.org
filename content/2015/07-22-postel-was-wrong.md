---
title: "The Harmful Consequences of Postel's Maxim"
tags: [langsec, protocol design, philosophy of security]
authors:
 - Thomson, Martin
year: 2015
venue: preprint
eprints:
 i-d: thomson-postel-was-wrong
...

Postel's Maxim of protocol design (also known as the Robustness
Principle or the Internet Engineering Principle) is "Be liberal in
what you accept, conservative in what you send."  It was first stated
as such (by [Jon Postel][]) in the 1979 and 1980 specifications
(e.g. [RFC 760][]) of the protocol that we now call IPv4. [[1]][] It's
been tremendously influential, for instance quoted as an "axiom" in
Tim Berners-Lee's design principles for the Web [[2]][] but has also
come in for a fair bit of criticism [[3]][] [[4]][].  (An expanded
version of the principle, in [RFC 1122][], anticipates many of these
criticisms and is well worth reading if you haven't.) Now we have an
[Internet-Draft][] arguing that it is fatally flawed:

> ... there are negative long-term consequences to interoperability if
> an implementation applies Postel's advice.  Correcting the problems
> caused by divergent behavior in implementations can be difficult or
> impossible.

and arguing that instead

> Protocol designs and implementations should be maximally strict.
>
> Generating fatal errors for what would otherwise be a minor or
> recoverable error is preferred, especially if there is any risk that
> the error represents an implementation flaw.  A fatal error provides
> excellent motivation for addressing problems.
>
> The primary function of a specification is to proscribe behavior in
> the interest of interoperability.

This is the first iteration of an Internet-Draft, so it's not intended
to be *done*, so rather than express an opinion as such, I want to put
forward some examples of real-world situations from the last couple
decades of Internet protocol design that the author may or may not
have considered, and ask how he feels they should be / have been
handled.  I also invite readers to suggest further examples where
strictness, security, upward compatibility, incremental deployment,
ergonomics, and so on may be in tension.

* The original IP and TCP (v4) specifications left a number of bits
  "reserved" in their respective packet headers.  In 2001 the [ECN][]
  specification gave meaning to some of those bits.  It was almost
  immediately discovered that many intermediate routers would silently
  discard packets with the ECN bits set; in consequence, fourteen
  years later ECN is still quite rarely used, even though there are
  far fewer such routers than there were in 2001. [[5]][] [[6]][]

* Despite the inclusion of a protocol version number in SSL/TLS, and a
  clear specification of how servers were supposed to react to clients
  offering a newer protocol than they supported, servers that drop
  connections from too-new clients are historically quite common, so
  until quite recently Web browsers would retry such connections with
  an older protocol version.  This enables a man-in-the-middle to force
  negotiation of an old, possibly insecure version, even if both sides
  support something better. [[7]][] [[8]][] [[9]][]  Similar to the
  ECN situation, this problem was originally noticed in 2001 and
  continues to be an issue in 2015.

* Cryptographic protocols (such as TLS) can be subverted---and I mean
  "complete breach of confidentiality" subverted---if they reveal
  *why* a message failed to decrypt, or *how long* it took to decrypt
  / fail to decrypt a message, to an attacker that can forge
  messages. [[10]][] [[11]][] To close these holes it may be necessary
  to run every message through the complete decryption process even if
  you already know it's going to fail.

* In the interest of permitting future extensions, HTML5 [[12]][] and
  CSS [[13]][] take pains to specify exact error recovery behavior;
  the idea is that older software will *predictably* ignore stuff it
  doesn't understand, so that authors can be sure of how their
  websites will look in browsers that both do and don't implement each
  shiny new feature.  However, this means you can predict how the
  *CSS* parser will parse *HTML* (and vice versa).  And in conjunction
  with the general unreliability of MIME types it means you used to be
  able to exploit that to extract information from a document you
  shouldn't be able to read. [[14]][]  (Browsers fixed this by
  becoming pickier about MIME types.)

[Jon Postel]: http://www.postel.org/postel.html
[RFC 760]: https://tools.ietf.org/html/rfc760#section-3.2
[[1]]: http://ironick.typepad.com/ironick/2005/05/my_history_of_t.html
[[2]]: http://www.w3.org/DesignIssues/Principles.html
[[3]]: https://tools.ietf.org/html/rfc3117#section-4.5
[[4]]: http://fishbowl.pastiche.org/2002/12/29/gresham_trumps_postel/
[Internet-Draft]: https://en.wikipedia.org/wiki/Internet_Draft
[ECN]: https://en.wikipedia.org/wiki/Explicit_Congestion_Notification
[[5]]: http://conferences.sigcomm.org/imc/2011/docs/p171.pdf
[[6]]: http://ecn.ethz.ch/ecn-pam15.pdf
[[7]]: https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/Notes_on_TLS_-_SSL_3.0_Intolerant_Servers
[[8]]: https://security.stackexchange.com/a/66785/10
[[9]]: https://www.imperialviolet.org/2011/02/04/oppractices.html
[[10]]: http://blog.cryptographyengineering.com/2013/02/attack-of-week-tls-timing-oracles.html
[[11]]: https://en.wikipedia.org/wiki/Padding_oracle_attack
[[12]]: https://html.spec.whatwg.org/multipage/syntax.html#an-introduction-to-error-handling-and-strange-cases-in-the-parser
[[13]]: http://dev.w3.org/csswg/css2/syndata.html#parsing-errors
[[14]]: https://hacks.owlfolio.org/pubs/2010-protecting.pdf
[RFC 1122]: https://tools.ietf.org/html/rfc1122#section-1.2.2
