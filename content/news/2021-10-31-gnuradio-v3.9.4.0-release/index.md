---
title: "GNU Radio 3.9.4.0"
author: "Jeff Long"
date: "2021-10-31"
sponsored: "0"
aliases: ["/news/3.9-release"]
categories: ["release"]
banner: gr_release_web.svg
---
# Release 3.9.4.0

## [3.9.4.0] - 2021-10-25

This is an API compatible update to GNU Radio 3.9. Code written for 3.9.X versions should compile and link without modification. The ABI is not guaranteed to be compatible, so a rebuild of OOT modules may be necessary.

### Changes

#### Regressions Fixes

- Remove `#include <filesystem>` (C++17 feature) from one file
- Restore `pyqwidget()` in gr-qtgui

#### GRC

- GRC now runs on Fedora 35 ... Gtk initialization checks were too strict
- Add keyboard shortcuts for zoom
- Account for scale factor when computing drawing area size
- Use font size from config for block comments
- Change type aliasing to allow interleaved short/byte to be connected to vectors of short/byte. Stricter type checking was added previously and caused some blocks to be unconnectable when using these types.
- Required params no longer default to `0` when left empty. This caused hard-to-find errors. Older flowgraphs that have empty required fields will need to be fixed.
- Tooltips fixed for categories and modules

#### gr-runtime

- PMT uses the VOLK allocator for vectors
- `get_tags_in_window()` Python wrapper calls the correct function
- Add `--pybind` option to `gnuradio-config-info` to get PyBind11 version

#### gr-blocks

- Add example for XMLRPC
- Add a unit test for Message Strobe
- Fix C++ support for Unpacked to Packed

#### gr-channels

- RNG seeds are initialized correctly



#### gr-digital

- Fix yml file for Header/Payload Demux

#### gr-network

- Suppress warning in tuntap

#### gr-qtgui

- Remove unusable int type in Number Sink yml
- Use `no_quotes()` function in several yml files

#### modtool

- Hashes can be fixed using modtool using `--update-hash-only`
- Use `tempfile()` instead of `/tmp` in bindtool and modtool
- Use `static_cast` instead of `reinterpret_cast` in templates
- Correct broken Python general block template

#### Build system

- Better check for Boost version
- Determine the Python prefix more reliably
- Use GR-specified compiler standard (C++14) in gr-soapy, instead of the SoapySDR standard (C++11)
- GrPython.cmake is compatible with older cmake

#### Documentation

- Man pages are in-tree
- Repair many examples, especially in gr-digital
- Allow UTF-8 in pydoc templates

#### CI

- Execute `make install` during test
- Add Ubuntu 18.04 test target
