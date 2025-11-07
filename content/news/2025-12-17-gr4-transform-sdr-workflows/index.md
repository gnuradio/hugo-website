---
title: "How GR4 Can Transform Your SDR Workflows"
author: "Josh Morman, John Sallay"
date: "2025-12-17"
categories: ["gnuradio", "gr4", "community"]
aliases: ["/news/gr4-transform-sdr-workflows"]
banner: "GR4-logo-embedded.svg"
---

### A New Chapter for GNU Radio

Imagine a GNU Radio built for the future - a framework where your rapid prototypes seamlessly evolve into deployable, production-grade systems, and where **AI-enabled SDR development** feels effortless.  It’s GNU Radio built to run in places once thought impossible.

With **GNU Radio 4 (GR4)**, that vision is becoming reality.

Whether you're building a HAM project, a classroom demo, a lab prototype, or a production pipeline, GR4 aims to give you the same core guarantees: clear APIs, predictable performance, and a modern, maintainable codebase.

---

### Evolution Toward GR4

For more than two decades, GNU Radio has been the backbone of open-source signal processing and SDR innovation. It has powered research, education, and products across countless domains - and we’re committed to continuing to support and enhance it.  

But the world of software-defined radio has changed. Today’s applications demand more: **custom scheduling, latency control, heterogeneous computing across CPUs, GPUs, and FPGAs, memory safety, and maintainable APIs**. Addressing those challenges meant starting fresh-designing a framework that could fully leverage modern C++ and compiler capabilities from the ground up.  

GR4 began as a question: *what if we could make GNU Radio more modular, especially around scheduling?* Early community (see [Bastian Bloessl's GRCon19 paper](https://www.bastibl.net/bib/bloessl2019benchmarking/)) and industry collaborations-including the [**DARPA SDR 4.0**](https://www.darpa.mil/research/programs/software-defined-radio) initiative-led to a series of promising proofs-of-concept.  

[GR4](https://github.com/gnuradio/gnuradio4) as it stands now, was co-developed by **GSI-FAIR (the Facility for Antiproton and Ion Research)**, where contributors needed a **modern GNU Radio framework for real-time measurement and signal-processing systems in particle accelerator operations**. Those demanding environments (critical infrastructure) helped define the engineering goals - **low latency, high throughput, and robust performance** - but GR4 itself is being built for the **entire GNU Radio community**, not just one institution.  

The result is a **clean, modern C++ framework** that emphasizes **speed, predictability, and maintainability**, using type-safe APIs, lock-free buffers, and compile-time optimizations - all under a permissive open-source license.  

GR4’s guiding philosophy is simple: the same quality and reliability expected in critical research infrastructure should also be available to **students, researchers, and hobbyists** - even those building their first SDR projects. Excellence shouldn’t be limited to enterprise systems - it should be part of open software by design.


---

### From Prototype to Product

Block-based development is at the heart of GNU Radio - modular, reusable, rapid.  
GR4 extends that concept into a truly **production-grade runtime**.  

Its new modular scheduler architecture optimizes block execution across heterogeneous compute resources, from CPUs to GPUs to accelerators. Custom buffer types and scheduling domains ensure the right data movement strategy for each device.  And because the scheduling system itself is modular, there’s no need for a one-size-fits-all approach: the flexible scheduler API lets developers build **custom schedulers** tailored to specific hardware, latency targets, or application needs.

In practice, this means your experimental flowgraph can scale into a deployable, high-performance system without rewriting the underlying framework.

---

### Killer Features That Redefine the GNU Radio Experience

GR4 introduces a number of transformative design features:

- **Type-strict C++ APIs** - leverage modern compiler optimizations with predictable behavior.  
- **Ease of Development** - new simplifications such as `processOne()` for block implementation (reduces boiler plate for most GR3 blocks down to a single function!)
- **Single-source-of-truth code model** - your block definition drives both build and documentation.  
- **Lock-free circular buffers** - eliminate bottlenecks in high-rate streaming chains.  
- **SIMD & Merge API** - fuse compatible operations for maximum throughput.  
- **Direct block testing** - validate each block independently of a full flowgraph.  
- **Modular schedulers** - select or build custom schedulers for your workload.
- **Modern UI and integration roadmap (WIP)** - GR4’s clean core architecture is ready for future web and desktop UI integration, opening new opportunities for **education, visualization, and interactive labs**.  

Together, these enable both **rapid development** and **production-class performance**.

---

### Where GR4 **REALLY** shines

One of GR4’s greatest strengths is that its core can function as a **header-only C++23 library**.  
This design enables true zero-cost abstractions - you only pay for the blocks and functionality you actually use - and allows the compiler to aggressively optimize **entire flowgraphs at compile time** for your specific architecture.  

For embedded or constrained environments, this means you can deploy a 2-3 MB standalone executable containing your entire signal processing chain, with zero dependencies on GNU Radio libraries or even a C++ runtime beyond libc++. This is transformative for IoT SDR, edge computing, or secure air-gapped systems.  This design eliminates the overhead of packaging and installing the full framework when your goal is simply to **run a fixed application**, while still allowing more complex systems to be built on top of the same lightweight core. 

It also avoids duplicating identical code for different scalar types - the same implementation can cover `int8/16/32/64`, `float`, `double`, complex types, or even structured and packetized data via the streaming interfaces.

The **permissive licensing** makes it even easier to integrate GR4 into downstream projects or products.  GR4's core runtime is MIT-licensed to make integration easier for industry and public infrastructures, while modules and surrounding ecosystem can remain (L)GPLv3. The intent is to keep GNU Radio free in practice, and never to turn it into a closed product.  We expect many contributed blocks and modules to remain (L)GPLv3, maintaining GNU Radio's free software heritage. The MIT core simply ensures that GR4 can be embedded in public infrastructure, automotive, medical devices, or other contexts where GPL compliance is complex or impossible.

GR4 also includes a **plugin system** and a **reflection-based control API** that makes it easy to expose block parameters and status to external tools or middleware.  In the usage at FAIR this is paired with an external middleware stack, called OpenCMW, for full RPC/network functionality, but the same GR4 hooks can be used with other frameworks as well.  GR4's reflection system exposes block metadata, ports, and parameters at runtime through a standardized introspection API.  This is the foundation for remote control, but networking, serialization, discovery, and protocol handling are intentionally left to external middleware layers.  This design means GR4 can work with REST APIs, gRPC, ZeroMQ, MQTT, or any other control protocol - the framework doesn't prescribe the transport layer.

Still, for most users, the simplicity of **statically compiled flowgraphs** is the easiest and most accessible entry point - one that unlocks GR4’s potential even on minimal hardware.

---


### AI-Ready SDR

AI-enabled SDR starts with a high-performance, predictable foundation - and GR4 delivers exactly that.  

Without a robust core, developers waste time reinventing DSP chains, schedulers, and I/O. GR4 provides a **production-grade signal-processing engine** that allows AI-generated code and AI-driven waveforms to focus on innovation, not reimplementation.  

A shared foundation means that models and outputs from machine-learning systems can be **immediately deployable and interoperable** with the rest of the SDR ecosystem.

#### Tensors: An AI-Ready Data Model

GR4 extends the traditional polymorphic-type (PMT) system into a **tensor-aware, metadata-rich data model** - a natural fit for modern AI and ML workflows in **PyTorch, TensorFlow, and ONNX**.  

In GR4, signal data can be represented as multidimensional tensors with defined shape, data type, and rank, while carrying associated context such as time, frequency, and other metadata.  
This makes every dataset inherently **training- and inference-ready**, without additional preprocessing or manual annotation.  The Tensor can be used both in message passing and streaming blocks.  This facilitates matrix-based Signal Processing applications like beam-forming in addition to AI.


---

### Data Movement and Compute Placement

To support heterogeneous compute, GR4 includes a custom buffer architecture that can support zero-copy paths to GPUs or accelerators, and early SYCL/CUDA prototypes demonstrate cross-device scheduling. This is an active area of development and a good place for contributors interested in heterogeneous compute to get involved.  Full production-grade heterogeneous scheduling is a 2025-2026 goal, but the architecture is designed to support it without requiring large core framework changes.

Multiple sub-schedulers handle CPU, GPU, and hybrid domains - seamlessly orchestrated by the global flowgraph.

---

### Latest GR4 Features

GR4 development has been humming along the past year.  Recent milestones include:

- **Permissively Licensed Core (MIT)** - build on top of GR4 with complete freedom.  Preserve copyleft character in module contributions
- **Custom user-defined schedulers**  
- **Low-latency execution (< 10 µs)** across multi-block chains [PR#603](https://github.com/fair-acc/gnuradio4/pull/603)
- **Runtime message-passing API** (enabling GUIs and dynamic reconfiguration)  
- **MIT-licensed SIMD FFT** (as fast or faster than FFTW) [PR#671](https://github.com/fair-acc/gnuradio4/pull/671)
- **Feedback Loop Support for Cyclic Directed Graphs** [PR#654](https://github.com/fair-acc/gnuradio4/pull/654)
- **Proof-of-concepts:** Windows builds, SYCL integration for GPUs/FPGAs, ONNX ML integration, and Tensor support <-- lots of room to get involved!

---

### Low-Hanging Fruit and Resources for Contributors

Now is the perfect time to get involved.  
Community contributions can have immediate impact:

- Port GR3 blocks and modules.  
- Add **SigMF**, **ONNX**, or **REST/HTTP** integrations.  
- Develop example flowgraphs (AM/FM, digital modulation/demodulation).  
- Create performance benchmarks.  

The best place to contribute is the [gr4-incubator](https://github.com/gnuradio/gr4-incubator) repo.  The bar is lower than pulling 
functionality in-tree, but we hope this is a good place to collect useful blocks that can be hardened as they work their way into the officially supported repos.

Another good resource is [this tutorial](https://github.com/mormj/gr4-block-tutorial).  It steps through some of the basic 
constructs of GR4.

Join the **Architecture Working Group** to follow progress and shape priorities.  
Meetings are held most **fourth Thursdays at 12 PM ET** - details on [chat.gnuradio.org](https://chat.gnuradio.org) (#architecture) or [groups.io/g/gnuradio-scheduler](https://groups.io/g/gnuradio-scheduler) <-- join this mailing list to get updated meeting invites!


---

### Toward Community Maintainership

The long-term goal is clear: **continue the transition of GR4 from a GSI/FAIR-driven refactoring effort to full community maintainership**.  

That means shared ownership of the:
- Core runtime and schedulers  
- Standard block set  
- Build and packaging frameworks  
- Documentation, tutorials, and Python bindings  

We will need maintainers for different subsystems: someone to own the documentation, someone to champion Windows builds, experts in GPU scheduling, etc. You don't need to be a C++ wizard to make critical contributions - expertise in testing, documentation, or platform-specific deployment is equally valuable.

FAIR's interest in GR4 is simple: they do a lot of RF and signal processing, as do many of their users that use their accelerator infrastructure for experimentation. Using common GR tooling both on-site and off-site lowers the bar for domain experts without deep software expertise. We all benefit when the broader research community uses standardized tooling. Common infrastructure means easier collaboration, reproducible results, and students/postdocs who arrive already trained on the tools we all love, share and use. 

The initial GR4 refactoring, driven by contributors at FAIR and across the community, was a substantial investment in the future of GNU Radio.  Now it’s our turn to build upon it.

---

### Let’s Make This a Reality

GR4 is real, powerful, and ready for you.  
Join the Architecture Working Group, contribute to the expanding blockset, or showcase your own GR4-based applications that demonstrate its performance and flexibility.

Together we can make GNU Radio 4 the standard for reproducible, AI-enabled signal-processing workflows - from research labs to production systems.

➡️ [**Reach Out** to us architecture@gnuradio.org](mailto:architecture@gnuradio.org)

➡️ [Join the discussion on chat](https://matrix.to/#/#architecture:gnuradio.org)

➡️ [Explore GR4 on GitHub](https://github.com/gnuradio/gnuradio4)  

➡️ [Add New Blocks](https://github.com/gnuradio/gr4-incubator)
