---
type: "grcon/grcon19"
layout: "presentation"
title: "Determining Optimized Radio settings for specific waveforms"
slides: "noslides"
authors: ['Robin Getz']
youtube: "novideo"
conference-day: Monday
weight: 8
---
In the book The Martian, Andy Weir wrote "I’m going to have to science the shit out of this." While most RF designs aren't the life and death Mr Weir was writing about in his book; people involved in RF receiver design have the same sort overwhelming odds of not receiving things as Mark Watney did on the surface of Mars.

This presentation will look at Automatic Dependent Surveillance—Broadcast (ADS–B), which uses a  1 Mbit/s Pulse Position Modulation (PPM) scheme at 1090 MHz for airplane position sensing. From defining quality metrics, to making a reproducible test framework, we will explore what sort of radio settings are needed to maximize reception of good packets using a specific radio (in this case the ADALM-PLUTO, which should be also applicable to the NI B200 series and the Nuand BladeRF 2.0 micro).