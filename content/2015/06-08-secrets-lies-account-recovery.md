---
title: "Secrets, Lies, and Account Recovery"
tags: [passwords, account recovery questions, authentication, usable security]
authors:
 - Bonneau, Joseph
 - Bursztein, Elie
 - Caron, Ilan
 - Jackson, Rob
 - Williamson, Mike
year: 2015
venue: WWW
...

Today's paper appeared in [WWW 2015][www2015] and was also
[summarized on Google's security blog][lupkqg-b].  The subtitle is
"[Lessons from the Use of Personal Knowledge Questions at Google][lupkqg],"
and the basic conclusion is: "security questions" (for recovering
access to an account when you've forgotten your password) are terribly
insecure.  "Well, duh," you are probably thinking, "the answers are
right there on my social network profile for anyone to read."  That's
true, but it's not the angle this paper takes.  This paper is more
interested in guessing by attackers who haven't read your social
network profile.  At most, they know your preferred language and
country of residence.  It turns out that, if you only ask one security
question for account recovery, three guesses by this adversary are
sufficient to penetrate 10--20% of accounts; that is how many people
typically share the most frequent three answers per language.
(Depending on the question and language, it might be much worse; for
instance, the three most common places of birth for Korean speakers
cover 40% of that population.)

They also observe that questions where there _should_ be no shared
answers ("what is your frequent flyer number?") _do_ have shared
answers, because people give fake answers, and the fake answers tend
to be things like 123456790.  This brings the security of such
questions down to the level of all the others.  Finally, there is a
user survey, from which the most telling two items are: People think
account recovery via security question is more secure and more
reliable than account recovery via a secret code sent to them in a
text message or email (precisely the opposite is true).  People give
fake answers because they want to avoid having the answers be visible
on their social network profile (or otherwise easy to find).

If someone knows almost nothing about you, why are they bothering to
try to take over your account?  Probably the two most important
reasons are "they need throwaway addresses to send spam with" and "if
they steal $100 from ten thousand people, that adds up to a million
dollars."  These are compelling enough that any major online service
provider (such as Google) sees continuous, bulk, brute-force attacks
by adversaries who _don't care_ which accounts they compromise.  The
authors don't say, but I wouldn't be surprised if those attacks
constituted a supermajority of _all_ attacks on Google accounts.

Turning it around, though, the probable negative consequences of
having your account cracked by a spammer who doesn't know or care
about you as a person are really not that bad, compared to what
someone who knows you and bears you a personal grudge could do.
([Ransomware][] is the most prominent counterexample at present.)
Google as a corporate entity is right to worry more about the most
frequent type of attack they see---but you as an individual are
probably _also_ right to worry more about an attack that's much less
common but has way more downside for you.  I think this contrast of
priorities explains fake answers _and_ the general reluctance to adopt
two-factor authentication, recovery codes, etc. all of which might
provide a security benefit in the future but definitely make life more
inconvenient now.
"[So Long, And No Thanks for the Externalities][externalities]" and
"[How Do We Design For Learned Helplessness?][helplessness]" go into
considerably more detail on that point.  (Facebook may well have
improved their password reset sequence since the latter was written.)
On a related note, if someone happens to have an email address or
phone number that isn't already looped back into the account that
needs a recovery contact point, they might well consider it critically
important that the panopticon running that account does _not_ find out
about it!

[www2015]: http://www2015.wwwconference.org/
[lupkqg-b]: http://googleonlinesecurity.blogspot.com/2015/05/new-research-some-tough-questions-for.html
[lupkqg]: https://cdn.elie.net/publications/secrets-lies-and-account-recovery-lessons-from-the-use-of-personal-knowledge-questions-at-google.pdf
[Ransomware]: http://www.howtogeek.com/174343/ransomware-why-this-new-malware-is-so-dangerous-and-how-to-protect-yourself/
[externalities]: http://research.microsoft.com/en-us/um/people/cormac/papers/2009/solongandnothanks.pdf
[helplessness]: http://pamgriffith.net/blog/how-do-we-design-for-learned-helplessness/
