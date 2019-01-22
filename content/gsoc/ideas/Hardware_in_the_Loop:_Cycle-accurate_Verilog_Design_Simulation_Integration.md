---
title: "Hardware in the Loop: Cycle-accurate Verilog Design Simulation Integration"
name: "Hardware_in_the_Loop:_Cycle-accurate_Verilog_Design_Simulation_Integration"
hash: "5178450163655621796"
mentors: ["","Marcus Müller","",""]
type: idea
---


Hardware accelerators are necessary or at least desirable in many SDR systems.

A typical development workflow for FPGA-accelerated DSP system looks like this:


* Write down the system specification, formulate the algorithm mathematically

* Implement the algorithm in Matlab, Python to make a Proof of Concept

* Write extensive test cases to make sure you've got everything right

* Iterate.

* Implement the same algorithm in a HDL, e.g. Verilog, and synthesize

* Write extensive (System)Verilog test benches, which mostly duplicate code from the software test cases in a less friendly development environment

* Run the test benches in simulation and the FPGA to prove functionality

* Iterate.

However, with [Verilator](https://www.veripool.org/wiki/verilator), there's a relatively mature tool to turn Verilog modules into compilable C++ code that offers a cycle-accurate simulator of the module.

The goal would be to use integrate verilator into the GNU Radio in a way that allows for rapid prototyping of small, well-defined Verilog modules; the idea is that you can, in the end, just drop your Verilog code file name in a GNU Radio block, and behind the scenes, the C++ code is generated, necessary "adapters" from native (GNU Radio) data types to simulated signals are added, and all is then executed at flow graph run time to process digital signals from within a flow graph.

## Prerequisites

* workable C++ proficiency

* basic idea of FPGA development

* Ability to read and write "hello world" verilog modules

## Outcome

* Adapter code to call Verilator-generated Code of modules with fixed interface from within a GNU Radio block's work routine

* Integration of verilator into either build infrastructure or runtime infrastructure (might require further dependencies, e.g. llvm)

* Examples and software test cases for fundamental blocks, e.g. a FIFO and a integer squarer


