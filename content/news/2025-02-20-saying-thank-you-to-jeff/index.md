---
title: 'Saying "thank you!" to Jeff'
author: "Marcus Müller"
date: "2025-02-20"
categories: []
aliases: ["/news/thank-you-jeff"]
---

# Thank you, Jeff!

It's time for me to express my gratitude for Jeff Long (willcode4, if you find him online), who's retiring from his role as the release manager and maintainer of GNU Radio. <br>
Jeff has been keeping the stable branches both _stable_ and _moving forward_ since March 2021 – a tiny bit of a Herculean task,
considering that when he started to take care of GNU Radio's releases, we we're just hitting version 3.8.3.0, which was in the middle of the biggest
transition GNU Radio had seen in half a decade. Juggling the version of GNU Radio that supported both Python 2 and 3 was definitely a challenge that we've
had a hard time keeping up with before he stepped up.

Since then, many a change has happened in GNU Radio, and one of the remarkable things that Jeff enabled there is that users very quickly benefited from 
work done on the development `main` branch. In a FOSS project, there's never enough volunteer time to go around – development of new things on one end,
handling bugs reported by users on the other, fixing these bugs, keeping the community flowing, converting community input into actionable development goals, 
helping new contributors be successful: These things are all competing for project developers' time.

That often means that development, has to happen in a place where prior concepts *can* be broken within reason to replace them with something better;
to help the user of tomorrow have a better piece of software. In this case: to let everyone have a better SDR framework for the masses!

However, that is at odds with what the users needs *today*. They need stability, reliability; they're not interested at all in updates for the sake
of updating. Nevertheless, of course, waiting years to bundle new features into a new 3.X release is strictly bad – it keeps useful improvements out
the reach of everyday, non-core-developer users, and also robs developers of the chance to get feedback on features from the breadth of the community.

Jeff really brought the game here to a completely different pace: In a day-to-day manner, he backported additions to the `main` branch to the `maint-3.x` branches,
from which the stable releases are rolled, given these additions and fixes did not break anyone's software¹. The amount of in-depth work that means,
as well as the scope of what you'd need to plan to not "paint yourself into a corner" there are really hard to grasp. Just to give an impression:

The `maint-3.8`, `maint-3.9`, and `maint-3.10` branches, since Jeff's stepping up, have seen more than **1680 commits**. Every single one of them has been
reviewed by Jeff, analyzed for impact, massaged to fit the maintenance requirements, merged and fixed by Jeff. He's tagged at least 32 releases.

All the while, Jeff has been an extraordinarily friendly member of the community – I've been far more grumpy a developer at times than he was a maintainer,
and he had to deal with *my and everyone else's* code output, not the other way around.

So:

*Thank you very much, Jeff!*

Enjoy your freshly won free time, you really deserve it.

# Voluntirement

I wrote "retiring from his role", but that sounds far too corporate for what it really was: it was a 100% volunteer, fully on his own time, no financial gain,
not for the selling any services, gift of his time to the project.

It'll be all kinds of hard to fill the gap that he's leaving. So, we're trying to distribute the load on multiple people; that's why you saw the "help wanted!" sign on our issue tracker for a long time now!

We're trying to install people akin to what one would know as subsystem maintainers from the Linux kernel: People with the competence (and authority) to keep an understanding
for what happens in "their" part of the GNU Radio source tree, so to both accelerate decision-making on the forward-development path
(so that calls on whether something is the right direction can be made with less reading into a topic),
as well as allowing stability and backporting decisions to be done by more than one person.

Thus, if you think you have both experience and an interest in helping a part of GNU Radio move forward, do still reach out to us – via the mailing list, the "help wanted" on the issue tracker, or in-person.

-----

¹ That means ABI as much as API stability, but also behavioural reliability and stability in critical output.
