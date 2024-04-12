---
title: "GNU Radio 3.10.2.0"
author: "Jeff Long"
date: "2022-04-10"
sponsored: "0"
aliases: ["news/3.10-release"]
categories: ["release"]
banner: gr_release_web.svg
---
# Release 3.10.2.0

## [3.10.2.0] - 2022-04-09

### Changed

#### Project Scope

- Clayton Smith continues the effort to replace Boost usage with modern C++ equivalents. In a related effort, he has continued the logging modernization started by Marcus Müller. In his spare time, he has tackled some tricky, intermittent CI failures, some of which turned out to be real bugs. Much of this work is invisible to end users, but is extremely useful in making GNU Radio more reliable and maintainable. Special thanks are due to Clayton for a lot of hard work this cycle.
- Use exceptions instead of `exit()` in several places.
- Fixed a variety of Python deprecation warnings.
- Packager note: `jsonschema` is required for the JSON Config and YAML Config blocks. Those blocks will be disabled if `jsonschema` is not found.

#### gnuradio-runtime

- Correct size/usage for single-mapped buffers (part of the new Custom Buffers feature).
- Correct buffer size allocation. This was actually the single change in v3.10.1.1, which did not get its own CHANGELOG entry.

#### GRC

- Improve discovery of xterm and related programs.
- Save generated hierarchical block code to the block library instead of the directory containing the current GRC flowgraph.
- New JSON Config and YAML Config blocks that load configuration variables from files at runtime. Those variables may then be used in block parameters.
- Store the GNU Radio version in flowgraph metadata when saving.
- Minor change in Python evaluation code to allow `affinity`, `minoutbuf` and `maxoutbuf` to be adjusted via script parameters.


#### Build system and packaging

- Require C++-17 for `gnuradio-runtime` and code compiled against it (via cmake flags).
- Add `pythonschema` to build- and run-time dependencies.

#### gr-blocks

- Add exponential distribution to Message Strobe Random block's `delay` selection.
- Quiet down debug messages in File Sink.
- Skip alignment check in File Source when the input file is not seekable (e.g., it is a pipe).

#### gr-filter

- Fix crash in Rational Resampler logging

#### gr-digital

- Add generic CRC blocks: CRC Append and CRC Check.

#### gr-qtgui

- Improve text/background color on Range widget.
- Digital Number Control emits message with new, instead of previous, value.
- Message Edit Box sends message only when return is pressed, rather than whenever focus is lost.
- Vector Sink allows legend to be disabled.
- Type error fixes (Python 3.10 is stricter about int casting).
 
#### gr-trellis

- Provide Python bindings for PCCC Encoder and Viterbi Combo.

#### gr-vocoder

- Add C++ generation support to gr-vocoder

#### Code generation tools

- Support strongly-typed enums in Python bindings

### Authors

The following people contributed commits to this release. There are may people who contribute in other ways ... discussions, reviews, bug reporting, testing, etc. We just don't have an easy way to provide credit for all that valuable work.

- A. Maitland Bottoms <bottoms@debian.org>
- André Apitzsch <andre.apitzsch@etit.tu-chemnitz.de>
- AsciiWolf <mail@asciiwolf.com>
- Bjoern Kerler <info@revskills.de>
- Campbell McDiarmid <campbell.mcdiarmid@icloud.com>
- Clayton Smith <argilo@gmail.com>
- Daniel Estévez <daniel@destevez.net>
- Davide Gerhard <rainbow@irh.it>
- David Sorber <david.sorber@blacklynx.tech>
- Håkon Vågsether <haakonsv@gmail.com>
- JaredD <jareddpub@gmail.com>
- jb41997
- Jeff Long <willcode4@gmail.com>
- Josh Morman <jmorman@peratonlabs.com>
- jsallay
- luz paz <luzpaz@users.noreply.github.com>
- Marcus Müller <mmueller@gnuradio.org>
- Philip Balister <philip@balister.org>
- Ron Economos <w6rz@comcast.net>
- Ryan Volz <ryan.volz@gmail.com>
- Volker Schroer