---
title: "A Survey on Encrypted Traffic Classification"
tags: [traffic classification, information leakage, survey paper]
authors:
 - Cao, Zigang
 - Xiong, Gang
 - Zhao, Yong
 - Li, Zhenzhen
 - Guo, Li
year: 2014
venue: ATIS
pages: 73--81
eprints:
 doi: "10.1007/978-3-662-45670-5_8"
...

This paper gives a brief overview of techniques for extracting
information from encrypted network traffic, covering the past five or
so years, mostly focusing on the (perceived) network-management need
to know what application is communicating within an encrypted tunnel.
It's not very good---it's a big list of other papers, each earning a
couple sentences of description, and not much else.  I would not be
surprised to learn that the authors have completely missed important
pieces of literature in this area.

I'm writing it up here for two reasons. First, it's useful to read
mediocre papers in order to learn how to do better.  In this case, the
missing element is synthesis.  A good survey paper is research _upon
the existing published research_ and, like primary research, has a
result of its own to demonstrate.  Typically, that result will have
something to do with the connections among the articles reviewed.  It
will highlight and compare lines of research, or it will demonstrate
how people's thinking about the topic has changed over time, or it
will highlight gaps where new work would be useful, or perhaps all of
the above.  A big list of articles, briefly described and classified,
is only the skeleton of such a survey.

Second, survey papers are often an entry point into the literature for
people outside a subfield.  Those people are less likely to share
assumptions with the people deeply embedded in a subfield.  For
instance: in this paper, the authors consistently assume, with only a
brief handwave in the direction of a justification, that it is
_necessary_ for network management tools to be able to identify at
least the protocol and perhaps also something about the data being
carried over an encrypted channel.  Now, me, I tend to think that if a
box in the middle can extract _any_ information from an encrypted
channel, that's a bug in the cryptosystem.  And I _am_ working in very
nearly this subfield, so I already know why the network-management
people think they need to be able to extract data from an encrypted
channel.  Someone coming at this paper from an application-security,
end-user privacy, or theory-of-crypto perspective might have an even
stronger negative reaction.  And that's the thing: the authors should
have anticipated that people who don't share their assumptions would
read their paper, so they should have taken steps to back up those
assumptions.
