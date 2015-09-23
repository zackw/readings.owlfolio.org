---
title: "Stealthy Dopant-Level Hardware Trojans"
tags: [hardware, sabotage, testing, reverse engineering]
authors:
 - Becker, Georg T.
 - Regazzoni, Francesco
 - Paar, Christof
 - Burleson, Wayne P.
year: 2013
venue: CHES
url: http://iacr.org/workshops/ches/ches2013/presentations/CHES2013_Session4_3.pdf
...

Most of the time we treat silicon chips---CPUs, for instance---as
black boxes.  The manufacturer publishes specifications for
integrating it into a larger widget and making use of it, we code to
those specifications, and the chip does its job.  But inside the
"package" is a fiendishly complicated machine, and there have been
plenty of incidents where it didn't work quite right, e.g. the
infamous [F00F][] and [FDIV][] bugs in the Pentium.  This is not to pick
on Intel; every CPU manufacturer has had similar troubles, but only
the x86 is sufficiently famous that its troubles make Wikipedia.

Anything that can happen by accident can happen on purpose.  Most chip
designers have to contract manufacture out to a [fab plant][] run by a
separate company, and the manufacturing process is opaque to them.  It
might occur to you to wonder whether the manufacturer can tamper with
the design.  It's possible to disassemble a chip under an electron
microscope and make sure all the wires are where they're supposed to
be, but this is expensive and destroys the chip, and it can only
detect some of the possible changes to the design.

This paper presents a technique a fab plant could use to sabotage a
chip design, that _can't_ be detected by any current technique for
inspecting a chip after the fact.  Basically, by changing the
"[dopant][] mask," the fab can turn individual transistors into shorts
to ground or V~cc~.  This is invisible to a microscope; all the wires
are where they're supposed to be, it's just that a block of
semiconductor has the wrong electronic properties.  They demonstrate
that this can be used to introduce subtle bugs that will not be caught
by functional testing, such as making the output of a hardware RNG
predictable, or introducing a power-consumption side channel into a
cryptographic accelerator.

No solutions are presented; I'm not much of a hardware person and I
have no idea what solutions might be possible.  This is the hardware
equivalent of a [malicious compiler][], and people are working on
[solving that problem][]---but they rely on the fact that you
can inspect the output of a compiler in detail, because it's "just"
another string of bits.  How do you detect that a block of silicon has
been doped with boron instead of phosphorus?  X-ray crystallography,
maybe?

[F00F]: https://en.wikipedia.org/wiki/Pentium_F00F_bug
[FDIV]: https://en.wikipedia.org/wiki/Pentium_FDIV_bug
[fab plant]: https://en.wikipedia.org/wiki/Semiconductor_fabrication_plant
[dopant]: https://en.wikipedia.org/wiki/Doping_%28semiconductor%29
[malicious compiler]: https://www.schneier.com/blog/archives/2006/01/countering_trus.html
[solving that problem]: https://wiki.debian.org/ReproducibleBuilds
