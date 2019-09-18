---
type: "grcon/grcon19"
layout: "presentation"
title: "Multichannel phase coherent transceiver system with GNU Radio interface"
slides: "Michael Hennerich - Multichannel phase coherent system.pdf"
authors: ['Michael Hennerich']
youtube: ""
conference-day: Wednesday
weight: 8
---
Many applications need multiple channels of phase and frequency synchronization and coherency. Applications like Direction of Arrival (DOA) accuracy are directly related to the number of channels and the synchronization between these channels. This presentation will look at these applications and look at how they can be solved with a 4 channel 200MHz wide phase coherent system with a GNU Radio interface. 

After this introduction we will then focus on the concepts, techniques and features being used which enables this system to scale up to N Rx and Tx channels. While ensuring end-to-end deterministic latency and RF frequency and phase coherent synchronization. We will cover the technical aspects and challenges of clocking trees, multichip synchronization, JESD204B interface link synchronization, integrated LO and phase synchronization, all available on this production ready hardware for prototyping and systems development.
