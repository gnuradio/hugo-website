---
title: "GNU Radio Enhancement Proposal Process"
author: "Martin Braun"
date: "2018-02-13"
sponsored: "0"
aliases: ["/blog/gnu-radio-enhancement-proposal-process", "/news/gnu-radio-enhancement-proposal-process"]
---

# The GNU Radio Enhancement Proposal Process

One thing that has been missing in the GNU Radio development process has been a transparent way to contribute, to see what people are working on, and to coordinate development between people developing new features for GNU Radio. To facilitate all of this, we&#8217;ve introduced the GREP process.

The process was announced on [February 5, 2018](https://lists.gnu.org/archive/html/discuss-gnuradio/2018-02/msg00019.html), on discuss-gnuradio. Here&#8217;s the  announcement:

Subject: [Discuss-gnuradio] Introducing the GREP process
Date: Mon, 5 Feb 2018 12:42:19 +0100
From: Martin Braun &lt;martin@gnuradio.org&gt;

Hi all,

in order to facilitate the development of GNU Radio, we will be
launching something new for GNU Radio: The GREP process. You may have
guessed it... GREP stands for "GNU Radio Enhancement Proposal".

If you want to take a look at what we've published so far, go here:

[https://github.com/gnuradio/greps/blob/master/grep-0000-greps.md](https://github.com/gnuradio/greps/blob/master/grep-0000-greps.md)

...but I'll be going a bit into the motivation in the following. You
might want to read this first.

Other projects have done this for a while now; most famously, the Python
project has the PEP process, from which we took heavy inspiration for
the GREP process.

**What is this good for?**

For GNU Radio feature development, we currently lack a way of planning
new features before any kind of development starts. For small things,
such as adding a specific API call to a block, people can simply submit
a "Feature Request" on github. However, there's no path forward, other
than hoping that someone will pick up the work and implement it, there's
no way of knowing what's happening with a feature request.

It's much worse for big changes. Any maintainers second largest fear
(after the fear of no one contributing) is the fear that someone submits
a many-thousand line pull request out of the blue. Worst case scenario
is when the maintainer needs to reject the pull request, and some
enthusiastic developer just wasted weeks or months of work.

For big feature development, we need a way to plan development and
coordinate it between contributors, maintainers, and lead developers.
This is the first big reason to introduce GREPs: They are a platform for
discussing feature development, publicly, ahead of time.

GREPs are so much more, though. They give us a tool to codify things
such as coding guidelines, but with a clear way of putting them up for
discussion. And they don't have to be technical; enhancement proposals
to the GNU Radio organization itself can also become GREPs. We
distinguish between GREPs that are technical enhancements,
organizational changes, and informational documents.

**How does this affect me?**

As you can imagine, we GNU Radio developers discuss things among each
other all the time. But do you know what we're talking about? Probably
not. We don't even use electronic media all the time, because many of us
know each other personally, and we can just chat face to face. That's
nice sometimes, but it's not transparent. GREPs are designed to change
that: Major technical or other discussions can now be publicly viewed,
and participation is highly encouraged. Say Marcus and Andrej are
planning changes to the testing system, they can write it up and post it
on github. If you're a user that happens to be affected by the changes,
you can go ahead and participate in the discussion before changes take
effect, and use that opportunity to contribute to the code base in a way
that is beneficial for you or your organization.

Even if you're not affected, you might be interested to see where the
project is going. As major changes shall become GREPs before they become
code, you can extrapolate future development and plan accordingly.

In other cases, we will submit GREPs that explain the way we do things,
such as coding guidelines. Having such documents in one place (i.e., the
GREP repository) will make it easier for you to understand rules and
conventions used in the project.


**How do GREPs work?**

GREPs are numbered, and GREP 0 is the GREP that explains the GREP
process itself, so I encourage you to go ahead and read it. In a
nutshell, suggestions are written down in a markdown document, and a
pull request is made to the GREP repository. Merging the pull request
means that the GREP meets formal criteria and is now open for
discussion (it does <b class="moz-txt-star">*not*</b> mean the GREP is accepted for implementation).

Find GREP 0 here:

[https://github.com/gnuradio/greps/blob/master/grep-0000-greps.md](https://github.com/gnuradio/greps/blob/master/grep-0000-greps.md)

**I have suggestions for improving the GREP process, now what?**

That's fine -- in fact, it's built into the GREP process itself. Truth
be told, we are assuming that we'll need to tweak and polish the process
for a while until we get into its final form (or maybe it'll never reach
a final form, as requirements keep changing).
So go ahead and submit issues on the GREP issue tracker, and we'll have
a discussion about them.
Ultimately, it'll be up to core GNU Radio devs to decide whether or not
we accept your suggestions for change, but since we don't know what the
perfect GREP process looks like yet, we're very interested to hear any
kind of feedback.

**Which GREPs are in the pipeline, and how do I get updates?**

If you have a github account, you can track the state of the greps
repository and receive notifications.  But of course, we'll be talking
about it on the mailing list, too. We very strongly encourage submitters
of GREPs to discuss them on the mailing list before submitting a pull
request anyway.

As for immediate future GREPs, we'll be writing down coding guidelines
as one of the next GREPs, as well as any other changes to the
development model that we plan to implement. Given the recent change in
maintainership, this is good timing to implement such documents.

Other than that, we have a few ideas for features and changes that will
become GREPs, but just keep an eye open for those.


## Martin Braun
