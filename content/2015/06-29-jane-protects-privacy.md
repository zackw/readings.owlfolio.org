---
title: "Why Doesn't Jane Protect Her Privacy?"
tags: [privacy, usable security, email]
authors:
 - Renaud, Karen
 - Volkamer, Melanie
 - Renkema-Padmos, Arne
year: 2014
venue: PETS
eprints:
  doi: 10.1007/978-3-319-08506-7_13
url: https://www.petsymposium.org/2014/papers/paper_81.pdf
...

Today's paper is very similar to
"[What Deters Jane from Preventing Identification and Tracking on the Web?][deters]"
and shares an author.  The main difference is that it's about email
rather than the Web.  The research question is the same: why don't
people use existing tools for enhancing the security and privacy of
their online communications?  (In this case, specifically tools for
end-to-end encryption of email.)  The answers are also closely
related. As before, many people think no one would bother snooping on
them because they aren't important people.  They may understand that
their webmail provider reads their email in order to select ads to
display next to it, but find this acceptable, and believe that the
provider can be trusted not to do anything *else* with its knowledge.
They may believe that the only people in a position to read their
email are nation-state espionage agencies, and that trying to stop
*them* is futile.  All of these are broadly consistent with the
results for the Web.

A key difference, though, is that users' reported understanding of
email-related security risks is often about a different category of
threat that end-to-end encryption doesn't help with: spam, viruses,
and phishing.  In fact, it may hurt: one of Gmail's (former) engineers
went on record with a detailed argument for why their ability to read
all their users' mail was essential to their ability to filter spam.
[[1]][] I'm not sure that isn't just a case of not being able to see
out of their local optimum, but it certainly does make the job
simpler.  Regardless, it seems to me that spam, viruses, and phishing
are a much more visible and direct threat to the average email user's
personal security than any sort of surveillance.  Choosing to use a
service that's very good at filtering, even at some cost in privacy,
therefore strikes me as a savvy choice rather than an ignorant one.
Put another way, I think a provider of end-to-end encrypted email
needs to demonstrate that it can filter junk just as effectively if it
wants to attract users away from existing services.

(In the current world, encryption is a signal of *not* being spam, but
in a world where most messages were encrypted, spammers would start
using encryption, and so would your
<abbr title="pointy-haired boss">PHB</abbr> who keeps sending you
virus-infected spreadsheets that you have to look at for your job.)

Another key difference is, you can unilaterally start using Tor,
anti-tracking browser extensions, and so on, but you can't
unilaterally start encrypting your email.  You can only send encrypted
email to people who can *receive* encrypted email.  Right now, that
means there is a strong network effect *against* the use of encrypted
email.  There's not a single word about this in the paper, and I find
that a serious omission.  It does specifically say that they avoided
asking people about their experiences (if any) with PGP and similar
software because they didn't want to steer their thinking that way,
but I think that was a mistake.  It means they can't distinguish what
people think about email privacy in general, from what they think
about end-to-end encryption tools that they may have tried, or at
least heard of.  There may be a substantial population of people who
only looked into PGP just enough to discover that it's only useful if
the recipient also uses it, and don't think of it anymore unless
specifically prompted about it.


[deters]: /2014/jane-prevents-tracking/
[[1]]: https://moderncrypto.org/mail-archive/messaging/2014/000780.html
