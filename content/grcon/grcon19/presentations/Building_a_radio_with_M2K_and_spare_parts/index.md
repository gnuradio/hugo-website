---
type: "grcon/grcon19"
layout: "presentation"
title: "Building a radio with M2K and spare parts"
slides: "Adrian Suciu - Building a radio with m2k and spare parts.pdf"
authors: ['Adrian Suciu']
youtube: ""
conference-day: Tuesday
weight: 9
---
The ADALM2000 (M2K) Active Learning Module is an affordable USB-powered measurement unit. With 12-bit ADCs and DACs running at 100 MSPS, the ADALM2000 enables electrical engineering students and hobbyists to explore signals and systems into the tens of MHz without the cost and bulk associated with traditional lab gear. The M2k, when coupled with Analog Devices' Scopy™ graphical application software running on a computer, provides the user high performance instrumentation such as oscilloscope, arbitrary function generator, spectrum analyzer, network analyzer and logic instruments.

However, the ADALM2000 can be coupled with another, more versatile tool, the libm2k. Libm2k is a C++ library which allows the user to interface with the ADALM2000 and create custom applications. Libm2k also provides Python3 and MATLAB bindings making capturing analog data, generating arbitrary waveforms or interacting with the digital signals easy. It’s high-speed dual ADC and DAC interfaces and the ability to power and control further digital and analog components makes it an ideal platform to directly interface with additional RF frontends, forming an additional IF stage or to be used as a direct conversion receiver, controlling filter banks, attenuators, gain blocks either by GPIO, I2C or SPI.  This presentation briefly introduces its capabilities and provides a number of examples how it can be utilized for various SDR applications.
