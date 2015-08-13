---
title: "Limitations of End-to-End Encryption in Secure Computer Networks"
tags: [side channels, information leakage, protocol design]
authors:
 - Padlipsky, Michael A.
 - Snow, D. W.
 - Karger, Paul A.
year: 1978
venue: preprint
url: http://www.dtic.mil/get-tr-doc/pdf?AD=ADA059221
...

Today we're going to go back in time, all the way to the the dawn of
computer networks.  When this technical report was filed, the largest
operational internetwork was still called "ARPAnet" and it still ran
on [<abbr title="Network Control Protocol">NCP</abbr>][NCP]; people
were still talking about "hosts" and "communications subnetwork
processors" as if they were two different physical devices, and
"security levels" as if that was the only possible way to
conceptualize access control; and I was five months old.

(I apologize for the poor quality of the linked PDF---to the best of
my knowledge, this is the only version to be found online.  Also, if
anyone knows D.W. Snow's first name, please tell me.)

To the best of my knowledge, this is the very first published article
to discuss the things that end-to-end encryption (what we would now
call a "secure channel protocol") does _not_ protect from an
eavesdropper.  Everyone doing computer security in 1978 was thinking
mostly about protecting classified government secrets, so the authors
frame the problem in terms of a Trojan Horse program with access to
such secrets, but forbidden by the OS from sending messages to anyone
who isn't cleared to access the same secrets: if all outgoing network
traffic is encrypted end-to-end to its (legitimate) recipient, can
this Trojan Horse still exfiltrate information to someone who _isn't_
a legitimate recipient?

They point out that, of necessity, a packet-switched network has to
reveal the destination address, transmission time, and length of every
packet in cleartext.  They model each of these as Shannonian
communication channels, and determine sending rates on the order of
100 bits per second for each---more than adequate to leak a text
document.  (They observe, by way of comparison, that "the standard
military teletype" runs at 75 bps.)

Nowadays, this threat model might seem quaint, even silly---we put a
lot more effort into preventing untrusted code from seeing secret
information in the first place.  The information leak, however, is
real, still exists, and can be used for other purposes.  The most
terrifying example I know is "[Hookt on fon-iks][]," in which a
completely passive eavesdropper can reconstruct the words spoken in an
encrypted VoIP phone conversation, just from the length and timing of
each packet.  Different syllables compress to different length
packets, and every natural language has rules about which syllables
can follow which; the rules can be modeled with a Markov chain, and
there you are.

The "countermeasures" and "conclusions" sections of this paper are
much more embarrassing in retrospect than the dated threat model.
They say, there's nothing one can practically do about this
end-to-end, but we can close the hole if we make every single
intermediate relay a trusted arbiter of the (one true) security
policy, at which point we don't need end-to-end encryption... I feel
quite confident in saying, even in 1978 it ought to have been obvious
that that was never going to happen.  What's sad is, if people hadn't
given up on end-to-end countermeasures back then, perhaps we would
actually have some by now.  (It's easy for VoIP!  All you have to do
is use a constant-bitrate compression algorithm.  Shame none of the
widely deployed VoIP programs bother.)

[NCP]: http://www.livinginternet.com/i/ii_ncp.htm
[Hookt on fon-iks]: http://www.ieee-security.org/TC/SP2011/PAPERS/2011/paper001.pdf
