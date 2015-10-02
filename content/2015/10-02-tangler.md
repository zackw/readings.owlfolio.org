---
title: "Tangler: A Censorship-Resistant Publishing System Based On Document Entanglements"
tags: [censorship, circumvention, peer to peer, overlay networks, publishing]
authors:
 - Waldman, Marc
 - Mazières, David
year: 2001
venue: CCS
url: https://gnunet.org/sites/default/files/tangler.pdf
...

Over the years there have been several attempts to build
"[anonymous publication][]" or "distributed anonymous storage"
systems---usually they start with a peer-to-peer file sharing protocol
not entirely unlike [BitTorrent][], and then build some combination of
indexing, replication, encryption, and anonymity on top.  All have at
least one clever idea.  None has achieved world domination.  (We'll
know someone's finally gotten it right when the web browsers start
shipping native support for their protocol.)

Tangler is a relatively old example, and its one clever idea is what
they call _document entanglement_.  To understand document
entanglement you have to know about something called "$k$-of-$n$
[secret sharing][]."  This is a mathematical technique that converts a
secret into $n$ _shares_.  Each share is the same size as the original
secret, possibly plus a little overhead.  Anyone who has a copy of $k$
of those $n$ shares can reconstruct the original secret, but if they
have even just one fewer, they can't.  $k$ and $n$ can be chosen
arbitrarily.  Secret sharing is normally not used for large secrets
(like an entire document) because each share is the same size as the
original, so you've just increased your overall storage requirement
$n$ times---but in a distributed document store like Tangler, you
were going to do that anyway, because the document should remain
retrievable even if some of the peers holding shares drop out of the
network.

Document entanglement, then, is secret sharing with a clever twist:
you arrange to have some of the $n$ shares of your document be the
same bitstring as *existing* shares for *other* documents.  This is
always mathematically possible, as long as fewer than $k$ existing
shares are used.  This reduces the amount of data added to the system
by each new document, but more importantly, it makes the
correspondence between shares and documents many-to-many instead of
many-to-one.  Thus, operators can honestly say they do not know which
documents are backed by which shares, and they have an incentive not
to cooperate with deletion requests, since deleting one document may
render many other documents inaccessible.

I am not convinced entanglement actually provides the security benefit
claimed; deleting all $n$ of the shares belonging to one document
should cause other documents to lose no more than *one* share and thus
not be permanently damaged.  (The originators of those documents would
of course want to generate new shares to preserve redundancy.)  It is
still probably worth doing just because it reduces the cost of adding
new documents to the system, but security-wise it's solving the wrong
problem.  What you really want here is: server operators should be
unable to determine which documents they hold shares for, *even if*
they know the metadata for those documents.  (And yet, somehow, they
must be able to hand out the right shares on request!)  Similar things
*are* possible, under the name [private information retrieval][], and
people *are* trying to apply that to anonymous publication, but what I
said one really wants here is even stronger than the usual definition
of PIR, and I'm not sure it's theoretically possible.

[anonymous publication]: http://freehaven.net/anonbib/full/topic.html#Anonymous_20publication
[BitTorrent]: https://en.wikipedia.org/wiki/BitTorrent
[secret sharing]: https://en.wikipedia.org/wiki/Secret_sharing
[private information retrieval]: https://en.wikipedia.org/wiki/Private_information_retrieval
