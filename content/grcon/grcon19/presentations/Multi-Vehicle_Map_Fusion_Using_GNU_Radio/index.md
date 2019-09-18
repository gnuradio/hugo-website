---
type: "grcon/grcon19"
layout: "presentation"
title: "Multi-Vehicle Map Fusion Using GNU Radio"
slides: "Augusto Vega - Multi-Vehicle Map Fusion.pdf"
authors: ['Akin Sisbot', 'Augusto Vega', 'Arun Paidimarri', 'John-David Wellman', 'Alper Buyuktosunoglu', 'Pradip Bose', 'David Trilla']
youtube: ""
conference-day: Wednesday
weight: 5
---
In this paper, we present a representative open-source application for fully/semi autonomous vehicles operating as a collaborative swarm using GNU Radio. This application is the driver of our PROJECT-NAME* project, focusing on system-on-a-chip (SoC) development. 
The PROJECT-NAME* Reference Application (ERA) incorporates local sensing, creation of occupancy grid maps, vehicle-to-vehicle (V2V) communication of grid maps between neighboring vehicles using a GNU Radio implementation of dedicated short-range communications (DSRC), and map fusion to create a joint higher accurate grid map. 
In this paper, we also analyze the GNU Radio-based DSRC transceiver workload on a Xilinx UltraScale+ ZCU102 board, and identify computation kernels for software or hardware acceleration. 
In particular, we present optimizations of complex exponentiation and Viterbi decoding that result in a measured 24% throughput improvement, with potential for up to 58% throughput improvement with additional optimizations.

* Project name removed to comply with the double blind review process.
