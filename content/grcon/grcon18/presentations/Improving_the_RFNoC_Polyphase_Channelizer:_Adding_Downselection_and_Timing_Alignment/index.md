---
type: "grcon/grcon18"
layout: "presentation"
title: "Improving the RFNoC Polyphase Channelizer: Adding Downselection and Timing Alignment"
authors: ["EJ Kreinar"]
slides: "7-EJ_Kreinar_Polyphase_Channelizer.pdf"
youtube: "https://www.youtube.com/watch?v=WRO9VD6MYy4"
conference-day: "Tuesday"
weight: 8
---
The open-source FPGA-based polyphase channelizer presented in the 2017 GNU Radio conference is a great start [1], but is missing a few critical features to be truly useful in an embedded system: 1) an FPGA channelizer needs to be able to downselect output channels, such that the processor is not required to absorb the full bandwidth of the frontend; this enables narrowband channel selection out of a wideband signal capture. 2) baseband sample timestamp alignment for arbitrary channels needs to be calculated and aligned correctly so the timestamps are valid and accurate.

This talk addresses both concerns in detail and presents Hawkeye 360's solution. A demo application shows on-the-fly channel selection within the maritime VHF band with minimal processor usage on an embedded Zynq-based platform (Ettus E310). The FPGA and software improvements will be open-sourced to help improve the world of FPGA polyphase channelizers.

[1] https://pubs.gnuradio.org/index.php/grcon/article/view/18
