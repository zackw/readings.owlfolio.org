---
title: "Using Memory Errors to Attack a Virtual Machine"
tags: [hardware, memory isolation]
authors:
 - Govindavajhala, Sudakhar
 - Appel, Andrew W.
year: 2003
venue: Oakland
url: https://www.cs.princeton.edu/~appel/papers/memerr.pdf
...

All modern operating systems include some form of process
isolation---a mechanism for insuring that two programs can run
simultaneously on the same machine without interfering with each
other.  Standard techniques include [virtual memory][] and
[static verification][].  Whatever the technique, though, it relies on
"the axiom that the computer faithfully executes its specified
instruction set" (as the authors of today's paper put it).  In other
words, a hardware fault can potentially ruin everything.  But how
practical is it to *exploit* a hardware fault?  They are
unpredictable, and the most common syndrome is for a single bit in RAM
to flip.  How much damage could one bit-flip do, when you have no
control over where or when it will happen?

Today's paper demonstrates that, if you are able to run at least one
program yourself on a target computer, a single bit-flip can give you
total control.  Their exploit has two pieces.  First, they figured out
a way to escalate a single bit-flip to total control of a Java virtual
machine; basically, once the bit flips, they have two pointers to the
same datum but with different types (integer, pointer) and that allows
them to read and write arbitrary memory locations, which in turn
enables them to overwrite the VM's security policy with one that lets
the program do whatever it wants.  That's the hard part. The easy part
is, their attack program fills up the computer's memory with lots of
copies of the data structure that will give them total control if a
bit flips inside it.  That way, the odds of the bit flip being useful
are greatly increased.  (This trick is known as "[heap spraying][]"
and it turns out to be useful for all sorts of exploits, not just the
ones where you mess with the hardware.)

This is all fine and good, but you're still waiting for a cosmic ray
to hit the computer and flip a bit for you, aren't you?  Well, maybe
there are other ways to induce memory errors.  Cosmic rays are
ionizing radiation, which you can also get from radioactivity.  But
readily available radioactive material (e.g. in smoke detectors) isn't
powerful enough, and powerful enough radioactive material is hard to
get (there's a joke where the paper suggests that the adversary could
"purchase a small oil drilling company" in order to get their hands on
a neutron source).  But there's also heat, and that turns out to work
quite well, at least on the DRAM that was commonly available in 2003.
Just heat the chips to 80--100˚C and they start flipping bits.  The
trick here is inducing enough bit-flips to exploit, but not so many
that the entire computer crashes; they calculate an "ideal" error rate
at which the exploit program has a 71% chance of succeeding before the
computer crashes.

The attack in _this_ paper probably isn't worth worrying about in real
life.  But attacks only ever get nastier.  For instance, about a
decade later some people figured out how to control _where_ the memory
errors happen, and how to induce them without pointing a heat gun at
the hardware: that was
"[An Experimental Study of DRAM Disturbance Errors][flipping bits]"
which I reviewed back in April.  _That_ attack is probably practical,
if the hardware isn't taking any steps to prevent it.

[virtual memory]: https://en.wikipedia.org/wiki/Virtual_memory
[static verification]: http://research.microsoft.com/en-us/projects/singularity/
[heap spraying]: http://www.darkreading.com/vulnerabilities---threats/heap-spraying-attackers-latest-weapon-of-choice/d/d-id/1132487
[flipping bits]: /2014/flipping-bits/
