---
title: "Filter Design Tool Enhancements"
name: "Filter_Design_Tool_Enhancements"
hash: "-1786154879759076196"
mentors: ["","Marcus Leech",""]
type: idea
---


GNU Radio provides many tools to design and use digital filters. Using these tools requires both some expertise in these areas as well as an understanding of the performance on the given platform. One example is the selection between FIR (convolution-based) and FFT (fast convolution-based) filters for different resampling rates. Another example is doing stages of filter decomposition when doing large down-sampling. Included in this is the polyphase filterbanks, which again are provided as primitive blocks that need tweaking to work.

This project is to improve our uses of these tools and blocks to make it more obvious to the users as well as automate some of the decisions for optimally using them. Some pointers:


* When used in GRC, we want to save the results of the tool in a local file or for use in actual blocks.

* It still currently runs on PyQWT, which is obsolete and needs to be updated to QT4/QT5

  * See https://github.com/trondeau/gnuradio/tree/filter/design_tool_newgui

* Add more support for filter design concepts and other filters.

  * Cascaded filters

  * Better support for creating PFB filters

## Prerequisites
Strong DSP background required. Python and QT knowledge highly useful (at least one of those is a must).


