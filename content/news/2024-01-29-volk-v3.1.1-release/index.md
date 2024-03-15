---
title: "VOLK v3.1.1 release"
author: "Johannes Demel"
date: "2024-01-29"
categories: ["release"]
aliases: ["news/volk-v3.1.1-release"]
banner: volk_release_web.svg
---

[Originally published on libvolk.org](https://www.libvolk.org/release-v311.html)

Hi everyone!

This is the VOLK v3.1.1 release! We want to thank all contributors. This release wouldn't have been possible without them.

This is a maintenance release to fix subtle bugs in many areas and to improve our tests where possible. All in all, our CI is more stable now and catches more errors.

### Contributors

- Clayton Smith <argilo@gmail.com>
- Johannes Demel <demel@uni-bremen.de>, <jdemel@gnuradio.org>
- Kenji Rikitake <kenji.rikitake@acm.org>
- Philip Balister <philip@opensdr.com>

### Changes

- CI fixes
  - Allow for rounding error in float-to-int conversions
  - Allow for rounding error in `volk_32fc_s32f_magnitude_16i`
  - Allow for rounding error in float-to-int interleave
  - Add missing `volk_16_byteswap_u_orc` to puppet
  - Fix 64-bit integer testing
  - Build and test neonv7 protokernels on armv7

- kernels
  - Remove broken sse32 kernels
  - Fix flaky `fm_detect` test
  - Fix flaky `mod_range` test
  - Remove unnecessary volatiles from `volk_32fc_s32f_magnitude_16i`
  - Remove SSE protokernels written in assembly
  - Remove inline assembler from `volk_32fc_convert_16ic_neon`
  - Use bit shifts in generic and `byte_shuffle` reverse
  - Remove disabled SSE4.1 dot product
  - Fix `conv_k7_r2` kernel and puppet
  - Remove unused argument from renormalize
  - Align types in ORC function signatures
  - Uncomment AVX2 implementation
  - Renormalize in every iteration on AVX2
  - Remove extraneous permutations
  - Compute the minimum over both register lanes
  - `volk_32fc_s32f_atan2_32f`: Add NaN tests for avx2 and avx2fma code

- fixes
  - Express version information in decimal
  - Remove `__VOLK_VOLATILE`
  - Remove references to simdmath library
  - cmake: Switch to GNUInstallDirs
  - fprintf: Remove fprintf statements from `volk_malloc`
  - release: Prepare release with updated files
  - Get the sse2neon.h file to a git submodule to avoid random copies.
