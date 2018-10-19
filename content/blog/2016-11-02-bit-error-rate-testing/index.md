---
title: "Bit Error Rate Testing"
author: "Tim O'Shea"
date: "2016-11-02"
sponsored: "0"
aliases: ["blog/bit-error-rate-testing"]
---

# Bit Error Rate Testing

When testing modems, its often a good idea to make sure the bit error rate (BER) of your receiver lines up with what you might expect from theory.  To this end, GNU Radio has long needed a handful of blocks which make this easy.  Test equipment often has built in psuedo-random test bit sequence (PRBS) modes which can produce known long strings of whitened bits for this sort of testing, but we&#8217;ve not had handy blocks to do this in a nice way without manually using the lfsr block, xor block, and something to count bit errors.

I&#8217;ve added prbs_source_b and prbs_sink_b to the [gr-mapper](https://github.com/gr-vt/gr-mapper) OOT module which provide ready made blocks for this purpose.  An example flowgraph application has been provided in gr-mapper called &#8220;[prbs_test.grc](https://github.com/gr-vt/gr-mapper/blob/master/apps/prbs_test.grc)&#8221; which provides a QPSK loopback test of these BER calculation blocks.  For the moment its just printing statistics to screen and averaging them linearly from startup to the current time, at some point these could output async messages if they needed to be incorporated into a larger suite or some downstream logic, and in the case of wanting a recent-rolling BER rather than an absolute BER over the entire run, we could implement some kind of IIR based averaging in the update.  These aren&#8217;t super complicated, fancy or exciting blocks, but they are perhaps useful tools that others can use in modem verification!  Screenshot below &#8211;

These same blocks should work equally well over the air &#8212; or with other modulations, so long as your framing/sync keeps them properly aligned!

<img class="alignnone size-large wp-image-433" src="https://oshearesearch.com/wp-content/uploads/2016/11/ber_testing-1024x688.jpg" alt="ber_testing" width="680" height="457" />

(cross posted from [https://oshearesearch.com/index.php/2016/11/02/bit-error-rate-testing-in-gnu-radio/](https://oshearesearch.com/index.php/2016/11/02/bit-error-rate-testing-in-gnu-radio/))

## Tim O'Shea
