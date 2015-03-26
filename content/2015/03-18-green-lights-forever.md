---
title: "Green Lights Forever: Analyzing the Security of Traffic Infrastructure"
tags: [embedded, safety-critical, security phase change]
authors:
 - Ghena, Branden
 - Beyer, William
 - Hillaker, Allen
 - Pevarnek, Jonathan
 - Halderman, J. Alex
year: 2014
bibtex_type: inproceedings
booktitle: Workshop on Offensive Technologies
booktitle_url: https://www.usenix.org/conference/woot14
organization: USENIX
url: https://www.usenix.org/system/files/conference/woot14/woot14-ghena.pdf
...

Consider the humble traffic light.  The basic design dates to the
1890s, the signals it displays can be explained to a toddler, they're
everywhere and no one thinks anything of them, but if they malfunction
an entire city could be paralyzed.  Also, for longer than you might
realize, they have not been controlled by simple, independent timing
circuits; "coordinated" light patterns, intended to ensure that traffic
flows smoothly along the entire length of a boulevard, date to the
1940s.  Nowadays each light's control box tends to have a computer
inside, and they talk to each other on radio links, because running
wires between all the intersections is expensive.

Today's paper is from
[WOOT 2014](https://www.usenix.org/conference/woot14) and is a case
study of the security of such networks of traffic lights.  If you have
any experience with embedded device security you can probably guess
how it turned out: The radio links are in the clear.  The protocols
are proprietary, but easy to reverse-engineer (or acquire software
for).  The computers run an outdated proprietary embedded OS and
there's no mechanism for ensuring it gets patched when necessary.
Operating-system-level debugging interfaces with complete control over
the device may have been left active and exposed to the network.
Management software fails to work correctly if passwords are changed
from the vendor's default.  And once you're connected, you can
completely reconfigure the traffic lights---which is by design, so
adjustments don't require sending a maintenance crew to every
intersection.

The saving grace is the "malfunction management unit."  This is a
separate circuit board, built with discrete logic and configured with
physical jumpers, which prevents the light at any single intersection
from displaying an unsafe combination of signals (e.g. green in all
directions).  If the computer tries to put the lights in a state that
isn't on the MMU's whitelist, or change them too rapidly, it will be
overridden and the lights will enter a failsafe mode (such as blinking
red in all directions) until someone physically resets the control
box.  This safety mechanism limits the damage an attacker can do, but
it's still perfectly possible to bring all traffic to a halt,
malcoordinate the lights to hinder rather than help traffic flow
(which might go completely unnoticed) or just give yourself green
lights all the time at everyone else's expense.

This paper is probably more valuable for its "broader lessons"
(section 6) than for this one case study.  Why is it that security
experts are not surprised when yet another embedded, safety-critical
system turns out to be wide open to remote explotation?  The authors
call this phenomenon the "security phase change."  You have an
industry with decades of experience designing, manufacturing, and
selling widgets which do not communicate with the outside world.  The
engineers have a solid understanding of how the widget might fail due
to accidents, wear and tear, manufacturing defects, etc, and what
needs to be done to make sure it fails safe---that malfunction
management unit is not in the traffic light controller by chance.  But
no one thinks about failures due to malice, because why would anyone
go around to each and every traffic light and monkeywrench it?  It
would take hours.  Someone would probably call the police.

To such a widget, features are incrementally added, each desirable in
its own terms.  Microcontrollers are cheaper and more flexible than
fixed-function logic boards.  Radio links are cheaper and more
flexible than running wires down the street.  If the fire trucks can
override the lights, they can get to the fire faster.  If all the
lights report diagnostics to a central monitoring station, we can
dispatch repair crews more efficiently and not need to make as many
inspections.

The security phase change happens when a series of these changes
culminates in a device that has a general-purpose computer inside,
connected directly to a network that anyone can tap into with
relatively little effort.  Suddenly the adversary *doesn't* need to
drive around the entire city to monkeywrench all the lights.  Or crack
open the hood of your car to get at the engine control computer's
maintenance interface.  Or be physically onsite at your chemical plant
to mess with the process controller.  I understand
[jet engines are a service](http://www.geaviation.com/commercial/services/flight-efficiency-services/)
now.  I would like to think that *those* engineers have thought about
channel security, at the very least.
