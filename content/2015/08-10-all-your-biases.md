---
title: "All Your Biases Belong To Us: Breaking RC4 in WPA-TKIP and TLS"
tags: [rc4, tkip, tls, cryptanalysis, random number generation]
authors:
 - Vanhoef, Mathy
 - Piessens, Frank
year: 2015
venue: USENIX Security
url: http://www.rc4nomore.com/vanhoef-usenix2015.pdf
...

[RC4][] is a very widely used [stream cipher][], developed in the late
1980s.  As wikipedia puts it, RC4 is "remarkable for its speed and
simplicity in software," but it has "weaknesses that argue against its
use in new systems."  Today's paper demonstrates that it is even
weaker than previously suspected.

To understand the paper you need to know how stream ciphers work.  The
core of a stream cipher is a random number generator.  The encryption
key is the starting "seed" for the random number generator, which
produces a "keystream"---a sequence of uniformly random bytes.  You
then combine the keystream with your message using the mathematical
[XOR][] operation, and that's your ciphertext.  On the other end, the
recipient knows the same key, so they can generate the same keystream,
and they XOR the ciphertext with the keystream and get the message
back.

If you XOR a ciphertext with the corresponding _plaintext_, you learn
the keystream.  This wouldn't be a big deal normally, but, the basic
problem with RC4 is that its keystream isn't uniformly random.  Some
bytes of the keystream are more likely to take specific values than
they ought to be.  Some bytes are more likely to _not_ take specific
values.  And some bytes are more likely to take the _same_ value as
another byte in the keystream.  (The "AB*S*AB bias," which is
mentioned often in this paper, is an example of that last case: you
have slightly elevated odds of encountering value A, value B, a middle
sequence *S*, and then A and B again.)  All of these are referred to
as "biases" in the RC4 keystream.

To use RC4's biases to decrypt a message, you need to get your attack
target to send someone (not you) the _same message_ many times,
encrypted with many different keys.  You then guess a keystream which
exhibits as many of the biases as possible, and you XOR this keystream
with all of the messages.  Your guess won't always be right, but it
will be right slightly more often than chance, so the correct
decryption will also appear slightly more often than chance.  It helps
that it doesn't have to be _exactly_ the same message.  If there is a
chunk that is always the same, and it always appears in the same
position, that's enough.  It also helps if you already know some of
the message; that lets you weed out bad guesses faster, and exploit
more of the biases.

Asking the attack target to send the same message many times might
seem ridiculous.  But remember that many Internet protocols involve
"headers" that are fixed or nearly so.  The plaintext of a
TKIP-encrypted message, for instance, will almost always be the WiFi
encapsulation of an IPv4 packet.  If you know the IP addresses of your
target and of the remote host it's communicating with, that means you
know eight bytes of the message already, and they'll always be the
same and in the same position.  The paper goes into some detail about
how to get a Web browser to make lots and lots of HTTPS requests with
a session cookie (always the same, but unknown---the secret you want
to steal) in a predictable position, with known plaintext on either
side of it.

All this was well-known already.  What's new in _this_ paper is:
first, some newly discovered biases in the RC4 keystream, and a
statistical technique for finding even more; second, improved attacks
on TKIP and TLS.  "Improved" means that they're easier to execute
without anyone noticing, and that they take less time.  Concretely,
the best known cookie-stealing attack before this paper needed to see
$13 \cdot 2^{30}$ HTTPS messages (that's about 14 billion) and this
paper cuts it to $9 \cdot 2^{27}$ messages (1.2 billion), which takes
only 75 hours to run.  That's entering the realm of practical in real
life, if only for a client computer that is left on all the time, with
the web browser running.

It's a truism in computer security (actually, security in general)
that _attacks only ever get better_.  What's important, when looking
at papers like this, is not so much the feasibility of any particular
paper's attack, but the _trend_.  The first-known biases in RC4
keystream were discovered only a year after the algorithm was
published, and since then there's been a steady drumbeat of
researchers finding more biases and more effective ways to exploit
them.  That means RC4 is no good, and everyone needs to stop using it
_before_ someone finds an attack that only takes a few minutes.
Contrast the situation with [AES][], where there are no known biases,
and fifteen years of people looking for _some_ kind of attack has
produced only a tiny improvement over brute force.

Advice to the general public: Does this affect you? Yes.  What can you
do about it?  As always, make sure your Web browsers are fully patched
up---current versions of Firefox, Chrome, and IE avoid using RC4, and
upcoming versions will probably take it out altogether.  Beyond that,
the single most important thing for you to do is make sure everything
you've got that communicates over WiFi---router, computers, tablets,
smartphones, etc.---are all set to use [WPA2][] and [CCMP][] *only*.
(The configuration interface may refer to CCMP as "AES-CCMP" or just
"AES"; in this context, those are three names for the same thing.)
The alternatives "WEP", "WPA", and "TKIP" all unavoidably involve RC4
and are known to be broken to some extent.  Any WiFi-capable widget
manufactured after 2006 has no excuse for not supporting WPA2 with
CCMP.  It should definitely be possible to set your home router up
this way; unfortunately, many client devices don't expose the
necessary knobs.

[RC4]: https://en.wikipedia.org/wiki/RC4
[stream cipher]: https://en.wikipedia.org/wiki/Stream_cipher
[TKIP]: https://en.wikipedia.org/wiki/Temporal_Key_Integrity_Protocol
[TLS]: https://en.wikipedia.org/wiki/Transport_Layer_Security
[WPA2]: https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access
[CCMP]: https://en.wikipedia.org/wiki/CCMP
[XOR]: https://en.wikipedia.org/wiki/Exclusive_or
[AES]: https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
