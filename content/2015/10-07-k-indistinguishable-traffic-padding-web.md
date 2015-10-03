---
title: "*k*-Indistinguishable Traffic Padding in Web Applications"
tags: [web, side channels, adversarial optimization, differential privacy, information leakage]
authors:
 - Liu, Wen Ming
 - Wang, Lingyu
 - Ren, Kui
 - Cheng, Pengsu
 - Debbabi, Mourad
year: 2012
venue: PETS
eprints:
 doi: 10.1007/978-3-642-31680-7_5
url: http://www.freehaven.net/anonbib/cache/traffic-padding-pets12.pdf
...

A Web application is a piece of software whose execution is split
between the client and the server, and it sends data between the two
sides every time you do something significant---even, perhaps, on
every single keystroke.  Inevitably, the volume of data has some
correlation with the action performed.  Since most Web applications
are offered to the general public at low or no cost, an adversary can
map out much of its internal state machine and develop a model that
lets them deduce what someone's doing from an observed sequence of
packets.  [[1]][] [[2]][] This has been successfully applied (in the
lab) to Web applications for highly sensitive tasks, such as tax
preparation and medical advice.

The only known solution to this problem is to pad the amount of data
passed over the network in each direction so that the adversary cannot
learn anything about the state of the web application from an observed
sequence of packets.  Unfortunately, the obvious way to do this
involves unacceptably high levels of overhead---this paper quotes
[[1]][] as observing "21074% overhead for a well-known online tax
system".  Today's paper proposes that techniques from the field of
_privacy-preserving data publishing_ (PPDP, [[3]][]) be brought to
bear on the problem.

The paper is mathematically heavy going and I'm not going to go into
details of their exact proposal, because it's really just a starting
point.  Instead, I'm going to pull out some interesting observations:

 * More padding is not always better.  They show an example case where
   padding messages to a multiple of 128 bytes is exactly as good as
   padding them to a multiple of 512 bytes, and padding them to a
   multiple of 520 bytes is _worse_.

 * Computing the optimal amount of padding for a web application (as
   they define it) is NP-hard even with complete, ideal knowledge of
   its behavior.  However, there are reasonably efficient and speedy
   approximations---if I understood them correctly, it might even be
   feasible to apply one of their algorithms *on the fly* with each
   client.

 * Because optimality is defined over an entire sequence of user
   interactions with an application, knowing how much padding to send
   in response to any given request may require the server to predict
   the future.  Again, however, there are approximations that avoid
   this problem.

 * PPDP offers a whole bunch of different ways to model the degree to
   which one has mitigated the information leak: *k*-anonymity is the
   model they spend the most time on, but there's also *l*-diversity,
   (*α*, *k*)-anonymity, *t*-closeness, etc. etc.  I don't follow that
   literature but I have the impression people are still actively
   making up new models and haven't spent a whole lot of time on
   figuring out which is best in which situations.

The great failing of this and all the other papers I've ever read in
this area is operationalization.  This paper's algorithms need a
complete, or nearly so, map of _all possible sequences of states_ that
a Web application can enter, and the authors shrug off the question of
how you create this map in the first place.  (I very strongly suspect
that task *can't be mechanized* in the general case---it will turn out
to be the [Halting Problem][] in another of its many disguises.)  They
also don't seem to realize that things like Google search suggestions
(the running example in the paper) are constantly changing.  (Of
course, that makes life harder for the adversary too.)  This doesn't
mean there is no hope; it only means you need more approximations.  I
think it ought to be possible to build good-enough automatic padding
into <abbr title="content management systems">CMSes</abbr>, and maybe
even into web application frameworks.  Trying that should be a
priority for future research.

[[1]]: http://www.msr-waypoint.net/pubs/119060/WebAppSideChannel-final.pdf
[[2]]: http://sysseclab.informatics.indiana.edu/projects/sidebuster/sidebuster-final.pdf
[[3]]: http://dmas.lab.mcgill.ca/fung/pub/FWCY10csur.pdf
[Halting Problem]: https://en.wikipedia.org/wiki/Halting_problem
