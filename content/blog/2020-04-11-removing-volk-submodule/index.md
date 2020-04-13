---
title: "The Path to 3.9: Removing the VOLK submodule"
author: "Martin Braun"
date: "2020-04-11"
sponsored: "0"
aliases: ["blog/removing-volk-submodule"]
---

As we continue to work on the next major release of GNU Radio (version 3.9), we
take the next big step: Remove VOLK as a submodule from the GNU Radio repository.
If you try and build master branch as of today, it might fail stating that CMake
cannot find VOLK -- this is expected, and easily remedied.

This removal is something we've always planned to do, ever since we created the
submodule -- but we never made a GREP, so let me take this opportunity to catch
up and explain what we're doing here.

<!--more-->

## VOLK: A new project, but part of GNU Radio

When VOLK was initially created, it was part of GNU Radio. We quickly understood
the value of VOLK as its own project, though, and thus spun off VOLK as libvolk,
with it's [own website](https://libvolk.org). However, VOLK was still part of
the source tree, and we really hate adding dependencies. Besides, VOLK is still
under development, so we always wanted the latest and greatest kernels. So what
to do?

We went the lazy route, left VOLK in GNU Radio as a submodule, which we updated
at random intervals, but made it look like VOLK was still in-tree. Other projects
could just use regular VOLK releases. This worked OK for a while, but it had
many disadvantages, too: It didn't fully respect VOLK as it's own project, and
it made it unclear which version of VOLK matches a GNU Radio version. By now,
the disadvantages are slowly overtaking the advantages, so we decided to pull
the trigger and remove VOLK from GNU Radio, and make it a required dependency.

## Scalpel, please: A VOLK-ectomy

Removing VOLK by itself was not hard. The actual
[pull request](https://github.com/gnuradio/gnuradio/pull/3346)
mostly consists of updating CMake files, and of course removing the submodule.
As band-aids go, this one was easy to rip off. Most work was done by Andrej Rode,
who did all the required BuildBot work for our CI infrastructure.

The downstream effects are a bit more involved though:

- Anyone building GNU Radio from source must first build VOLK separately (or
  install a binary version). Before, this was one step (VOLK and GNU Radio got
  built together, if no other version was found)
- Distro and binary maintainers will have to make sure that VOLK is properly
  packaged separately, and is tagged as a dependency for GNU Radio.
- A fix in VOLK is now no longer immediately available in GNU Radio. We have to
  wait for a VOLK release to occur, and then we can update the minimum VOLK
  version -- but only on master, because the maint branches can no longer update
  the minimum VOLK version, as that would violate our contract regarding stable
  branches.
- As it stands now, the 3.7 release cycle of GNU Radio uses (and will
  continue to use) VOLK 1.4.0, and the 3.8 release cycle uses VOLK 2.0.0. GNU
  Radio 3.9 will require a VOLK version that is to be determined, but it will be at
  least 2.1.0.
- PyBOMBS users need to wait for an update until we have a recipe that will
  install VOLK for you automatically.

Altogether, this is still the better solution. We fully respect VOLK as a proper
project and treat it like all the other dependencies, so there's no weird
middle-ground just for VOLK.

## VOLK and GNU Radio: Best Buddies

At this point, it's a good time to give a shoutout to the current maintainers of
VOLK: Michael Dickens and Johannes Demel. Both are valued members of the GNU
Radio community and long-time contributors. If anything, this submodule removal
will increase the necessity for VOLK and GNU Radio to collaborate, and we have
all the confidence the projects will remain linked at the hip as before.

VOLK has also been doing some work to facilitate the separation of projects:
Starting with version 2.2.0,
[VOLK has a `volk_version.h` header](https://github.com/gnuradio/volk/pull/346)
which lets us query the VOLK version at a macro level.

## TL;DR: Install VOLK separately

If you build GNU Radio from source, they key takeaway is: You might also need to
build VOLK from source, and CMake will tell you if that's the case.

Remember you don't have to build GNU Radio from source: We provide
[binary packages](https://wiki.gnuradio.org/index.php/InstallingGR#From_Binaries)
for GNU Radio if your distribution's version is too old for you.
