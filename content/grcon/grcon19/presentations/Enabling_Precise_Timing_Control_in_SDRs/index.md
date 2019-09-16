---
type: "grcon/grcon19"
layout: "presentation"
title: "Enabling Precise Timing Control in SDRs"
slides: "noslides"
authors: ['Srikanth Pagadarai']
youtube: "novideo"
conference-day: Thursday
weight: 8
---
The necessity to estimate loopback timing delay of a waveform arises as a pre-requisite in a variety of signal processing applications namely, power amplifier digital predistortion, radar and radio frequency identification (RFID). In this presentation, we will present the architectural details that need to be considered for implementing a loopback timing delay estimation algorithm in the FPGA of an SDR. 

Using digital predistortion (DPD) as a motivating example, we will present the design decisions to be considered when allocating the various intermediate operations such as correlation, interpolation, alignment, control etc. to the programmable logic (PL) and processing system (PS) of a standard SoC. Along the way, we will present the theoretical principles of the underlying integer and fractional delay estimation algorithms that encourage such an allocation. Finally, we will demonstrate how this solution can be seamlessly integrated into any custom DPD application that relies on the reference and the observation waveforms to be accurately aligned in time for reliable model extraction. We will use AD9361 as the RF front-end and gr-iio as the software tool to interact with the IP. In summary, the emphasis of this presentation is on the general framework that comprises the implementation of loopback timing delay estimation and correction.