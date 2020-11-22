---
title: "VOLK v2.3.0 release"
author: "Johannes Demel"
date: "2020-05-09"
categories: ["release"]
aliases: ["news/volk-v2.3.0-release"]
thumbnail: "volk_release"
---
[Originally published on libvolk.org](https://www.libvolk.org/category/news.html)

Hi everyone!

[VOLK 2.3](https://github.com/gnuradio/volk/releases/tag/v2.3.0) is out! We want to thank all contributors. This release wouldn't have been possible without them. We saw lots of great improvements.

On GNU Radio 'master' VOLK was finally removed as a submodule.

Currently we see ongoing discussions on how to improve CPU feature detection because VOLK is not as reliable as we'd like it to be in that department. We'd like to benefit from other open source projects and don't want to reinvent the wheel. Thus, one approach would be to include `cpu_features` as a submodule.

### Highlights

* Better reproducible builds
* CMake improvements
    - ORC is removed from the public interface where it was never supposed to be.
    - CMake fixes for better usability
* Updated and new CI chain
    - TravisCI moved to new distro and does more tests for newer GCC/Clang
    - Github Actions
        - Add Action to check proper code formatting.
        - Add CI that also runs on MacOS with XCode.
* Enforce C/C++ coding style via clang-format
* Kernel fixes
    - Add puppet for `power_spectral_density` kernel
    - Treat the `mod_range` puppet as a puppet for correct use with `volk_profile`
    - Fix `index_max` kernels
    - Fix `rotator`. We hope that we finally found the root cause of the issue.
* Kernel optimizations
    - Updated log10 calcs to use faster log2 approach
    - Optimize `complexmultiplyconjugate`
* New kernels
    - accurate exp kernel is finally merged after years
    - Add 32f_s32f_add_32f kernel to perform vector + scalar float operation

### Contributors

* Bernhard M. Wiedemann <bwiedemann@suse.de>
* Clayton Smith <argilo@gmail.com>
* Johannes Demel <demel@ant.uni-bremen.de> <demel@uni-bremen.de>
* Michael Dickens <michael.dickens@ettus.com>
* Tom Rondeau <tom@trondeau.com>
* Vasil Velichkov <vvvelichkov@gmail.com>
* ghostop14 <ghostop14@gmail.com>

### Changes

* Reproducible builds
    - Drop compile-time CPU detection
    - Drop another instance of compile-time CPU detection
* CI updates
    - ci: Add Github CI Action
    - ci: Remove Ubuntu 16.04 GCC5 test on TravisCI
    - TravisCI: Update CI to bionic distro
    - TravisCI: Add GCC 8 test
    - TravisCI: Structure CI file
    - TravisCI: Clean-up .travis.yml
* Enforce C/C++ coding style
    - clang-format: Apply clang-format
    - clang-format: Update PR with GitHub Action
    - clang-format: Rebase onto current master
* Fix compiler warnings
    - shadow: rebase kernel fixes
    - shadow: rebase volk_profile fix
* CMake
    - cmake: Remove the ORC from the VOLK public link interface
    - versioning: Remove .Maint from libvolk version
    - Fix endif macro name in comment
* Kernels
    - volk: accurate exp kernel
        - exp: Rename SSE4.1 to SSE2 kernel
    - Add 32f_s32f_add_32f kernel
        - This kernel adds in vector + scalar functionality
    - Fix the broken index max kernels
    - Treat the mod_range puppet as such
    - Add puppet for power spectral density kernel
    - Updated log10 calcs to use faster log2 approach
    - fix: Use unaligned load
    - divide: Optimize complexmultiplyconjugate