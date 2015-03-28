---
title: Analysis of the HTTPS Certificate Ecosystem
tags: [pki, https, field observations]
authors:
 - Durumeric, Zakir
 - Kasten, James
 - Bailey, Michael
 - Halderman, J. Alex
year: 2013
bibtex_type: inproceedings
booktitle: Internet Measurement Conference
booktitle_url: http://conferences.sigcomm.org/imc/2013/
pages: 291--304
organization: ACM SIGCOMM
doi: 10.1145/2504730.2504755
pdf_url: https://jhalderm.com/pub/papers/https-imc13.pdf
...

The
_[Internet Measurement Conference](http://conferences.sigcomm.org/imc/2013/)_
brings us an attempt to figure out just how
[X.509 server certificates](http://www.digicert.com/ssl.htm) are being
used “in the wild,” specifically for HTTPS servers. Yet more
specifically, they are looking for endemic operational problems that
harm security.  The basic idea is to scan the entire IPv4 number space
for servers responding on port 443, make note of the certificate(s)
presented, and then analyze them.

This research question is nothing new; the [EFF](https://www.eff.org/)
famously ran a similar study back in 2010, the
[SSL Observatory](https://www.eff.org/observatory). And operational
concerns about the way certificates are used in the wild go back
decades; see [Peter Gutmann](http://www.cs.auckland.ac.nz/~pgut001)’s
slide deck “[Everything you Never Wanted to Know about PKI but were
Forced to Find Out](http://www.cs.auckland.ac.nz/~pgut001/pubs/pkitutorial.pdf)”
(PDF).  What makes this study interesting is, first, it’s three years
later; things _can_ change very fast in Internet land (although, in
this case, they have not).  Second, the scale: the authors claim to
have successfully contacted 178% more TLS hosts (per scan) and
harvested 736% more certificates (in total, over the course of 110
scans spanning a little more than a year) than any previous such
study.

What do we learn?  Mostly that yeah, the TLS PKI is a big mess, and it
hasn’t gotten any better since 2010.  There are too many root
CAs. There are _far_ too many unconstrained intermediate certificates,
and yet, at the same time, there are too _few_ intermediates! (The
point of intermediates is that they’re easy to replace, so if they get
compromised you don’t have a catastrophe on your hands. Well,
according to this paper, some 26% of all currently valid HTTPS server
certificates are signed by _one_ intermediate. No way is that going to
be easy to replace if it gets compromised.)  Lots of CAs ignore the
“baseline” policies for certificate issuance and get away with it.
(Unfortunately, the paper doesn’t say whether there are similar
problems with the EV policies.)

Zoom out: when you have a piece of critical infrastructure with
chronic operational issues, it’s a safe bet that they’re symptoms and
the _real_ problem is with operator incentives.  The paper doesn’t
discuss this at all, unfortunately, so I’ll throw in some speculation
here. The browser vendors are notionally in the best position to Do
Something about this mess, but they don’t: because the only real
option they have is to delete root certificates from the Official
List. Not only does this tend to put the offending CA out of business,
it also causes some uncertain-but-large number of websites (most or
all of which didn’t do anything wrong) to stop working.  Such a
drastic sanction is almost never seen to be appropriate.  Browsers
have hardly any good _positive_ incentives to offer the CAs to do
things right; note that EV certificates, which get special treatment
in the browser UI and can therefore be sold at a premium, do come with
a tighter set of CA requirements (stronger crypto, reliable OCSP, that
sort of thing) which are, as far as I’m aware, followed.

Zoom out again: there’s no shortage of technical suggestions that
could turn into less drastic sanctions and incentives for the CAs, but
they never get implemented: why?  Well, you ask me, I say it’s because
both OpenSSL and NSS are such terrible code that nobody wants to hack
on them, and the brave souls who do it anyway are busy chipping away
at the mountain of technical debt and/or at features that are _even
more_ overdue. (*cough* TLS 1.1) This, though, we know how to fix. It
only takes money.
