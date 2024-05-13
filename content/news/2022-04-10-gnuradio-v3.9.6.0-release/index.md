---
title: "GNU Radio 3.9.6.0"
author: "Jeff Long"
date: "2022-04-10"
sponsored: "0"
aliases: ["/news/3.9-release"]
categories: ["release"]
banner: gr_release_web.svg
---
# Release 3.9.6.0

## [3.9.6.0] - 2022-04-09

### Changed

#### Project Scope

- PEP8 formatting applied and enforced on all Python files.

#### GRC

- New JSON Config and YAML Config blocks that load configuration variables from files at runtime. Those variables may then be used in block parameters.
- Store the GNU Radio version in flowgraph metadata when saving.
- Minor change in Python evaluation code to allow `affinity`, `minoutbuf` and `maxoutbuf` to be adjusted via script para
meters.
- Show blocks with "deprecated" flags as deprecated.
- Bug fix: initialize value for "priority" parameter in Python Snippets.
- Don't blacklist `default` as a flowgraph ID to prevent always starting in an error state
- 
#### Runtime

- Add ownership and locking to hier_block2 to avoid crash/freeze after disconnect.

#### gr-analog

- Fix C++ code generation for random_uniform_source

#### gr-blocks

- Add exponential distribution to Message Strobe Random block's `delay` selection.
- Skip alignment check in File Source when the input file is not seekable (e.g., it is a pipe).

#### gr-filter

- Fix crash in Rational Resampler logging
- Bug fix: buses should now work with PFB channelizer and synthesizer.

#### gr-trellis

- Provide Python bindings for PCCC Encoder and Viterbi Combo.

#### gr-qtgui

- Improve text/background color on Range widget.
- Digital Number Control emits message with new, instead of previous, value.
- Message Edit Box sends message only when return is pressed, rather than whenever focus is lost.
- Vector Sink allows legend to be disabled.
- Type error fixes (Python 3.10 is stricter about int casting).
- Frequency/Waterfall Sinks force power of 2 for fft size

#### gr-uhd

- Correct descriptor names in uhd_fpga_ddc/duc.

#### Code generation tools

- Support strongly-typed enums in Python bindings

### Authors

The following people contributed commits to this release. There are may people who contribute in other ways ... discussions, reviews, bug reporting, testing, etc. We just don't have an easy way to provide credit for all that valuable work.

- André Apitzsch <andre.apitzsch@etit.tu-chemnitz.de>
- Armin Ghani <ghani.armin@gmail.com>
- AsciiWolf <mail@asciiwolf.com>
- Bjoern Kerler <info@revskills.de>
- Campbell McDiarmid <campbell.mcdiarmid@icloud.com>
- Clayton Smith <argilo@gmail.com>
- David Winter <david.winter@analog.com>
- JaredD <jareddpub@gmail.com>
- jb41997
- Jeff Long <willcode4@gmail.com>
- Josh Morman <jmorman@peratonlabs.com>
- jsallay
- Marcus Müller <mmueller@gnuradio.org>
- Philip Balister <philip@balister.org>
- Ron Economos <w6rz@comcast.net>
- Ryan Volz <ryan.volz@gmail.com>
- Thomas Habets <habets@google.com>
- Vladisslav P <vladisslav@inbox.ru>
- Volker Schroer