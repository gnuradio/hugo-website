---
type: "grcon/grcon18"
layout: "presentation"
title: "GNU Radio and RFNoC in Space: How Hawkeye 360 uses GNU Radio on Small-Satellites"
authors: ["Edward Kreinar", "Dan CaJacob"]
slides: "11-EJ-GNURadio_in_Space.pdf"
youtube: ""
conference-day: "Wednesday"
weight: 11
---
Hawkeye 360 is launching a cluster of three small satellites to perform high-precision geolocation of RF emitters. In this talk, we'll discuss the architecture and use-cases of RFNoC and GNU Radio on a custom small-satellite payload with three AD9361 frontends and one Zynq 7045.

              Software signal processing applications are developed for the payload using GNU Radio; FPGA development uses RFNoC. In the end state, Hawkeye 360's software-defined radio has the capability to arbitrarily and asynchronously enable/disable software applications attached to different frontends, swapping in FPGA blocks as required by application.

              The ground-to-spacecraft data link is implemented using an FPGA-based OQPSK modem and Reed Solomon codec that were developed and tested first in software, second on COTS hardware, then finally ported seamlessly to our custom payload - We'll discuss the full life cycle of creating this OQPSK modem implementation in FPGA. Additional RFNoC applications are commonly used on the payload to perform high data-rate correlation, signal detection, and spectrum survey, with an emphasis on using the FPGA to intelligently downsample higher bandwidths than the Zynq's ARM can typically process in software (> 2 MHz or so). A raw collection application allows the Zynq to burst up to one second of contiguous 40 MHz sample-rate data to processor RAM before writing to disk. We look forward to our literal product launch when we will begin using the software in an orbital deployed environment.
