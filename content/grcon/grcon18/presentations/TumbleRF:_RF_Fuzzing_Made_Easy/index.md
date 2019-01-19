---
type: "grcon/grcon18"
layout: "presentation"
title: "TumbleRF: RF Fuzzing Made Easy"
authors: ["Matt Knight"]
slides: "07-MattKnight-TumbleRF.pdf"
youtube: "https://www.youtube.com/watch?v=tSHxw3rBZTE"
conference-day: "Thursday"
weight: 7
---
This session introduces an open source software framework for fuzzing arbitrary RF protocols, all the way down to the PHY. While fuzzing has long been relied on by security researchers to identify software bugs, applying fuzzing methodologies to RF and hardware systems has historically been challenging due to siloed tools and the limited capabilities of commodity RF chipsets.

The TumbleRF fuzzing orchestration framework addresses these shortfalls by defining core fuzzing logic while abstracting a hardware interface API that can be mapped for compatibility with any RF driver. Thus, supporting a new radio involves merely extending an API, rather than writing a protocol-specific fuzzer from scratch.

Attendees can expect to leave this talk with an understanding of how RF and hardware physical layers actually work, and how to identify security issues that lie latent in these designs.
