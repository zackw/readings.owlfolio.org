---
title: "Robust and Efficient Elimination of Cache and Timing Side Channels"
tags: [side channels, information leakage, adversarial optimization]
authors:
 - Braun, Benjamin A.
 - Jana, Suman
 - Boneh, Dan
year: 2015
venue: preprint
eprints:
 arxiv: 1506.00189 [cs.CR]
...

We're closing out Unpublished Results Week here with a paper that was
"submitted to [CCS 2015][]" last May, but doesn't appear to have made
it.

I've talked about [side channels][] a little before, but let me repeat
why time and cache channels keep coming up and why they're hard to get
rid of: they're side effects of hardware-design choices that, most of
the time, are exactly what you want, if you want your computer to go
fast.  Think about long versus short division, for instance.  It takes
less mental effort, and less scratch paper, to manually divide
123456789 by 3 than by 29; the same is true (sort of) for your
computer.  So if it's your job to design the CPU, why _shouldn't_ the
integer divide instruction finish quicker in the former case?
Especially if you have profiling information that says that _most_ of
the time integer divide gets used with small divisors.  Memory caches
are even more vital---the other day I saw a graph suggesting that it
takes order of _17,000_ clock cycles for the CPU to come all the way
back up to full number crunching speed after a context switch; most of
that is probably due to stuff falling out of the cache and having to
be pulled back in.

So: side channels are hard to get rid of in hardware because that
would involve making design tradeoffs that would hurt performance for
the supermajority of code that isn't crunching sensitive data, and
they're hard to get rid of in _software_ because the hardware, and the
compiler, are actively fighting you.  (The paper says several times
that side-channel-free cryptographic primitives pretty much have to be
done in hand-written assembly language, and that getting them right is
"extremely difficult" even by the standards of people who write
assembly language by hand.)  Wouldn't it be nice to find a big hammer
that would make the problem just ... go away?  That's this paper.

A principal design goal for the big hammer in this paper is ease of
use.  The only thing the application programmer has to do is label
"protected functions" that need to have their side channels
eliminated.  And it's _not_ a compiler paper; they haven't come up
with a way to make a compiler do the extremely difficult assembly
tuning for you.  All the magic happens at runtime.  Given all that, it
works pretty much the only way it _could_ work: it measures how much
the timing varies and then it pads out the fast cases to the same
length as the slow cases.  It also flushes state from the protected
function out of as many CPU caches as possible (memory, TLB, branch
target buffer, ...) after the function is done, and takes steps (page
coloring, CPU and memory pinning, realtime scheduling priority) to
ensure that the protected function is not perturbed by what malicious
code has done _before_ it starts executing.  The authors demonstrate
reliability by testing several different crypto primitives that
definitely do have side-channel information leaks, and showing that
the leak is rendered unavailable in all cases.  They also claim the
overhead is acceptable (8.5%).

I really like the concept and hope to see more in this vein in the
future.  I can't speculate on why this particular paper didn't get
accepted at CCS, but I do feel that the overhead measurements were
inadequate: they don't consider indirect costs of flushing caches and
pinning stuff to CPUs all the time.  I'd like to see whole-system
benchmarking of, say, a shared-hosting HTTPS server.  And at least one
round of adversarial testing would be nice.  It is one thing to
demonstrate that _your_ measurements show that the side channels you
already knew about have been closed; it is another thing if someone
who spends all their time thinking of side-channel attacks cannot find
any in your system.

[CCS 2015]: http://www.sigsac.org/ccs/CCS2015/pro_paper.html
[side channels]: /t/side-channels/
