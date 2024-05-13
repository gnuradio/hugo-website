---
title: "GNU Radio 3.9.3.0"
author: "Jeff Long"
date: "2021-10-09"
sponsored: "0"
aliases: ["/news/3.9-release"]
categories: ["release"]
banner: gr_release_web.svg
---
# Release 3.9.3.0

The September updates for GNU Radio are out. Here is the changelog summary for [v3.9.3.0](https://github.com/gnuradio/gnuradio/releases/tag/v3.9.3.0).

<!--more-->

## [3.9.3.0] - 2021-09-30

This is an API compatible update to GNU Radio 3.9. Code written for 3.9.X versions should
compile and link without modification. The ABI is not guaranteed to be compatible, so
a rebuild of OOT modules may be necessary.

### Changes

#### General

- Many cleanups and some C++ modernization changes
- Replace Boost with stdc++ equivalents (ongoing effort)
- Logging cleanup and performance improvements (ongoing effort)
- Cleanup of many unused includes
- Various block yaml cleanups and repairs
- Use Soapy instead of UHD for flowgraph testing in gr-analog and gr-dtv

#### GRC

- Improvements in C++ templates and code generation, more blocks are usable
- Add specification of packages to find (via cmake) for C++ templates
- Fix C++ hier block param template
- Add GUI hints for widgets in C++ code generation
- Add no_quotes() convenience function to strip quotes from strings, callable from templates
- Allow short and byte as valid types in an enum
- Fix desync when dragging block (block would not always track cursor)
- Correctly evaluate interdependent variables
- Allow error messages to be copied to clipboard
- Update disabled blocks if they depend on others

#### gnuradio-runtime

- Deprecate tag_checker class (will be removed in 3.10)
- Detect and follow symbolic links for installation prefix in gr::prefix()
- Add "<" operator for comparison of tags (instead of offset_compare())

#### gr-blocks

- New Matrix Interleaver block
- Throttle and Head blocks can be input-only when no output is needed, improving performance
- Fix tag propagation in (un)pack-k-bits blocks
- Fix namespace for nco and vco in benchmarks

#### gr-digital

- New Async CRC16 block
- Add NRZI option to Differential En/Decoder
- Constellation performance improvements
- Fix constellation normalization by average power
- Remove unimplemented msg output port from Chunks to Symbols block
- Make unpacking of bits optional in GMSK modulator so the blocks can accept unpacked bits
- In GFSK/GMSK hier blocks, replace M&M clock recovery with newer and more capable Digital Symbol Sync block

#### gr-fec

- Cleanups and code improvements

#### gr-fft

- Add a "shift" paramenter to Log Power FFT, to place DC bin at center

#### gr-filter

- Performance improvement in PFB Arbitrary Resampler when interpolating, especially at low rates

#### gr-qtgui

- Fix display of tags on the last sample (would be dropped)
- Python wrapping: replace pyqwidget() with qwidget() - this is not intended to be a visible fix, but is mentioned here in case it causes trouble for anyone
- C++ generation
  - add double quotes to cpp_opts keys with colons
  - position windows correctly depending on gui_hint
  - use option attributes to generate enums
  - use the cpp enums for wintype and trigger_type

#### gr-uhd

- Fix input filename in freq hopping examples
- Make RFNoC a separately enabled component in cmake
- Python bindings for rfnoc_graph,_rx/tx_streamer

#### gr-video-sdl

- U and V channels were reversed on sink blocks

#### gr-soapy

- Added message support for SoapySDR 0.8 API

#### modtool

- Set VERSION_PATCH to 0 instead of "git" in new modules
- Fix "rm", "bind", disable", "rename" and "makeyml" which had unexpected side effects, or did not work as a user would expect

#### Build System

- Correct minimum version checking for Mako
- Ensure that RC_*_VERSION are numeric (Windows)
- Fix finding libunwind
- Pass through extra arguments to GR_PYTHON_INSTALL to install command
- Remove absolute paths and private links from exported targets
- Add gir1.2-gtk-3.0 as deb runtime dependency

#### Documentation

- Code of Conduct updates and link to Wiki

#### CI

- Do not error out on deprecations, allowing testing of deprecated code

### Contributors
At LEAST the following people contributed code to this release.

- Adrien Michel
- cmrincon cmrincon611@hotmail.com
- Daniel Estévez daniel@destevez.net
- David Pi david.pinho@gmail.com
- David Winter david.winter@analog.com
- Håkon Vågsether hauk142@gmail.com
- Igor Freire igor@blockstream.com
- japm48
- JaredD jareddpub@gmail.com
- Jason Uher jason.uher@jhuapl.edu
- Jeff Long willcode4@gmail.com
- jfmadeira jf.madeira@campus.fct.unl.pt
- jmadeira jmadeira@pdmfc.com
- Marc L marcll@vt.edu
- Marcus Müller mmueller@gnuradio.org
- Mark Bauer markb5@illinois.edu
- Martin Braun martin@gnuradio.org
- Nicholas Corgan n.corgan@gmail.com
- Oleksandr Kravchuk open.source@oleksandr-kravchuk.com
- Pavon pavon@protonmail.com
- Rohan Sharma rhnsharma5113@gmail.com
- Ron Economos w6rz@comcast.net
- Ryan Volz ryan.volz@gmail.com
- Seth Hitefield sdhitefield@gmail.com
- Solomon solomonbstoner@yahoo.com.au
- Solomon Tan solomonbstoner@yahoo.com.au
- Volker Schroer
