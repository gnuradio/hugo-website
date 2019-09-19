---
type: "grcon/grcon19"
layout: "presentation"
title: "The GNU Radio PDU Utilities"
slides: "Jacob Gilbert - The gr pdu utils.pdf"
authors: ['Jacob Gilbert']
youtube: ""
conference-day: Thursday
weight: 2 
---
The GNU Radio PDU Utilities [1] serve to extend functionality of GR’s in-tree PDU API, and enhance user ability to understand and interact with the RF Spectrum. At a basic level there are a number of general purpose PDU ‘feature’ blocks analogous to GR streaming DSP blocks such as filtering and data conversion, an efficient implementation of M. Ossman’s WPCR [2], and many basic data operations applied to PDUs. Additionally, there is a straightforward and robust set of blocks for converting between streaming and PDU based data that can be combined with the GR Timing Utilities [3] to enable precise interaction with low-complexity bursty communication systems (e.g.: FHSS ISM Radios). In a more general sense, this module allow SDR applications to react to RF energy at a given time/frequency with RF energy at a specified time/frequency which is something that can be surprisingly difficult using in-tree functionality.

This talk will include an overview of the PDU Utilities theory of operation, provide details of implementation, summarize key blocks, describe how it fits into existing GR design practices, and discuss how it compares to other packet-data implementation patterns that exist within GR such as T. O'Shea's gr-eventstream and GR’s Packet Communications API. The talk will also cover some off-label applications of the features contained in this module.

While it was published in early 2018, announced on the mailing list [4], and included in PyBombs, the PDU Utilities addresses a number of common requests on Slack and the GR mailing list. It was intended for demo at the 2018 conference but scheduling conflicts prevented submission. This module will see a significant update from what is available on github today in the June timeframe as approvals for open source release work their way through DOE approval chains. It may slip slightly but the update will be published before the 2019 conference.

[1] https://github.com/sandialabs/gr-pdu_utils  
[2] https://github.com/mossmann/clock-recovery/blob/master/wpcr.py  
[3] https://github.com/sandialabs/gr-timing_utils  
[4] http://lists.gnu.org/archive/html/discuss-gnuradio/2018-04/msg00103.html  

Sandia National Laboratories is a multimission laboratory managed and operated by National Technology & Engineering Solutions of Sandia, LLC, a wholly owned subsidiary of Honeywell International Inc., for the U.S. Department of Energy’s National Nuclear Security Administration under contract DE-NA0003525.
