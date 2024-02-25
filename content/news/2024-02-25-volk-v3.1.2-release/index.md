---
title: "VOLK v3.1.2 release"
author: "Johannes Demel"
date: "2024-02-25"
categories: ["release"]
aliases: ["news/volk-v3.1.2-release"]
thumbnail: "volk_release"
---

[Originally published on libvolk.org](https://www.libvolk.org/release-v312.html)

Hi everyone!

This is the VOLK v3.1.2 release! We want to thank all contributors.
This release wouldn't have been possible without them.

The last maintenance release revealed issues in areas that are difficult to test. 
While the changes to the library should be minimal, usability should be improved. 
Most notably, we build and deploy [the VOLK documentation](https://www.libvolk.org/docs) 
automatically now.

### Contributors

- Andrej Rode <mail@andrejro.de>
- Clayton Smith <argilo@gmail.com>
- Johannes Demel <demel@uni-bremen.de>, <jdemel@gnuradio.org>
- Marcus Müller <mmueller@gnuradio.org>
- Rick Farina (Zero_Chaos) <zerochaos@gentoo.org>

### Changes

- Documentation improvements, and automatically generate and publish
    - docs: Add VOLK doc build to CI
    - docs: Add upload to GitHub actions
    - cpu_features: Update hints in README
- Remove sse2neon with a native NEON implementation
    - Replace sse2neon with native NEON
    - Remove loop unrolling
    - Simplify Spiral-generated code
- Improve CI pipeline with new runner
    - flyci: Test CI service with M2 instance
    - actions: Update GH Actions checkout
- Auto-format CMake files
    - cmake: Add .cmake-format.py
    - cmake: Apply .cmake-format.py
- Release script fixes
    - scripts/release: fix multi-concatenation of submodule tars
    - shellcheck fixes
    - bash negative exit codes are not portable, let's be positive
