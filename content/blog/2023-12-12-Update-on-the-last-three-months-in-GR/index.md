---
title: "Update on the Last Three Months in GNU Radio"
author: "Marcus Müller"
date: "2023-12-12"
aliases: ["blog/update-on-2023-September-to-December"]
---

We tried to establish a bit of a newsletter. Here's what I've written down about what I think a wider audience would want to know *after* GRCon'23

GNU Radio Releases and Code Highlights
======================================

GNU Radio
---------

We released 3.10.8.0, and we're hoping to be on track for upcoming major packaging releases (mostly, Ubuntu's next Long Term Support release).

In the meantime, work on the main development branch is ongoing, with quite a few architectural experiments, many of which find a way as non-API-breaking enhancements to developer experience in GNU Radio 3.10.x.

VOLK - For Those Who Want to Math Faster
----------------------------------------

Much progress was made in GNU Radio, but also in one of the GNU Radio ecosystem projects: VOLK. [VOLK](https://libvolk.org), the Vector-Optimized Library of Kernels, might not be widely known, but it's a very handy collection of hand-optimized SIMD code for common numerical vector operations; comes with microbenchmarking, test-suit, automatic dispatching to the optimal implementation. It was spun off years ago to bundle the machine-specific vector operations that where strewn across GNU Radio's code base.

VOLK 3 saw the switch from GPLv3 to LGPLv3. Now we have a version 3.1.0, and I personally think that this is a release that's going to be surprisingly useful for a lot of people – whether you use the library as dynamically linked as is, or whether you include the headers you need directly in your platform-specific code.

I'd encourage everyone that can consume C or C++ APIs (or just C ABI) and who has a lot of numbers in contiguous memory to which they're applying mathematical operations: Give it a try, and complain extensively, on https://github.com/gnuradio/volk/ and in [chat](https://matrix.to/#/#volk:gnuradio.org).

SigMF - The Signal Metadata Format
----------------------------------

Exchanging data is paramount to science, and managing large amounts of signal data is important to the ever-growing field of Machine Learning for RF. SigMF itself is not a GNU Radio "spinoff", but it's been personally tightly coupled, and heavily supported, by GNU Radio and its community.

SigMF defines a metadata scheme for your RF recordings. Supplementing the several large-scale semantic metadata frameworks that exist in large-scale users of scientific data (like Zenodo, or the Helmholtz Metadata initiative), SigMF allows to standardize annotating whole RF signal recordings, and sections (in time and in frequency) in them, for example with detected interfering signals, possible transmissions and the classifier outputs putting these through ML algoriths, and allows for well-structured extension with use case-specific metadata. It's metadata that makes neither your librarian nor your programming team weep!

SigMF's [specification](https://github.com/sigmf/SigMF) had hit v1.0.0 January 2022, but I'm mentioning it now, because with the recent v1.1.3 release of the official [Python support module](https://github.com/sigmf/sigmf-python) it's now really ready for mass deployment.

We currently are very happy to see our friends at [IQEngine](https://iqengine.org) use it to display and edit live annotations! (Check out IQEngine if you need to share ginormous time signals with other people, by the way.)

GNU Radio Community Highlights
==============================

Next year we will see another European GNU Radio meeting, probably with very high-quality speakers from HPC computing and C++ standardization – keep your eyes out for official announcements!

GNU Radio will also be present at FOSDEM. We're happy that we can contribute to the "Software Defined Radio and Amateur Radio" devroom ([schedule](https://fosdem.org/2024/schedule/track/radio/)). We're sharing a booth with IQEngine. Come by and say hi!

Many will be happy to hear GRCon'23 videos [are now
available](https://www.youtube.com/@GNURadioProject/videos). We've got Lindy
Elkins-Tanton, head of NASA's Psyche mission [talking about leading large
projects, and of course, space
science](https://www.youtube.com/watch?v=wSEUCOyRHb0), we've got [Ralph
Steinhagen talking about GR 4.0 usage at the FAIR accelerator
facility](https://www.youtube.com/watch?v=UkSr18dk4HY), we have [Updates on
TorchSig, the Signal Processing ML
toolkit](https://www.youtube.com/watch?v=2OBGBa6Oq2c), and much more!
