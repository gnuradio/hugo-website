---
type: "grcon/grcon19"
layout: "presentation"
title: "VLBI with GNU Radio and White Rabbit"
slides: "Paul Boven - VLBI with GNU Radio.pdf"
authors: ['Paul Boven']
youtube: ""
conference-day: Thursday
weight: 6
---
Very Long Baseline Interferometry (VLBI) is a technique in radio astronomy that allows for unprecedented resolution by phasing up participating radio telescopes all over the world. This phasing up requires very stable atomic clocks at each observatory, in order to coherently combine the signals. The Joint Institute for VLBI ERIC (JIVE) in Dwingeloo, the Netherlands processes the data for the European VLBI Network (EVN). As part of the European 'ASTERICS' research project, we have contributed to investigations on the suitability of the open 'White Rabbit' standard for the distribution of highly stable time and frequency reference signals.

CAMRAS (C.A. Muller Radio Astronomy Station) operates the historic 25m Dwingeloo Radio telescope in the Netherlands. Once the largest fully steerable radio telescope in the world, it is now retired and run by volunteers. We increasingly use SDRs and GNU Radio for our astronomical and other observations.

In this presentation we will show how, with some improvements, the White Rabbit system can be used as a reference for VLBI, even at 169km link distance. Timestamping and recording the broadband data at the Dwingeloo telescope was done with an USRP, using a GNU Radio flowchart.
