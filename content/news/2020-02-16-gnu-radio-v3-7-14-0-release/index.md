---
title: "GNU Radio 3.7.14.0"
author: "Marcus Müller"
date: "2020-02-16"
sponsored: "0"
aliases: ["/news/3.7.14.0-release"]
categories: ["release"]
banner: gr_release_web.svg
---
Dearest most-enduring SDR community to ever roam the galaxy,

the legacy 3.7 release series sees a [bug fix
release](https://github.com/gnuradio/gnuradio/releases/tag/v3.7.14.0). We had to
bump the maint version from 13 to 14, because we fundamentally changed the
(pseudo) random number generation – which has the effect that pre-3.7.14.0
flowgraphs use different random scramblers and pilots, amongst other things.

Find the release notes below.

Cheers,
Marcus


# Release 3.7.14.0

## Contributors

* Chris <christopher.donohue@gmail.com>
* Christoph Mayer <hcab14@gmail.com>
* Eric Johnson <ejohnson73@gmail.com>
* gmazilla
* Håkon Vågsether <haakonsv@gmail.com>
* Josh Morman <jmorman@perspectalabs.com>
* Marcus Müller <mmueller@gnuradio.org>
* Martin Braun <martin.braun@ettus.com>
* Michael Dickens <michael.dickens@ettus.com>
* rear1019 <rear1019@posteo.de>
* Ron Economos <w6rz@comcast.net>
* Ryan Volz <rvolz@mit.edu>
* Sebastian Müller <gsenpo@gmail.com>
* Thomas Habets <thomas@habets.se>

## [3.7.14.0] - 2020-02-15

### Fixed
#### Project Scope
- replace remaining calls to thread-unsafe `rand` with internal random
generators

#### gnuradio-runtime
- don't give up on looking for configuration files if system directory
doesn't exist
- `get_tags_in_range` on delay blocks
- premature tag pruning

#### gr-blocks
- 8 bit WAV file reading
- `matrix_multiply` no longer wrongly converts complex float to double
- Boost 1.70 compat

#### gr-digital
- UHD packet example: frame bit fixes
- `additive_scrambler` count-based reset
- `map_bb` buffer overflow, thread safety

#### gr-dtv
- falsely failing assert

#### gr-fec
- `cc_encoder`: constraint length > 8

#### grc
- Ctrl-F unselects blocks (so that "d" doesn't disable them)

### Added
#### gnuradio-runtime
- XOROSHIRO128+-based PRNG

#### gr-digital
- `additive_scrambler` test

#### gr-uhd
- future UHD compat layer

### Changed
#### Project Scope
- COMPATIBILITY WARNING: Replaced non-threadsafe (s)rand with our own
xoroshiro-based PRNG
- Whole tree code reformatting

#### gr-blocks
- replaced reconfiguring selector with 3.8 backport

#### gr-channels
- removed unnecessary delay in selective fading model

#### gr-digital
- COMPATIBILITY: Change of random OFDM pilots
- backport of 3.8 constellation changes

#### gr-trellis
- COMPATIBILITY: random interleaver: PRNG change -> different interleaver

