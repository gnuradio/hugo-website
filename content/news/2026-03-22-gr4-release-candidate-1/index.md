---
title: "First Release Candidate for GR4"
date: "2026-03-22"
categories: ["gnuradio", "gr4", "community"]
aliases: ["/news/gr4-release-candidate-1"]
banner: "GR4-logo-embedded.svg"
---


GNU Radio 4.0 has come a really long way and has now reached its first release candidate (RC1). Recent changes on `main` give a fairly clear picture of where things are landing. There’s still work to do, but the overall direction is stabilizing, and improvements in compile times and memory usage make it practical to build GR4 even on lower-end machines.

One particular thing to take note is that the API is continuing to simplify. The latest set of changes removes some legacy patterns and replaces them with more direct, type-safe interfaces.

A set of user-facing API changes has landed on `main` around the RC1 milestone. The only required migration for most users is updating `connect()` calls. Everything else is additive.

## Connection API

The fluent `.connect().to()` chain has been removed. Connections are now explicit calls returning `std::expected<void, Error>`.

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

Errors are handled via `std::expected`; `ConnectionResult` is removed.

## Compile-Time Block Composition

`<gnuradio-4.0/BlockMerging.hpp>` introduces compile-time composition of block types. This removes runtime buffers and allows full inlining and vectorization.

### Linear merge

```cpp
using Chain = gr::Merge<ScaleA<float>, "out", ScaleB<float>, "in">;
auto& merged = graph.emplaceBlock<Chain>();
```

### Feedback merge

Used for IIR, PLL, AGC-style loops:

```
in ──> Fwd ──> out ──> Fb ──┐
       ^                    │
       └────────────────────┘
```

```cpp
using IIR = gr::FeedbackMerge<
    Adder<float>, "out",
    Scale<float, alpha>, "out", "in2"
>;
```

### Parallel paths

```cpp
using Diff = gr::SplitMergeCombine<
    gr::OutputSigns<+1.0f, -1.0f>,
    ScaleA,
    ScaleB
>;
```

These constructs are composable and can be nested arbitrarily.

## Performance

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

Observations:

* Eliminating inter-block buffers gives 2–10× improvement.
* Feedback topologies improve by ~100× due to removal of scheduler-driven single-sample loops.
* Fully compile-time (`constexpr`) execution removes the scheduler entirely and enables full SIMD vectorization, exceeding scalar implementations.

## SIMD-Aware Sources

Source blocks can implement:

```cpp
processOne(constexpr_value auto N)
```

The runtime selects an optimal SIMD width instead of invoking scalar loops.

## Build System

`find_package(gnuradio4)` now works for installed prefixes. libc++ is optional under Clang via `GR4_USE_LIBCXX`.

## Platform Notes

* WASM support improved (Emscripten 5.0.2)
* macOS ARM64 builds pass all tests but are not fully production-supported yet

## Summary

* Replace `.connect().to()` with `graph.connect(...)`
* Handle errors via `std::expected`
* Optional: adopt compile-time composition for performance-critical paths

## Acknowledgements

GR4 has been co-developed by the team at FAIR (GSI), where it originated from the need for a modern, high-performance framework for real-time accelerator signal processing, and that environment has strongly influenced its design goals around safety, latency, throughput, and determinism. At the same time, development is happening in the open, with ongoing contributions and direction from the broader GNU Radio community, reflecting a mix of research, industry, and hobbyist use cases rather than a single institutional focus, but we are grateful for the incredible development effort and foundation from the researchers at FAIR.  

## Getting Involved

We would like to get more contributions and applications developed using GR4.  Please give RC1 a try - Further changes beyond RC1 are expected to be additive.

* Repository: https://github.com/gnuradio/gnuradio4 (synced to tagged releases from https://github.com/fair-acc/gnuradio4)

* Join the conversation on https://chat.gnuradio.org

* Email us architecture@gnuradio.org with any questions

