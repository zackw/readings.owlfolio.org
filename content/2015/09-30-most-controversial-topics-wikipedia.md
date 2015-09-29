---
title: "The Most Controversial Topics in Wikipedia: A multilingual and geographical analysis"
tags: [large sample, natural language, culture]
authors:
 - Yasseri, Taha
 - Spoerri, Anselm
 - Graham, Mark
 - Kertész, János
year: 2014
venue: inbook
booktitle: "Global Wikipedia: International and cross-cultural issues in online collaboration"
editors:
 - Fichman, Pnina
 - Hara, Noriko
isbn: "0-8108-9101-8"
publisher: Scarecrow Press
eprints:
 arxiv: 1305.5566 [physics.soc-ph]
...

One of my more social-science-y interests lately has been in
reverse-engineering the *rationale* for nation-state censorship
policies from the data available.  Any published rationale is almost
always quite vague ("harmful to public order", "blasphemous", sort of
thing).  Hard data in this area consists of big lists of URLs, domain
names, and/or keywords that are known or alleged to be blocked.
Keywords are great, when you can get them, but URLs are less helpful,
and domain names even less so.  I have a pretty good idea why the
Federal Republic of Germany might have a problem with a site that
sells sheet music of traditional European folk songs (actual example
from [#BPjMleak][]), but I don't know which songs are at stake,
because they blocked the entire site.  I could find out, but I'd
probably want a dose of [brain bleach][] afterward.  More to the
point, no matter how strong my stomach is, I don't have the *time* for
the amount of manual research required to figure out the actual issue
with all 3000 of the sites on that list---and that's just one country,
whose politics and history are relatively well-known to me.

So, today's paper is about mechanically identifying controversial
Wikipedia articles.  Specifically, they look through the revision
history of each article for what they call *mutual reverts*, where two
editors have each rolled back the other's work.  This is a
conservative measure; [edit warring][] on Wikipedia can be much more
subtle.  However, it's easy to pick out mechanically.  Controversial
articles are defined as those where there are many mutual reverts,
with extra weight given to mutual reverts by pairs of "senior editors"
(people with many contributions to the entire encyclopedia).  They ran
this analysis for ten different language editions, and the bulk of the
article is devoted to discussing how each language has interesting
peculiarities in what is controversial.  Overall, there's strong
correlation across languages, strong correlation with external
measures of political or social controversy, and strong correlation
with the geographic locations where each language is spoken.  An
interesting exception to that last is that the Middle East is
controversial in all languages, even those that are mostly spoken very
far from there; this probably reflects the ongoing wars in that area,
which have affected everyone's politics at least somewhat.

What does this have to do with nation-state censorship?  Well,
politically controversial topics in language X ought to be correlated
with topics censored by nation-states where X is commonly spoken.
There won't be perfect alignment; there will be topics that get
censored that nobody bothers to argue about on Wikipedia (pornography,
for instance) and there will be topics of deep and abiding Wikipedia
controversy that nobody bothers to censor (Spanish football teams, for
instance).  But if an outbound link from a controversial Wikipedia
article gets censored, it is reasonably likely that the censorship
rationale has something to do with the topic of the article.  The same
is true of censored pages that share a significant number of keywords
with a controversial article.  It should be good enough for hypothesis
generation and rough classification of censored pages, at least.

[#BPjMleak]: https://bpjmleak.neocities.org/
[brain bleach]: http://knowyourmeme.com/memes/brain-bleach-eye-bleach-mind-bleach
[edit warring]: https://en.wikipedia.org/wiki/Wikipedia:Edit_warring
