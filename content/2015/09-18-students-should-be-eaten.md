---
title: "Students Who Don't Understand Information Flow Should Be Eaten: An Experience Paper"
tags: [information leakage, game theory, education]
authors:
 - Ensafi, Roya
 - Jacobi, Mike
 - Crandall, Jedidiah R.
year: 2012
venue: CSET
url: https://www.usenix.org/system/files/conference/cset12/cset12-final23.pdf
...

On a completely different and much lighter note from Wednesday, today
we're going to look at a paper about teaching students
information-flow theory with [Werewolf][].

Werewolf (also known as Mafia) is a game in which the players are
divided into two groups, the werewolves (or mafiosi) and the
villagers, and each is trying to wipe the other out at a rate of one
murder per turn.  There are a whole bunch of variants.  Normally this
is played around a table, as a game of strategic deception: only the
werewolves know who the werewolves are, and they participate _as
villagers_ on the villagers' turn.  In this paper, it becomes a game
played online, of surveillance and countersurveillance: the villagers
are actively encouraged to exploit information leaks in the game
server and discover who the werewolves are.  (In a normal game this
would be cheating.)

The authors don't report how this teaching method compares to
traditional lectures on any quantitative basis (e.g. final exam
scores, class grades).  However, they do say that the students loved
the exercise, met up outside of official class hours to discuss
strategies and plan, and that over the term the exploits and
countermeasures grew steadily more sophisticated, in some cases
requiring adjustments to the game server to ensure that both sides
could still win.  It's hard to imagine this level of student
engagement _not_ leading to better grades, better retention, and
deeper interest in the material.

I think this is a brilliant idea and not just for teaching information
flow.  One of the hardest things to teach in a security course is what
Bruce Schneier calls the [security mindset][]: intentionally thinking
about how a system can be caused to fail, to do something it's not
intended to do.  In particular, it is in tension with the usual
engineering mindset, which focuses on verifying that something works
_when used as designed_.  (Safety engineering and failure analysis
have more of the security mindset about them, but usually focus on
failures due to accident rather than malice.)  But it is exactly how
you need to think to successfully cheat at a game, or to notice when
someone else is cheating---and in that context, it's going to be
familiar to most college students.  Using a game of strategic
deception as the backdrop will also encourage students to think along
the right lines.  I'd like to see this idea adapted to teach other
challenging notions in security---penetration testing is the obvious
one, but maybe also code exploitation and key management?

[Werewolf]: https://en.wikipedia.org/wiki/Mafia_%28party_game%29
[security mindset]: https://www.schneier.com/blog/archives/2008/03/the_security_mi_1.html
