---
title: "GNU Radio 3.8.4.0"
author: "Jeff Long"
date: "2021-10-09"
sponsored: "0"
aliases: ["news/3.8-release"]
categories: ["release"]
thumbnail: "gr_release"
---
# Release 3.8.4.0

The September updates for GNU Radio are out. Here is the changelog summary for [v3.8.4.0](https://github.com/gnuradio/gnuradio/releases/tag/v3.8.4.0).

<!--more-->
## [3.8.4.0] - 2021-09-30

API is compatible with C++ code written against previous v3.8 releases.

ABI (link time) compatibility is not guaranteed. Out-of-tree C++ code
linked to previous v3.8 releases should be rebuilt against this version.

### Changed

#### GRC

- Fix drag and drop issue with Quartz
- Fix desync when dragging block
- Update disabled blocks if they depend on others
- Allow short and byte as valid types in an enum
- Fix evaluation of interdependent variables

#### modtool

- Set VERSION_PATH to 0 in new modules, instead of using GIT rev
- For Python3, return correct exeption ModuleNotFoundError instead of ImportError

#### gr-blocks

- New Matrix Interleaver block

#### gr-channels

- Fix "hide" expressions in yml files

#### gr-digital

- Remove unused msg output port from Chunks To Symbols block yml

#### gr-fft

- Add "shift" parameter to Log Power FFT

#### gr-qtgui

- Fix: tags on the last sample were not shown

#### gr-video-sdl

- Fix: U and V channels were reversed on sink blocks

At LEAST the following authors contributed to this release.

- Adrien Michel <adriengit@users.noreply.github.com>
- David Winter <david.winter@analog.com>
- Emmanuel Blot <emmanuel.blot@free.fr>
- Håkon Vågsether <hauk142@gmail.com>
- Jared Dulmage <jared.dulmage@caliola.com>
- Jason Uher <jason.uher@jhuapl.edu>
- Jeff Long <willcode4@gmail.com>
- Marc L <marcll@vt.edu>
- Marcus Müller <mmueller@gnuradio.org>
- Martin Braun <martin@gnuradio.org>
- Ron Economos <w6rz@comcast.net>
- Volker Schroer
