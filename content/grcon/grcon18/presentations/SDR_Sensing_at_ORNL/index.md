---
type: "grcon/grcon18"
layout: "presentation"
title: "Application of Software Radios for Sensing and Instrumentation at Oak Ridge National Laboratory"
authors: ["James Humphries"]
draft: true
slides: "4-James-Humphries-SDR_Sensing_at_ORNL.pdf"
youtube: ""
conference-day: "Monday"
weight: 4
---
In the Sensors & Embedded Systems Group at Oak Ridge National Laboratory (ORNL), we are exploring various sensing and instrumentation applications using software defined radio (SDR). SDR has been utilized for both wireless surface acoustic wave (SAW) sensor interrogation as well as measurement of carbon fiber tow properties during fabrication. While vector network analyzers (VNA) could be used for each application, they are much too expensive and not robust enough to be deployed in the field. A conventional hardware radio composed of commercial-off-the-shelf (COTS) components could also be used, but these tend to be difficult to fine-tune and don't offer much adaptability. SDR, on the other hand, can offer comparable performance to a VNA or conventional hardware radio and can be easily adapted for a given application.

There has been great interest in the development of passive, wireless SAW sensors for electrical grid, nuclear energy, and national security applications. With this, there is a push for small, low-cost, high-performance wireless systems that can remotely interrogate the sensors. At ORNL we have developed an interrogation system based on noise RADAR techniques that utilizes the USRP B200mini, an UDOO x86 embedded computing platform, and a custom designed RF daughterboard. The system is currently being used to test a variety of SAW sensors for temperature, methane, and HF gas detection.

The Carbon Fiber Technology Facility (CFTF) at ORNL is exploring systems that can probe carbon fiber tow in production without physical contact. The goal is to be able to provide near-instantaneous process control feedback instead of waiting for physical analysis of the tow after it has completed the entire fabrication process. We have developed an USRP B200 based system, which mimics a scalar network analyzer, to transmit microwave frequency signals through the carbon fiber as a measure of resistivity. Current results have shown good correlation between the SDR resistivity measurements and measurement obtained from physical analysis of the tow.


Current results for each system will be discussed along with plans for further testing and integration for their respective applications.
