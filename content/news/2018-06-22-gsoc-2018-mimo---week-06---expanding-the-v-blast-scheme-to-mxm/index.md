---
title: "GSoC 2018 MIMO - Week 06 - Expanding the V-BLAST scheme to MxM"
author: "Moritz Luca Schmid"
date: "2018-06-22"
externalurl: "https://mimognuradio.wordpress.com/2018/06/22/week-06-expanding-the-spatial-mux-to-mxm/"
sponsored: "0"
aliases: ["blog/gsoc-2018-mimo---week-06---expanding-the-v-blast-scheme-to-mxm"]
---
I expanded the 2×2 V-BLAST zero-forcing scheme to a general MxM scheme. For a general MxM matrix, the inverse cannot be precalculated by hand as I did for the 1×1 and 2×2 scheme. The inversion of a possibly large channel matrix can quickly get a very complex problem which needs a lot of computation power, especially if it is recalculated frequently, for example each micro second when assuming a coherence time of 1μs and therefore a CSI update rate of 1MHz.
<!--more-->