---
type: "grcon/presentations"
title: "ARM PlutoSDR With Custom Applications"
authors: ["Michael Hennerich"]
slides: "8-Michael_Hennerich.pdf"
draft: true
youtube: ""
conference-day: "Monday"
weight: 8
---
The ADALM-PLUTO also known as PlutoSDR can be used as a RF streaming device over High-Speed USB 2.0 to Linux's Industrial I/O (IIO) clients like GNU Radio, or custom applications written in C, C++, C# or Python. However it can also be used as a standalone device, since it is an open Linux based ARM system. Therefore signal processing applications may be targeted to also run directly on the device itself. The libiio user space library abstracts the low-level details of the hardware, and provides a simple yet complete programming interface. In addition it makes the transport transparent, so it abstracts the transport medium (USB, IP network, serial, or local) away from the application. With a single line code change, and a cross compiler, applications can move from being run on a remote host, to run local on the device itself. This tutorial uses an open source ADS-B receiver as an example and shows multiple options on how to run it on the target.

This tutorial is not just applicable for the PlutoSDR, it's of general interest for anyone using the Linux IIO subsystem for high speed data capture and libIIO. Only lately, optionally community IIO support was added for the EPIQ Sidekiq Z2 and the Ettus E310, so that the content covered in this tutorial also applies for these commercial of the shelf SDR radios.

A brief introduction to the Linux IIO subsystem will be given. This presentation will furthermore talk about bottlenecks and limitations of the IIO subsystem for high speed sampled data systems. Introduce Linux Continuous (CMA) and DMA-able memory allocation issues. Latency and overhead trade-offs between buffer size and number of buffers. How Linux Zero-Copy decreases overhead and increase performance. A few words about libiio context timeouts and how they can be avoided. Last but not least this tutorial will highlight future enhancements and show work in progress.

Michael is Open Source Engineering Manager at Analog Devices GmbH in Munich, and also passionate and licensed HAM Radio Amateur.  He first talked about Embedded Linux for DSPs on the Embedded Systems Conference Silicon Valley back in 2006, since then Michael is an active Linux kernel developer and open source contributor.
