---
title: Identifying Webbrowsers in Encrypted Communications
tags: [fingerprinting, web, information leakage, deanonymization]
authors:
 - Yu, Jiangmin
 - Chan-Tin, Eric
year: 2014
bibtex_type: inproceedings
booktitle: Workshop on Privacy in the Electronic Society
booktitle_url: https://www.cylab.cmu.edu/news_events/events/wpes2014/
organization: ACM SIGSAC
pages: 135--138
doi: 10.1145/2665943.2665968
pdf_url: http://www.cs.okstate.edu/~chantin/WPES2014.pdf
...

If you are a website, it is fairly easy to identify the web browser in
use by each of your visitors, even if they take steps to suppress the
blatant things like the `User-Agent` header. [[1]][] [[2]][] It is so
easy, in fact, that researchers typically try to make it harder for
themselves, trying instead to identify individual users even as they
move around, change IP addresses, flush their cookies, etc. [[3]][]
[[4]][]

If you are a passive eavesdropper *in between* the browser and the
website, and the network traffic is encrypted, and particularly if you
are isolated from the client's IP address by anonymizing relays
(e.g. [Tor][]), the task should logically be much harder.  Or is it?
The authors of this short paper did the most obvious thing: capture
packet traces and throw them at an off-the-shelf machine classifier.
The feature vectors seen by the machine classifier are not described
as clearly as I'd like, but I *think* they divided the trace into
equal-length intervals and aggregated packet sizes in each direction
in each interval; this is also one of the most basic and obvious
things to do (the "future work" bit talks a little about better
feature engineering).  Despite the lack of tuning, they report 70--90%
classification accuracy on a four-way choice among browsers (Chrome,
Firefox, IE, Tor Browser) and 30--80% accuracy for a 13-way choice
among "browser and plugin combinations" (by which they seem to mean
"whether or not JavaScript and Flash were enabled") (note that for a
13-way choice, chance performance would be 7.7% accuracy).

This is a short workshop paper, so it is to be expected that the
results are a little crude and have missing pieces.  The authors
already know they need to tune their classifier.  I hope someone has
told them about [ROC curves][]; raw accuracies make me grind my teeth.
Besides that, the clear next step is to figure out what patterns the
classifiers are picking up on, and then how to efface those patterns.
I think it's quite likely that the signal they see depends on gross
characteristics of the different HTTP implementations used by each
browser; for instance, at time of publication, Chrome implemented
[SPDY][] and [QUIC][], and the others didn't.

The paper contains some handwaving in the direction of being able to
fingerprint individual users with this information, but I'd want to
see detectable variation among installations of the *same* browser
before I'd be convinced that's possible.

[[1]]: https://panopticlick.eff.org/
[[2]]: http://www.sba-research.org/wp-content/uploads/publications/jsfingerprinting.pdf
[[3]]: http://www.ieee-security.org/TC/SP2013/papers/4977a541.pdf
[[4]]: https://www.internetsociety.org/sites/default/files/11_3.pdf
[Tor]: https://www.torproject.org/
[ROC curves]: https://en.wikipedia.org/wiki/Receiver_operating_characteristic
[SPDY]: https://en.wikipedia.org/wiki/SPDY
[QUIC]: https://en.wikipedia.org/wiki/QUIC
