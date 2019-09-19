---
type: "grcon/grcon19"
layout: "presentation"
title: "Demonstration of GNU Radio Compatibility with a NASA Space Communications Network Modem (GRCON2019)"
slides: "David Miller -  NASA Space Communications Network Modem.pdf"
authors: ['David Miller']
youtube: ""
conference-day: Thursday
weight: 10
---
This paper presents the results of testing that the author recently conducted to demonstrate that a GNU Radio Software Defined Radio (SDR) receiver is compatible with a typical National Aeronautics and Space Administration (NASA) satellite ground station vendor modem and NASA waveforms within the scope of this initial testing phase. The author implemented the GNU Radio SDR receiver for this testing by installing the open source GNU Radio software on a Dell laptop and using a Commercial Off-The-Shelf (COTS) RTL-SDR hardware dongle. During the demonstration testing, the NASA vendor modem transmitted a repeating bit pattern to the GNU Radio SDR receiver using Binary Phase Shift Keying (BPSK) modulation for one test case and Quadrature Phase Shift Keying (QPSK) modulation for a second test case. The GNU Radio SDR received and demodulated the signal in order to recover the transmitted bit stream. This paper provides the specific GNU Radio SDR receiver design developed and implemented for this testing, the detailed demonstration test configurations, and the demonstration test results. This paper also concludes by listing many possible functions that the GNU Radio SDR could provide in a NASA satellite ground station. For example, NASA could employ the GNU Radio SDR as a mobile test unit tool in the ground station, as a modem in a test bed to develop and test possible new communication services waveforms, as an inexpensive intermediate frequency and baseband recorder, and even as an inexpensive backup spare modem for operations.
