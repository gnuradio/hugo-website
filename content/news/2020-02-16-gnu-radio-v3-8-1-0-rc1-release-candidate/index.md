---
title: "Release Candidate GNU Radio 3.8.1.0-rc1"
author: "Marcus Müller"
date: "2020-02-16"
sponsored: "0"
aliases: ["news/3.8.1.0-rc1"]
categories: ["release"]
thumbnail: "gr_release"
---


Dear bravest FOSS SDR fellowship to ever been heard of in Middle-earth,

it's a relief to be able share this **release candidate** with you:

https://github.com/gnuradio/gnuradio/releases/tag/v3.8.1.0-rc1

This contains a lot of bug fixes when comparing it directly to 3.8.0.0;
it's also home of a lot of interesting features and featurettes (see the
release notes below).

Please do test this release candidate for any failure to perform – be it
in building on your favourite platform (is anyone still working on GR on
NetBSD?), or in cooperating with your most important OOT module.

If all goes well, we'll have a 3.8.1.0 release by the first week of March.

Namárië,
Marcus

# Release Candidate 3.8.1.0-RC1

## Contributors

* Alba Mendez <me@alba.sh>
* Anders Kalør <anders@kaloer.com>
* Artem Pisarenko <artem.k.pisarenko@gmail.com>
* Bastian Bloessl <mail@bastibl.net>
* Brennan Ashton <bashton@brennanashton.com>
* Chris <christopher.donohue@gmail.com>
* Clayton Smith <argilo@gmail.com>
* CMorin <barthy42@laposte.net>
* Daniel Estévez <daniel@destevez.net>
* Davide Gerhard <rainbow@irh.it>
* Derek Kozel <derek.kozel@gmail.com>
* duggabe
* Glenn Richardson <glenn.richardson@live.com>
* Grant Cox <grant.cox@deepspaceamps.com>
* Gwenhael Goavec-Merou <gwenhael.goavec-merou@trabucayre.com>
* Håkon Vågsether <haakonsv@gmail.com>
* Igor Freire <igor.auad@gmail.com>
* Jan Kraemer <kraemer.jn@gmail.com>
* japm48
* Josh Morman <jmorman@perspectalabs.com>
* karel
* luz.paz
* Marc L <marcll@vt.edu>
* Marcus Müller <mmueller@gnuradio.org>
* Martin Braun <martin.braun@ettus.com>
* Michael Dickens <michael.dickens@ettus.com>
* Michael Roe <mroe@cornstalk.org.uk>
* Nathan West <nwest@deepsig.io>
* Nicolas Cuervo <cuervonicolas@gmail.com>
* Philip Balister <philip@balister.org>
* rear1019 <rear1019@posteo.de>
* RedStone002
* Ron Economos <w6rz@comcast.net>
* Ryan Schutt
* Ryan Volz <rvolz@mit.edu>
* Sebastian Koslowski <sebastian.koslowski@gmail.com>
* Sebastian Müller <gsenpo@gmail.com>
* Sylvain Munaut <tnt@246tNt.com>
* Terry May <terrydmay@gmail.com>
* Thomas Habets <thomas@habets.se>
* Vasil Velichkov <vvvelichkov@gmail.com>
* Volker Schroer
* wcampbell <wcampbell1995@gmail.com>

## [3.8.1.0-rc1] - 2020-02-16

### Changed

#### Project Scope

- clang-tidy improvements
  - Throw exceptions by value, catch by reference
  - `emplace_back` where applicable
  - `empty()` instead of `vector::size() == 0`

### Fixed

#### Project scope

- FindQwt paths
- floatAlmostEqual unittest assert function wrongly passing on sequence
types
- Only require boost unittest when testing is enabled
- FindLOG4CPP typo

#### gnuradio-runtime

- block gateway shadowed system port
- Flaky message passing unit test contained timeout (not the test's job)
- ctrlport/`rpcaggregator` & Co: removed storage of references to
scope-lifetime objects
- Sine table generation python was wrong
- `get_tags_in_range` for delay < (end-start)
- premature tag pruning

#### gr_modtool

- wrong use of `input` -> `raw_input`
- allow empty argument list
- testing
- check for and deny TSB under Python
- QA addition bugs

#### gr-analog

- clipping in FM receiver: remove superfluous gain
- C++ generation for multiple blocks

#### gr-audio

- portaudio source: lock acquisition

#### gr-blocks

- broken `rotator` workaround

#### gr-digital

- `map_bb` buffer overflow
- `map_bb` thread safety
- `additive_scrambler `count based reset

#### gr-fec

- heap corruption in `async_decoder`
- `cc_encoder` was broken for constraint lengths > 8

#### gr-fft

- restore Boost 1.53 compat

#### gr-qtgui

- no longer requiring unnecessary key in `edit_box_msg`

#### gr-uhd

- fixed examples under Py3
- multichannel objects not populating channels

#### GRC

- several issues with YAML files
- nested objects now properly populate namespaces
- comments now included in block bounds calculation
- Wiki documentation link removed from OOT blocks' docs tab
- Dragging connections to auto-hide ports works now

### Added

#### Project Scope

- Codec2 development branch / future compat
- Boost 1.71 compat
- CI now checks for formatting

#### gnuradio-runtime

- dot graphs now contain message edges

#### gr-uhd

- UHD Filter API

#### GRC

- block affinity, buffer sizes available as advanced options for blocks
- testing
