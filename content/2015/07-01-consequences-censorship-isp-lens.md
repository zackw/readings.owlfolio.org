---
title: "A Look at the Consequences of Internet Censorship Through an ISP Lens"
tags: [censorship, circumvention, pakistan]
authors:
 - Khattak, Sheharbano
 - Javed, Mobin
 - Khayam, Syed Ali
 - Uzmi, Zartash Afsal
 - Paxson, Vern
year: 2014
venue: IMC
eprints:
  doi: 10.1145/2663716.2663750
url: http://www.icir.org/vern/papers/censorship-response.imc14.pdf
...

When a national government decides to block access to an entire
category of online content, naturally people who wanted to see that
content---whatever it is---will try to find workarounds.  Today's
paper is a case study of just such behavior.  The authors were given
access to a collection of bulk packet logs taken by an ISP in
Pakistan.  The ISP had captured a day's worth of traffic on six days
ranging from October 2011 through August 2013, a period that included
two significant changes to the national censorship policy.  In late
2011, blocking access to pornography became a legal mandate
(implemented as a blacklist of several thousand sites, maintained by
the government and disseminated to ISPs in confidence---the authors
were not allowed to see this blacklist).  In mid-2012, access to
Youtube was also blocked, in retaliation for hosting anti-Islamic
videos [[1]][].  The paper analyzes the traffic in aggregate to
understand broad trends in user behavior and how these changed in
response to the censorship.

The Youtube block triggered an immediate and obvious increase in
encrypted traffic, which the authors attribute to an increased use of
circumvention tools---the packet traces did not record enough
information to identify exactly what tool, or to discriminate
circumvention from other encrypted traffic, but it seems a reasonable
assumption.  Over the next several months, alternative video
sharing/streaming services rose in popularity; as of the last trace in
the study, they had taken over roughly 80% of the market share
formerly held by Youtube.

Users responded quite differently to the porn block: roughly half of
the inbound traffic formerly attributable to porn just disappeared,
but the other half was redirected to different porn sites that didn't
happen to be on the official blacklist. The censorship authority did
_not_ react by adding the newly popular sites to the blacklist.
Perhaps a 50% reduction in overall consumption of porn was good enough
for the politicians who wanted the blacklist in the first place.

The paper also contains also some discussion of the mechanism used to
block access to censored domains.  This confirms prior literature
[[2]][] so I'm not going to go into it in great detail; we'll get to
those papers eventually.  One interesting tidbit (also previously
reported) is that Pakistan has two independent filters, one
implemented by local ISPs which falsifies DNS responses, and another
operating in the national backbone which forges TCP RSTs and/or HTTP
redirections.

The authors don't talk much about *why* user response to the Youtube
block was so different from the response to the porn block, but it's
evident from their discussion of what people do right after they hit a
block in each case.  This is very often a search engine query
(unencrypted, so visible in the packet trace).  For Youtube, people
either search for proxy/circumvention services, or they enter keywords
for the _specific video_ they wanted to watch, hoping to find it
elsewhere, or at least a transcript.  For porn, people enter keywords
corresponding to a general type of material (sex act, race and gender
of performers, that sort of thing), which suggests that they don't
care about finding a specific video, and will be content with whatever
they find on a site that isn't blocked.  This is consistent with
analysis of viewing patterns on a broad-spectrum porn 'hub' site
[[3]][].  It's also consistent with the way Youtube is integrated into
online discourse---people very often link to or even "embed" a
specific video on their own website, in order to talk about it; if you
can't watch that video you can't participate in the conversation.  I
think this is really the key finding of the paper, since it gets at
when people will go to the trouble of using a circumvention tool.

What the authors do talk about is the consequences of these blocks on
the local Internet economy.  In particular, Youtube had donated a
caching server to the ISP in the case study, so that popular videos
would be available locally rather than clogging up international data
channels.  With the block and the move to proxied, encrypted traffic,
the cache became useless and the ISP had to invest in more upstream
bandwidth.  On the other hand, some of the video services that came to
substitute for Youtube were Pakistani businesses, so that was a net
win for the local economy.  This probably wasn't intended by the
Pakistani government, but in similar developments in China [[4]][] and
Russia [[5]][], [import substitution][] is clearly one of the
motivating factors.  From the international-relations perspective,
that's also highly relevant: censorship only for ideology's sake
probably won't motivate a bureaucracy as much as censorship that's
seen to be in the economic interest of the country.

[[1]]: http://www.washingtonpost.com/business/economy/youtube-blocked-in-pakistan/2012/09/17/30081fa2-00ea-11e2-b257-e1c2b3548a4a_story.html
[[2]]: https://www.usenix.org/conference/foci13/workshop-program/presentation/nabi
[[3]]: http://conferences2.sigcomm.org/imc/2013/papers/imc096-tysonA.pdf
[[4]]: http://chinadigitaltimes.net/2015/01/china-seeks-digital-control-u-n-cpu/
[[5]]: http://europe.newsweek.com/russia-set-launch-government-run-alternative-wikipedia-reflect-life-nation-284517
[import substitution]: https://en.wikipedia.org/wiki/Import_substitution_industrialization
