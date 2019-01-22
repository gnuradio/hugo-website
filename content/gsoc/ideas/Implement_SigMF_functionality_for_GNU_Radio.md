---
title: "Implement SigMF functionality for GNU Radio"
name: "Implement_SigMF_functionality_for_GNU_Radio"
hash: "-9105982812584563944"
mentors: ["","Bastian Bloessl",""]
type: idea
---


SigMF is the "Signal Metadata Format" that was defined during the 2017 DARPA Hackfest in Brussels. Its purpose is to annotate raw binary dumps of signals with metadata, thus giving meaning to a raw mass of samples.<br />
SigMF is specified and has a minimal reference [implementation](https://github.com/gnuradio/sigmf).

GNU Radio needs its own implementation of SigMF that ties into the block structure. The following things need to be written:


* Source and Sink blocks for SigMF (similar to the current metadata blocks)

* Converters for files generated with the current metadata file formats

* Static analysis tools using SigMF

## Prerequisites
Basic understanding of how to write GNU Radio blocks is required. Also, the student needs to explain that she or he has understood the concepts of SigMF, although SigMF is a very simple, JSON-based file format.<br />
Depending on the precise path that the student and the mentor define, experience in GUI development would also be useful.

## Outcome
The source and sink blocks are by the far the most important outcomes of this project. We estimate it would take about a third of the active coding time to implement those, and have them merged around the midterms.<br />
This leaves plenty of time for further development. The next most important task are the converters, so existing metadata files will continue to be useful. After that, the student should define own tasks based on their interests. A very relevant problem is the ability to effectively visualize metadata in combination with signals.


