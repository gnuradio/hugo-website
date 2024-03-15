---
title: "GNU Radio 3.10.7.0"
author: "Marcus Müller"
date: "2023-07-19"
sponsored: "0"
aliases: ["news/3.10.7.0-release"]
categories: ["release"]
banner: gr_release_web.svg
---
# Release 3.10.7.0 & Others

We haven't done a release announcement in a while, but there's been several releases. On the 3.9 release series, we've bumped versions up to 3.9.8.0.

But more importantly, the 3.10 series is getting very mature: see the latest release notes below.

If you're using Ubuntu 20.04LTS or 23.04, a simple 

```
sudo add-apt-repository ppa:gnuradio/gnuradio-releases
sudo apt-get update
sudo apt-get install gnuradio python3-packaging
```

should get you our binary build. (But warning, that might break all the out-of-tree modules you manually built against your older GNU Radio!)

We'll probably see a *radioconda* release later, so that installation on other platforms, including Windows and MacOS (both x86 and Apple Silicon) also becomes rather smooth.

Generally, up-to-date information on installing GNU Radio can be found on the [Installing GNU Radio](https://wiki.gnuradio.org/index.php?title=InstallingGR#Quick_Start) page on the wiki.

# Release notes

## [3.10.7.0] - 2023-07-15

### Changed

#### Runtime
- Setting the minimum buffer size should have the desired effect now, and
not be overwritten. NOTE: `the value returned by min_buffer_size()` is not
intended to indicate the actual buffer size. Header Payload Demod was the
only block attempting to use this value, and was corrected.
- Use a set to store thread group (more efficient)
- Message Debug can now output via the logging system
- The field `prefs.singleton` is no longer externally exposed (was unintentional)
- PMT dict can be generated more easily using `pmt::dict_from_mapping()`

#### GRC
- Save changes under all exit conditions (a couple were previously missed)
- Prevent silent Generate/Run failures for unsaved flowgraphs

#### Testing
- Add Fedora 38, using the clang compiler
- Remove EOL Fedora 36

#### gr-analog
- C++ code generation for Quadrature Demod
- Add max_gain parameter for AGC

#### gr-blocks
- Probe Rate adds a name parameter, for clearer logging
- Selector has a new "sync" more that consumes the same number of items from all
inputs. Default is now to consume as many items as possible from the active input,
and no more than that many items from other inputs. The previous behavior was, well,
broken.
- Throttle reset item count on restart, to avoid long delays

#### gr-digital
- Constellation Encoder and Decoder: constellation can be changed at runtime

#### gr-filter
- Filter design tool: multiple improvements in bounds checking and exception handling
- Filter design tool: update QMessageBox to work in Qt5

#### gr-network
- Multiple memory management errors fixed in UDP Source/Sink and TCP Sink


#### gr-soapy
- Better AGC and gain behavior in RTL, AirspyHF and SDRPlay blocks
- Support bias controls in RTL and SDRPlay blocks

#### gr-uhd
- Remove possibility of infinite recursion for network overruns
- Support fmtlib v10
- RFNoC: bindings and block yml for Vector IIR, Replay and Log Power blocks
- RFNoC: add S16 format to RX Streamer

#### gr-vocoder
- Support additional codec2 modes

#### Modtool
- Don't override user-defined `CMAKE_INSTALL_PREFIX`


## [3.10.6.0] - 2023-03-31

### Changed

#### Runtime
- Add Python loggers to top_block and hier_block2
- Change the default log level (in the config file) to INFO instead of DEBUG
- Logging improvements in the scheduler
- Correctly determine native page size for Windows

#### GRC
- Fixed: opening the source of a hierachical block using the toolbar button produced an error
- Use the logger, instead of print statements, in generated top blocks
- Remove libX11 load from generated Python code - this was unncessary and produced warnings
- Choose Editor dialog stays above parent

#### gr-analog
- Signal Source: option to hide the message port

#### gr-blocks
- Throttle: supports max time or number of samples per work iteration, useful for reducing latency at low sample rates
- Delay block: option to hide the message port
- File Meta Sink: fix missing Python import in template code

#### gr-channels
- Default taps should be 1.0, not 1.0 + j1.0

#### gr-digital
- Async Decoder: several changes to improve performance robustness (see the commit log for more details)

#### gr-fec
- Tagged Decoder: correctly calculate the frame size for terminated CC decoder

#### gr-filter
- Fixed reverse parameters in fir_filter_with_buffer and pfb_arb_resampler, which could cause crashes
- Fixed PFB Arbitrary Resampler was ignoring attenuation parameter

#### gr-iio
- Set gain mode as specified (was always manual)
- Use the specified gain parameter for second channel (was same as first channel)

#### gr-qtgui
- Histogram Sink: calculate range of bins correctly to avoid strange distributions
- Save (to image) dialogs add file extensions and have a Save button (i.e., they work now)

#### gr-soapy
- Sources: add tags when the frequency changes

#### gr-uhd
- Support for more RFNoC blocks
  - Fosphor, which produces data to drive an on-screen, OpenGL-based renderer which is expected to be in the next release
  - Moving Average
  - Switchboard
  - Split Stream
- FFT: add properties for direction, magnitude and scaling
- RX Stream: flush after timeout
- Fully support multi-channel TX/RX (params were available for one one channel)

#### gr-vocoder
- Add a number of new codec modes for Codec2 and FreeDV

#### gr-zmq
- Selectable bind/connect to support more flexible ZMQ patterns and NAT'd networks
- Stream sources produce when available, instead of waiting for a buffer to fill, helping with latency

#### Modtool
- Use interp and decim keywords correctly when generating blocks

#### Build system and packaging
- Uninstall removes icons and desktop files


## [3.10.5.1] - 2023-01-25

Some important blocks turned out to be broken in 3.10.5.0. This unscheduled release fixes those regressions and includes a small number of other cleanups and fixes. v3.10.5.1 is intended to be ABI compatible with v3.10.5.0. We'd still recommend rebuilding dependent packages, if possible.

### Changed

#### Runtime
- Restore the ability to set a default block buffer size using the `buffer_size` parameter in the config file. This was lost during refactoring in v3.9.

#### GRC
- Add Python snipped hook point at "init before blocks", right before blocks are instantiated.

#### gr-audio
- Remove support for OSX 10.3 and earlier.

#### gr-digital
- Make tags visible to subclasses of OFDM Frame Equalizer.

#### gr-dtv
- Correct constant in DVBS2 Modulator.

#### gr-fec
- Fix errors in Channel Construction AWGN

#### gr-iio
- Fix IIO blocks, which were broken due to a build-time dependency problem.

#### gr-network
- Fix crash in UDP Source when buffer overruns.

#### gr-qtgui
- Remove support for QWT 6.0 and earlier.

#### gr-uhd
- Add async message port to USRP Source and publish overflow notifications.
- Add bindings and example for RFNoC AddSub block.

## [3.10.5.0] - 2022-12-19

### Changed

#### Runtime
- Python block have access to the block logger, as in C++
- Default log level changed to INFO (from OFF)
- Memory-based logger `gr.dictionary_logger_backend()` added for log debugging
- API Note: The Python block gateway is now completely implemented in the PyBind11 wrapper, in order to clean up Python dependencies. This is technically an API change, but should not have any external effect.
- PMT serialization of Complex32 vectors is now `REAL | IMAG` on all platforms
- Python IO signature replication (multiple ports specified by one signature) fixed

#### GRC
- Continue processing block connections after a connection error occurs
- Drawing/scaling fixes that improve user experience on HiDPI and Windows machines

#### Build system and packaging
- Many deprecation warnings fixed
- Make target link libraries PRIVATE wherever possible, removing unnecessary downstream dependencies
- Add Fedora 37 and drop Fedora 35 CI targets
- Conda re-rendered with more recent packages - thanks to Ryan Volz for making Conda an easy-to-use, cross-platform method of installing GNU Radio
- Debian and Fedora packaging specs are no longer included in the code base, since they were out of date, and are maintained by downstreams

#### Testing
- Code formatting rules for clang format updated to v14
- Removed all compiler warning suppression
- Enable Python block testing for Conda on macOS
- Many other improvements that make maintenance easier - thanks again to Clayton Smith. In the process of fixing tests, a number of latent bugs were fixed throughout the code.

#### gr-analog
- AGC3 performance and bug fixes
- Python has access to `control_loop` parent class in PLL blocks
- CTCSS detection of standard tones improved by fixing floating point comparison

#### gr-blocks
- Probe Signal cross platform reliability improved by better thread synchronization

#### gr-digital
- CRC32 and CRC16 blocks use little-endian order regardless of host order. This is a wire format change. The options were to have different endian machines unable to communicate, or older and newer versions unable to communicate. Note that there is a more general set of blocks (CRC Append and CRC Check) that are recommended for use wherever possible.
- Packet headers use consistent bit order across machines
- Floating point/rounding fix in constellation lookup table

#### gr-fec
- LDPC G matrix `n` and `k` can be access from Python
- LDPC matrix output size calculation corrected
- CCSDS/Viterbi path metrics overflow fix

#### gr-network
- Improve UDP Source/Sink efficiency by removing a layer of buffering and using the GR circular buffer instead of the Boost equivalent

#### gr-qtgui
- Fixed Python code generation for Msg CheckBox, Digital Number Control, Toggle Button, Toggle Switch

#### gr-soapy
- Sources will generate `rx_time`, `rx_freq` and `rx_rate` tags, as in UHD sources, where supported by the underlying Soapy driver

#### gr-uhd
- Re-enable `uhd.find_devices()`, in addition to `uhd.find()`
- RFNoC: generate correct Python code when using clock/time source
- RFNoC: allow specification of adapter IDs for streamers
- RFNoC: enable setting of vlen and types for streamers
- RFNoC: streamers pay attention to stream args
- RFNoC: sync block controller with gr-ettus OOT
- RFNoC:`set_property()` and `get_property()` added to the C++ and Python APIs
- RFNoC: Python binds added for `rfnoc_block_generic`

#### gr-zeromq
- Sinks will optionally block on full queue, providing backpressure. Previously, overflow data was dropped.

## [3.10.4.0] - 2022-09-16

### Changed

#### Project Scope
- Replace `get_initial_sptr()` calls with `make_block_sptr()` calls. There were a number of places the incorrect function was being used.

#### Runtime
- Use correctly typed arguments to log messages to prevent build errors.

#### GRC
- Add xfce4-terminal and urxvt to the list of terminal emulators discovered during the build process.
- Suppress GUI hint errors that were being shown in the terminal window.
- Use integers for screenshot size (floats were causing Cairo errors).

#### Build system and packaging
- Reformat cmake files and make cmake formatting part of the workflow.
- Allow GNU Radio to be a part of other cmake-based projects.
- Correct linking to libiio and libad9361 on macOS.
- Update method for determining Python installation directory. This should work correctly now on (all?) distro releases.

#### gr-blocks
- New Block Interleaver/Deinterleaver interleaves blocks of symbols
- Correct calculation of `items_remaining` in File Source, which allows `seek()` to work correctly.
- Add an example for Wavefile Sink

#### gr-digital
- Deprecate the CRC32 and CRC16 blocks, which will be removed in the future. There are more general CRC blocks which do the same thing (and more).

#### gr-filter
- Fix demo for PFB channelizer

#### gr-iio
- FMCOMMS2 Sink assumes CS16 data is scaled to 32768, rather than 2048.
- FMCOMMS2 returns the correct samples for the second channel in 2-channel mode.

#### gr-trellis
- Correct Python bindings for `trellis::metrics`.

#### gr-qtgui
- Range widget can now output messages when value changes.
- Add C++ code generation for Time Sink
- Regenerate Python bindings for some blocks when necessary.
- Waterfall Sink correctly uses half spectrum for float input.

#### gr-uhd
- Add Python bindings for the UHD `find()` functino.

#### gr-zeromq
- Support newer `get()` and older/deprecated `getsockopt()` functions in cppzmq depending on availability.

#### Modtool
- Parse IO signatures with or without `gr::` prefix.

#### Documentation

- Update certain file lists to keep build paths out of documentation.

#### Testing
- Update Conda recipe for Qt 5.15 and re-render CI support files.
- Add testing on Ubuntu 22.04.
- Link tests directly against spdlog with not linking to GR runtime.
- Ignore Python "missing whitespace after keywork" formatting error.

## [3.10.3.0] - 2022-06-09

### Changed

#### Project Scope

- Continue replacement of Boost functionality with standard C++ continues, where practical, making the code more maintainable.
- Fix more flaky CI tests that were failing unnecessarily. This helps greatly with maintenance.

#### gnuradio-runtime
- Only catch Thrift transport exceptions
- Import PyQt5 before matplotlib to work around a bug
- Fix broken log format string in set_min_output_buffer
- Process system messages before others. This helps with orderly flowgraph termination.
- Custom buffers: add missing (simulated) data transfer to input/output_blocked_callback functions in host_buffer class
- Fix Mach-kernel timebase (numer and denom were reversed)
- Fix signed integer overflows in fixed-point table generation

#### GRC
- Add parentheses on arithmetic expressions to avoid operator precedence problems in templated code
- Fix create hier / missing top_block error

#### Build system and packaging
- CI: Add testing for Fedora 36, remove Fedora 34.
- cmake: Use platform-specific Python install schemes
- cmake: Always prefix git hash used as version with "g"
- cmake: Allow MPIR/MPLIB package find to fail gracefully
- cmake: Remove 'REQUIRED' flag for Volk

#### gr-blocks
- Fix rotator_cc scheduled phase increment updates
- Wavefile Sink: add support for Ogg Opus if libsndfile is >= 1.0.29
- Probe Signal: synchronize access to d_level to prevent race conditions

#### gr-digital
- Use memcmp for CRC comparisons to avoid alignment errors

#### gr-dtv
- Use unsigned integer for CRC calculation
- Fix use of uninitialized memory
- Fix initialization of L1Post struct

#### gr-filter
- Fix various bugs in Generic Filterbank

#### gr-iio
- Fix grc pluto sink attenuation callback

#### gr-qtgui
- Several sinks produce wrong error messages, when GUI Hint is used. Reorder params in yml files to fix.

#### gr-soapy
- Deactivate stream before closing. Some modules depend on this behavior.

#### gr-uhd
- Implement `get_gpio_attr()`

#### Code generation tools
- C++ generation: Fix various template errors

#### Modtool
- gr_newmod: Fix copying python bindings to test dir on Windows
- gr_newmod: Make untagged conda package version less specific
- modtool: Add a conda recipe to the OOT template
- Make the pydoc_h.mako more clang compliant

#### Documentation
- Add shim Sphinx config for readthedocs

