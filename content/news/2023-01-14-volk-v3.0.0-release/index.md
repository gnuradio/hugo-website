---
title: "VOLK v3.0.0 major release"
author: "Johannes Demel"
date: "2023-01-14"
categories: ["release"]
aliases: ["news/volk-v3.0.0-release"]
banner: volk_release_web.svg
---

[Originally published on libvolk.org](https://www.libvolk.org/release-v300.html)

Hi everyone!

This is the VOLK v3.0.0 major release! This release marks the conclusion of a long lasting effort to complete [GREP 23](https://github.com/gnuradio/greps/blob/main/grep-0023-relicense-volk.md) that proposes to change the VOLK license to LGPLv3+. We would like to thank all VOLK contributors that they allowed this re-licensing effort to complete. This release wouldn't have been possible without them.

For VOLK users it is important to note that the VOLK API does NOT change in this major release. After a series of discussion we are convinced a license change justifies a major release. Thus, you may switch to VOLK 3 and enjoy the additional freedom the LGPL offers.

### Motivation for the switch to LGPLv3+

We want to remove usage entry barriers from VOLK. As a result, we expect greater adoption and a growing user and contributor base of VOLK. This move helps to spread the value of Free and Open Source Software in the SIMD community, which so far is dominated by non-FOSS software. Moreover, we recognize the desire of our long term contributors to be able to use VOLK with their contributions in their projects. This may explicitly include proprietary projects. We want to enable all contributors to be able to use VOLK wherever they want. At the same time, we want to make sure that improvements to VOLK itself are easily obtained by everyone, i.e. strike a balance between permissiveness and strict copyleft.

Since VOLK is a library it should choose a fitting license. If we see greater adoption of VOLK in more projects, we are confident that we will receive more contributions. May it be bug fixes, new kernels or even contributions to core features.

Historically, VOLK was part of GNU Radio. Thus, it made total sense to use GPLv3+ just like GNU Radio. Since then, VOLK became its own project with its own repository and leadership. While it is still a core dependency of GNU Radio and considers GNU Radio as its main user, others may want to use it too. Especially, long term VOLK contributors may be able to use VOLK in a broader set of projects now.

After a fruitful series of discussions we settled on the LGPLv3+. We believe this license strikes a good balance between permissiveness and strict copyleft for VOLK. We hope to foster contributions to VOLK. Furthermore, we hope to see VOLK usage in a wider set of projects.

### Contributors

The VOLK 3.0.0 release is only possible because all contributors helped to make it possible. Thus, we omit a list of contributors that contributed since the last release.
Instead we want to thank everyone again!

### Changes

* License switch to LGPLv3+
* Fix build for 32 bit arm with neon
* Add experimental support for MIPS and RISC-V
