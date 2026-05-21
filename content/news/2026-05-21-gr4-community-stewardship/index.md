---
title: "GNU Radio 4: Community Stewardship and the Road to 4.0"
date: "2026-05-21"
author: "The GNU Radio Board"
categories: ["gnuradio", "gr4", "community"]
aliases: ["/news/gnuradio-community-is-the-steward-of-gnuradio-4"]
banner: "GR4-logo-embedded.svg"
---

Today, GNU Radio is reaffirming that GNU Radio&nbsp;4 will continue as an officially community-maintained release line under the [GNU Radio project’s established governance structure](https://github.com/gnuradio/gr-governance). Development will proceed from [the current MIT-licensed core code base](https://github.com/gnuradio/gnuradio4/commit/c946b140996efae16486f2118e0faca6f8e52c14), and we encourage users and contributors to follow and participate through the official [GNU Radio&nbsp;4 repository](https://github.com/gnuradio/gnuradio4).

We have been fortunate to work closely with the team at GSI/FAIR, and GNU Radio has benefited enormously from their technical expertise, sustained investment, and commitment to advancing free software radio. Their work has produced a strong architecture, a modern developer API, and a framework with significant promise for the future of GNU Radio. We are grateful for what GSI/FAIR and its developers have contributed to the project and to the broader SDR community.

GNU Radio has always been more than a code base. For more than two decades, it has been a community of users, developers, researchers, educators, hobbyists, companies, and institutions working together to build and share software-defined radio technology. Since 2020, GNU Radio has also operated under a more formal governance structure intended to make project stewardship transparent, community-led, and resistant to control by any single person or institution.

Work toward a next-generation GNU Radio architecture has been underway for many years, including work prior to and including the SDR 4.0 program ([newsched](https://github.com/gnuradio/gnuradio/tree/dev-4.0)). GNU Radio&nbsp;4 builds on that long-running effort: a clean-slate rethinking of the runtime, scheduler, developer model, and system architecture needed for the next generation of SDR applications. GSI/FAIR played a central role in carrying that work forward and bringing the current implementation to its present level of maturity.

The result is a code base with substantial technical promise. GNU Radio&nbsp;4 is designed to improve performance, developer experience, modularity, and deployment flexibility. It also opens a path toward applications and environments where GNU Radio 3.x has historically been difficult to use, while preserving the goal that GNU Radio should remain useful to the broad community that has built and sustained it.

## Why GNU Radio&nbsp;4’s core is MIT-licensed

Because GNU Radio&nbsp;4 was developed as a clean-slate implementation, its licensing could be considered separately from the active GNU Radio 3.x code base. After discussion with contributors, users, and potential adopters, the project adopted MIT licensing for the GNU Radio&nbsp;4 runtime, default schedulers, and fundamental processing blocks.

That decision was made to reduce barriers to adoption, integration, contribution, and deployment. GNU Radio is used across research, education, commercial engineering, embedded systems, amateur radio, government-funded science, and many other environments. A permissive license for the core makes it easier for organizations in all of those settings to evaluate, adopt, and contribute to GNU Radio&nbsp;4 without unnecessary legal or integration friction.

The MIT licensing of GNU Radio&nbsp;4 has since been discussed publicly in [conference project talks](http://www.youtube.com/watch?v=lf28lPVJiEI&t=1h17m10s), [code and documentation](https://github.com/gnuradio/gnuradio4/blame/main/LICENSE), and community conversations. Contributors and potential adopters have reasonably understood it to be the licensing basis for the core runtime in this next release line.

This is not a rejection of LGPL, GPL, or copyleft licensing. GNU Radio has long benefited from copyleft software, and different GNU Radio components, block libraries, and out-of-tree modules will have different licensing needs and desires. The question here is narrower: what licensing model best serves the GNU Radio&nbsp;4 core as broadly adopted community infrastructure. For that purpose, GNU Radio intends to continue the community release line under MIT. Blocks ported directly from GNU Radio 3 will retain their GPLv3 license. GNU Radio Studio, the current candidate for a GNU Radio Companion-like experience, is GPLv3. 

## Governance and release-line clarity

Recently, GSI/FAIR proposed a different direction for GNU Radio&nbsp;4, which would replace the community ownership of the project with a GSI-centered governance model, with a higher focus on technical details than on API stability, and a switch to LGPLv3 with a static linking exception. We understand that GSI/FAIR has institutional requirements, leadership preferences, and technical priorities that may reasonably lead it toward different decisions around licensing, release cadence, tooling, and stewardship.

GNU Radio’s responsibility is different. The GNU Radio project needs to maintain a stable, community-governed platform for a broad ecosystem of users and contributors. That ecosystem includes researchers, educators, hobbyists, commercial users, system integrators, out-of-tree module authors, downstream projects, and long-term maintainers. For that ecosystem to have confidence in GNU Radio&nbsp;4, the project’s licensing, governance, and release identity need to be predictable.

For that reason, GNU Radio intends to continue the existing community release line from the current MIT-licensed code base under GNU Radio governance. If GSI/FAIR chooses to pursue a separately licensed development line, we hope that work can remain technically compatible where possible, and we remain open to continued collaboration. Clear project identities will help users understand which release line they are adopting and which governance and licensing model applies.

## What happens next

The immediate goal is to prepare GNU Radio for a stable 4.0.0.0 release. That work includes development infrastructure, documentation, packaging, examples, testing, release planning, and a roadmap for the features that should land before and after the first GNU Radio&nbsp;4.0 release. These are all important, 

We are also working to make GNU Radio&nbsp;4 easier to approach. That includes graphical frontends, improved software interfaces, better documentation workflows, practical examples, reduced build friction, and clearer paths for new contributors. GNU Radio&nbsp;4 should support demanding high-performance applications, but it must also remain accessible to the wider GNU Radio community.

These are important and promising times for GNU Radio. GNU Radio&nbsp;4 gives us a path toward applications, architectures, and performance levels that were difficult or impossible with GNU Radio 3.x. It also gives us an opportunity to renew the project’s commitment to openness, usability, shared stewardship, and broad participation.

We invite the community to get involved: test the code, file issues, write examples, improve documentation, build applications, join the discussions, and help shape the GNU Radio&nbsp;4 roadmap. GNU Radio has always been strongest when many people and institutions contribute from different perspectives, and that remains the model for GNU Radio&nbsp;4.

GitHub: [https://github.com/gnuradio/gnuradio4](https://github.com/gnuradio/gnuradio4)  
Chat (Matrix): [\#gnuradio:gnuradio.org](https://app.element.io/#/room/#gnuradio:gnuradio.org)  
Mailing List: [discuss-gnuradio@gnu.org](https://lists.gnu.org/mailman/listinfo/discuss-gnuradio)
