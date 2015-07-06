---
title: "Security Analysis of Consumer-Grade Anti-Theft Solutions Provided by Android Mobile Anti-Virus Apps"
tags: [device security, usable security, privacy, data erasure]
authors:
 - Simon, Laurent
 - Anderson, Ross
year: 2015
venue: MoST
url: http://www.ieee-security.org/TC/SPW2015/MoST/papers/s3p3.pdf
...

Today we have another analysis of Android device security against
scenarios where the owner loses control of the phone, by the same
researchers who wrote "[Security Analysis of Android Factory Resets][afr]."
Here, instead of looking at what happens when the owner deliberately
erases a phone in order to sell it, they study what happens when the
phone is stolen and the owner tries to wipe or disable it remotely.
A remote disable mechanism is commonly included in anti-virus programs
for Android, and this study looks at ten such mechanisms.

As with factory reset, the core finding boils down to "none of them
work."  The root causes are slightly different, though.  The core of
Android, naturally, is at pains to *prevent* normal applications from
doing something as destructive as initiating a memory wipe, rendering
the phone unresponsive to input, or changing passwords.  To be
properly effective the anti-theft program needs "administrative"
privileges, which can be revoked at any time, so there's an inherent
race between the owner activating the anti-theft program and the thief
disabling it.  To make matters worse, UX bugs make it easy for these
programs to *appear* to be installed correctly but not have the
privileges they need; implementation bugs (possibly caused by unclear
Android documentation) may leave loopholes even when the program *was*
installed correctly; and several device vendors added backdoor
capabilities (probably for in-store troubleshooting) that allow a
thief to bypass the entire thing---for those familiar with Android
development, we're talking "if the phone is turned off and then
plugged into a computer it boots into recovery mode and activates
[ADB][]."

There is a curious omission in this paper: since 2013, Google itself
has provided a remote lock/wipe feature as part of the "Google Apps"
bundle that's installed on most Android devices [[1]][].  Since the
Apps bundle is, nowadays, Google's way of getting around vendors who
can't be bothered to patch the base operating system in a timely
fashion, it has all the privileges it needs to do this job correctly,
and the feature *should* be available regardless of Android base
version.  The UX is reasonable, and one would presume that the
developers are at least somewhat less likely to make mistakes in the
implementation.  This paper, however, doesn't mention that at all,
despite (correctly) pointing out that this is a difficult thing for a
third-party application to get right and the device vendors should
step up.

Practical advice for phone-owners continues to be: encrypt the phone
on first boot, before giving it any private information, and use a
nontrivial unlock code.  Practical advice for antivirus vendors, I
think, is "you're not testing your software adversarially enough."
The implementation bugs, in particular, suggest that the vendors' test
strategy confirmed that remote lock/wipe *works*, when set up
correctly, but did not put enough effort into thinking of ways to
*defeat* the lock.

[afr]: /2015/security-android-factory-resets/
[[1]]: http://www.androidcentral.com/how-set-android-device-manager-lock-and-wipe-your-phone
[ADB]: https://developer.android.com/tools/help/adb.html
