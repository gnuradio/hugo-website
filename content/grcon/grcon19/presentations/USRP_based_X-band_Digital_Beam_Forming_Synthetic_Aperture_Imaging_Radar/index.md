---
type: "grcon/grcon19"
layout: "presentation"
title: "USRP based X-band Digital Beam Forming Synthetic Aperture Imaging Radar"
slides: "Peter Stenger - Synthetic Aperture Imaging Radar.pdf"
authors: ['Peter Stenger', 'Michael Blue', 'Marius Urdareanu', 'Grant Steans', 'Nathan Henry', 'Tyree Lewis']
youtube: ""
conference-day: Wednesday
weight: 11
---
A Universal Software Radio Peripheral (USRP) transceiver is investigated as a digital radar transceiver in an elemental digital beam forming (DBF) up/down converter scheme at X-band that images a scene spatially with signal time division multiplexing (TDM) implemented across multiple input-output (MIMO) transmit-receive elements. This forms a synthetic aperture radar (SAR) image of the scene with no moving parts. A wide instantaneous bandwidth (IBW) of 44.8 MHz is achieved with an Ettus Research B200 USRP that transmits and receives linear frequency modulated (LFM) pulses that are synchronized between two transmit antenna elements and eight receive antenna elements forming 16 virtual elements that resolve 1.17 degrees of spatial angular resolution across +/- 8.75 degrees of unambiguous field of view. A peripheral commercial Field Programmable Gate Array (FPGA) evaluation board is used to generate a one pulse per second (1PPS) timing signal to synchronize the USRP generated waveform with the RF switches that excite each transmit/receive virtual element. A commercial component based up/down converter front end extends the RF carrier frequency of the USRP to 10 GHz at each switched aperture element.
