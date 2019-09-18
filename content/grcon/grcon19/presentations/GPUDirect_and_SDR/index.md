---
type: "grcon/grcon19"
layout: "presentation"
title: "GPUDirect + SDR: How to Move One Billion Samples per Second over PCIe"
slides: ""
authors: ['Ben Hilburn']
youtube: ""
conference-day: Wednesday
weight: 7 
---
We are at an interesting time with SDR system development: channel bandwidths are pushing from hundreds of MHz to GHz, channel counts continue to increase, and computational components such as CPUs, FPGAs, and GPUs are rapidly evolving. Software developers can easily exhaust the signal processing resources of a general purpose CPU, and are turning to GPUs more and more to perform the task at hand. The core challenge of getting digitized radio samples into a GPU still typically involves a CPU in the middle doing nothing more than shuttling samples around. This is not only inefficient, but it will ultimately lead to a bottleneck in the system for wide bandwidth signal processing tasks.

This talk will discuss the work that Epiq Solutions has been tackling to integrate Nvidia’s GPUDirect framework for use in transporting digitized radio samples from an SDR directly into a GPU over PCIe. Leveraging GPUDirect alleviates the burden on the CPU while simultaneously increasing the achievable throughput by a substantial margin. Real world benchmarks leveraging the PCIe DMA driver utilized by Epiq’s Sidekiq SDR cards will be presented, including transport throughput benchmarks for the Nvidia Quadro P2000 GPU as well as an Nvidia Xavier GPU platform. 
