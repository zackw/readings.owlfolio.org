---
title: "Security Analysis of Android Factory Resets"
tags: [device security, usable security, privacy, data erasure]
authors:
 - Simon, Laurent
 - Anderson, Ross
year: 2015
venue: MoST
url: http://www.ieee-security.org/TC/SPW2015/MoST/papers/s1p3.pdf
...

Unlike the last two papers, today's isn't theoretical at all.  It's a
straightforward experimental study of whether or not any data can be
recovered from an Android phone that's undergone a "factory reset".
Factory reset is *supposed* to render it safe to sell a phone on the
secondhand market, which means any personal data belonging to the
previous owner should be erased *at least* thoroughly enough that the
new owner cannot get at it without disassembling the phone.  (This is
NIST "logical media sanitization," for those who are familiar with
those rules---"digital sanitization," where the new owner cannot
extract any data short of taking an electron microscope to the memory
chip, would of course be better, but in the situations where the
difference matters, merely *having a cell phone* may mean you have
already failed.)

The paper's core finding is also straightforward: due to a combination
of UI design errors, major oversights in the implementation of the
factory-reset feature, driver bugs, and the market's insistence that
flash memory chips have to pretend to be traditional "spinning rust"
hard disks even though they don't work anything like that, *none* of
the phones in the study erased everything that needed to get erased.
The details are confusingly presented, but they're not that important
anyway.  It ends with a concrete set of recommendations for future
improvements, which is nice to see.

There are a few caveats.  The study only covers Android 2.3 through
4.3; it is unclear to me whether the situation is improved in newer
versions of Android.  They don't discuss device encryption at
all---this is at least available in all versions studied, and *should*
completely mitigate the problem provided that a factory reset
successfully wipes out the old encryption keys, and that there's no
way for unencrypted data to survive the encryption process.
(Unfortunately, the normal setup flow for a new phone, at least in the
versions I've used, asks for a bunch of sensitive info *before*
offering to encrypt the phone.  You can bypass this but it's not
obvious how.)  It would be great if someone tested whether encryption
is effective in practice.

Beyond the obvious, this is also an example of Android's notorious
update problem.  Many of the cell carriers cannot be bothered to push
security updates---or *any* updates---to phones once they have been
sold.  [[1]][] They are also notorious for making clumsy modifications
to the software that harm security, usability, or both.  [[2]][] In
this case, this means driver bugs that prevent the core OS from
erasing everything it *meant* to erase, and failure to deploy patches
that made the secure erase mechanism work better.  Nobody really has a
good solution to that.  I personally am inclined to say that neither
the telcos nor Google should be in the business of selling phones, and
conversely, the consumer electronics companies who *are* in that
business should not have the opportunity to make any modifications to
the operating system.  Whatever the hardware is, it's got to work with
a stock set of drivers, and the updates have to come direct from
Google.  That would at least simplify the problem.

(Arguably Google shouldn't be in the OS business either, but that's a
more general antitrust headache.  One thing at a time.)

[[1]]: http://www.androidcentral.com/why-you-ll-never-have-latest-version-android
[[2]]: http://www.howtogeek.com/163558/how-carriers-and-manufacturers-make-your-android-phones-software-worse/
