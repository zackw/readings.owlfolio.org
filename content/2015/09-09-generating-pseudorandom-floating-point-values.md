---
title: "Generating Pseudo-random Floating-Point Values"
tags: [random number generation, floating point]
authors:
 - Downey, Allan B.
year: 2007
venue: preprint
url: http://allendowney.com/research/rand/downey07randfloat.pdf
...

Like Monday's paper, today's has not been officially published
anywhere, and in fact appears never to have been _finished_.  It's on
a fairly arcane topic, and one that's not _directly_ related to
security---as I said
[a while back](/2015/subnormal-fp-abnormal-timing/), floating-point
numbers usually aren't used in security-critical algorithms.  However,
it deserves more attention, being both a case of "everyone everywhere
is Doing It Wrong," and a nice example of the danger of forgetting
that an abstraction is hiding something from you.

For numerical and statistical computation, one frequently needs random
floating-point numbers in the open interval $(0,\,1)$.  However, all
off-the-shelf pseudorandom number generators produce either random
_integers_, or a stream of random _bits_ (which is functionally the
same thing---bits are trivially put together into integers and vice
versa).  The easy, obvious way to bridge the gap is to divide (in
floating point) the integers by the largest value the PRNG can
produce.  This is how it's done basically everywhere, including
industrial-grade statistical languages like [R][]...but what the paper
is saying is, it's wrong.

To understand why it's wrong, you need to understand in detail how
floating-point numbers are _not_ mathematical real numbers.  On one
level this is obvious: an IEEE single occupies 32 bits and a double
64, so at most they could represent $2^{32}$ or $2^{64}$ different
numbers, respectively; that isn't even _countably_ infinite.  (A
large chunk of the encoding is reserved for "not a number" values, so
the true count is somewhat smaller.)  But high-level programming
languages encourage us to _use_ floating point numbers as if they were
the reals, and most of the time we're working with values that are
well-approximated by floats, and we get away with it.

The numbers that a binary floating-point format can represent are all
of the form

<math display="block"><mi mathvariant="italic">±m.mmm…m</mi><mo>×</mo><msup><mn>2</mn><mi mathvariant="italic">±e.eee…e</mi></math>

where
<math display="inline"><mi mathvariant="italic">±m.mmm…m</mi></math>
(the _mantissa_) and
<math display="inline"><mi mathvariant="italic">±e.eee…e</mi></math>
(the _exponent_) are binary numbers of fixed length.  For IEEE
singles, the mantissa has 25 bits and the exponent 8, counting their
respective signs in both cases, and there's a clever trick (not
relevant here) to fit that all into 32 bits total.  This is "just" the
scientific notation you probably learned in high school, in base 2
instead of base 10, and _if the mantissa and exponent were infinitely
wide_ it could represent all real numbers.  However, they are finite,
and this means not only that it can't, but that the values it can are
not uniformly distributed over the real line.  Every time you pass a
power of two, the exponent ticks up or down by one, but the mantissa
stays the same length, so it loses or gains one bit of precision.
Therefore, there are the same number of representable values between 1
and 2 as there are between 0.5 and 1, between 0.25 and 0.5, and so on,
and each range's representable numbers are twice as far apart as those
in the next smaller range.

<figure class="fig-width-75 fig-smallgap"><img
src="/i/2007/downey01-fig1.svg"><figcaption>Some of the numbers
representable by an IEEE single-precision float (top row) and
producible by dividing a 32-bit unsigned integer by $2^{32}-1$ (bottom
row).</figcaption></figure>

Now, when you generate a random integer and divide it by the largest
integer the RNG can produce, the result _is_ uniformly distributed
over $(0,\,1)$.  If the largest integer the RNG can produce is
$2^{32}-1$, as is often the case (even on systems with 64-bit
integers), the gap between values producible by this method will be
about $2 \times 10^{-10}$.  The figure above compares the spacing of
these values along the real line with the spacing of the values
representable by an IEEE single-precision float.  Only from
0.001953125 ($2^{-9}$) to 0.003906250 ($2^{-8}$) is there a one-to-one
correspondence.  Above $2^{-8}$, the representable numbers are more
widely spaced than the values that the RNG will produce, which means
clusters of RNG-produced values will get rounded to the same
representable number, which introduces non-uniformity.  Below
$2^{-9}$, it's the other way around: all of the RNG-produced values
are exactly representable, but there are many more that can't be
produced.  Downey estimates that over the entire range, only 7% of the
numbers are producible.

The most significant gap is right _at_ zero.  The smallest number IEEE
single can represent is on the order of $10^{-38}$ or $10^{-45}$
(depending on whether you allow "[denormals][]"), and IEEE double goes
all the way down to $2 \times 10^{-308}$ (or $5 \times 10^{-324}$ with
denormals).  But, the smallest number producible by the simple RNG
method is $2 \times 10^{-10}$, dozens or hundreds of decimal orders of
magnitude bigger.  Downey suggests that this could cause serious
problems for statistical algorithms, such as
[inverse transform sampling][] of the exponential distribution.

Downey's proposed fix rests on the observation that a random number
uniformly distributed over $(0,\,1)$ will be greater than 0.5 exactly
half of the time; when it isn't, it will be greater than 0.25 exactly
half of the time; and so on.  Therefore, his algorithm first selects
an exponent by flipping coins in a loop---that is, drawing one _bit_
at a time from the output of the RNG.  The exponent starts out as −1,
corresponding to a number between 0.5 and 1; each time the bit is 0,
the exponent is reduced by 1 and another bit is drawn, until either a
1 is drawn or the exponent reaches its minimum allowable value.  Then
the algorithm fills in the mantissa with random bits.  Finally,
there's a small correction: if the mantissa happens to come out zero,
flip another bit and if it's 1, _increase_ the exponent by 1 again.
This accounts for values that are exactly 1 over a power of two,
which straddle a boundary between exponents and therefore can be
selected from either side; without the correction they would be
selected slightly more often than is appropriate.

It's too bad Downey never finished this paper.  The biggest missing
piece is a clear and convincing demonstration that the naïve algorithm
_does_ introduce significant errors into common calculations.  For
exponential sampling by inverse transform, there is an inarguable
_error_ (the distribution is truncated on the right) but one could
argue that it doesn't rise to the level of _significance_ because
exponential deviates larger than 9.3 should only get drawn one time in
$10^{10}$ or so.  There are no other examples of potentially
problematic tasks, and I am not enough of a statistician to think of
any myself.  IEEE _double_ has enough mantissa, even in the range from
0.5 to 1, that it can represent every multiple of $2 \times 10^{-10}$,
so nonuniformity does not occur if you're generating doubles by the
simple method, only missing values.

There are also a couple of practical problems with the algorithm.  A
potentially-lengthy run of coin tosses, with the requirement that
every bit is independent and identically distributed, is poorly
handled by many "ordinary" RNGs; I would only use this algorithm with
a cryptographic RNG.  Relatedly, on average the coin-tossing phase
will terminate quickly, but if you do hit a long run of zeroes it'd be
observably slower in that case.  I don't see a good way to implement
the algorithm so that it uses a _fixed_ number of random bits per
float generated, though, short of "generate _all_ the coin tosses in
advance" which would consume 1078 bits of randomness for every IEEE
double; this would probably be unacceptably slow overall.

[R]: http://r-project.org/
[denormals]: https://en.wikipedia.org/wiki/Denormal_number
[inverse transform sampling]: https://en.wikipedia.org/wiki/Inverse_transform_sampling
