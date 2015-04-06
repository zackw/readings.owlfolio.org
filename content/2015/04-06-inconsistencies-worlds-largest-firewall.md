---
title: "Large-scale Spatiotemporal Characterization of Inconsistencies
        in the World's Largest Firewall"
tags: [censorship, china, field observations, side channels]
authors:
 - Ensafi, Roya
 - Winter, Philipp
 - Mueen, Abdullah
 - Crandall, Jedidiah R.
year: 2014
venue: preprint
eprints:
 arxiv: 1410.0735 [cs.NI]
...

Lots of academic research on Internet censorship treats the countries
doing the censorship as monoliths: that is, measurements will
typically only be conducted from one client in one fixed location
(often a commercial VPS or colocation provider), and the results are
assmued to reflect the situation countrywide.  When you're talking
about a country as large as China, that assumption seems poorly
justified, and there have been several studies aiming to collect more
fine-grained information. [[1]][] [[2]][] [[3]][] This paper is in
that line of research, with a systematic survey of censorship of one
application ([Tor][]) in roughly 150 different locations across China,
repeating the measurement at hourly intervals for 27 days.  The
measurement clients are diverse both in terms of geographic location
and network topology.

The results largely confirm what was already suspected. This
particular application is indeed blocked consistently across China,
with the possible exception of CERNET (China Education and Research
Network), whose filtering is less aggressive.  The filtering occurs at
major China-wide <abbr title="Internet Exchange Points">IXPs</abbr>,
as suspected from previous studies.  The firewall appears to operate
primarily by dropping _inbound_ traffic to China, perhaps because the
system is optimized for keyword filtering on inbound traffic [[4]][].
Finally, there is concrete evidence for "failures", lasting hours at a
time, uncorrelated with geographic location, where traffic passes
uncensored.  This was anecdotally known to happen but not previously
studied in any kind of detail, to my knowledge.  This paper doesn't
speculate at all on *why* the failures happen or how we could figure
that out, which I think is unfortunate.

The techniques used to collect the data are more interesting, at least
to me.  The principal method is called "hybrid idle scanning," first
presented by some of the same authors in a different paper [[5]][].
It allows a measurement host to determine whether a client can
complete a TCP handshake with a server, *without* itself being either
the client or the server; if the handshake does not complete
successfully, it reveals whether client-server or server-client
packets are being lost.  It does rely on an information leak in older
client TCP stacks (predictable IP-ID sequences, [[6]][]) but millions
of hosts worldwide still run operating systems with these bugs---the
authors report an estimate that they they comprise 1% of the global
IPv4 address space.  Thus, it's possible to find a measurement client
in any geographic location with reasonably common Internet usage.
Data from this technique is backed up with more detailed information
from traceroutes and SYN probes from a smaller number of locations.
They describe a previously-unreported server-side information leak in
Linux's handling of half-open TCP connections, which can be used to
study what IP-based blacklisting of a server looks like *to that
server*, without access to that server.

I'm also impressed with the authors' systematic presentation of the
hypotheses they wanted to test and how they chose to test each of
them.  Anyone interested in network measurements could probably learn
something about how to structure an experiment from this paper.

[[1]]: http://pam2011.gatech.edu/papers/pam2011--Xu.pdf
[[2]]: http://www.pseudonymity.net/~joss/doc/papers/2012/wright12variation.pdf
[[3]]: https://www.usenix.org/system/files/conference/foci14/foci14-anonymous.pdf
[[4]]: http://xylonpan.com/2013/12/14/%E7%BF%BB%E5%A2%99%E8%B7%AF%E7%94%B1%E5%99%A8%E7%9A%84%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E7%8E%B0/
[[5]]: http://arxiv.org/abs/1312.5739
[[6]]: https://nmap.org/book/idlescan.html
[Tor]: https://torproject.org/
