---
title: "VOLK v2.2.0 release"
author: "Johannes Demel"
date: "2020-02-16"
categories: ["release"]
aliases: ["/news/volk-v2.2.0-release"]
banner: volk_release_web.svg
---

Hi everyone,

we have a new VOLK [release
v2.2.0](https://github.com/gnuradio/volk/releases/tag/v2.2.0)!

We want to thank all contributors. This release wouldn't have been
possible without them.

We're curious about VOLK users. Especially we'd like to learn about VOLK
users who use VOLK outside GNU Radio.

If you have ideas for VOLK enhancements, let us know. Start with an
issue to discuss your idea. We'll be happy to see new features get
merged into VOLK.

The v2.1.0 release was rather large because we had a lot of backlog. We
aim for more incremental releases in order to get new features out there.

### Highlights

VOLK v2.2.0 updates our build tools and adds support functionality to
make it easier to use VOLK in your projects.

* Dropped Python 2 build support
    - Removed Python six module dependency
* Use C11 aligned_alloc whenever possible
    - MacOS `posix_memalign` fall-back
    - MSVC `_aligned_malloc` fall-back
* Add VOLK version in `volk_version.h` (included in `volk.h`)
* Improved CMake code
* Improved code with lots of refactoring and performance tweaks

### Contributors

*  Carles Fernandez <carles.fernandez@gmail.com>
*  Gwenhael Goavec-Merou <gwenhael.goavec-merou@trabucayre.com>
*  Albin Stigo <albin.stigo@gmail.com>
*  Johannes Demel <demel@ant.uni-bremen.de> <demel@uni-bremen.de>
*  Michael Dickens <michael.dickens@ettus.com>
*  Valerii Zapodovnikov <val.zapod.vz@gmail.com>
*  Vasil Velichkov <vvvelichkov@gmail.com>
*  ghostop14 <ghostop14@gmail.com>
*  rear1019 <rear1019@posteo.de>

### Changes

* CMake
    - Fix detection of AVX and NEON
    - Fix for macOS
    - lib/CMakeLists: use __asm__ instead of asm for ARM tests
    - lib/CMakeLists: fix detection when compiler support NEON but nor
neonv7 nor neonv8
    - lib/CMakeLists.txt: use __VOLK_ASM instead of __asm__
    - lib/CMakeLists.txt: let VOLK choose preferred neon version when
both are supported
    - lib/CMakeLists.txt: simplify neon test support. Unset neon version
if not supported
    - For attribute, change from clang to "clang but not MSC"
* Readme
    - logo: Add logo at top of README.md
* Build dependencies
    - python: Drop Python2 support
    - python: Reduce six usage
    - python: Move to Python3 syntax and modules
    - six: Remove build dependency on python six
* Allocation
    - alloc: Use C11 aligned_alloc
    - alloc: Implement fall backs for C11 aligned_alloc
    - alloc: Fix for incomplete MSVC standard compliance
    - alloc: update to reflect alloc changes
* Library usage
    - Fixup VolkConfigVersion
    - add volk_version.h
* Refactoring
    - qa_utils.cc: fix always false expression
    - volk_prefs.c: check null realloc and use temporary pointer
    - volk_profile.cc: double assignment and return 0
    - volk_32f_x2_pow_32f.h: do not need to _mm256_setzero_ps()
    - volk_8u_conv_k7_r2puppet_8u.h: d_polys[i] is positive
    - kernels: change one iteration for's to if's
    - kernels: get rid of some assignments
    - qa_utils.cc: actually throw something
    - qa_utils.cc: fix always true code
    - rotator: Refactor AVX kernels
    - rotator: Remove unnecessary variable
    - kernel: Refactor square_dist_scalar_mult
    - square_dist_scalar_mult: Speed-Up AVX, Add unaligned
    - square_dist_scalar_mult: refactor AVX2 kernel
    - kernel: create AVX2 meta intrinsics
* CI
    - appveyor: Test with python 3.4 and 3.8
    - appveyor: Add job names
    - appveyor: Make ctest more verbose
* Performance
    - Improve performance of generic kernels with complex multiply
    - square_dist_scalar_mult: Add SSE version
    - Adds NEON versions of cos, sin and tan


