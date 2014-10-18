Title: Security Analysis of Pseudo-Random Number Generators with Input
Date: 2013-10-24
Tags: theory, random number generation

Coming up in this year’s [CCS](http://www.sigsac.org/ccs/CCS2013/) is
a paper with the provocative subtitle“[`/dev/random` is not
Robust](http://eprint.iacr.org/2013/338),” and thanks to widespread
availability of online preprints, it’s already scored quite a bit of
online attention, e.g. [at Bruce Schneier’s
blog](https://www.schneier.com/blog/archives/2013/10/insecurities_in.html)
and [on Hacker News](https://news.ycombinator.com/item?id=6548893).

I’m going to pass over the alleged attacks on the Linux kernel CSPRNG,
which are adequately covered in both of the above discussions; suffice
it to say that in this paper “robust” is a precisely defined
theoretical security property, and there’s a solid case that it’s
stronger than necessary to guarantee _practical_ security.  What I’m
interested in is the “simple and very efficient PRNG construction that
is provably robust,” advertised in the abstract.  CSPRNG-robustness
(as defined here) may not be _necessary_ for practical security, but
if you can have it essentially for free, _why wouldn’t you_ adopt it?
Unfortunately it turns out that there’s a major palmed card in their
definition of a “CSPRNG with input,” and another one in the
construction itself, rendering the algorithm useless in practice.

The first problem is that the definition of a CSPRNG with input
includes a “setup” phase that produces a _random seed which is not
known to the adversary_.  Despite consistently calling this item a
“public parameter,” the text of the paper makes it clear that it must
not be known to the adversary, and they consider this both essential
and unproblematic:

> Unfortunately, it is well known that no deterministic extractor is
> capable to simultaneously extract good randomness from _all_
> efficiently samplable high-entropy distributions (e.g. consider
> nearly full entropy distribution *I* which is random, except the
> first bit of Extract(*I*) is zero).

> ... [Therefore], we chose ... to assume the existence of the `setup`
> procedure ... this will allow one to consider a *seeded* extractor
> ... which can now extract entropy from _all_ high-entropy
> distributions.  As a warning, this nice extra generality comes at a
> price that the [seed] is not passed to the [adversarial]
> distribution sampler ...

But this is impossible to achieve in real life. If the seed is
generated on the device that will use it, we have a chicken-and-egg
problem, because initial startup is precisely when environmental
randomness is least available; the authors should have been aware of
actual, catastrophic exploits of systems with little or no access to
randomness on first boot,
e.g. “[Mining your Ps and Qs](https://www.factorable.net/paper.html).”
If the seed is _not_ generated on the device that will use it, then
the adversary can probably learn it; in particular, if the seed for
all devices of a particular model is embedded in a firmware image that
anyone can download off the manufacturer's website, you have
accomplished precisely nothing.

The second problem is in the technical details of their proposed
CSPRNG construction, which I will now quote verbatim. This next bit
won't display correctly if your browser doesn't support MathML
(embedded in HTML without benefit of XML goo).

> Let <math><mrow><mrow><mi mathvariant="bold">G</mi></mrow><mo stretchy="false">:</mo><mo stretchy="false" fence="false">{</mo><mn>0</mn><mo stretchy="false">,</mo><mn>1</mn><msup><mo stretchy="false" fence="false">}</mo><mi>m</mi></msup><mo stretchy="false">→</mo><mo stretchy="false" fence="false">{</mo><mn>0</mn><mo stretchy="false">,</mo><mn>1</mn><msup><mo stretchy="false" fence="false">}</mo><mrow><mi>n</mi><mo stretchy="false">+</mo><mi>l</mi></mrow></msup></mrow></math> be a (deterministic) pseudorandom generator where <math><mrow><mi>m</mi><mo stretchy="false">&lt;</mo><mi>n</mi></mrow></math>. We use the notation <math><mrow><mo stretchy="false">[</mo><mi>y</mi><msubsup><mo stretchy="false">]</mo><mn>1</mn><mi>m</mi></msubsup></mrow></math> to denote the first <math><mrow><mi>m</mi></mrow></math> bits of <math><mrow><mi>y</mi><mo stretchy="false">∈</mo><mo stretchy="false" fence="false">{</mo><mn>0</mn><mo stretchy="false">,</mo><mn>1</mn><msup><mo stretchy="false" fence="false">}</mo><mi>n</mi></msup></mrow></math>. Our construction of PRNG with input has parameters <math><mrow><mi>n</mi></mrow></math> (state length), <math><mrow><mi>l</mi></mrow></math> (output length), and <math><mrow><mi>p</mi><mo stretchy="false">=</mo><mi>n</mi></mrow></math> (sample length), and is defined as follows:

> * <math><mrow><mtext>setup</mtext></mrow></math>: Output <math><mrow><mtext>seed</mtext><mo stretchy="false">=</mo><mo stretchy="false">(</mo><mi>X</mi><mo stretchy="false">,</mo><msup><mi>X</mi><mi mathvariant="normal">′</mi></msup><mo stretchy="false">)</mo><mo stretchy="false">←</mo><mo stretchy="false" fence="false">{</mo><mn>0</mn><mo stretchy="false">,</mo><mn>1</mn><msup><mo stretchy="false" fence="false">}</mo><mrow><mn>2</mn><mi>n</mi></mrow></msup></mrow></math>.
> * <math><mrow><msup><mi>S</mi><mi mathvariant="normal">′</mi></msup><mo stretchy="false">=</mo><mtext>refresh</mtext><mo stretchy="false">(</mo><mi>S</mi><mo stretchy="false">,</mo><mi>I</mi><mo stretchy="false">)</mo></mrow></math>: Given <math><mrow><mtext>seed</mtext><mo stretchy="false">=</mo><mo stretchy="false">(</mo><mi>X</mi><mo stretchy="false">,</mo><msup><mi>X</mi><mi mathvariant="normal">′</mi></msup><mo stretchy="false">)</mo></mrow></math>, current state <math><mrow><mi>S</mi><mo stretchy="false">∈</mo><mo stretchy="false" fence="false">{</mo><mn>0</mn><mo stretchy="false">,</mo><mn>1</mn><msup><mo stretchy="false" fence="false">}</mo><mi>n</mi></msup></mrow></math>, and a sample <math><mrow><mi>I</mi><mo stretchy="false">∈</mo><mo stretchy="false" fence="false">{</mo><mn>0</mn><mo stretchy="false">,</mo><mn>1</mn><msup><mo stretchy="false" fence="false">}</mo><mi>n</mi></msup></mrow></math>, output <math><mrow><msup><mi>S</mi><mi mathvariant="normal">′</mi></msup><mo stretchy="false">=</mo><mi>S</mi><mo stretchy="false">⋅</mo><mi>X</mi><mo stretchy="false">+</mo><mi>I</mi></mrow></math>, where all operations are over <math><mrow><msub><mrow><mi mathvariant="double-struck">F</mi></mrow><mrow><msup><mn>2</mn><mi>n</mi></msup></mrow></msub></mrow></math>.
> * <math><mrow><mo stretchy="false">(</mo><msup><mi>S</mi><mi mathvariant="normal">′</mi></msup><mo stretchy="false">,</mo><mi>R</mi><mo stretchy="false">)</mo><mo stretchy="false">=</mo><mtext>next</mtext><mo stretchy="false">(</mo><mi>S</mi><mo stretchy="false">)</mo></mrow></math>: Given <math><mrow><mtext>seed</mtext><mo stretchy="false">=</mo><mo stretchy="false">(</mo><mi>X</mi><mo stretchy="false">,</mo><msup><mi>X</mi><mi mathvariant="normal">′</mi></msup><mo stretchy="false">)</mo></mrow></math> and a state <math><mrow><mi>S</mi><mo stretchy="false">∈</mo><mo stretchy="false" fence="false">{</mo><mn>0</mn><mo stretchy="false">,</mo><mn>1</mn><msup><mo stretchy="false" fence="false">}</mo><mi>n</mi></msup></mrow></math>, first compute <math><mrow><mi>U</mi><mo stretchy="false">=</mo><mo stretchy="false">[</mo><msup><mi>X</mi><mi mathvariant="normal">′</mi></msup><mo stretchy="false">⋅</mo><mi>S</mi><msubsup><mo stretchy="false">]</mo><mn>1</mn><mi>m</mi></msubsup></mrow></math>. Then output <math><mrow><mo stretchy="false">(</mo><msup><mi>S</mi><mi mathvariant="normal">′</mi></msup><mo stretchy="false">,</mo><mi>R</mi><mo stretchy="false">)</mo><mo stretchy="false">=</mo><mrow><mi mathvariant="bold">G</mi></mrow><mo stretchy="false">(</mo><mi>U</mi><mo stretchy="false">)</mo></mrow></math>.

It's a blink-and-you-miss-it sort of thing: by “all operations are
over <math><mrow><msub><mrow><mi
mathvariant="double-struck">F</mi></mrow><mrow><msup><mn>2</mn><mi>n</mi></msup></mrow></msub></mrow></math>”
they are specifying that both the “refresh” and “next” steps make use
of arithmetic over finite Galois fields (more usually referred to as
<math><mi>GF</mi><mo
stretchy="false">(</mo><msup><mn>2</mn><mi>n</mi></msup><mo
stretchy="false">)</mo></math> in crypto literature).
<math><mi>n</mi></math> has to be large—section 6.1 of the paper
suggests specific fields with
<math><mi>n</mi><mo>=</mo><mn>489</mn></math>,
<math><mi>579</mi></math>, and <math><mi>705</mi></math>. I am
informed that such arithmetic is “awful” to implement in software, not
just difficult but risking side-channel attacks if not done perfectly,
and often quite slow.

Both problems arise from the same source, namely wanting to build the
algorithm around a keyed hash so that the entropy extractor is fully
general, and then taking a mathematical construct with convenient
*theoretical* but inconvenient *practical* properties as that hash.
If we back down to the use of an *unkeyed*, but computationally
secure, hash as the entropy extractor, we'd have to redo the analysis,
but I think it ought to be possible to arrange that, *without* any
secret unknown to the adversary, it is still computationally
infeasible for the adversary to bias the entropy pool; and we could
then pick that hash for its practical utility.

... Oddly enough, this hypothetical construction looks an awful lot
like the existing Linux CSPRNG.

    @inproceedings{dodis2013,
      author =       {Dodis, Yevgeniy and Pointcheval, David and
                      Ruhault, Sylvain and Vergnaud, Damien and
                      Wichs, Daniel},
      title =        {{Security Analysis of Pseudo-Random Number
                      Generators with Input: \texttt{/dev/random}
                      is not Robust}},
      booktitle =    {Computer and Communication Security},
      year =         2013,
      url =          {http://eprint.iacr.org/2013/338}
    }
