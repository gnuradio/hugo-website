---
title: "GNU Radio 4.0.0-RC3 Release"
date: "2026-10-13"
author: "Josh Morman"
categories: ["gnuradio", "gr4", "github", "community", "official"]
aliases: ["/news/gnuradio4-rc3-release"]
banner: "GR4-logo-embedded.svg"
---

**GNU Radio 4.0.0 Release Candidate 3 (RC3) is now available!** While this release brings significant improvements to the runtime, expanded signal processing capabilities, and continued progress on developer tooling, it also marks an important milestone for the GNU Radio project: **RC3 is the first GNU Radio 4 release candidate maintained by the broader GNU Radio community.**

Following the transition to community stewardship earlier this year, RC3 demonstrates the progress that comes from bringing together developers with different backgrounds, experiences, and interests. We are particularly excited to welcome a number of new contributors to GNU Radio 4, alongside longtime members of the GNU Radio community.  We want to thank everyone who contributed code to this release, as well as those who participated in development discussions, tested builds, reported issues, and provided feedback.

**Building a healthy contributor community is just as important as building great software.** Seeing new developers get involved with GR4 is particularly encouraging, and we hope RC3 is just the beginning.


## What's New in RC3?

RC3 includes substantial technical improvements as we continue working toward a production GNU Radio 4.0 release.

Some highlights include:

**A more modular project structure.** GNU Radio 4 is organized into independently maintained repositories for the core runtime, DSP libraries and blocks, control plane, and GNU Radio 4 Studio. A unified top-level build makes it easy to assemble a complete development environment while allowing individual components to evolve independently.

**Runtime and scheduler improvements.** Significant work has gone into improving execution efficiency, reducing scheduler overhead, strengthening graph lifecycle management, and addressing correctness and shutdown behavior.

**An expanding collection of signal processing blocks.** RC3 adds numerous analog and digital communications capabilities, including synchronization, modulation, coding, filtering, and networking functionality.

**A better developer experience.** Improvements to block registration, compilation, and the installed SDK make it easier to develop independent block libraries and applications without modifying the GNU Radio source tree.

**Continued progress on GNU Radio 4 Studio.** The browser- and desktop-based graphical environment continues to evolve, bringing interactive flowgraph development, visualization, and runtime control to GR4 applications.

For the complete list of changes, including API updates and migration guidance, see the [GNU Radio 4.0.0 RC3 release notes](https://github.com/gnuradio/gnuradio4/releases/tag/4.0.0-RC3).

## Building on a Strong Foundation

We also want to recognize the tremendous work of the development team at GSI/FAIR, whose years of investment and technical leadership established much of the foundation for GNU Radio 4.  Their work on the architecture, runtime, scheduler, and developer interfaces made this next generation of GNU Radio possible.

RC3 builds on that foundation and represents an important transition toward broader community participation in the development and long-term maintenance of GR4.

Our goal is to preserve the technical strengths of this architecture while making GNU Radio 4 increasingly accessible, extensible, and useful to the diverse community that depends on GNU Radio.

## Try RC3 and Get Involved!

GNU Radio 4 remains under active development, but RC3 represents a big step toward a final production release. We encourage developers to begin experimenting with it, building applications, porting blocks, and sharing their experiences.

Getting started is straightforward:

```bash
git clone https://github.com/gnuradio/gnuradio4.git
cd gnuradio4
cmake --preset dev
cmake --build --preset dev
source build/dev/activate.sh
```

There are many ways to contribute, whether you're interested in developing signal processing blocks, improving documentation, adding hardware support, testing applications, or helping improve the overall developer experience.

Join the discussion on [GNU Radio Matrix](https://chat.gnuradio.org), participate in our regular GR4 developer meetings, or explore the [GNU Radio 4 GitHub repository](https://github.com/gnuradio/gnuradio4).

**RC3 is an important milestone not just because of what we've built, but because of who's building it.**

We are excited to see GNU Radio 4 growing into a truly community-maintained project, and we look forward to welcoming even more contributors as we work toward GNU Radio 4.0.

**Thank you to everyone helping make GNU Radio 4 a reality!**