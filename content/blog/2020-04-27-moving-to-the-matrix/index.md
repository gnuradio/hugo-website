---
title: "Goodbye Slack: GNU Radio is moving into the Matrix"
author: "Martin Braun"
date: "2020-04-27"
sponsored: "0"
aliases: ["blog/moving-to-the-matrix"]
---

With the growth of a project there come changes. For GNU Radio, a big change is
in the pipeline too: We're moving from our chat service from Slack to
[Matrix](https://chat.gnuradio.org).
Untypically for us, this decision came about pretty quickly, and without much
community involvement. Let me go through why did this, how we reached a decision,
and, most importantly, how you can join the new chat service as well.

<!--more-->


## Stop talking, and let me chat: Instructions for the impatient

If you're already done reading, all you need to do is head over to
[chat.gnuradio.org](https://chat.gnuradio.org) and create an account, or use
your existing Matrix federation account if you have one.
Once you're registered, you will find a chat service that looks similar to our Slack
domain. Some of the existing channels on Slack have already been re-established
on Matrix, and some groups, like the documentation team lead by Marc Lichtman,
have already moved their base of operations to Matrix.

Other channels are still moving, and we expect the move to take a little bit.
But technically speaking, there's nothing from stopping you to join right now!

Once you've registered, you can also join our chat server from your phone using
the Android and iOS apps provided by [Riot](https://riot.im). Other clients for
your [desktop are also available](https://matrix.org/clients/).

More detailed information, in particular on how to set up Matrix on your mobile
devices, can be found [on our wiki](https://wiki.gnuradio.org/index.php/Chat).

## Why on earth are you doing this? Isn't this a lot of work to move chat services?

Yes, it is a lot of work. We have plenty of good reasons to move away from our
current Slack setup, though:

- Currently, we're on the free plan for Slack. This means that only a brief
  history is stored for all chats. Unless someone has set up some IRC bridge,
  and logs history themselves, it's not possible to go back in time very far to
  read past discussions, which can be very annoying. Of course, we could start
  paying Slack to see the full history. But...
- Slack is fairly expensive, and is charged per user. Depending on how we count
  users, we have between approx. 150 users (those are the active ones) and over
  a thousand (if you count all of them). Even if we got a discounted price (us
  being an open source project and all), we'd still be looking at some serious
  expenditure. That by itself is fine -- we all know that good software and
  services, even if it's free software, is not free to build and we are willing
  to pay for it. But if we're already paying, we might as well look at
  alternatives, right?
- Let's say we stuck with Slack and went to a paid plan with full history. We'd
  still be locked into the Slack ecosystem. Slack is not open source, and stores
  all chat history on proprietary serves owned by Slack themselves. As an open
  source project, that should at least give us a pause to think if that's really
  what we want.
- The Slack clients are generally fine, and have definitively improved in recent
  months. But overall, they're nothing special, and still can become CPU hogs.
  Very few features in the actual clients are *that* important that we felt
  compelled to stick with Slack.

After considering all of this, we realized it's time to take a step back, and
decide objectively how we can best organize the real-time communication (aka chat)
service for GNU Radio.

## How we picked a new service

There were a few criteria we specifically looked out for:

- There needed to be clients for Android and iOS, so users could easily
  participate via their phones on the go.
- Also, a web-based client was a must
- Interaction with IRC, in particular Freenode, had to be possible. We still
  consider `#gnuradio` on Freenode part of our GNU Radio infrastructure.
- Cost should be reasonable. We weren't expecting a free service, but we also
  don't want to squander GNU Radio funds.
- There had to be an available service provider that would run the infrastructure
  for us, so our GNU Radio leadership didn't have to manually run the servers.

Some other criteria fell under the nice-to-have category:

- All things equal, we would certainly prefer an open source solution to a
  proprietary one.
- An open standard for interoperability was considered important, if not
  essential. This would allow easy interaction, e.g., between IRC and our chat
  service.
- Desktop clients and terminal-based clients were considered a great plus.
- Ideally, this is a service that is used by other organizations as well.
- GitHub integration and bells and whistles similar to that were considered a
  plus as well.

Using these criteria, we surveyed a bunch of options, including Mattermost,
sticking with Slack, Discord, gitter, and of course Matrix.

To test not only chat solutions, but also hosters, we rented a Mattermost and
Matrix instance from a [Swiss hoster](https://ungleich.ch) and tested them within
a closed circle. Other services we could test with a free plan from their
respective providers.

After several weeks of trial, we conceded that Matrix ticked most of the boxes:

- It is fully open-source, and committed to open standards
- Matrix is used by many organizations such as KDE, Gnome, the Wikimedia Foundation,
  and the French government, to name a few.
- Matrix instances can connect to each other ("federation"). This means from our
  GNU Radio chat, we can access other organizations on Matrix, even if they're
  not part of the GNU Radio chat instance. This includes the main Matrix instance
  on [matrix.org](https://matrix.org), where projects such as our friends from
  SatNOGS are located.
- That means that people already on Matrix don't have to do a whole lot to join
  our Matrix server.
- Bridging to IRC is also easy, and will have a high likelihood of working
  indefinitely.
- The open standards nature of Matrix, and the availability of open source
  reference clients, means that there are lots of clients out there, including
  things like a [Weechat plugin](https://github.com/poljar/weechat-matrix).


## The matter of Transparency, or why am I only hearing about this now?

While the GNU Radio leadership team definitely did their due diligence in
picking a new service, one thing that definitely shouldn't become the norm for
decisions around the GNU Radio project is the fact that we decided this behind
closed doors within the leadership team. For example, we did not publish a GREP
ahead of time for a public discussion.

After extensive discussions, we agreed that without actually having tried it,
the decision for a chat service would almost exclusively be a battle of
opinions. Having all reasonable opinions among us, we decided to forgo
fragmenting the community and instead conducted a closed testing of the most
promising candidates.

## What happens to the GNU Radio Slack?

We will turn off Slack end of August 2020.
The main development, documentation, and variety of other discussions regarding
the project will be held on our
Matrix instance going forward, in order to preserve them in history.

Many people from the GNU Radio leadership will be leaving the Slack server, and
won't be reachable there going forward, even before August.

We could keep Slack running, since it's free, but we decided against it. This is
for multiple reasons:
- Even if administering the Slack instance is very little work, it is still work
  and we don't want to have yet another task.
- All GNU Radio leadership will move off of the Slack channel, so calling it a
  GNU Radio chat service is a stretch anyway at that point.
- Closing the service is the only way to guarantee that everyone on the GNU Radio
  Slack definitely hears about the deprecation of our Slack.
- We don't want to risk any GPDR issues by being responsible for other people's
  data.

## The new setup, and yes, we're still tuning it

As of April 2020, we have rented a hosted Matrix setup at Swiss hosting company
[ungleich.ch](https://ungleich.ch/u/products/hosted-matrix-chat/). Our custom
entry point [chat.gnuradio.org](https://chat.gnuradio.org) points to their
server, but unlike Slack, we can pack up our chat and move it elsewhere if we're
unhappy with the hosting service provided. The hosting service was chosen based
on an internet research and a comparison of services provided, and cost. We have
no other affiliations with the hosting company.

We only recently set this up, and we probably want to tune this quite a bit. For
example, the [GitHub ticker](https://matrix.to/#/#github-gnuradio:gnuradio.org)
looks a bit different.  We're still experimenting with the IRC
gateway, which might be most confusing right now, as we haven't fully set it up
like we want it to be, and we're also bridging over into Slack. So, things are
still in flux, but that's because we're optimizing to our needs.

Join us on Matrix and give us your feedback!

One thing you can help us is find a nicer
[background image for the login page](https://matrix.gnuradio.org/themes/riot/img/backgrounds/valley.jpg).
If you have a suggestion (2560x1505 pixels please), let us know!


## Is that it? When's the next Chat server move?

Hopefully, we'll never move chat services again. As mentioned before, the existing
chat service on [chat.gnuradio.org](https://chat.gnuradio.org) is still
evolving. We're looking forward to seeing you there!

