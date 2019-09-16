---
type: "grcon/grcon19"
layout: "presentation"
title: "UHD Streaming with DPDK: Raising the Throughput Ceiling with Drivers in User Space"
slides: "noslides"
authors: ['Alex Williams']
youtube: "novideo"
conference-day: Wednesday
weight: 8
---
Software latency is the biggest impediment to high-speed streaming from a computer, and expensive kernel interactions are the primary source. System calls and buffer copying add to processing time, and the kernel's scheduler can cause large latency spikes. Consequently, engineers have compensated by adding large buffers to the other side. Is there another way?

Enter projects like the Data Plane Development Kit (DPDK). By implementing the driver outside the kernel, DPDK enables our applications to reduce processing and take control of scheduling. In this presentation, we look at how DPDK addresses the latency problem and how we used the technology in UHD to create our own network stack and blast through our throughput ceiling.

Why now? The recently-released N320 offers the widest per-channel bandwidth of any USRP developed so far. At 250 MSPS per channel, the stream could not be sustained with our previous architecture's throughput over the 10 GbE link. With technologies like DPDK, we can enable higher, more reliable throughput and spend fewer resources on buffering for those high-bandwidth applications. However, for GNU Radio to access this level of performance, it will necessitate a more efficient use of resources, including a revamp of the scheduler to use some of the same ideas.