---
title: "First Release Candidate for GR4"
date: "2026-03-22"
categories: ["gnuradio", "gr4", "community"]
aliases: ["/news/gr4-release-candidate-1"]
banner: "GR4-logo-embedded.svg"
---

**GNU Radio 4.0 RC1: A New Foundation for High-Performance Signal Processing**

GNU Radio 4.0 has reached its first release candidate (RC1)—a major milestone that signals the transition from active development to **near-production readiness**.

At this stage, the core architecture is stable, the execution model is well-defined, and the API is no longer expected to undergo major breaking changes. Developers can begin building against GR4 today with confidence that their work will carry forward into the final release.

But this is more than a stabilization point.

GNU Radio 4 is a **fundamental re-architecture** of the system—designed for modern C++, deterministic execution, and high-performance pipelines that scale from embedded systems to large, complex DSP applications. The result is not just incremental improvement, but a platform that expands what is possible in GNU Radio.

---

## What’s New and Exciting in GNU Radio 4

### Modular execution and scheduler flexibility

GR4 introduces a fundamentally new execution model built around **modular schedulers and explicit control over data movement and execution**.

Rather than relying on a single, fixed scheduler, GR4 allows developers to **select or implement schedulers** that match their specific workload and deployment environment. This makes execution a configurable part of the system, not a hidden implementation detail.

This model is designed to support a wide range of use cases:

- Low-latency streaming pipelines  
- High-throughput batch processing  
- Execution across heterogeneous compute environments (CPU, GPU, accelerators)  

By separating the *what* (the signal processing graph) from the *how* (the execution strategy), GR4 enables systems to evolve more naturally from research prototypes to production deployments.

This approach aligns with GR4’s broader goal of transforming SDR workflows—making systems more portable, adaptable, and easier to optimize across different platforms.

---

### Compile-time composition for zero-overhead pipelines

Signal chains in GR4 can be composed at compile time, enabling:

- Elimination of intermediate buffers  
- Full compiler optimization across block boundaries  
- Highly efficient, fused execution paths  

This capability is central to GR4’s performance gains.

---

### Modern C++ with type-safe design

GR4 is built on modern C++ principles with a strong emphasis on **type safety, clarity, and developer productivity**.

- Strongly typed interfaces  
- Compile-time validation of connections and configurations  
- Explicit error handling via `std::expected`  

At the same time, the developer workflow is intentionally simple. A block can often be implemented with minimal boilerplate using a `processOne` method, letting the framework handle scheduling, buffering, and vectorization.

For example, a simple gain block:

```cpp
template <typename T>
struct Multiply {
    T k;

    Multiply(T gain) : k(gain) {}

    auto processOne(T in) {
        return in * k;
    }
};
```

That’s it—no manual buffer management, no scheduler interaction, and no complex inheritance hierarchy. 

GR4 handles:
- Invoking `processOne` with the appropriate SIMD width  
- Managing input/output flow  
- Integrating the block into larger pipelines  

This model makes it easy to write clean, testable DSP components while still benefiting from the full performance of the GR4 runtime.

---


### Plugin system with built-in reflection

GR4 introduces a plugin architecture with **built-in reflection**, providing a single source of truth for block definitions.

This enables:

- Automatic discovery of blocks and capabilities  
- Schema-driven tooling and UI generation  
- Dynamic validation and configuration  
- Integration with higher-level systems, including AI-driven workflows  

This is a foundational capability that unlocks an entire class of tooling beyond traditional DSP pipelines.

---


### SIMD-first architecture and SimdFFT

GR4 is designed from the ground up for SIMD efficiency.

The introduction of **SimdFFT** (PR #671) extends this philosophy to FFT operations:

- SIMD-aware FFT implementation aligned with GR4 pipelines  
- Reduced overhead compared to traditional FFT integration approaches  
- Seamless integration with compile-time composition and fused pipelines  

This makes SIMD a **first-class concern across the entire signal chain**, not just isolated kernels.

![SimdFFTResults](SimdFFTResults.png)

Try out the new FFT blocks on your machine and see how your benchmarks compare.

Reference: https://github.com/fair-acc/gnuradio4/pull/671


---

### Performance that redefines the baseline

GR4 delivers substantial performance improvements:

- 2–10× gains from eliminating inter-block buffers  
- Orders-of-magnitude improvements in feedback-heavy systems (e.g., IIR, PLL)  
- Fully compile-time execution reaching **tens of GS/s**  

These improvements fundamentally expand what is feasible in GNU Radio.

---

### WebAssembly (WASM) support

GR4 includes improved **WebAssembly support**, enabling DSP pipelines to run directly in browser and sandboxed environments.

This unlocks entirely new classes of applications:

- Interactive, browser-based DSP tools  
- Portable demos and training environments  
- Secure, sandboxed execution of signal processing pipelines  

A great example of this direction is **OpenDigitizer**, which demonstrates how GR4-based processing can be paired with a modern web frontend. By running DSP components in WASM and connecting them to browser-based visualization and control, applications can be delivered with zero local installation—just a URL.

![OpenDigitizer](OpenDigitizer.png)

This model enables:

- Rich, interactive SDR applications accessible from anywhere  
- Tight integration between DSP pipelines and modern web UIs  
- Rapid sharing of experiments, demos, and tools  

WASM support in GR4 is a key step toward making signal processing more accessible, portable, and integrated with modern application ecosystems.

---

### SoapySDR integration

Built-in **SoapySDR integration** simplifies access to a wide range of SDR hardware:

- Unified hardware abstraction layer  
- Easier portability across devices  
- Cleaner separation between DSP logic and hardware  

---

### Permissive core licensing

The GR4 core adopts a more **permissive licensing model**, lowering barriers for adoption:

- Easier integration into commercial systems  
- Greater flexibility for mixed-license environments  
- Broader ecosystem participation  

---

### Integrated filter design capabilities

GR4 continues to build on GNU Radio’s long-standing strength in **digital filter design**, while evolving toward tighter integration with the runtime and modern APIs.

With ongoing work (PR #218), filter design is becoming part of a more **unified, end-to-end system design workflow**:

- Filter design is no longer a disconnected preprocessing step  
- Designed filters integrate naturally into compile-time pipelines  
- Parameters can be tied into runtime configuration and reflection metadata  
- Enables future schema-driven and tool-generated filter design  

This aligns with GR4’s broader direction: a **cohesive signal processing environment** rather than a collection of loosely connected tools.

There are even console plotting tools included in the designer to keep dependencies minimal!

![FilterDesign](FilterDesign.png)


Reference: https://github.com/fair-acc/gnuradio4/pull/218

---

### macOS support (seeking contributors)

macOS ARM64 support has made strong progress, with builds now passing tests (PR #725).

To reach full production readiness, this effort needs a dedicated maintainer to track issues, maintain CI stability, and drive platform polish.

Contributors interested in helping push macOS support forward are encouraged to get involved.

Reference: https://github.com/fair-acc/gnuradio4/pull/725

---

## Recent API Changes

As GR4 approaches production readiness, the API has been simplified and stabilized.  But take note of these things if you have already been working with applications in GR4.

### Connection API

The fluent `.connect().to()` chain has been removed in favor of explicit calls returning `std::expected`:

```cpp
// runtime (plugins, Python, GRC)
graph.connect(src, "out", sink, "in");

// compile-time (C++)
graph.connect<"out", "in">(source, sink);

// chaining
graph.connect<"out", "in">(src, filter)
    .and_then([&] {
        return graph.connect<"out", "in">(filter, sink);
    });
```

This improves clarity, removes implicit behavior, and aligns with modern C++ design patterns.

---

### Compile-Time Block Composition

`BlockMerging.hpp` introduces compile-time composition of block types.

#### Linear merge

```cpp
using Chain = gr::Merge<ScaleA<float>, "out", ScaleB<float>, "in">;
auto& merged = graph.emplaceBlock<Chain>();
```

#### Feedback merge

```cpp
using IIR = gr::FeedbackMerge<
    Adder<float>, "out",
    Scale<float, alpha>, "out", "in2"
>;
```

#### Parallel paths

```cpp
using Diff = gr::SplitMergeCombine<
    gr::OutputSigns<+1.0f, -1.0f>,
    ScaleA,
    ScaleB
>;
```

These constructs can be composed and nested to build highly optimized signal graphs.

---

### Performance Snapshot

Single-threaded benchmarks (GCC 15, `-O3`, float):

```
┌──────────────────────────────┬───────────┬───────────────┬───────────┐
│ topology                     │ runtime   │ merged        │ constexpr │
├──────────────────────────────┼───────────┼───────────────┼───────────┤
│ src→copy→sink                │ 162 MS/s  │ 381 MS/s      │ 25.4 GS/s │
│ src→mult→div→add→sink        │  87 MS/s  │ 187 MS/s      │ 25.4 GS/s │
│ src→(mult→div→add)^10→sink   │  10 MS/s  │ 133 MS/s      │  2.9 GS/s │
│ IIR low-pass (feedback)      │ 994 kS/s  │ 113 MS/s      │ 656 MS/s  │
└──────────────────────────────┴───────────┴───────────────┴───────────┘
```

---

### SIMD-Aware Sources

Source blocks can implement:

```cpp
processOne(constexpr_value auto N)
```

The runtime selects an optimal SIMD width automatically.

---

### Build and Platform Notes

- `find_package(gnuradio4)` supported for installed prefixes  
- Optional libc++ support under Clang  
- Improved WASM support via Emscripten  

---

## Getting Involved

We would like to get more contributions and applications developed using GR4.  Please give RC1 a try - Further changes beyond RC1 are expected to be additive.

Areas where contributions are especially impactful:

- Block development and migration from GNU Radio 3  
- Hardware integration (SoapySDR and beyond)  
- Tooling and ecosystem development  
- Platform support (including macOS)  
- Documentation and examples  

For more info:
* Repository: https://github.com/gnuradio/gnuradio4 (synced to tagged releases from https://github.com/fair-acc/gnuradio4)
* Join the conversation on https://chat.gnuradio.org
* Email us architecture@gnuradio.org with any questions or comments - tell us about your use case and results!!!

---

## Acknowledgements

GNU Radio 4 represents years of work across a dedicated and growing community.  GR4 has been co-developed by the team at FAIR (GSI), where it originated from the need for a modern, high-performance framework for real-time accelerator signal processing, and that environment has strongly influenced its design goals around safety, latency, throughput, and determinism, which benefits users across industries and applications. At the same time, development is happening in the open, with ongoing contributions and direction from the broader GNU Radio community, reflecting a mix of research, industry, and hobbyist use cases rather than a single institutional focus, but we are grateful for the incredible development effort and foundation from the researchers at FAIR.  

---

## Summary

GNU Radio 4.0 RC1 marks a turning point:

- A **stable, near-production platform**  
- A **modern, high-performance architecture**  
- A foundation for the next generation of DSP applications  

If you’ve been waiting to adopt GNU Radio 4—the time is now.





