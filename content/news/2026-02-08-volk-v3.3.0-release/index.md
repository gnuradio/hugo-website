---
title: "VOLK v3.3.0 release"
author: "Johannes Sterz Demel"
date: "2026-02-08"
categories: ["release"]
thumbnail: "volk_release"
---

[Originally published on libvolk.org](https://www.libvolk.org/release-v330.html)

Hi everyone!

This is the VOLK v3.3.0 release! We want to thank all contributors.
This release wouldn't have been possible without them.

We received a lot of improvements to existing kernels, new kernels,
and optimized support for a lot of existing kernels.
Moreover, a lot more implementations make use of AVX512 now, as well as
more optimizations for RISC-V, and more NEON implementations.
Thus, overall this is a very exciting release!

Additionally, we received updates all over the code base to improve code quality.
Obsolete code was removed, we get closer and closer to being able to remove the
cpu_features submodule and rely on the distribution package everywhere.
Besides, our throughput test output received a face lift to make it easier to digest.

Finally, over the years, we discussed in-place kernel operations repeatedly.
While we don't test correct in-place operation, e.g., GNU Radio relies on it for
multiple kernels. Finding a way to check and document this behavior is an ongoing effort.

### Contributors

- Anil Gurses <anilgurses98@gmail.com>
- Johannes Sterz Demel <jdemel@gnuradio.org>
- Magnus Lundmark <magnuslundmark@gmail.com>
- Marcus Müller <mmueller@gnuradio.org>
- Olaf Bernstein <camel-cdr@protonmail.com>

### Changes

- New kernels
	- volk_16i_x2_add_saturated_16i
	- volk_16u_x2_add_saturated_16u
	- volk_32f_sincos_32f_x2.h
	- volk_64f_x2_dot_prod_64f.h
	- volk_8i_x2_add_saturated_8i.h
	- volk_8u_x2_add_saturated_8u.h
- Improvements to a lot of kernels
	- RISC-V kernels are further improved and fixed
	- RVV index_max/min kernels always return the correct (first) index now
	- New AVX512 implementations for a lot of kernels
	- Add more NEON kernels with better accuracy
- Documentation
	- Working on auto-publishing latest docs
	- More clarification on our software library dependencies policy
	- Improved documentation on the underlying algorithms that are used
- Code quality
	- cx-limited-range: Reduce scope of compile feature
	- Fully rely on std::filesystem (we used to have a boost::filesystem fallback)
	- Align CMake auto-format with GNU Radio
	- Update to modern PIC enablement
	- Fix NEON compile checks
	- Update code style in more places
	- tighter
- CI
	- Add -Werror flag to CI for C compilation
	- Remove obsolete CI, add new CI
	- Fix obsolete MacOS Intel CI
- Tests
	- Add specialized test suite for the rotator kernel
	- Improved usability with gtest
	- Tighter error bounds for a lot of implementations
- Usability
	- new performance test output
	- fastest implementation is marked with a star
	- speed up vs. generic implementation is printed
	- test "heat up" added
