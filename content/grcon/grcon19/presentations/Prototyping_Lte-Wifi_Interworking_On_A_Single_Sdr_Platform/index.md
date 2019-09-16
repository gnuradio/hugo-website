---
type: "grcon/grcon19"
layout: "presentation"
title: "Prototyping Lte-Wifi Interworking On A Single Sdr Platform"
slides: "noslides"
authors: ['Walter Nitzold', 'Clemens Felber', 'Vincent Kotzsch']
youtube: "novideo"
conference-day: Thursday
weight: 8
---
New use cases and requirements of future communication systems have driven the focus of research towards the coordination and coexistence of heterogeneous wireless technologies such as LTE, WiFi as well as 5G. 
We present a prototyping system focused on the joint real-time prototyping of LTE and WiFi. The system consists of real-time FPGA implementations of WiFi and LTE PHY layers using NI Application Frameworks. These run on the FPGAs of an USRP-2974 and an attached USRP-2953. A complete setup for joint prototyping would consist of a USRP-2974 and USRP-2953 as LTE eNB and WiFi AP while a second USRP-2974 and USRP-2953 are used as LTE UE and WiFi STA. 
To integrate the PHY layer implementations with higher layers and enable joint prototyping of these two wireless standards, we use network simulator 3 (ns3) -- a widely known open-source simulation environment for end-to-end communication research. 
Our contribution is a generalized API definition that specifies the connection between the PHY and the MAC layer. The API itself is vendor-independent and can be used to interface any LTE and WiFi PHY implementation with any given MAC layer implementations of LTE and WiFi.
We exemplarily implemented this API within the LTE and WiFi Application Frameworks as well as in ns3 such that LTE and WiFi is directly coupled to ns3. With this system, one can model arbitrary network topologies in ns3 that include LTE and WiFi radio access technologies and benefit from the use of real SDR hardware and over-the-air (OTA) transmission on the PHY layer. In this respect, the system bridges the gap between network research and real-world SDR prototyping and therefore enables real-world experiments to be as easy as simulations.
The API specification itself is openly available as part of the user manuals of the NI LTE and 802.11 Application Frameworks. Our exemplary implementations of the API can be found in the NI LTE and 802.11 Application Frameworks as well as in a customized implementation of ns3 to be accessed under https://github.com/ni/NI-ns3-ApplicationExample.
The use of an USRP-2974 has been shown beneficial as this device includes an embedded controller with Intel CPU that can directly run the API handler as well as ns3 on a real-time Linux and therefore make efficient use of the computing resources with a small footprint.