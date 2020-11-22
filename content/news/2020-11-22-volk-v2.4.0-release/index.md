---
title: "VOLK v2.4.0 release"
author: "Johannes Demel"
date: "2020-11-22"
categories: ["release"]
aliases: ["news/volk-v2.4.0-release"]
thumbnail: "volk_release"
---

[Originally published on libvolk.org](https://www.libvolk.org/category/news.html)


Hi everyone!

We have another VOLK release! We're happy to announce [VOLK v2.4.0](https://github.com/gnuradio/volk/releases/tag/v2.4.0)! We want to thank all contributors. This release wouldn't have been possible without them.

We introduce `cpu_features` as a private submodule in this release because we use it to detect CPU features during runtime now. This should enable more reliable feature detection. Further, it takes away the burden to implement platform specific code. As a result, optimized VOLK kernels build for MacOS and Windows with AppleClang/MSVC out-of-the-box now.


### Highlights

* Documentation
    - Update README to be more verbose and to improve usefulness.

* Compilers
    - MSVC: Handle compiler flags and thus architecture specific kernels correctly. This enables optimized kernels with MSVC builds.
    - AppleClang: Treat AppleClang as Clang.
    - Paired with the `cpu_features` introduction, this enables us to use architecture specific kernels on a broader set of platforms.
* CI
    - Update to newest version of the Intel SDE
    - Test the rotator kernel with a realistic scalar
    - Introduce more test cases with newer GCC and newer Clang versions.
* CMake
    - Enable to not install `volk_modtool`.
    - Remove "find_package_handle_standard_args" warning.
* cpu_features
    - Use `cpu_features` v0.6.0 as a private submodule to detect available CPU features.
    - Fix incorrect feature detection for newer AVX versions.
    - Circumvent platform specific feature detection.
    - Enable more architecture specific kernels on more platforms.
* Kernels
    - Disable slow and broken SSE4.1 kernel in `volk_32fc_x2_dot_prod_32fc`
    - Adjust min/max for `32f_s32f_convert_8i` kernel
    - Use `INT8_*` instead of `CHAR_*`


### Contributors

* Adam Thompson <adamt@nvidia.com>
* Andrej Rode <mail@andrejro.de>
* Christoph Mayer <hcab14@gmail.com>
* Clayton Smith <argilo@gmail.com>
* Doron Behar <doron.behar@gmail.com>
* Johannes Demel <demel@ant.uni-bremen.de>, <demel@uni-bremen.de>
* Martin Kaesberger <git@skipfish.de>
* Michael Dickens <michael.dickens@ettus.com>
* Ron Economos <w6rz@comcast.net>


### Changes

* Documentation
    - Update README to include ldconfig upon volk build and install completion
    - Update README based on review
    - readme: Fix wording
    - docs: Fix conversion inaccuracy

* MSVC
    - archs: MSVC 2013 and greater don't have a SSE flag

* CI
    - update to newest version of the Intel SDE
    - Test the rotator kernel with a realistic scalar

* CMake
    - build: Enable to not install volk_modtool
    - cmake: Remove "find_package_handle_standard_args" warning.
    - cmake: Ensure that cpu_features is built as a static library.

* cpu_features
    - readme: Add section on supported platforms
    - readme: Make supported compiler section more specific
    - travis: Add GCC 9 test on focal
    - travis: Add tests for clang 8, 9, 10
    - travis: Fix incorrect CXX compiler assignment
    - cpu_features: Remove unused feature checks
    - ci: Update TravisCI for cpu_features
    - cpu_features: Fix MSVC build
    - pic: Fix BUILD_PIC issue
    - ci: Update CI system configuration
    - cpu_features: Bump submodule pointer to v0.6.0
    - docs: Add hints how to handle required submodules
    - cpu_features: Switch to cpu_features
    - ci: Update CI system for cpu_features
    - cpu_features: Force PIC build flag
    - appveyor: Add recursive clone command
    - cpu_features: Remove xgetbv checks
    - pic: Cache and force BUILD_PIC
    - ci: Remove explicit BUILD_PIC from cmake args
    - ci: Remove BUILD_PIC from CI cmake args
    - cpu_features: Remove commented code
    - cpu_features: Assume AppleClang == Clang
    - cpu_features: Remove obsolete code in archs.xml
    - fix for ARM cross-compiling CI
    - ARM CI: remove unneeded environment variables

* Housekeeping
    - structure: Move release scripts to scripts folder

* Kernels
    - emit an emms instruction after using the mmx extension
    - volk_32fc_x2_dot_prod_32fc: disable slow & broken SSE4.1 kernel
    - fix: Adjust min/max for 32f_s32f_convert_8i kernel
    - fix: Use INT8_* instead of CHAR_*
