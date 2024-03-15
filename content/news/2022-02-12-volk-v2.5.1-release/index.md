---
title: "VOLK v2.5.1 release"
author: "Johannes Demel"
date: "2022-02-12"
categories: ["release"]
aliases: ["news/volk-v2.5.1-release"]
banner: volk_release_web.svg
---

[Originally published on libvolk.org](https://www.libvolk.org/release-v251.html)

Hi everyone!

We have a new VOLK release! We are happy to announce VOLK v2.5.1! We want to thank all contributors. This release wouldn't have been possible without them.

The list of contributors is pretty long this time due to a lot of support to relicense VOLK under LGPL. Currently, we are "almost there" but need a few more approvals, please support us. We thank everyone for their support in this effort.

We use `cpu_features` for a while now. This maintainance release should make it easier for package maintainers, FreeBSD users, and M1 users to use VOLK. Package maintainers should be able to use an external `cpu_features` module. For everyone else, `cpu_features` received support for M1 and FreeBSD.

You can find [VOLK on Zenodo DOI: 10.5281/zenodo.3360942](https://doi.org/10.5281/zenodo.3360942).
We started to actively support Zenodo now via a `.zenodo.json` file. This might come in handy for people who use VOLK in publications. As a contributor, if you want more information about yourself added to VOLK, feel free to add your ORCiD and affiliation.

In the past, we relied on Boost for several tasks in `volk_profile`. For years, we minimized Boost usage to `boost::filesystem`. We mostly switched to C++17 `std::filesystem` years ago. The last distribution in our CI system that required Boost to build VOLK, was Ubuntu 14.04. Thus, now is the time to remove the Boost dependency completely and rely on C++17 features.

Some VOLK kernels are untested for years. We decided to deprecate these kernels but assume that nobody uses them anyways. If your compiler spits out a warning that you use a deprecated kernel, get in touch. Besides, we received fixes for various kernels. Especially FEC kernels are notoriously difficult to debug because issues often pop up as performance regressions.

Finally, we saw a lot of housekeeping in different areas. Scripts to support us in our LGPL relicensing effort, updated docs, and updated our code of conduct. We could remove some double entries in our QA system and fixed a `volk_malloc` bug that ASAN reported.
Finally, we switched to the Python `sysconfig` module in our build system to ensure Python 3.12+ does not break our builds.



### Contributors

* A. Maitland Bottoms <bottoms@debian.org>
* Aang23 <qwerty15@gmx.fr>
* AlexandreRouma <alexandre.rouma@gmail.com>
* Andrej Rode <mail@andrejro.de>
* Ben Hilburn <ben@hilburn.dev>
* Bernhard M. Wiedemann <bwiedemann@suse.de>
* Brennan Ashton <bashton@brennanashton.com>
* Carles Fernandez <carles.fernandez@gmail.com>
* Clayton Smith <argilo@gmail.com>
* Doug <douggeiger@users.noreply.github.com>
* Douglas Anderson <djanderson@users.noreply.github.com>
* Florian Ritterhoff <ritterho@hm.edu>
* Jaroslav Škarvada <jskarvad@redhat.com>
* Johannes Demel <demel@uni-bremen.de>
* Josh Blum <josh@joshknows.com>
* Kyle A Logue <kyle.a.logue@aero.org>
* Luigi Cruz <luigifcruz@gmail.com>
* Magnus Lundmark <magnus@skysense.io>
* Marc L <marcll@vt.edu>
* Marcus Müller <marcus@hostalia.de>
* Martin Kaesberger <git@skipfish.de>
* Michael Dickens <michael.dickens@ettus.com>
* Nathan West <nwest@deepsig.io>
* Paul Cercueil <paul.cercueil@analog.com>
* Philip Balister <philip@balister.org>
* Ron Economos <w6rz@comcast.net>
* Ryan Volz <ryan.volz@gmail.com>
* Sylvain Munaut <tnt@246tNt.com>
* Takehiro Sekine <takehiro.sekine@ps23.jp>
* Vanya Sergeev <vsergeev@gmail.com>
* Vasil Velichkov <vvvelichkov@gmail.com>
* Zlika <zlika_ese@hotmail.com>
* namccart <namccart@gmail.com>
* dernasherbrezon <rodionovamp@mail.ru>
* rear1019 <rear1019@posteo.de>


### Changes

* Kernels
    - Fixup underperforming GENERIC kernel for volk_8u_x4_conv_k7_r2_8u
    - volk_32fc_x2_conjugate_dot_prod_32fc: New generic implementation
    - Add volk_32f(c)_index_min_16/32u
    - Fix volk_32fc_index_min_32u_neon
    - Fix volk_32fc_index_min_32u_neon

* Misc
    - Fix volk_malloc alignment bug
    - qa: Remove repeating tests
    - python: Switch to sysconfig module
    - deprecate: Add attribute deprecated
    - deprecate: Exclude warnings on Windows
    - docs: Update docs
    - Add the list of contributors agreeing to LGPL licensing
    - Add a script to count the lines that are pending resubmission
    - Testing: Add test for LGPL licensing
    - Update CODE_OF_CONDUCT file

* Boost
    - boost: Remove boost dependency
    - c++: Require C++17 for std::filesystem

* cpu_features
      cpu_features: Update submodule pointer
      cpu_features: Make cpu_features submodule optional

* Zenodo
      zenodo: Add metadata file
      zenodo: Re-organize .zenodo.json

