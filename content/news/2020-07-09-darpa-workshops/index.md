---
title: "GNU Radio - SDR framework for the future"
author: "Josh Morman"
date: "2020-07-09"
sponsored: "0"
aliases: ["/blog/darpa-workshops", "/news/darpa-workshops"]
---


We all know GNU Radio as a powerful framework for developing streaming, real-time signal processing applications for Software Defined Radio (SDR) on general purpose processors.  The core of GNU Radio - what we call the "scheduler", however, has not changed much in the last decade - which is a testament to the original design and vision. One of the consistent themes of modern SDR systems is heterogeneous compute architectures, which is something that GNU Radio is not particularly well suited to handle in its current state.  There have been several efforts over the years to run GNU Radio on specific platforms with heterogeneous topologies, but solving the general problem and making it part of standard GR operation requires a major rethinking of the structure of GR. 

The Defense Advanced Research Projects Agency (DARPA) has two on-going programs, run by DARPA Program Manager and former GNU Radio Project Lead Dr. Tom Rondeau, carrying out R&D that can benefit GR and progress the core of the project towards true heterogeneous processing support.  

1) The DSSoC program ([Domain Specific Scheduler on Chip](https://www.darpa.mil/program/domain-specific-system-on-chip)), which includes projects from Arizona State University (with support from University of Arizona among others), IBM (including Columbia University), and Oak Ridge National Labs, seeks to create heterogeneous SoCs where compiler frameworks and ontology tools can intelligently map compute tasks to the appropriate processing elements to utilize these types of hardware effectively.  Intelligent scheduling is a key component of this research and one we are hoping to learn more about and incorporate in our runtime.

2) The SDR 4.0 program (unrelated to GNU Radio version 4.0) is being led by a team of researchers at [BlackLynx](https://blacklynx.tech).  The goal of this program is more directly targeted toward improving some key functionalities of GR, namely improving native support for accelerated signal processing both with coprocessors and on embedded SDR platforms such as the MPSoC and RFSoC.  BlackLynx is closely collaborating with the GNU Radio leadership team to ensure that this work will have immediate impact and will make it upstream in the near future.

To truly make GNU Radio the framework for future of SDR, and incorporate varying ideas for what scheduling and distributed processing should be, it is worth taking a step back and formulating a vision:

  **Straightforward implementation of (distributed) SDR systems that make efficient use of the platform and its accelerators**

Imagine being able to throw down a flowgraph that can then run on a variety of different hardware platforms with little additional effort, pushing the processing of some blocks to the GPU or even have the flowgraph distributed across machines, while also maintaining the simplicity of setting up and running as if it was running on a single machine.  What will it take for GNU Radio to be able to accomplish this?  That is what we are investigating.

Prior to undertaking substantial changes to the GR codebase, over the last couple of months several of the GNU Radio officers (Marcus Müller - Karlsruhe Institute of Technology, Bastian Bloessl - Technische Universität Darmstadt, Josh Morman - Perspecta Labs, Philip Balister - OpenSDR, and Derek Kozel - Cardiff University) have coordinated a "Virtual Hackfest" with the teams on the DSSOC and SDR 4.0 programs that has since morphed into a series of workshops to understand the technology currently under development and propose solutions for a truly heterogeneous and modular GNU Radio.  

## So where do we go from here?  

Our next milestone is to produce a whitepaper based on the ideas that have been proposed in these workshops, and begin to produce a proof of concept framework - a sandbox to test out and benchmark various scheduling implementations and the API required to support them.  

Additionally as this proof of concept matures, there will be many ways for the community to get involved, as there are many moving pieces that will need to be designed/developed/integrated into an updated framework.  

We are all excited about this endeavor and will keep the community posted as opportunities for collaboration and involvement arise.  Please reach out if you have questions or would like to get involved in the effort.









