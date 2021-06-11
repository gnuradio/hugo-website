---
title: "GNU Radio 3.8.3.1"
author: "Jeff Long"
date: "2021-06-10"
sponsored: "0"
aliases: ["news/3.8-release"]
categories: ["release"]
thumbnail: "gr_release"
---
# Release 3.8.3.1

The June updates for GNU Radio are out. Here is the changelog summary for [v3.8.3.1](https://github.com/gnuradio/gnuradio/releases/tag/v3.8.3.1).

<!--more-->

## [3.8.3.1] - 2021-06-10

This is a PATCH level revision. The API is compatible with C++ code written for previous v3.8 releases. ABI (shared library signature) is intended to be compatible, so code linked against v3.8.3.0 should not require recompilation.

### Changed

#### Build system

- Improved messages related to dependencies MPIR and GMP. Only one of these packages is required, and the previous error messages were confusing.

#### GRC

- Parameter expressions and/or values can be displayed in blocks on the flowgraph. Previously, only values were displayed. Look for the "Show Parameter ..." toggles under the View menu.
- Vector length is now correctly applied to all input ports.
- Validation has been improved. Raw types are validated. Port connections are checked by type rather than by item size.
- Variable names that cause conflicts in Python code (e.g., package names) are rejected.
- Bus logic fixes.
- Blocks can no longer be dragged off the screen and lost forever.

#### gr-dtv

- VL-SNR bugs fixed (incorrect constants).

#### gr-qtgui

- Improve autoscaling for vector sinks.

#### gr_filter_design

- "File/Save" is disabled until the taps have been computed, and the GUI is reset after a save, to make it clearer which data is being saved.
- Entries are hidden for parameters that do not apply to the selected filter type.

At LEAST the following authors contributed to this release.

- 0xloem <0xloem@gmail.com>
- Christophe Seguinot <christophe.seguinot@univ-lille.fr>
- David Pi <david.pinho@gmail.com>
- Igor Freire <igor@blockstream.com>
- Jeff Long <willcode4@gmail.com>
- Josh Morman <jmorman@perspectalabs.com>
- Marcus Müller <mmueller@gnuradio.org>
- Ron Economos <w6rz@comcast.net>
- Solomon Tan <solomonbstoner@yahoo.com.au>
- Volker Schroer
- Zackery Spytz <zspytz@gmail.com>
