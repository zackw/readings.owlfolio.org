---
title: The Correctness-Security Gap in Compiler Optimization
tags: [langsec, optimization, formal models, theory]
authors:
 - D'Silva, Vijay
 - Payer, Mathias
 - Song, Dawn
year: 2015
venue: LangSec
url: http://nebelwelt.net/publications/15LangSec/CorrectnessSecurityGap-LangSec15.pdf
...

At this year's [LangSec Workshop][], a paper on formal analysis of
cases where compiled-code optimizations can introduce security holes
that weren't present in the source code.  This class of problems has
been a concern for some time; for a general overview, see this series
of posts on John Regehr's blog: [[1][]] [[2][]] [[3][]].  I'll give one
concrete example, which happens to be the running example in the
paper.

~~~~ {.c}
void crypt (...)
{
    key = load_secret_key();
    ...;          // work with the secure key
    key = 0x0;    // scrub memory
}
~~~~

No *correct* C program can observe values in local variables after a
function returns, so the compiler is very likely to delete the final
store to `key` as unnecessary ("dead" in compiler jargon).  However,
the programmer's intent was to ensure that the secret value in `key`
does not survive in memory after `crypt` returns, where it might be
accessible to *malicious* code---the adversary is not bound by the
definition of "correct C program."  By removing the "dead" store, the
compiler introduces a security hole.

This paper proposes a general strategy for analyzing compiler
optimizations to determine whether or not they can introduce security
holes.  They observe that the definition of "correct C program" is in
terms of an "abstract machine" that ignores or leaves undefined many
low-level nuances.  Continuing with the above example, the C standard
says only that if code *executing in the same program* attempts to
access the memory allocated to `key` after `crypt` returns, "the
behavior is undefined"---anything at all can happen.  In particular,
reading from that memory might legitimately return either zero or the
secret key ... or some other value altogether, or it might crash the
program.  And the standard takes no notice at all of the possibility
that *another* program (such as a debugger, or malware) might gain
access to this program's memory.

The real computer on which the program is executing, by contrast,
exhibits some concrete and (usually) deterministic behavior for any
arbitrary sequence of machine operations.  Even when the architecture
specification leaves an outcome undefined, some concrete thing will
happen on a physical CPU and it will usually be the *same* concrete
thing for all instances of that model of CPU.  This paper's proposal
is simply that compiler optimizations have the potential to introduce
security holes whenever they change the observable behavior of the
physical machine.  Therefore, a correctness proof for an optimization
can be converted into a "does not introduce security holes" proof by
changing its model from the abstract machine to a physical machine.
In the `crypt` example, deleting the final store to `key` is invisible
in the abstract machine, and therefore a valid optimization of the
original code.  But in the physical machine, it means the previous,
secret value persists on the stack (a concept which doesn't even
*exist* in the C abstract machine) and may be retrievable later.  If
the stack is included in the machine model, the original correctness
proof for dead-store elimination will detect the information leak.

Dead-store elimination is well understood as a source of this kind of
problem, and library-level band-aids exist.  I suspect the greatest
value of this technique will be in identifying other optimizations
that can potentially introduce information leaks.  There is some
discussion of this in the paper (common subexpression elimination as a
source of timing-channel vulnerabilities) but they do not take it all
the way to a model.  It would be interesting to know, for instance,
whether the scary-sophisticated algebraic loop-nest transformations
that you might *want* applied to your cryptographic primitives can
introduce data-dependent timing variation that wasn't present in the
source code.

Sadly, this technique by itself is not enough to *prevent*
compiler-introduced vulnerabilities; a dead-store elimination pass
that was valid in the physical machine for all memory writes would
wind up doing almost nothing, which is not what we want.  (The authors
acknowledge this, implicitly, when they talk about the undesirability
of turning all optimizations off.)  To some extent, tightening up the
language specification---making the abstract machine exhibit less
undefined behavior---can help, by making the effects of optimization
more predictable.  John Regehr has a proposal for "[Friendly C][]"
along those lines; I think it throws several babies out with the
bathwater, but as a starting point for discussion it's worthwhile.
It also won't cure all the problems in this area: another example from
the paper is

~~~~ {.c}
int *alloc(int nrelems)
{
    int size = nrelems * sizeof(int);  // may overflow
    if (size < nrelems) abort();       // attempt to check for overflow
    return malloc(size);
}
~~~~

According to the rules of the C abstract machine, signed integer
overflow causes undefined behavior, which means the compiler is
entitled to assume that the comparison `size < nrelems` is always
false.  Unfortunately, making signed integer overflow well-defined
*does not* render this code safe, because the check itself is
inadequate: fixed-width twos-complement wraparound multiplication
(which is the behavior of the integer multiply instruction on most
CPUs) can produce values that are larger than either multiplicand but
smaller than the mathematically correct result, even when one
multiplicand is a small number.  (In this example, with the usual
`sizeof(int) == 4`, passing 1,431,655,766 for `nrelems` would produce
1,431,655,768 for `size` when it should be 5,726,623,064.) For the
same reason, making all the variables unsigned does not help.

On a higher level, compiler authors will fight tooth and nail for
aggressive optimization, because compiler authors (kinda by
definition) *like* writing optimizations, but also because they've got
to satisfy three conflicting user groups at once, and the latter two
are more numerous and have deeper pockets:

1. Systems programmers, who want their C to be translated directly and
   transparently to machine language, and believe that "undefined
   behavior" exists to allow variation in *CPU* behavior but not
   *compiler* behavior.

1. Applications programmers, who want the compiler to crush as many
   abstraction penalties as possible out of their gigantic
   white-elephant C++ codebases which there will never be time or
   budget to clean up.

1. Number crunchers, who care about four things: speed, speed, not
   having to code in FORTRAN or assembly language anymore, and speed.

And what makes this extra fun is that cryptographers are
simultaneously in group 1 and group 3.  I'm not going to make [ETAPS
2015][], but I am *very* curious to know what [DJB][] is going to say
about "[the death of optimizing compilers][]" there.

[LangSec Workshop]: http://spw15.langsec.org/index.html
[1]: http://blog.regehr.org/archives/213
[2]: http://blog.regehr.org/archives/226
[3]: http://blog.regehr.org/archives/232
[Friendly C]: http://blog.regehr.org/archives/1180
[ETAPS 2015]: http://www.etaps.org/index.php/2015
[DJB]: http://cr.yp.to/djb.html
[the death of optimizing compilers]: http://blog.cr.yp.to/20150314-optimizing.html
