---
type: "grcon/grcon18"
layout: "presentation"
title: "Using GNU Radio to do signal acquisition and analysis with Scopy"
authors: ["Adrian Suciu"]
slides: "3-Adrian_Suciu-signal_acquisition_with_Scopy.pdf"
youtube: "https://www.youtube.com/watch?v=aQfJV69IwdQ"
conference-day: "Tuesday"
weight: 3
---
GNU Radio is the go-to library when it comes to open source software-defined radio. However GNU Radio can go beyond that. In this paper we will discuss the use of GNU Radio as a base library for an end product application that requires general signal processing as well as other decoding libraries. Specifically, we will address how GNU Radio can be leveraged for applications beyond software defined radio and other communication systems.

In order to create Scopy - an open source mixed signal analysis and generation toolkit, we chose to use GNU Radio, along with a variety of open source libraries and frameworks such as libiio, libsigrok, Qt5 or Qwt. Scopy currently interfaces with the ADALM-2000 hardware which provides two analog input channels, two analog output channels, as well as 16 digital I/O pins - capable of high speed synchronized buffered operations. Future plans include extending Scopy to interface with other hardware.

Scopy uses libiio to interface with ADALM-2000. This allows Scopy to connect to the hardware via USB, as well as ethernet. By using an off the shelf (COTS)  Wi-Fi dongle, the hardware can connect to a wireless network and Scopy can acquire data remotely from the ADALM-2000.

GNU Radio is used in this context to multiplex the data streams received from the hardware via gr-iio to the oscilloscope/ spectrum analyzer/ network analyzer. GNU Radio's efficient vector-optimized operations are used to implement instrument functionalities such as the oscilloscope reference waveform, digital AC coupling as well as math channels. The network analyzer uses the GNU Radio flow to create a full network analyzer signal chain. Combined with the M2K hardware it is able to characterize circuits up to 30MHz and represent the results on Bode, Nichols and Nyquist plots. The spectrum analyzer allows marker operations as well as different types of windowing up to 50MHz. The signal generator uses GNU Radio to output various types of user configurable signals such as sine, square waves or the results of time-dependant mathematical equations.

We used GNU Radio for an end application that does not comply with the traditional scope of the framework. Although GNU Radio is well modularized, starting and stopping instruments has been one of the challenges we faced. Since there is no trivial way to reconfigure a GNU Radio flow, we had to develop a method that recursively deletes blocks starting with a parent. This and the use of the copy block eased up flow reconfiguration.

GNU Radio is a good fit for this application as it abstracts the complexities of signal acquisition and analysis into an efficient data flow giving us more headroom to develop a more user friendly, touchscreen compatible GUI.

### Background

The ADALM-2000 also known as M2k is a Software Defined Measurement Platform that is a cross platform (Windows, Mac and Linux) USB oscilloscope and multi-function instrument that allows users to measure, visualize, generate, record, and control mixed-signal circuits of all kinds. It features two-channel digital oscilloscope and arbitrary function generator, with Time, Network and Spectrum Analyzer views. A 16-channel digital logic analyzer and pattern generator, with a countless number of Bus Analyzers for all kind of protocols such as I2C, SPI, UART, CAN, JTAG, SPDIF, etc. just to mention a few. Besides this it also has true RMS voltmeters and programmable power supplies all in a pocket sized instrument.
