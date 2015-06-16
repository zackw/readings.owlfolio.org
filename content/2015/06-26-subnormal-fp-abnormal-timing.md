---
title: On Subnormal Floating Point and Abnormal Timing
tags: [side channels, information leakage, floating point, hardware]
authors:
 - Andrysco, Marc
 - Kohlbrenner, David
 - Mowery, Keaton
 - Jhala, Ranjit
 - Lerner, Sorin
 - Shacham, Hovav
year: 2015
venue: Oakland
url: http://www.ieee-security.org/TC/SP2015/papers-archived/6949a623.pdf
...

Most of the time, people think the floating-point unit has no security
significance, simply because you don't *use* the floating-point unit
for anything with security significance.  Cryptography,
authentication, access control, process isolation, virtualization,
trusted paths, it's all done with integers.  Usually not even negative
integers.

Today's paper presents some situations where that is not the case:
where the low-level timing behavior of floating-point arithmetic is,
in fact, security-critical.  The most elemental of these situations
involves displaying stuff on the screen---nowadays, everything on the
screen gets run through a 3D rendering pipeline even if it *looks*
completely flat, because you have the hardware just sitting there, and
that process intrinsically involves floating point.  And there's an
API to tell you how long it took to render the previous "frame" of
"animation" because if you were actually animating something you would
genuinely need to know that.  So if there's something being displayed
on the screen that you, a malicious program, are not allowed to know
what it is, but you *can* influence *how* it is being displayed, you
might be able to make the information you're not allowed to know
affect the rendering time, and thus extract the information---slowly,
but not too slowly to be practical.  There is also a scenario
involving "[differentially private][]" databases, where you're allowed
to know an approximation to an aggregate value but not see individual
table rows; the aggregate is computed with floating point, and,
again, computation time can reveal the secret values.

In both cases, the floating-point computations are uniform, with no
data-dependent branches or anything like that, so how does timing
variation sneak in?  It turns out that on all tested CPUs and GPUs,
primitive floating-point arithmetic operations---add, multiply,
divide---don't always take the same amount of time to execute.
Certain combinations of input values are slower than others, and
predictably so.  As the authors point out, this is a well-known
problem for numerical programmers.  It has to do with a feature of
IEEE floating point known as "subnormal numbers."  These allow IEEE
floating point to represent numbers that are very close to zero, so
close that they don't fit into the bit representation without bending
the rules.  This is mathematically desirable because it means that if
two floating-point values are unequal, subtracting one from the other
will never produce zero.  However, subnormals are awkward to implement
in hardware; so awkward that CPUs in the 1990s were notorious for
suffering a slowdown of *100x or more* for basic arithmetic on
subnormals.  Nowadays it's not so bad; if I'm reading the (poorly
designed) charts in this paper correctly, it's only a 2--4x slowdown
on modern hardware.  But that's still enough to detect and build a
timing channel out of.

Timing channels are a perennial problem because they tend to be
side-effects of something desirable.  Algorithms are often easier to
understand if you dispose of special cases up-front---this paper also
talks about how division by zero might be much *faster* than division
by a normal value, presumably because the CPU doesn't bother running
through the divide circuit in that case.  Running fast *most* of the
time, slow in unusual cases, is often an excellent algorithmic choice
for overall performance: hash tables, quicksort, etc.  The papers that
defined the concept of "covert channels" [[1]][] [[2]][] discuss
timing channels introduced by data caching, without which Moore's Law
would have been hamstrung by fundamental physics decades ago.

However, I don't think there's any excuse for variable-time arithmetic
or logic operations, even in floating point. (I *might* be persuaded
to allow it for division, which is genuinely algorithmically hard.)
In particular I have never understood why subnormal numbers are a
problem for hardware.  Now I don't know beans about hardware design,
but I *have* written floating-point emulation code, in assembly
language, and here's the thing: in software, subnormals are
straightforward to implement.  You need larger internal exponent
precision, an additional test in both decode and encode, a
count-leading-zeroes operation on the way in and an extra bit-shift on
the way out.  I didn't try to make my emulator constant-time, but I
can imagine doing it without too much trouble, at least for addition
and multiplication.  In hardware, that seems like it ought to
translate to a wider internal data bus, a couple of muxes, a
count-leading-zeroes widget, and a barrel shifter that you probably
need anyway, and it should be *easy* to make it constant-time across
both subnormals and normals, without sacrificing speed at all.

Constant time floating point operations for *all* inputs and outputs
does strike me as harder, but only because IEEE floating point is
specified to generate hardware faults and/or out-of-band exception
bits under some circumstances.  This was a mistake.  A floating-point
standard that has neither control nor status registers, and generates
exclusively in-band results, is decades overdue.  It would require
sacrificing a bit of mantissa for a sticky "this number is inexact"
flag, but I think that should be acceptable.

As a final headache, how long do you suppose it'll be before someone
comes up with an exploit that can only be fixed by making all of the
transcendental function library (sin, cos, log, exp, ...)
constant-time?  Never mind performance, I doubt this can be done
without severely compromising *accuracy*.

[differentially private]: http://research.microsoft.com/en-us/projects/DatabasePrivacy/
[[1]]: http://gray-world.net/papers/lampson73note.pdf
[[2]]: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.455.2841&rep=rep1&type=pdf
