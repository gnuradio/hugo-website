---
title: "VOLK v3.1.0 release"
author: "Johannes Demel"
date: "2023-12-05"
categories: ["release"]
aliases: ["/news/volk-v3.1.0-release"]
banner: volk_release_web.svg
---

[Originally published on libvolk.org](https://www.libvolk.org/release-v310.html)

Hi everyone!

This is the VOLK v3.1.0 release! We want to thank all contributors. This release wouldn't have been possible without them.

This release introduces new kernels, fixes a lot of subtle bugs, and introduces an updated API that allows VOLK to run on PowerPC and MIPS platforms without issues. Namely, complex scalar values are passed to kernels by pointer instead of by value. The old API is still around and will be for the whole VOLK v3 release cycle. However, it is recommended to switch to the new API for improved compatibility. Besides, we saw improvements to our `cpu_features` usage that should make it easier for package maintainers. Finally, a lot of tests received fixes that allow our CI to run without hiccups.

### Contributors

* A. Maitland Bottoms <bottoms@debian.org>
* Andrej Rode <mail@andrejro.de>
* Ashley Brighthope <ashley.b@reddegrees.com>
* Clayton Smith <argilo@gmail.com>
* Daniel Estévez <daniel@destevez.net>
* Johannes Demel <demel@uni-bremen.de>, <jdemel@gnuradio.org>
* John Sallay <jasallay@gmail.com>
* Magnus Lundmark <magnus@skysense.io>, <magnuslundmark@gmail.com>
* Marcus Müller <mmueller@gnuradio.org>
* Michael Roe <michael-roe@users.noreply.github.com>
* Thomas Habets <thomas@habets.se>


### Changes

- Build and dependency updates
      - omit build path
      - cmake: Link to cpu_features only in BUILD_INTERFACE
      - cpu_features: Update submodule pointer and new CMake target name
      - cmake: Removed duplicated logic
      - cmake: Do not install cpu_features with volk
      - Use CMake target in one more place
      - Fix typo in the CMake target name
      - Use CpuFeatures target
      - Use cpu_features on RISC-V platforms
      - cpu_features: Update submodule pointer
      - Add UBSAN to ASAN builds

- CI fixes
      - Add length checks to volk_8u_x2_encodeframepolar_8u
      - Fix flaky qa_volk_32f_s32f_convertpuppet_8u
      - Use absolute tolerance for stddev_and_mean
      - Use absolute tolerance for sum_of_poly kernel
      - Add length checks to conv_k7 kernels
      - Fix variable name in dot product kernels
      - Fix buffer overflow in volk_32fc_x2_square_dist_32f_a_sse3
      - Increase tolerance for volk_32f_log2_32f
      - Re-enable tests on aarch64 clang-14
      - Fix undefined behaviour in volk_8u_x4_conv_k7_r2_8u
      - Fix undefined behaviour in volk_32u_reverse_32u
      - Fix aligned loads and stores in unaligned kernels
      - Fix register size warnings in reverse kernel
      - Fix undefined behaviour in dot product kernels
      - Use an absolute tolerance to test the dot product kernels
      - Always initialize returnValue
      - Add length checks to puppets
      - Add carriage return to error message
      - Include ORC in neonv8 machine definition
      - Add back volk_32f_exp_32f test
      - Generate random integers with uniform_int_distribution
      - Fix puppet master name for volk_32u_popcnt
      - Avoid integer overflow in volk_8ic_x2_multiply_conjugate_16ic corner case
      - Use a reasonable scalar and tolerance for spectral_noise_floor
      - Increase volk_32f_x2_dot_prod_16i tolerance to 1
      - Increase tolerance for the power_spectrum test
      - Decrease the range for signed 16-bit integer testing
      - Use a puppet to pass positive values to volk_32f_x2_pow_32f
      - Use absolute tolerances for accumulator and dot product
      - Fix AppVeyor git checkout

- new kernel API
      - Use pointers to pass in s32fc arguments
        - The old API is deprecated but will be available for the foreseeable future

- updated kernels
      - Remove unused ORC code
      - Prefer NEON kernels over ORC
      - Require all kernels to have a generic implementation
      - Remove redundant a_generic kernels
      - Remove ORC kernels that use sqrtf
      - reverse: Rename dword_shuffle to generic
      - volk_32f_s32f_convert_8i: code style
      - volk_32fc_x2_divide_32fc: add documentation about numerical accuracy
      - kernel: Refactor 32f_s32f_multiply_32f kernel
      - kernel: Refactor 32f_x2_subtract_32f kernel
      - convert 32f->32i: fix compiler warnings about loss of int precision
      - 64u_ byteswape: remove buggy Neonv8 protokernel
      - 64u_ byteswape: remove buggy Neon protokernel
      - Remove broken volk_16i_max_star_16i_neon protokernel
      - Fix truncate-toward-zero distortion
      - Fix encodepolar documentation

- new kernels
      - add volk_32f_s32f_x2_convert_8u kernel
      - Fix documentation for the clamp kernel
      - added new kernel: volk_32f_s32f_x2_clamp
      - new kernels for atan2
      - Add 32f_s32f_multiply_32f RISC-V manually optimized assembly
      - Add .size to volk_32f_s32f_multiply_32f_sifive_u74
      - Add volk_32fc_x2_dot_prod_32fc_sifive_u74
