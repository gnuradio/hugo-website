---
type: "grcon/grcon19"
layout: "presentation"
title: "Mega Hertz, Mega Samples, Mega bits, Mega Confusing"
slides: "noslides"
authors: ['Robin Getz']
youtube: "novideo"
conference-day: Monday
weight: 8
---
In this presentation we will review and discuss the data paths between the RF (air interface) and the payload (the data interface), and the common and overloaded terms and units throughout the chain, and how they are used/abused, using a few different examples – Single Side Band (SSB), Frequency Shift Keying (FSK), single carrier Quadrature Phase Shift Keying (QPSK), multi carrier Orthogonal Frequency-Division Multiplexing (OFDM) - and what the introduction of advanced topics like Digital Pre-Distortion (DPD) and JESD204 means. Confusing terms like occupied RF bandwidth, synthesized RF bandwidth, single side bandwidth, Samples per second (with respect to converters), interpolation and decimation, samples per second (with respect to interface), symbols per second, bits per second, payload overhead, to bytes per second will all be explained with examples.

This discussion will be kept generic to all zero IF radios, and is applicable to all sorts of devices from the RTL-SDR, to the Analog Devices ADALM-PLUTO to the Naund bladeRF 2.0 to the National Instruments B200 and B210 family of devices.