---
title: "GNU Radio 3.9.0.0"
author: "Marcus Müller"
date: "2021-01-17"
sponsored: "0"
aliases: ["news/3.9-release"]
categories: ["release"]
banner: gr_release_web.svg
---
# Release 3.9.0.0

The future is not set, there is no fate but what we make for ourselves. In this
very spirit, GNU Radio 3.9 packs a whole bunch of power when it comes to
transforming the way GNU Radio and its ecosytem can be developed in the future.

You'll find the release tags and signed tarballs now on
[github](https://github.com/gnuradio/gnuradio/releases/tag/v3.9.0.0), and later
on https://www.gnuradio.org/releases/gnuradio/.

Not only did we have great progressions from old dependencies that proved to be
all too problematic (SWIG, Python2), but also did we see an incredibly influx of
people actively working on how maintainable this code base is. This will nurture
the project for years to come.

All in all, the main breaking change for pure GRC users will consist in a few
changed blocks – an incredible feat, considering the amount of shift under the
hood. Mentioning large shifts, the work that went into the PyBind binding, the
CMake modernization, the C++ cleanup, the bug-fixing and the CI infrastructure
is worthy of explicit call out; I especially thank

* Josh Morman
* Thomas Habets
* Jacob Gilbert
* Andrej Rode
* Ryan Volz

here.

For developers of OOTs, I'm sure PyBind11 will pose a surprise. If you're used
to SWIG, yes, that's more code to write yourself. But in effect, it's less code
that breaks, and when it breaks, it breaks in much more understandable ways.
Josh has put a lot of effort into automating as much of that as possible.
There's certainly no shortage of demand for that! The ecosystem (remember GNU
Radio's tagline?) is in a steady upwind. We've seen more, and more stable,
contributions from OOT maintainers. That's great!

For in-tree development, newer dependencies and removal of anachronisms will
make sure things move much smoother. Our CI is getting – lately literally every
day – better, which means we not only catch bugs earlier, but also allow for
much quicker review cycles.

One central change:

If you're contributing code upstream, we no longer need you to submit a CLA;
instead, we ask you to just certify, yourself, that you're allowed to contribute
that code (and not, e.g. misappropriating someone else's code).

That's what the DCO (Developer Certificate of Origin) is: Just a quick, "hey,
this code is actually for me to contribute under the project's license"; nothing
more.

Which means that our infrastructure will refuse to let your code into the tree
if you didn't add a

`Signed-off-by: Maxime Example <maxime@example.com>`

to your commit message. Luckily, git can do that for you: `git commit -s`.

## Changed

### Project Scope

- **We now require commits to be signed off (DCO)**; this means you have to
attach `-s` to your `git commit` command line
- License headers now SPDX format
- C++14
 - use C++11 facilities in a lot of places where Boost was still used,
   especially smart pointers, range loops
 - lambdas where `boost::bind` was used
- C11
- Dependency versions:
  - Python 3.6.5
  - numpy 1.13.3
  - VOLK 2.4.1
  - CMake 3.10.2
  - Boost 1.65
  - Mako 1.0.7
  - PyBind11 2.4.3
- Compiler options:
  - GCC 8.3.0
  - Clang 11.0.0 / Apple Clang 1100
  - MSVC 1910 (Microsoft VS 2017 15.0)
- VOLK now "regular" dependency, not in-tree submodule
- numpy now also a CMake-checked hard dependency for Python support
- Exception Handling: throw by value, catch by reference (clang-tidy check)
- C++11: Emplace in vectors where you can; brings performance boni, but not
  included in clang-tidy-checks
- Further clang-tidy based code optimizations:
- empty() instead of size() == 0
- override where overriding virtual functions (which we do a lot)
- Logging: removed all `std::cerr` and `fprintf(stderr,…)` by GNU Radio logging
- Logging: Changed logging format for many multiline error logs
- purged `snprintf`, `printf` logging
- There were a lot of places where a malloc'ed object was used internally, where
  that was inappropriate. Using simple instance-holding fields now.
- `const` for members that were only set at construction time is now desired,
  and implemented in most places
- `const` -> `constexp` in a lot of places.
- `assert` -> `static_assert`
- An exception-throwing block will now terminate the flow graph process,
  configurable through `top_block`
- `gr-utils` cleanup, folder restructuring
- config version checks installed CMake file will accept "at least this version"
  now
- PyBind11 replaces SWIG
  - Full tree conversion from SWIG to Pybind11 bindings
- Doxygen now uses MathJax, full LaTeX installation no longer required

**NOTE**: Most of the changes above change the generally preferred coding style
in a lot of situations.

### GRC

- start flowgraph in folder where it resides

### gnuradio-runtime

- When calculating offsets in non-integer rate FEC, `lround`
- default seed for `gr::random` now actually as documented time-dependent
- loggers moved from `gr::block` to `gr::basic_block`
- PMT serialization
- PMT dicts no longer indistinguishable from pairs
- PMT symbol hashing no longer suffers under oddball own implementations

### gr-audio

- Increased ALSA buffer nperiods

### gr-blocks

- `add`, `add_const` VOLK'ized, templated
  - this seems to break things in other places, even if it proves to be
    mathematically identical
- `wavfile` infrastructure: `libsndfile` now dependency

### gr-digital

- `transcendental` block: default to 32 bit float complex, not double
- Linear equalizer: separate adaptive algorithm, allows for using e.g. trained
  sequences instead of the classical LMS, CMA
- DFE: better structure for decision history

### gr-dtv

- LDPC encoder: template functions instead of `#define`d macros
- LDPC encoder: smaller tables through `uint16_t` for index tables

### gr-fec

- API `uint8_t`, not `char`

### gr-fft

- FFT blocks/functions templatized

### gr-filter

- logging format
- `rational_resampler_base` -> `rational_resampler`

### gr-uhd

- Required UHD version bumped to 3.9.7
- logging format

## Deprecated

### gr-analog

- `sig_source`: `freq` port will be removed in the future

### gr-audio

- `audio-sink`, `-source`: Windows audio sink/source deprecated, the portaudio
sink/source works even better under windows anyway

### gr-digital

- In favor of `symbol_sync`, deprecate:
  - `clock_recovery_mm`
  - `msk_timing_recovery`
  - `pfb_clock_sync`

## Added

### Project Scope

- C++ Generation all over the place
- PyBind bindings + generator
- Github actions
- Reproducible builds-compatible CMake TIMESTAMP

### gnuradio-runtime

- `block_gateway`: `set_max_output_buffer`
- `GR_PREFS_PATH` environment variable sensitivity to configure the path to the
  config file
- `gnuradio-config-info --print-all`

### GRC

- option to toggle ID visibilities globally
- Validation check for QT GUI hints
- Python snippets

### block header parsing tool

- block header parsing tool (GSoC 2019)

### gr_modtool

- option to convert blacklisted files

### gr-analog

- `sig_source`: `cmd` port adds support for dicts, setting of frequency,
amplitude, offset and phase parameters

### gr-blocks

- `selector` now has control message ports
- Rotator-based freq shift convenience wrapper
- Message-to-Variable and vice versa blocks
- DC Spike removal
- IQ Swap
- Complex to interleaved char / short: scaling option
- Delay block: control message port
- Phase Shift block with message port
- `wavfile_sink`, `_source` can now deal with a lot of audio formats:
  uncompressed WAV/AIFF, µ- and A-law compressed audio, OGG/Vorbis, FLAC, even
  octave files
- Stream Demux, which demuxes streams according to lengths vector
- `rotator`: `phase()` getter

### gr-digital

- OFDM: multiple CP lengths
- `ofdm_equalizer_simpledfe`: `enable_soft_output`
- Constellation Encoder
- Constellation: normalization options

### gr-fec

- `{en,de}code_rs_8`, `{en,de}code_rs_ccsds`: Reed-Solomon en- and decoders

### gr-fft

- Windows:
  - Gaussian
  - Flat Top
  - Tukey
- Window build() call now with default beta

### gr-filter

- GRC: File taps loader block
- Low pass FFT filter convenience wrapper
- ichar / ishort decimator
- phase continuity for `freq_xlating_fir_filter`

### gr-network

- `gr-network`: a whole new networking blocks module!
  - TCP
  - UDP
- Much better lockup/multithreading support than 3.7-era `blks2` nightmare
  infrastructure :)


### gr-qtgui

- Azimuth/Elevation plot
- Autocorrelation plot
- Compass visualization
- Dial control
- Gauge: dial, level
- Distance plot
- LED-like indicator
- Message-passing check box
- Message-passing numeric control
- Message-passing push button
- Toggle Button
- Eye sink
- Vertical slider

### gr-uhd

- Filter API
- UHD 4.0 support
- Power Reference API
- Bidirectional setting messages on both sink, source

### gr-vocoder

- Codec2 dev branch support
- FreeDV: In/output rates can differ
- FreeDV: text message output

### gr-zeromq

- C++ GRC templates
- Tag filtering for tag-forwarding blocks

## Removed

### Project Scope

- VOLK is no longer a submodule
- Sphinx: consolidate into doxygen, or wiki-maintained block list.
- Python 2
- SWIG
- `gru` python module

### gnuradio-runtime

- `circular_file.cc`
- `math/common_factor.hpp`

### gr-blocks

- `bin_statistics_f`
- `log2_const`

### gr-digital

- PFB clock sync: `set_taps`
- deprecated old OFDM infrastructur
  - `ofdm_frame_acquisition`
  - `ofdm_frame_sink`
  - `ofdm_insert_preamble`
  - `ofdm_sync_fixed`
  - `ofdm_sync_pn`
  - `ofdm_sync_pnac`
  - `ofdm_sync_ml`
  - `ofdm_receiver`
- `digital_voice`

### gr-fft

- `malloc_float`, `_double`: rely on VOLK
- Goertzel: dtor superfluous

### gr-filter

- deprecated window function duplicates (use them from gr-fft!)

## Fixed

### Project Scope

- CMake: Qwt, Log4Cpp detection
- ctrlport strings unicodified
- Freedesktop install script was not executed
- Redundant icons installed
- Path substitution on Windows was backslash-broken
- YAML definitions: more than I can count
- Cross-building: py interpreter at runtime != build time

### gnuradio-runtime

- ctrlport: unholy stored reference to stack-allocated object removed
- Sine table generation for fixed point math
- `gr_unittest`: `floatAlmostEqual` had a lot of false passes due abuse of
  `all()`
- `get_tags_in_range` for `delay < (end-start)`
- Premature tag pruning
- release flattened flowgraph after stopping, fixes restartability/shutdown
  problem
- PMT serialization portability
- latency issue caused by setting block alias on msg block
- Windows logging errors
- ctrlport: Thrift >= 0.13 broke

### GRC

- Tab widget ID visibilities
- A lot of YAML templates
- Default setting in qtgui chooser restored
- Boolean parameters no longer switch buttons
- Nested namespace handling
- Don't rely on set ordering in tests
- configparser import
- input box color theme on dark themes
- Search box typing doesn't inadvertedly interact with the rest of GRC anymore

### gr_modtool

- Empty argument lists allowed
- Boost UTF replaced CppUnit, this needed to be done here, too

### gr-analog

- `wfm` left/right, filters

### gr-audio

- portaudio: lock acquisition was improper

### gr-blocks

- Throttle now uses monotonic clock
- Tag debug only saved last `work` call's tags
- File sink flushes on `stop`
- `gr_read_file_metadata.py` used to lose `rx_time` precision
- File source big file handling under Windows
- `file_*`: `fseek` errors used to be ignored

### gr-digital

- `map_bb`: thread safety, buffer overflows
- `additive_scrambler`: reset was broken
- Constellation scalefactor wasn't always initialized
- long-standing `qa_header_payload_demux` bug addressed by waiting for both RX
  and TX, not only either
- false triggers in `correlate_access_code`

### gr-dtv

- rate mismatch in ATSC flowgraphs

### gr-fec

- `async_decoder` Heap corruption
- `cc_encoder`: constraint length K > 8 led to wrong output

### gr-fft

- thread safety of copy assignment/ctor
- log power FFT Python

### gr-filter

- `variable_band_pass_filter` GRC complex taps input
- RRC filter gain for alpha = 1

### gr-qtgui

- Remove copies of image data in returns by using move semantics
- Remove bogus overriding in drawing functions of `plot_raster`, `_waterfall`
- Edit MSG box: don't require key to be set
- Don't check for Python2 libs
- Number Sink ignored averaging setting

### gr-uhd

- UHD apps: Py3 fixes
- USRP blocks: multichannel objects not properly populating channels

### gr-video-sdl

- YUV formats fixed

### gr-zeromq

- Don't depend on deprecated ZMQ functionality (fix warnings, include what you
  use)
- Unhandled exceptions now handled, much calmer
- Avoid infinite blocking in `tb.stop()` by using `ZMQ_LINGER`

# Contributors

* Adrien Michel
* Alba Mendez <me@alba.sh>
* Alekh Gupta <alekhgupta1441@gmail.com>
* A. Maitland Bottoms <bottoms@debian.org>
* Anders Kalør <anders@kaloer.com>
* Andrej Rode <mail@andrejro.de>
* Andriy Gelman <andriy.gelman@gmail.com>
* Antetokounpo <antor.232@outlook.com>
* Arpit Gupta <guptarpit1997@gmail.com>
* Artem Pisarenko <artem.k.pisarenko@gmail.com>
* arualok22 <arualok22@gmail.com>
* Bastian Bloessl <mail@bastibl.net>
* Behnam Sabaghi <behnamsabaghi@gmail.com>
* Brennan Ashton <bashton@brennanashton.com>
* Brett Gottula <brett@astranis.com>
* Chris Donohue <christopher.donohue@gmail.com>
* Chris Mayo <aklhfex@gmail.com>
* Christophe Seguinot <christophe.seguinot@univ-lille.fr>
* Clayton Smith <argilo@gmail.com>
* CMorin <barthy42@laposte.net>
* Daniel Estévez <daniel@destevez.net>
* Davide Gerhard <rainbow@irh.it>
* David Pi <david.pinho@gmail.com>
* Derek Kozel <derek@bitstovolts.com>
* devnulling
* Doron Behar <doron.behar@gmail.com>
* duggabe <barry@dcsmail.net>
* Eduardo Sánchez Muñoz <esm@eduardosm.net>
* efardin <efardin@ieee.org>
* elms <elms@freshred.net>
* Emmanuel Blot <emmanuel.blot@free.fr>
* ewxl <elof@wecksell.se>
* Fabian P. Schmidt <kerel@mailbox.org>
* gateship1 <mg3676@drexel.edu>
* ghostop14 <ghostop14@gmail.com>
* Glenn Richardson <glenn.richardson@live.com>
* Grant Cox <grant.cox@deepspaceamps.com>
* Gwenhael Goavec-Merou <gwenhael.goavec-merou@trabucayre.com>
* Håkon Vågsether <haakonsv@gmail.com>
* Huang Rui <vowstar@gmail.com>
* Hugh Pyle <hpyle@cabezal.com>
* Igor Freire <igor@blockstream.com>
* Ilya Tagunov <tagunil@gmail.com>
* Jacob Gilbert <mrjacobagilbert@gmail.com>
* Jan Kraemer <kraemer.jn@gmail.com>
* japm48
* Jay Kamat <jaygkamat@gmail.com>
* Jeff Long <willcode4@gmail.com>
* Johannes Demel <demel@ant.uni-bremen.de>
* Johannes K Becker <jkbecker@bu.edu>
* Josh Morman <jmorman@perspectalabs.com>
* karel
* kc1212
* luzpaz
* Marc L <marcll@vt.edu>
* Marcus Müller <mmueller@gnuradio.org> <mueller@kit.edu>
* Martin Braun <martin.braun@ettus.com> <martin@gnuradio.org>
* Mathias Rasmussen <mathiasvr@gmail.com>
* Matt Mills <mmills@2bn.net>
* Maximilian Stiefel <stiefel.maximilian@online.de>
* Michael Byers <ByersJR.Michael@gmail.com>
* Michael Dickens <michael.dickens@ettus.com>
* Michael Roe <mroe@cornstalk.org.uk>
* Mike Walters <mike@flomp.net>
* Nathan West <nwest@deepsig.io>
* Nicholas Corgan <n.corgan@gmail.com>
* Nick Østergaard <oe.nick@gmail.com>
* Nicolas Cuervo <cuervonicolas@gmail.com>
* Notou <barthy42@laposte.net>
* Oleksandr Kravchuk <open.source@oleksandr-kravchuk.com>
* Oliver
* Paul Boven <p.boven@xs4all.nl>
* Paul Wicks <pwicks86@gmail.com>
* Philip Balister <philip@balister.org>
* rear1019 <rear1019@posteo.de>
* RedStone002
* Ron Economos <w6rz@comcast.net>
* Ryan Govostes
* Ryan Schutt
* Ryan Volz <rvolz@mit.edu>
* Scott Torborg <storborg@gmail.com>
* Sebastian Koslowski <sebastian.koslowski@gmail.com>
* Sebastian Müller <gsenpo@gmail.com>
* Sebastian Olsen <sebastian.olsen@aero.org>
* Seeker <meaningseeking@protonmail.com>
* sidkapoor97 <16ec142siddharth@nitk.edu.in>
* Stefan `Sec` Zehl <sec@42.org>
* Swapnil Negi <swapnil.negi09@gmail.com>
* Sylvain Munaut <tnt@246tNt.com>
* Terry May <terrydmay@gmail.com>
* Thomas Habets <thomas@habets.se> <habets@google.com>
* Valerii Zapodovnikov <val.zapod.vz@gmail.com>
* Vasil Velichkov <vvvelichkov@gmail.com>
* Volker Schroer
* wcampbell <wcampbell1995@gmail.com>
* William Barnhart <williambbarnhart@gmail.com>
* Yamakaja <dastw@gmx.net>
* Zackery Spytz <zspytz@gmail.com>
