---
type: "grcon/grcon19"
layout: "presentation"
title: "Fixing the E310 Bottleneck: Implementing a High-Rate Heterogeneous FPGA DMA Transport"
slides: "EJ Kreinar - GRCon2019-HE360-Heterogenous-DMAs-Kreinar-Metzger-CaJacob.pdf"
authors: ['Edward Kreinar', 'Lorin Metzger', 'Dan CaJacob']
youtube: ""
conference-day: Monday
weight: 8
---
FPGAs are a common solution when accelerating software defined radio processing in an embedded form factor, but several implementation-specific limitations need to be addressed in order to take full advantage of today’s heterogeneous processing capabilities. Case in point: Ettus’s E310 embedded family of devices, a Zynq-based architecture, struggles to transfer an uninterrupted stream of 2 Msps between the FPGA and a Gnuradio application running in the Zynq’s ARM-based processor. As a counter example, Analog Devices’s “libiio” family of software, which is compatible with Zynq and Altera SoCs, is able to transfer the full rate of multichannel (2x) TX/RX streaming data at 61.44 Msps between FPGA and host processor. In an effort to build FPGA-based applications within RFNoC, Hawkeye 360 has explored the limitations, causes, and potential resolutions to the E310’s relatively poor FPGA/ARM transport performance, and in doing so, has created an alternate transport for the E310 hardware which achieves full-rate data transfers between FPGA and ARM.

This talk will first discuss the observed limitations of the E310 performance bottleneck; when can the existing embedded E310 transport be used “as-is”? Secondly, the talk will summarize common software and hardware paradigms for direct memory access (DMA) transport between FPGA and host in a SoC architecture, and identify the root cause of poor performance; why does the libiio architecture perform an order of magnitude better than the E310 solution? Finally, Hawkeye 360 will discuss a “do it yourself” approach, whereby a Xilinx DMA core plus a custom kernel module optimized for high-rate data transfers can sustain continuous and bursted data transfers into Gnuradio applications within a heterogenous RFNoC flowgraph.
