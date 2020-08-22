---
title: "GNU Radio Conference 2020"
date: 2019-11-22
type: grcon/grcon20
layout: single
aliases:
  - grcon-2020/workshops
  - grcon20/workshops
---


Throughout the week a wide variety of workshops will be run alongside the main-track technical talks and available to anyone who has a Full Conference registration. 

## Decoding Interplanetary Spacecraft
**Daniel Estévez**

Decoding interplanetary spacecraft is not as hard as you may think! The protocols are relatively well-documented and not very complex. This Workshop shows how to build a GNU Radio flowgraph to decode deep space telemetry signals from the ground up, starting just from a signal recording and using mainly standard blocks. Some basics of the CCSDS protocols will be explained. The level is suitable for GNU Radio beginners. The material is based on some work the author did with ESA's spacecrafts SolarOrbiter and BepiColombo earlier this year.

[Register](https://tickets.gnuradio.org/workshops20)

## Writing GNU Radio Blocks
**Wylie Standage-Beier**

This workshop is a beginners introduction to writing GNU Radio blocks, graphs, and systems.This is a guided hands on introduction to writing GNU Radio blocks and systems. In this workshop the participants go from simple python simulation of phase shift keyed signal in white noise to a functioning communications system using GNU Radio architecture and runtime. GNU Radio exerence is not required but Python experience is recommended.

[Register](https://tickets.gnuradio.org/workshops20)

## Python for the Rest of Us
**Mark Thoren, Analog Devices**

GNU Radio, at its core, makes extensive use of Python. Users’ understanding of this connection varies - from being somewhat aware that a “top_block.py” Python file is generated when executing a flowgraph, to the (Python expert) scientist capturing data sets with GNU Radio, to whom GNU Radio’s use of Python is trivial. There are many other ways to leverage Python in and around GNU Radio applications - in this 2-hour workshop, attendees will explore interfacing GNU Radio to external hardware through Python: An accelerometer connected to a Raspberry Pi will be used as an example to illustrate the use of GNU Radio IIO blocks, while learning a bit about Linux device drivers along the way. Once the basic operation is understood, we’ll explore using Python to control and read data from this device, both from within a GNU Radio embedded Python block, as well as from an external Python script that uses the GNU Radio project for signal processing. Finally, a few examples of Python interfaces to more radio-centric devices such as PLLs, RF oscillators, and beamformers will be given.

[Register](https://tickets.gnuradio.org/workshops20)

## Hands on with SETI Data and the Allen Telescope Array
**Steve Croft, UC Berkeley and SETI Institute**

The SETI Institute's Allen Telescope Array, located in remote Northern California, consists of 42 6-meter dishes that are currently in the process of being re-commissioned and upgraded for use in the search for radio technosignatures - potential indicators of technology developed by extraterrestrial intelligence. The current backend is being upgraded using modern hardware such as CASPER's SNAP boards, but we are also adding USRPs for the use of the GNU Radio community in helping to develop digital signal processing and RF analysis pipelines, as well as to observe targets of interest such as satellites.

This workshop will give a detailed introduction to the ATA signal path, data formats, control and monitoring software, and hooks into the GNU Radio system. We'll provide datasets from the array and walk participants through the process of visualizing spectrograms and identifying interesting signals, including from the Voyager 1 spacecraft. We'll also explore GNU Radio flowgraphs that can ingest data from the array for processing in the GNU Radio infrastructure.

[Register](https://tickets.gnuradio.org/workshops20)

## Phased Array Beamforming: Understanding and Prototyping
**Jon Kraft, Analog Devices**

In this workshop, we will demystify phased array and equip the audience with a powerful understanding of its underlying principles. We will setup a live demo of a phased array beamformer and use it to track an RF source, plot its beam characteristics, and take advantage of the features integrated into our beamformers. We will learn about steering angle, beam width, null locations, beam tapering, grating lobes, and beam squint. At each stage we will go through the math behind all of this and compare to our measured results. At the end, we put it all together to develop a monopulse tracking algorithm that locks into a moving RF source.

Phased array beamforming for communication and radar systems is becoming of greater importance to our world. 5G, satellite, airborne, and military applications all are taking advantage of analog and digital phased array technology. But the fundamental aspects of how to these systems work is hard to get a grasp on. It can feel like just a lot of math and angles to work through!

But in this workshop, we use GNU Radio to go hands on with beamforming! Put away your arcsin calculator! Instead, we will control the beam, “see” the beam, and make measurements on that beam. We will go through together step by step, and then correlate our measurements to the math and theory of phased array beamformers (so get back out that arcsin calculator!). At the end, we put it all together to develop our very own monopulse tracking algorithm and "lock" into our RF source as it moves around. In all, this workshop covers steering angle, beam width, null locations, beam tapering, grating lobes, beam squint, and monopulse tracking.

[Register](https://tickets.gnuradio.org/workshops20)

## Supporting New Hardware Using the OpenCPI Support Project Process
**OpenCPI**

This workshop will present how the integration of OpenCPI as an infrastructure for GNU Radio will enable GNU Radio applications to both exploit the hardware of an embedded heterogeneous processing system, as well as be easily ported to multiple hardware configurations.  OpenCPI is an open-source software framework for developing and executing component-based applications on heterogeneous embedded systems. The latest OpenCPI integration with GNU Radio provides an open infrastructure for supporting heterogeneous processing.

During the workshop, the attendee will have hands-on experience and initial familiarity with the tasks of taking a GNU Radio application, such as a Zigbee based application, developed using GRC to build, and execute on multiple dissimilar embedded hardware platforms.  The breadth of hardware platforms that OpenCPI supports includes multiple processor architectures (e.g. general, multi-core, manycore processors, GPUs), different FPGA architectures and FPGA toolchains, and connected devices such as transceivers.  The attendee will become familiar with how the integration of OpenCPI as an infrastructure for GNU Radio will allow GR blocks to have alternative implementations, such as C++ or VHDL, ready to run on CPUs or with different FPGA vendors and configurations. The OpenCPI framework selects the appropriate implementation of every block to be used depending on the available hardware and can execute an application across multiple, different Software-Defined Radios.

[Register](https://tickets.gnuradio.org/workshops20)

## FPGA Programming on the USRP using the RFNoC Framework
**Neel Pandeya, Ettus Research and NI**

Ettus Research's RFNoC (RF Network-on-Chip) software framework is designed to decrease the development time for experienced FPGA engineers seeking to integrate IP into the USRP FPGA signal processing chain. RFNoC is the framework for USRP devices that use Xilinx 7-series and Zynq FPGAs (E310, E312, E320, X300, X310, N300, N310, N320, N321). RFNoC is built around a packetized network infrastructure in the FPGA that handles the transport of control and sample data between the host CPU and the radio. Users target their custom algorithms to the FPGA in the form of Computation Engines (CE), which are processing blocks that attach to this network. CEs act as independent nodes on the network that can receive and transmit data to any other node (e.g., another CE, the radio block, or the host CPU). Users can create modular, FPGA-accelerated SDR applications by chaining CEs into a flow graph. RFNoC is supported in UHD and GNU Radio. In this workshop, we will present an interactive hands-on tutorial on RFNoC, including a discussion on its design and capabilities, demonstrations of several existing examples, and a walk-through on implementing a user-defined CE and integrating the CE into GNU Radio. A discussion of the changes and updates in the newest version of RFNoC will also be included.

[Register](https://tickets.gnuradio.org/workshops20)

