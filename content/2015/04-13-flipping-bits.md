---
title: "Flipping Bits in Memory Without Accessing Them:
        An Experimental Study of DRAM Disturbance Errors"
tags: [hardware, memory isolation]
authors:
 - Kim, Yoongu
 - Daly, Ross
 - Kim, Jeremie
 - Fallin, Chris
 - Lee, Ji Hye
 - Lee, Donghyuk
 - Wilkerson, Chris
 - Lai, Konrad
 - Mutlu, Onur
year: 2014
venue: ISCA
eprints:
  doi: 10.1145/2663716.2663750
url: http://www.cfall.in/pubs/isca2014_bitflips.pdf
...

A few weeks ago, a new exploit technique called "[rowhammering][]" was
making the rounds of all the infosec news outlets.  Turns out you can
flip bits in RAM by *reading* over and over and over again from bits
that are physically adjacent on the RAM chip; turns out that with
sufficient cleverness you can leverage that to escape security
restrictions being enforced in software.  Abstractly, it's as simple
as toggling the "this process is allowed to do whatever it wants" bit,
which is a real bit in RAM on many operating systems---most of the
cleverness is in "grooming" the layout of physical RAM so that that
bit is physically adjacent to a group of bits that you're allowed to
read from.

This paper describes and analyzes the underlying physical flaw that
makes this exploit possible.  It is (as far as I know) the first
suggestion in the literature that this might be a *security*
vulnerability; chip manufacturers have been aware of it as a
*reliability* problem for much longer. [[1]][] [[2]][] If you're not
familiar with the details of how [DRAM][] works, there are two
important things to understand.  First, DRAM deliberately trades
stability for density.  You can (presently) pack more bits into a
given amount of chip surface area with DRAM than with any other
design, but the bits don't retain their values indefinitely; each bit
has an electrical charge that slowly leaks away.  DRAM is therefore
"refreshed" continuously; every few tens of milliseconds, each bit
will be read and written back, restoring the full charge.

Second, software people are accustomed to thinking of memory at the
lowest level of abstraction as a one-dimensional array of bytes, an
"address space."  But DRAM is physically organized as a
*two*-dimensional array of *bits*, laid out as a grid on the
two-dimensional surface of the chip.  To read data from memory, the
CPU first instructs the memory bank to load an entire "row" into a
buffer (unimaginatively called the "row buffer"), and then to transmit
"columns" (which are the width of entire cache lines) from that row.
Rows are huge---32 to 256 kilobits, typically; larger than the "page"
granularity of memory access isolation.  This means, bits which are
far apart in the CPU's address spaces (even the so-called "physical"
address space!) may be right next to each other on a RAM chip.  And
bits which are right next to each other on a RAM chip may belong to
different memory-isolation regions, so it's potentially a security
problem if they can affect each other.

Now, the physical flaw is simply that loading one row of a DRAM chip
into the row-buffer can cause adjacent rows to leak their charges
faster, due to unavoidable electromagnetic phenomena, e.g. capacitative
coupling between rows.  Therefore, if you force the memory bank to
load a particular row over and over again, enough charge might leak
out of an *adjacent* row to make the bits change their values.
(Reading a row implicitly refreshes it, so the "attack" row itself
won't be affected.)  It turns out to be possible to do this using only
ordinary CPU instructions.

The bulk of this paper is devoted to studying exactly when and how
this can happen on a wide variety of different DRAM modules from
different vendors.  Important takeaways include: All vendors have
affected products.  Higher-capacity chips are more vulnerable, and
*newer* chips are more vulnerable---both of these are because the
bit-cells in those chips are smaller and packed closer together.  The
most common error-correcting code used for DRAM is inadequate to
protect against or even detect the attack, because it can only correct
one-bit errors and detect two-bit errors within any 64-bit word, but
under the attack, *several* nearby bits often flip at the same time.
(You should still make a point of buying error-correcting RAM, plus a
motherboard and CPU that actually take advantage of it.  One-bit
errors are the normal case and they can happen as frequently as once a
day.  See "[Updates on the need to use error-correcting memory][dram-errors]"
for more information.)

Fortunately, the authors also present a simple fix: the memory
controller should automatically refresh nearby rows with some low,
fixed probability whenever a row is loaded.  This will have no visible
effect in normal operation, but if a row is being "hammered," nearby
rows will get refreshed sufficiently more often that bit flips will
not happen.  It's not clear to anyone whether this has actually been
implemented in the latest motherboards, vendors being infamously
closemouthed about how their low-level hardware actually works.
However, several of the authors here work for Intel, and I'd expect
them to take the problem seriously, at least.

[rowhammering]: http://googleprojectzero.blogspot.com/2015/03/exploiting-dram-rowhammer-bug-to-gain.html
[DRAM]: https://en.wikipedia.org/wiki/Dynamic_random-access_memory
[dram-errors]: http://lambda-diode.com/opinion/ecc-memory-2
[[1]]: https://www.google.com/patents/US5010524
[[2]]: https://www.google.com/patents/US7388796
