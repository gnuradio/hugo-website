---
title: "GNU Radio 3.9.2.0"
author: "Jeff Long"
date: "2021-06-10"
sponsored: "0"
aliases: ["news/3.9-release"]
categories: ["release"]
thumbnail: "gr_release"
---
# Release 3.9.2.0

The June updates for GNU Radio are out. Here is the changelog summary for [v3.9.2.0](https://github.com/gnuradio/gnuradio/releases/tag/v3.9.2.0).

<!--more-->

## [3.9.2.0] - 2021-06-10

### Changed

#### SoapySDR support (gr-soapy)
The new gr-soapy built-in module provides access to Soapy hardware drivers using the SoapySDR driver framework. See https://wiki.gnuradio.org/index.php/Soapy for more information.

If SoapySDR 0.7.2 or newer is available during GNU Radio configuration, the gr-soapy module will be enabled.

The SoapySDR framework and Soapy driver modules are not maintained by the GNU Radio project. Driver modules are dynamically discovered and linked. They may be added and updated independently from the GNU Radio release cycle.

#### GRC

- Parameter expressions and/or values can be displayed in blocks on the flowgraph. Previously, only values were displayed. Look for the "Show Parameter ..." toggles under the View menu.
- Deprecated blocks are shown in a distinct color (orange), and the optional `deprecated` property has been added to block yaml
- Dark theme works better, especially for parameter fields
- Vector length is now correctly applied to all input ports
- Validation has been improved. Raw types are validated. Port connections are checked by type rather than by item size.
- Variable names that cause name conflicts in Python code (e.g., with package names) are rejected
- Bus logic fixes
- Blocks can no longer be dragged off the screen and lost forever

#### gnuradio-runtime

- Remove `pmt::pmt_*` functions, which were not actually implemented. This is technically an API change, but any use of the API would have resulted in a link error.
- Remove Python bindings for internal buffer functions

#### gr-analog

- Added an example for PLL Frequency Detector
- Better names for parameters in PLL GRC blocks

#### gr-blocks

- Consistent naming for Vector Length parameter in GRC blocks
- `count_bits` uses VOLK `popcnt` for better performance (used for example in the Correlate Access Code block)
- Rotator block phase increment parameter is controllable via a message, and a tag can be added at the point where the increment is adjusted

#### gr-digital

- MPSK example updated to use a Linear Equalizer (replacing deprecated block)

#### gr-filter

- Filter Delay documentation improvement
- Interpolating FIR filter can generate C++ code

#### gr-dtv

- VL-SNR bugs fixed (incorrect constants).

#### gr-qtgui

- Improve autoscaling for vector sinks
- Fix floating-point resolution problems in several widgets, due to interpretation of PMT doubles as floats

#### gr-uhd

- Add policy enum to Python bindings for `tune_request` 
- Additional time spec options on UHD blocks (PC Clock on Next PPS, GPS Time on Next PPS)
- Fix up code that was generating warnings
- Fix command handler logic to apply commands from messages to the correct channel

#### gr_filter_design

- "File/Save" is disabled until the taps have been computed, and the GUI is reset after a save, to make it clearer which data is being saved.
- Entries are hidden for parameters that do not apply to the selected filter type.
- Save window type as an integer instead of a Python enum name

#### gr_modtool

- Improve validation of module and block names

#### Build System and Infrastructure

- Improved messages related to dependencies MPIR and GMP. Only one of these packages is required, and the previous error messages were confusing.
- Cleaner builds for Windows and Conda. A number of general cmake improvements have resulted from this work.
- In-tree packaging files for DEB and RPM, used with Launchpad and COPR
- Added man pages for GNU Radio tools
- Test code generation for all in-tree GRC examples
- In GrPybind.cmake, `PYBIND11_INCLUDE_DIR` (incorrect) was changed to `pybind11_INCLUDE_DIR`

### Contributors
At LEAST the following authors contributed to this release. Note that only authors of commits are included here. A number of people contribute in other ways, including code review, documentation and testing.

- 0xloem <0xloem@gmail.com>
- Christophe Seguinot <christophe.seguinot@univ-lille.fr>
- Chuang Zhu <genelocated@yandex.com>
- Codey McCodeface <Codey.McCodeface@gmail.com>
- Ferenc Gerlits <fgerlits@gmail.com>
- Håkon Vågsether <hauk142@gmail.com>
- Igor Freire <igor@blockstream.com>
- Jacob Gilbert <jacob.gilbert@protonmail.com>
- Jeff Long <willcode4@gmail.com>
- Josh Morman <jmorman@perspectalabs.com>
- Liu, Andrew Z <liu.andrew@vast-inc.com>
- Marcus Müller <mmueller@gnuradio.org>
- Martin Braun <martin@gnuradio.org>
- Martyn van Dijke <martijnvdijke600@gmail.com>
- Nicholas Corgan <n.corgan@gmail.com>
- Ron Economos <w6rz@comcast.net>
- Ryan Volz <ryan.volz@gmail.com>
- Solomon Tan <solomonbstoner@yahoo.com.au>
- Volker Schroer
- Zackery Spytz <zspytz@gmail.com>
