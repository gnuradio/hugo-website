---
title: "Android"
name: "Android"
hash: "-3643262949841599838"
mentors: ["","Ben Hilburn",""]
type: idea
---


One effort of the past years was to improve Android support for GNU Radio. We're getting to a point where we've figured out '''how''' to do it, so the next step is to make it more accessible to users and developers.

The Android ecosystem is an entirely different beast from the rest of GNU Radio. To make writing Android/GR apps easy, the following needs to happen (and shall be part of this project):


* Improve support for development environment

  * Create Dockers for easy start of development

* Visualization classes for PSD, spectrogram and oscilloscope

  * Easy reuse in other apps, like the gr-qtgui widgets, but for Android SDKs

* Interactivity concepts

  * Gestures and config for radio params (e.g., freq, gain, bandwidth)

  * Create an example FM receiver app that allows easy channel selection etc. through motions and gestures

## Prerequisites

* Some Android experience

* Enjoy writing GUI widgets

* C++/Java experience


