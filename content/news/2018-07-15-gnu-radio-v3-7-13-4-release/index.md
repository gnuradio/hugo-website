---
title: "GNU Radio v3.7.13.4 Release"
author: "Marcus Müller"
date: "2018-07-15"
sponsored: "0"
aliases: ["news/gnu-radio-v3-7-13-4-release"]
thumbnail: "gr_release"
---
Dear Community,

we've released a new version of our 3.7 maintenance line – 3.7.13.4.
Whilst this maintains binary compatibility with its predecessor, it
fixes build breakage on systems with boost 1.67, it fixes a bunch of
out-of-bound vector accesses (which on some systems triggered bug
safeguards which aborted the applications doing them), and it also
fixed a bug in how the "Skip Head" block deals with tags. Also, there
was a logging bug that we've fixed.

My thanks go out to all our contributors, but especially to Cate
Miller, Karel Pärlin and Paul wicks, all three first-time contributors
to a release. Thanks everyone for the great help!

You can find the release as tag v3.7.13.4 (make sure to verify the GPG
signature ;) ), on github under

https://github.com/gnuradio/gnuradio/releases/tag/v3.7.13.4

and

https://www.gnuradio.org/releases/gnuradio/

Happy hacking!
Marcus


## Contributors

* Andrej Rode <mail@andrejro.de>
* Cate Miller <cate@skysafe.io>
* Karel Pärlin <karelparlin@gmail.com>
* Marcus Müller <marcus@hostalia.de>
* Martin Braun <martin.braun@ettus.com>
* Paul Wicks <pwicks86@gmail.com>
* Sebastian Koslowski <sebastian.koslowski@gmail.com>

## [3.7.13.4] - 2018-07-15

### Fixed
#### Project Scope
- Fix Boost 1.67 linking issue
#### gnuradio-runtime
- Logging: fixed issues where messages weren't properly written to
stdout/stderr due to incorrect strings
#### gr-analog
- `fmdet_cf`'s derivative coefficients were wrong.
#### gr-blocks
- `skiphead` used to incorrectly handle tags, now properly shifts
#### gr-digital
- `qa_packet_format`: Unit test used to potentially lock up due to
incorrect conditionals
- `clock_recovery_cc`, `crc32_bb`: Accessing the `[0]` element of an
empty vector is UB, even if you don't use the result afterwards.
#### gr-fec
- `polar_encoder`/`_common`: Fixed multiple out-of-bound accesses due
to insufficient vector length checks
#### gr-filter
- `fft_filter`, `filter_delay`: Accessing the `[0]` element of an empty
vector is UB, even if you don't use the result afterwards.
