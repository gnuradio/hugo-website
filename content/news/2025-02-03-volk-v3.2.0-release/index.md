---
title: "VOLK v3.2.0 release"
author: "Johannes Demel"
date: "2025-02-03"
categories: ["release"]
aliases: ["/news/volk-v3.2.0-release"]
thumbnail: "volk_release"
---

[Originally published on libvolk.org](https://www.libvolk.org/release-v320.html)

Hi everyone!

This is the VOLK v3.2.0 release! We want to thank all contributors.
This release wouldn't have been possible without them.

Thanks to Olaf Bernstein, VOLK received well optimized RiscV implementations for almost every kernel.
Together with the appropriate CI, this contribution makes VOLK way more powerful on a whole new architecture.

We started to use gtest as an additional test framework. The current "one kinda test fits all" approach is often insufficient to test kernels where they really should not fail.
Now, this approach should allow us to implement more powerful tests more easily.

Besides the x86 platform, we see more and more ARM activity. The corresponding kernels can now be tested natively on Linux and MacOS.
This approach is way faster than before with QEMU. A single job runs in ~1min instead of ~12min now.

### Contributors

- Doron Behar <doron.behar@gmail.com>
- Johannes Demel <jdemel@gnuradio.org>
- John Sallay <jasallay@gmail.com>
- Magnus Lundmark <magnuslundmark@gmail.com>
- Olaf Bernstein <camel-cdr@protonmail.com>
- Ron Economos <w6rz@comcast.net>
- Sam Lane <sl01172@surrey.ac.uk>
- Suleyman Poyraz <zaryob.dev@gmail.com>
- tinyboxvk <13696594+tinyboxvk@users.noreply.github.com>

### Changes

- New and improved kernels
    - add RISC-V Vector extension (RVV) kernels
    - New AVX512F implementation
- Improved and modernized CI
    - ci: Add first native Linux ARM runners
    - macos: Fix CI dependency error
    - appveyor: Update to VS 2022/Python 3.12
    - Update android_build.yml
- Improved builds
    - cmake: Fix 64bit host CPU detection
    - cmake: Suppress invalid escape sequence warnings with Python 3.12
    - cmake/pkgconfig: use CMAKE_INSTALL_FULL_* variables
    - cmake: Fix VOLK as a submodule build issue
    - Adds toolchain file for Raspberry Pi 5
- New and improved tests
    - gtest: Start work on new test infrastructure
    - tests: Add a log info print test
    - gtest: Make gtest an install dependency
    - gtest: Enable GTests in CI workflows
    - tests: Beautify test output
- Documentation
    - cpu_features: Update hints in README
- Code quality
    - Add const to several args
- Usability features
    - feature: add env variable kernel override
