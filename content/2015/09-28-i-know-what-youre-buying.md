---
title: "I Know What You're Buying: Privacy Breaches on eBay"
tags: [privacy, anonymity, information leakage, user tracking, web]
authors:
 - Minkus, Tehila
 - Ross, Keith W.
year: 2014
venue: PETS
url: https://petsymposium.org/2014/papers/paper_22.pdf
...

eBay intends not to let anyone else figure out what you're in a habit
of buying on the site.  Because of that, lots of people consider eBay
the obvious place to buy things you'd rather your neighbors not know
you bought (there is a survey in this very paper confirming this
fact).  However, this paper demonstrates that a determined adversary
*can* figure out what you bought.

(Caveat: This paper is from 2014.  I do not know whether eBay has made
any changes since it was published.)

eBay encourages both buyers and sellers to leave "feedback" on each
other, the idea being to encourage fair dealing by attaching a
persistent reputation to everyone.  Feedback is associated with
specific transactions, and anyone (whether logged into eBay or not)
can see each user's complete feedback history.  Items sold are
visible, items bought are not, and buyers' identities are obscured.
The catch is, you can match up buyer feedback with seller feedback by
the timestamps, using obscured buyer identities as a disambiguator,
and thus learn what was bought.  It involves crawling a lot of user
pages, but it's possible to do this in a couple days without coming to
eBay's notice.

They demonstrate that this is a serious problem by identifying users
who purchased gun holsters (eBay does not permit the sale of actual
firearms), pregnancy tests, and HIV tests.  As an additional fillip
they show that people commonly use the same handle on eBay as Facebook
and therefore purchase histories can be correlated with all the
personal information one can typically extract from a Facebook
profile.

Solutions are pretty straightforward and obvious---obscured buyer
identities shouldn't be correlated with their real handles; feedback
timestamps should be quantized to weeks or even months; feedback on
buyers might not be necessary anymore; eBay shouldn't discourage use
of various enhanced-privacy modes, or should maybe even promote them
to the default.  (Again, I don't know whether any of these solutions
has been implemented.)  The value of the paper is perhaps more in
reminding website developers in general that cross-user correlations
are always a privacy risk.
