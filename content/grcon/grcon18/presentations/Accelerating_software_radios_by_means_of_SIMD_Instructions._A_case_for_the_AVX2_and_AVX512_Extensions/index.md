---
type: "grcon/grcon18"
layout: "presentation"
title: "Accelerating software radios by means of SIMD Instructions. A case for the AVX2 and AVX512 Extensions"
authors: ["Damian Miralles", "Jessica Iwamoto"]
slides: "8-Jessica_Iwamoto-SIMD.pdf"
draft: true
youtube: ""
conference-day: "Wednesday"
weight: 8
---
Current computer architecture trends are moving towards parallelization by means of node replication and data parallelization, which optimize the execution speed of a given application. Increasing the number of nodes is constrained by the hardware platform in use; however, effective data parallelization techniques can improve processing speeds by leveraging existing resources of the platform. This paper presents the AVX2 and AVX512 instruction addition to several kernels in the VOLK library. We discuss the capabilities of the new extensions and their interaction with the VOLK library. Finally, we show profiling results of the speed enhancements added to the library for AVX capable machines.
