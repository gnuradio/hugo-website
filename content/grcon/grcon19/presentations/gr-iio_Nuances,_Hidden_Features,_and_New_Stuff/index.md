---
type: "grcon/grcon19"
layout: "presentation"
title: "gr-iio: Nuances, Hidden Features, and New Stuff"
slides: "Travis Collins - gr_iio.pdf"
authors: ['Travis Collins']
youtube: ""
conference-day: Wednesday
weight: 3 
---
In this presentation, we will discuss the current out-of-tree module gr-iio which enables data streaming and control of any device with an Industrial Input/Output (IIO) kernel driver. The module not only supports SDRs like ADALM-PLUTO and USRP-E310 today but also provides access to hundreds of sensor devices and even gigasample converters using the standard kernel framework.
 
We will provide a basic introduction to gr-iio and IIO for new users. We will also discuss how the standard blocks can be extended using the new Attribute blocks. This will focus on advanced features of the controlling drivers for AD936X based radios, as well as new enhancements made to current blocks. For advanced users, we will demonstrate how gr-iio can be used to interact with deployed IP on an FPGA, which will be done using an ADALM-PLUTO. This demonstration will examine controlling the frequency hopping features of the AD9363 transceiver using custom IP and controlling IIO driver. Finally, we will discuss merging gr-iio into mainline GNU Radio to allow simplified adoption for end users.
