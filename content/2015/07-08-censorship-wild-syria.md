---
title: "Censorship in the Wild: Analyzing Internet Filtering in Syria"
tags: [censorship, circumvention, syria, israel]
authors:
 - Chaabane, Abdelberi
 - Chen, Terence
 - Cunche, Mathieu
 - De Cristofaro, Emiliano
 - Friedman, Arik
 - Kaafar, Mohamed Ali
year: 2014
venue: IMC
eprints:
 doi: 10.1145/2663716.2663720
url: http://conferences2.sigcomm.org/imc/2014/papers/p285.pdf
...

Last week we looked at a case study of Internet filtering in
[Pakistan][]; this week we have a case study of Syria.  (I think this
will be the last such case study I review, unless I come across a
really compelling one; there's not much new I have to say about them.)

This study is chiefly interesting for its data source:
a set of log files from the [Blue Coat brand][]
<abbr title="deep packet inspection">DPI</abbr>
routers that are allegedly used [[1]][] [[2]][]
to implement Syria's censorship policy,
covering a 9-day period in July and August of 2011.
leaked by the [Telecomix][] hacktivist group.
Assuming that these log files are genuine,
this gives the researchers what we call _ground truth:_
they can be certain that sites appearing in the logs are,
or are not, censored.
(This doesn't mean they know the _complete_ policy, though.
The routers' blacklists could include sites or keywords
that nobody tried to visit
during the time period covered by the logs.)

With ground truth it is possible to make more precise deductions from
the phenomena.  For instance, when the researchers see URLs of the
form `http://a1b2.cdn.example/adproxy/cyber/widget` blocked by the
filter, they know (because the logs say so) that the block is due to a
keyword match on the string '`proxy`', rather than the domain name,
the IP address, or any *other* string in the HTTP request.  This, in
turn, enables them to describe the censorship policy quite pithily:
Syrian dissident political organizations, anything and everything to
do with Israel, instant messaging tools, and circumvention tools are
all blocked.  This was not possible in the Pakistani case---for
instance, they had to guess at the exact scope of the porn filter.

Because the leaked logs cover only a very short time window, it's not
possible to say anything about the time evolution of Syrian
censorship, which is unfortunate, considering the tumultuous
past few years that the country has had.

The leak is from several years ago.  There is heavy reliance on
keyword filtering; it would be interesting to know if this has changed
since, what with the increasing use of HTTPS making keyword filtering
less useful.  For instance,
[since 2013 Facebook has defaulted to HTTPS for all users][facebook-https].
This would have made it much harder for Syria to block access to
specific Facebook pages, as they were doing in this study.

[Pakistan]: /2014/consequences-censorship-isp-lens/
[Blue Coat brand]: https://en.wikipedia.org/wiki/Blue_Coat_Systems
[[1]]: http://www.bbc.co.uk/news/mobile/technology-15437696
[[2]]: http://www.dailydot.com/news/blue-coat-syria-iran-spying-software/
[Telecomix]: http://telecomix.org/
[facebook-https]: https://www.facebook.com/notes/facebook-engineering/secure-browsing-by-default/10151590414803920
