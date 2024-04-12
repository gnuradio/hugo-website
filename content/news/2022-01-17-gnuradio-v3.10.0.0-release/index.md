---
title: "GNU Radio 3.10.0.0"
author: "Josh Morman"
date: "2022-01-17"
sponsored: "0"
aliases: ["news/3.10-release"]
categories: ["release"]
banner: gr_release_web.svg
---
# Release 3.10.0.0

## [3.10.0.0] - 2022-01-14

It is with much excitement that we release the next step forward for GNU Radio - 3.10.0.0!

Not only does this release bring in some extremely useful new modules (gr-iio, gr-pdu, and arguably gr-soapy thought that thankfully made it also into recent 3.9 maintenance releases), but also sets a path forward for using GNU Radio in heterogeneous compute environments by providing "custom buffers" for more efficiently interacting with accelerators (GPUS, FPGAs, TPUs, etc.).

We have been fortunate this year to have extremely active backporting and consistent maintenance releases from co-maintainter Jeff Long - so many of the fixes and smaller feature (and larger ones) have already seen the light of day in the 3.9.x.x and even 3.8.x.x releases.  

A special specific thanks to the contributors that made these larger features and upstreamed modules possible, but much appreciation to all that contributed through code, documentation, review, and just generally being a part of this wonderful community.
- gr-pdu: Jacob Gilbert and the team at Sandia National Labs
- gr-iio: Travis Collins and the team at Analog Devices as well as Adam Horden, David Winter, and Volker Shroer for bringing this in-tree and working through many of the complexities.
- Custom Buffers Support: We have David Sorber to thank for this incredible, yet advanced, feature that came out of the DARPA SDR 4.0 program and should get a lot of traction.  Check out https://wiki.gnuradio.org/index.php/Custom_Buffers for more of the gory detail.  Also thanks to Seth Hitefield whose initial work in this area helped get this concept into the mainstream for GNU Radio.
-  Logging Infrastructure Overhaul: A huge thanks to Marcus Müller for fixing all of this up, replacing Log4CPP with spdlog and also for providing ongoing architectural leadership to the project

### Changed

- Moved PDU blocks from gr-blocks to gr-network and gr-pdu
   - Compatibility shim included to allow access to these blocks from gr-blocks
     but these are deprecated from the gr-blocks namespace and the shim is
     scheduled for removal in 3.11.
- gr::blocks::pdu namespace has been reorganized in gr
   - PDU vector types are accessible in gr::types
   - PDU functions are accessible in gr::pdu
   - Common msg port names are accessible in gr::ports
- Logging Infrastructure changed to use spdlog
   - +dependency spdlog, -dependency Log4CPP
   - New, more convenient logging methods
   - Modernized Interface
   - Removed iostream and cstdio from logging statements

#### Project Scope

- C++17
  - requires MSVC 1914 (Microsoft VS 2017 15.7)
  - replace boost::filesystem with std::filesystem
- Windows build: removed unnecessary MSVC-specific system include overrides
- Removed unused volk_benchmark
- Use Pre-Compiled Headers - speeds up compilation time
- Further replacements of boost::bind with lambda functions
- Remove more manual memory management and general c++ modernization
- PEP8 formatting applied and enforced on all Python files
- Centralized min dependency and compiler versions in one place for GR and modtool created OOTs
- Update QA tests to work with OpenEmbedded cross compilations
- Dependency versions:
  - Python 3.6.5
  - numpy 1.17.4
  - VOLK 2.4.1
  - CMake 3.16.3
  - Boost 1.69
  - Mako 1.1.0
  - PyBind11 2.4.3
  - pygccxml 2.0.0
- Compiler options:
  - GCC 9.3.0
  - Clang 11.0.0 / Apple Clang 1100
  - MSVC 1916 (Microsoft VS 2017 15.9)
- Replace deprecated distutils in CMake macros
- Build targets with python dependencies conditionally on `ENABLE_PYTHON`


#### gr-blocks

- Remove deprecated networking blocks: `udp_source`, `udp_sink`, `tcp_server_sink`; replaced
  in 3.9 with more capable blocks in `gr-network`
- Document the supported operations in transcendental

#### gr-analog

- `fastnoise_source`: Use `uint64_t` seed API, use `size_t` for vector length/indices
- `fastnoise_source`: Use a simple bitmask if the random pool length is a power
  of 2 to determine indices, instead of `%`, which consumed considerable CPU
- `sig_source`: Remove deprecated `freq` message port of signal source block; Use `cmd` port instead

### gr-filter

- Remove deprecated `mmse_interpolator` block; Replaced previously by `mmse_resampler`
- Speed up filter building with moves
- Add const to temporary tap vectors

### gr-digital

- Remove deprecated simple_{correlator,framer}
- Remove deprecated cma, lms, kurtotic equalizers; replaced in 3.9 by `linear_equalizer`
- Un-deprecate pfb_clock_sync
- Add header payload demux example 
- Remove crc32 utility and most of packet_utils 
- Remove yml files for non-existent QAM mod/demod blocks

#### gr-dtv

- Refactor ATSC blocks to have separate metadata stream rather than passing structs
- Add energy normalization for DVB-S2X constellations

#### gr-network

- Fix segfaults when TCP and UDP are restarted

#### gr-qtgui

- Remove spurious volk includes
- Fix segfaulting overflow in time_sink and waterfall
- Support for Qwt 6.2
- Frequency/Waterfall Sinks expand range to 32k and enums in GRC
- Frequency/Waterfall Sinks force power of 2 for fft size

#### gr-uhd

- Python bindings for RFNoC blocks

#### gr-utils

- gr_modtool bind workaround for pygccxml incompatibility with spdlog

#### gr-video-sdl

- Clean up the SDL sinks:
   -  Remove unused format parameter 

#### gnuradio-runtime

- `gr::random` uses xoroshiro128+ internally, takes `uint64_t` seed
- Remove unused misc.cc/h
- Accelerator Device Support
    - Major changes to the runtime to support "custom buffers"
    - Single Mapped Buffer abstraction that can be inherited out of tree
- Remove Tag Checker
- Explicitly convert path to string to fix MSVC build
- size_t for vmcircbuf constructor and buffer factories
- Reconfigurable timer value for input blocked condition (scheduler detail workaround)

#### grc

- grcc --output switch for hierarchical blocks
- Clean up Bokeh server loop
- Don't blacklist `default` as a flowgraph ID to prevent always starting in an error state

#### Testing

- rm dependencies from disabled components in blocks/runtime tests

#### Misc.

- dtools: Added run-clang-tidy-on-codebase, which does what the name suggests,
  then updates all bindtool hashes, and commits everything appropriately
- `gr_filter_design` 
  - update to support PyQt5
  - fix loading of previously saved .csv files

### Added

- New in-tree module gr-pdu
- New in-tree module gr-iio
