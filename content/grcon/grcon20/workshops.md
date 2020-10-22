---
title: "GNU Radio Conference 2020"
date: 2019-11-22
type: grcon/grcon20
layout: single
aliases:
  - grcon-2020/workshops
  - grcon20/workshops
---

## Decoding Interplanetary Spacecraft
**Daniel Estévez**

Decoding interplanetary spacecraft is not as hard as you may think! The protocols are relatively well-documented and not very complex. This Workshop shows how to build a GNU Radio flowgraph to decode deep space telemetry signals from the ground up, starting just from a signal recording and using mainly standard blocks. Some basics of the CCSDS protocols will be explained. The level is suitable for GNU Radio beginners. The material is based on some work the author did with ESA's spacecrafts SolarOrbiter and BepiColombo earlier this year.

* [Video](https://www.youtube.com/watch?v=RDbs6l4rMhs)
* [Slides](https://github.com/daniestevez/grcon2020-workshop/raw/master/slides/slides.pdf)
* [Code and Supporting Files](https://github.com/daniestevez/grcon2020-workshop)

## Writing GNU Radio Blocks
**Wylie Standage-Beier**

This workshop is a beginners introduction to writing GNU Radio blocks, graphs, and systems.This is a guided hands on introduction to writing GNU Radio blocks and systems. In this workshop the participants go from simple python simulation of phase shift keyed signal in white noise to a functioning communications system using GNU Radio architecture and runtime. GNU Radio exerence is not required but Python experience is recommended.

* [Video](https://www.youtube.com/watch?v=CnJObODsx0I)
* [Slides](https://github.com/TheWylieStCoyote/writing_GNURadio_blocks_python/raw/master/Presentation_workshop.pdf)
* [Code and Supporting Files](https://github.com/TheWylieStCoyote/writing_GNURadio_blocks_python)

## Python for the Rest of Us
**Mark Thoren, Analog Devices**

GNU Radio, at its core, makes extensive use of Python. Users’ understanding of this connection varies - from being somewhat aware that a “top_block.py” Python file is generated when executing a flowgraph, to the (Python expert) scientist capturing data sets with GNU Radio, to whom GNU Radio’s use of Python is trivial. There are many other ways to leverage Python in and around GNU Radio applications - in this 2-hour workshop, attendees will explore interfacing GNU Radio to external hardware through Python: An accelerometer connected to a Raspberry Pi will be used as an example to illustrate the use of GNU Radio IIO blocks, while learning a bit about Linux device drivers along the way. Once the basic operation is understood, we’ll explore using Python to control and read data from this device, both from within a GNU Radio embedded Python block, as well as from an external Python script that uses the GNU Radio project for signal processing. Finally, a few examples of Python interfaces to more radio-centric devices such as PLLs, RF oscillators, and beamformers will be given.

* [Video](https://youtu.be/cO5sBarLiVk)
* [Slides](/grcon/grcon20/grcon20_mthoren_Python_for_the_rest_of_us.pdf)
* [Code and Supporting Files](https://github.com/mthoren-adi/gnuradio_projects/tree/grcon_2020)
* [Info on the Hardware Setup](https://wiki.analog.com/university/labs/software/iio_intro_toolbox)

## Hands on with SETI Data and the Allen Telescope Array
**Steve Croft, UC Berkeley and SETI Institute**

The SETI Institute's Allen Telescope Array, located in remote Northern California, consists of 42 6-meter dishes that are currently in the process of being re-commissioned and upgraded for use in the search for radio technosignatures - potential indicators of technology developed by extraterrestrial intelligence. The current backend is being upgraded using modern hardware such as CASPER's SNAP boards, but we are also adding USRPs for the use of the GNU Radio community in helping to develop digital signal processing and RF analysis pipelines, as well as to observe targets of interest such as satellites.

This workshop will give a detailed introduction to the ATA signal path, data formats, control and monitoring software, and hooks into the GNU Radio system. We'll provide datasets from the array and walk participants through the process of visualizing spectrograms and identifying interesting signals, including from the Voyager 1 spacecraft. We'll also explore GNU Radio flowgraphs that can ingest data from the array for processing in the GNU Radio infrastructure.

## Phased Array Beamforming: Understanding and Prototyping
**Jon Kraft, Analog Devices**

In this workshop, we will demystify phased array and equip the audience with a powerful understanding of its underlying principles. We will setup a live demo of a phased array beamformer and use it to track an RF source, plot its beam characteristics, and take advantage of the features integrated into our beamformers. We will learn about steering angle, beam width, null locations, beam tapering, grating lobes, and beam squint. At each stage we will go through the math behind all of this and compare to our measured results. At the end, we put it all together to develop a monopulse tracking algorithm that locks into a moving RF source.

Phased array beamforming for communication and radar systems is becoming of greater importance to our world. 5G, satellite, airborne, and military applications all are taking advantage of analog and digital phased array technology. But the fundamental aspects of how to these systems work is hard to get a grasp on. It can feel like just a lot of math and angles to work through!

But in this workshop, we use GNU Radio to go hands on with beamforming! Put away your arcsin calculator! Instead, we will control the beam, “see” the beam, and make measurements on that beam. We will go through together step by step, and then correlate our measurements to the math and theory of phased array beamformers (so get back out that arcsin calculator!). At the end, we put it all together to develop our very own monopulse tracking algorithm and "lock" into our RF source as it moves around. In all, this workshop covers steering angle, beam width, null locations, beam tapering, grating lobes, beam squint, and monopulse tracking.

* [Video](https://youtu.be/0hnWfTvETcU)
* [Slides](https://github.com/jonkraft/PhasedArray/blob/master/PhasedArrayWorkshop_Presentation.pdf)
* [Code and Supporting Files](https://www.github.com/jonkraft/phasedarray)
* [Raspberry Pi image with workshop files](http://download.analog.com/phased-array-lab/raspi.7z)

## Introduction to GRC Development for OpenCPI
OpenCPI

This workshop will present how the integration of OpenCPI as an infrastructure for GNU Radio will enable GNU Radio applications to both exploit the hardware of an embedded heterogeneous processing system, as well as be easily ported to multiple hardware configurations.  OpenCPI is an open-source software framework for developing and executing component-based applications on heterogeneous embedded systems. The latest OpenCPI integration with GNU Radio provides an open infrastructure for supporting heterogeneous processing.

During the workshop, the attendee will have hands-on experience and initial familiarity with the tasks of taking a GNU Radio application, such as a Zigbee based application, developed using GRC to build, and execute on multiple dissimilar embedded hardware platforms.  The breadth of hardware platforms that OpenCPI supports includes multiple processor architectures (e.g. general, multi-core, manycore processors, GPUs), different FPGA architectures and FPGA toolchains, and connected devices such as transceivers.  The attendee will become familiar with how the integration of OpenCPI as an infrastructure for GNU Radio will allow GR blocks to have alternative implementations, such as C++ or VHDL, ready to run on CPUs or with different FPGA vendors and configurations. The OpenCPI framework selects the appropriate implementation of every block to be used depending on the available hardware and can execute an application across multiple, different Software-Defined Radios.

The relationship between the OpenCPI framework and GNU Radio will be discussed.  At the conclusion of the Workshop, each attendee will have the chance to execute the demonstrated GR application on at least two very different hardware systems.  The GR application developer will have utilized the OpenCPI infrastructure that supports heterogeneous processing and a breadth of hardware and toolchains, in order to avoid the limitations of vendor-specific hardware and tool-chain solutions.  At the end of the workshop, there will be a demonstration of testing the GR application code using the CNF Continuous Integration (CI) Test infrastructure.

## Supporting New Hardware Using the OpenCPI Support Project Process
**OpenCPI**

This workshop will present how the integration of OpenCPI as an infrastructure for GNU Radio will enable GNU Radio applications to both exploit the hardware of an embedded heterogeneous processing system, as well as be easily ported to multiple hardware configurations.  OpenCPI is an open-source software framework for developing and executing component-based applications on heterogeneous embedded systems. The latest OpenCPI integration with GNU Radio provides an open infrastructure for supporting heterogeneous processing.

During the workshop, the attendee will have hands-on experience and initial familiarity with the tasks of taking a GNU Radio application, such as a Zigbee based application, developed using GRC to build, and execute on multiple dissimilar embedded hardware platforms.  The breadth of hardware platforms that OpenCPI supports includes multiple processor architectures (e.g. general, multi-core, manycore processors, GPUs), different FPGA architectures and FPGA toolchains, and connected devices such as transceivers.  The attendee will become familiar with how the integration of OpenCPI as an infrastructure for GNU Radio will allow GR blocks to have alternative implementations, such as C++ or VHDL, ready to run on CPUs or with different FPGA vendors and configurations. The OpenCPI framework selects the appropriate implementation of every block to be used depending on the available hardware and can execute an application across multiple, different Software-Defined Radios.

## FPGA Programming on the USRP using the RFNoC Framework
**Neel Pandeya, Ettus Research and NI**

Ettus Research's RFNoC (RF Network-on-Chip) software framework is designed to decrease the development time for experienced FPGA engineers seeking to integrate IP into the USRP FPGA signal processing chain. RFNoC is the framework for USRP devices that use Xilinx 7-series and Zynq FPGAs (E310, E312, E320, X300, X310, N300, N310, N320, N321). RFNoC is built around a packetized network infrastructure in the FPGA that handles the transport of control and sample data between the host CPU and the radio. Users target their custom algorithms to the FPGA in the form of Computation Engines (CE), which are processing blocks that attach to this network. CEs act as independent nodes on the network that can receive and transmit data to any other node (e.g., another CE, the radio block, or the host CPU). Users can create modular, FPGA-accelerated SDR applications by chaining CEs into a flow graph. RFNoC is supported in UHD and GNU Radio. In this workshop, we will present an interactive hands-on tutorial on RFNoC, including a discussion on its design and capabilities, demonstrations of several existing examples, and a walk-through on implementing a user-defined CE and integrating the CE into GNU Radio. A discussion of the changes and updates in the newest version of RFNoC will also be included.

* [Video](https://www.youtube.com/watch?v=M9ntwQie9vs)

## Networked GNURadio: NS3 meets GNU Radio
### Delivering a full-stack shared-code live, virtual constructive simulation framework
Bishal Thapa (Ph.D.), Guevara Noubir (Ph.D.), and Colin Funai (Ph.D.)

Although GNU Radio has brought customizable open wireless modems, in the form of  SDRs, to the research community, often times testing higher layer protocols, such as novel Medium Access and Networking protocols, while maintaining clear layers of abstraction, remains out of reach for many SDR developers. As a result, full-stack development of novel wireless networking solutions often turn to network simulators (e.g., NS3) as the tool of choice. NS3 is a discrete event simulator, meaning that the system's state is sampled at quantized time steps, that is widely used by the academic community. NS3 can simulate all layers of the OSI stack, some at a higher fidelity than others. Specifically, it supports a variety of communication models, mobility models, energy harvesting models, and channel models but at a significantly lower fidelity and with less realistic assumptions. E.g. NS3 has native support for underwater acoustic networks (UAN).  Although NS3 can be used to simulate channel level aberrations and noise, real world testing remains a much needed step in validating any protocol due to the complexity in accurately modeling the wireless channel. To bridge this gap, we present NS3-GNU Radio shim, as a means of seamlessly linking higher layer NS3 efforts with GNU Radio based SDR development effort. Our work will not only allow live, virtual, constructive simulation with a seamless real world validation capability, but also enable a comprehensive view into how any proposed changes will coexist with incumbent protocols and systems. This would be most relevant to ongoing 5G/xG and undersea acoustic network research effort.

## Introduction to the ADALM-PLUTO SDR
Dr. Travis Collins and Robin Getz, Analog Devices

This workshop will provide a thorough and practical introduction to the AD9361, the ADALM-PLUTO SDR, and other IIO based hardware and the open-source software toolchain (IIO utils and IIO-Scope). We will examine the hardware and architecture of the PLUTO software-defined radio in addition to discussing topics such as how to get started using a new PLUTOSDR device, how to install and configure the open-source software toolchain, programming the PLUTO using the libIIO API from Python, C or C++, and other tools using PLUTO SDR. Other hardware capable of running the IIO framework will be discussed, such as the Ettus E310, the Epiq SideKiq Z2, and Analog Device's RF SOM. Several exercises will be performed on the ADALM-PLUTO SDR, such as implementing an FM transmitter and receiver. Various demonstrations of other wireless systems will be shown. For those interested in MATLAB or Simulink the Pluto Hardware support package will be shown.

Attendees should come away with a solid foundation and practical understanding of how to configure, program, and use the Pluto SDR and other IIO based hardware to implement a wide range of wireless systems.

* [Video](https://youtu.be/05nLPVJW9Uo)
* [Slides](https://wiki.analog.com/_media/plutoworkshop.pdf)
* [Supporting Documentation and Files](https://wiki.analog.com/grcon2020)
