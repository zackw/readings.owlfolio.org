---
title: Security Analysis of Pseudo-Random Number Generators with Input
tags: [theory, random number generation]
authors:
 - Dodis, Yevgeniy
 - Pointcheval, David
 - Ruhault, Sylvain
 - Vergnaud, Damien
 - Wichs, Daniel
year: 2013
venue: CCS
pages: 647--658
eprints:
  doi: 10.1145/2508859.2516653
  iacr: 2013/338
...

Coming up in this year’s [CCS](http://www.sigsac.org/ccs/CCS2013/) is
a paper with the provocative subtitle “[`/dev/random` is not
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
> nearly full entropy distribution $I$ which is random, except the
> first bit of $\operatorname{Extract}(I)$ is zero).
>
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
CSPRNG construction, which I will now quote verbatim.

> Let $\mathbf{G}: \{0,1\}^m \to \{0,1\}^{n+l}$ be a (deterministic)
> pseudorandom generator where $m < n$. We use the notation $[y]_1^m$
> to denote the first $m$ bits of $y \in \{0,1\}^n$. Our construction
> of PRNG with input has parameters $n$ (state length), $l$ (output
> length), and $p = n$ (sample length), and is defined as follows:
>
> * $\operatorname{setup}:$ Output
>   $\text{seed} = (X, X^\prime)\leftarrow\{0,1\}^{2n}$.
> * $S^\prime = \operatorname{refresh}(S,I):$ Given
>   $\text{seed} = (X, X^\prime)$,
>   current state $S \in \{0,1\}^n$, and a sample $I \in \{0,1\}^n$,
>   output $S^\prime = S \cdot X + I$, where all operations are over
>   $\mathbb{F}_{2^n}$.
> * $(S^\prime, R) = \operatorname{next}(S):$ Given
>   $\text{seed} = (X, X^\prime)$
>   and a state $S \in \{0,1\}^n$, first compute $U = [X^\prime \cdot S]_1^m$.
>   Then output $(S^\prime, R) = \mathbf{G}(U)$.

It's a blink-and-you-miss-it sort of thing: by “all operations are
over $\mathbb{F}_{2^n}$” they are specifying that both the “refresh”
and “next” steps make use of arithmetic over finite Galois fields
(more usually referred to as $\operatorname{GF}(2^n)$ in crypto
literature).  $n$ has to be large—section 6.1 of the paper suggests
specific fields with $n$ = 489, 579, and 705. I am informed that such
arithmetic is “awful” to implement in software, not just difficult but
risking side-channel attacks if not done perfectly, and often quite
slow.

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
