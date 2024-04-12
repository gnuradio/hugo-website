---
title: "VOLK v2.5.0 release"
author: "Johannes Demel"
date: "2021-06-05"
categories: ["release"]
aliases: ["news/volk-v2.5.0-release"]
banner: volk_release_web.svg
---

[Originally published on libvolk.org](https://www.libvolk.org/release-v250.html)


Hi everyone!

We have a new VOLK release! We are happy to announce VOLK v2.5.0! We want to thank all contributors. This release wouldn't have been possible without them.

This release adds new kernel implementations and fixes. Some of these were longstanding PRs that could only be merged recently thanks to our switch from CLA to DCO.

### Announcements

I would like to point out one upcoming change. After this release, we will rename our development branch to `main` as discussed in [issue #461](https://github.com/gnuradio/volk/issues/461).


I'd like to point the community to this [VOLK relicensing GREP](https://github.com/gnuradio/greps/pull/33).
This is an ongoing effort to relicense VOLK under LGPLv3.
We're looking for people and organizations that are interested in leading this effort.

### Contributors

* Aang23 <qwerty15@gmx.fr>
* Carles Fernandez <carles.fernandez@gmail.com>
* Florian Ritterhoff <ritterho@hm.edu>
* Jam M. Hernandez Quiceno <jamarck96@gmail.com>, <jam_quiceno@partech.com>
* Jaroslav Škarvada <jskarvad@redhat.com>
* Johannes Demel <demel@uni-bremen.de>
* Magnus Lundmark <magnus@skysense.io>
* Michael Dickens <michael.dickens@ettus.com>
* Steven Behnke <steven_behnke@me.com>
* alesha72003 <alesha72003@ya.ru>
* dernasherbrezon <rodionovamp@mail.ru>
* rear1019 <rear1019@posteo.de>


### Changes

* Kernels
    - volk_32f_stddev_and_mean_32f_x2: implemented Young and Cramer's algorithm
    - volk_32fc_accumulator_s32fc: Add new kernel
    - volk_16ic_x2_dot_prod_16ic_u_avx2: Fix Typo, was `_axv2`.
    - Remove _mm256_zeroupper() calls
    - Enforce consistent function prototypes
    - 32fc_index_max: Improve speed of AVX2 version
    - conv_k7_r2: Disable broken AVX2 code
    - improve volk_8i_s32f_convert_32f for ARM NEON
    - Calculate cos in AVX512F
    - Calculate sin using AVX512F


* Compilers
    - MSVC
        - Fix MSVC builds
    - GCC
        - Fix segmentation fault when using GCC 8
    - MinGW
        - add support and test for MinGW/MSYS2

* The README has received several improvements

* Build
    - Fix python version detection
    - cmake: Check that 'distutils' is available
    - c11: Remove pre-C11 preprocessor instructions

* CI
    - Add more CI to GitHub Actions
    - Remove redundant tests from TravisCI
    - Add non-x86 GitHub Actions
    - Update compiler names in CI
    - Disable fail-fast CI
    - Add more debug output to tests

* Contributing
    - contributing: Add CONTRIBUTING.md and DCO.txt
