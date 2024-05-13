---
title: "Elemental Building Blocks: Filtering time-series data"
author: "Marcus Müller"
date: "2016-05-24"
sponsored: "0"
aliases: ["/blog/filtering-time-series-data__elemental-building-blocks", "/news/filtering-time-series-data__elemental-building-blocks"]
---

# Elemental Building Blocks: Filtering time-series data

## Solving typical problems – the easy way

## Post by Marcus Müller

Over at [StackOverflow](https://stackoverflow.com/) and [DSP Stackexchange](https://dsp.stackexchange.com/), I often meet questions that involve processing of data.

People wonder how to do basic tasks such as in [this question on how to filter sets of EEG data](https://dsp.stackexchange.com/questions/28965/filtering-frequency-bands-out-of-a-signal) into different, EEG-typical frequency bands, efficiently:<!--more-->

> **Let&#8217;s say I have a 2 second data set taken at 220Hz sample rate and I would like to filter out the frequency bands associated with the EEG Spectrum:**
<p>$$\begin{align}<br />
\Delta:&amp; [1,3]\text{ Hz}\\<br />
\theta:&amp; [4,7]\text{ Hz}\\<br />
\alpha_1:&amp; [8,9]\text{ Hz}\\<br />
\alpha_2:&amp; [10,12]\text{ Hz}\\<br />
\beta_1:&amp; [13,17]\text{ Hz}\\<br />
\beta_2:&amp; [18,30]\text{ Hz}\\<br />
\gamma_1:&amp; [31,40]\text{ Hz}\\<br />
\gamma_2:&amp; [41,50]\text{ Hz}<br />
\end{align}<br />
$$</p>
**What would be the most simple approach to do this ?**

Well, of course, being the GNU Radio fan that I am, my reaction to this was:

> So the simplest approach was this GNU Radio companion-designed flowgraph:

![GNU Radio companion filtering flow graph](https://i.stack.imgur.com/LFQ7o.png "https://i.stack.imgur.com/LFQ7o.png")


GNU Radio companion filtering flow graph
Generating [this flowgraph file](https://gist.githubusercontent.com/marcusmueller/8c09996dd1d3857fbd35fb3265dfceda/raw/444fa1e9ff94a3f551c1ac3f5e1b2ab9cfeb8175/banpdasses.grc) generates a python program that uses GNU Radio to do the signal processing, on as many CPU cores as there are.
You can then run it as

    $ ./bandpass_filters.py -f {input file containing float32 samples, one after the other}


&nbsp;

## What&#8217;s happening underneath

This isn&#8217;t the *most* elegant way of doing things, but I think the idea is straightforward:

1. We take his eight passbands, and instantiate a **Band Pass Filter** block for each
1. As an input, we take a simple sample file – just 32bit floats, one after the other. Any programming language I can think of has a way of writing a file containing arrays of raw binary data – so let&#8217;s just use our **File Source** block to get the samples from a file.
1. To set the file name we&#8217;re reading the samples from, we use a **Parameter**. That is a woefully underused feature – more on it below.
1. And we&#8217;ll finally write out the resulting digital signals (=sequences of numbers) to files with the input file name and a suffix describing the individual pass band it contains, using **File Sink** blocks.

Now, what happens when you click the &#8220;generate&#8221; button <img class="alignnone wp-image-1039 size-full" src="https://gnuradio.org/wp-content/uploads/2016/05/generate_button.png" alt="generate button" width="82" height="33" /> is that GNU Radio companion takes this graphical flow graph and converts it to a python file, which instantiates all the blocks, and tells the GNU Radio Runtime which blocks are connected, and then tells GNU Radio to start and run the flow graph, until its work is done.

What happens at execution time is exactly that:

- Python loads the GNU Radio Runtime library, which contains all the logic on how to get samples in and out of blocks, and the libraries containing the actual blocks (here, that&#8217;s gr-blocks for the File blocks, and gr-filter for the Filters), it evaluates the flags given at the command line according to the Parameters we used (that&#8217;s why the &#8220;-f&#8221; works)
- instantiates these Blocks (which happen to be C++ classes, which get mapped to Python classes here), and
- using connect calls it tells the GNU Radio runtime that as soon  as the flow graph is started, the individual blocks should be asked to produce, process and consume samples, hand them over to the right &#8220;downstream&#8221; block, and repeat that until everything is done.

So although it seems we designed our DSP in a very abstract, &#8220;sandboxy&#8221; environment, we actually just generated a bit of Python code that uses a C++ library.

All the actual marshalling (i.e. calling the individual blocks&#8217; signal processing functionality on input data, and making sure the output of the filters reaches the file sinks) is done in C++; which also means that we don&#8217;t really need to worry a lot about performance here; we just design our flow graph.

&nbsp;

## Things are **fast** (and how we figure out whether they are)

Talking about real-world performance:: Each of these blocks runs in its own thread; that means that this flow graph will automatically make the most of multicore CPUs which you&#8217;re likely to find in anything you want to run signal processing on – but it will still work, reasonably well, even on a single CPU, because these filters were written and refined with performance in mind.

William John-Pierre Duhe, the person asking this question, did so, originally, on the Mathematica Stackexchange daughter site; for him, who seemingly has a strong Mathematica background, 16GB of samples seem to be &#8220;a lot of data&#8221;, as he mentions in [a comment](https://dsp.stackexchange.com/questions/28965/filtering-frequency-bands-out-of-a-signal#comment54289_28972):

>
**I have roughly 16gb of data laying there that will need to be analyzed! Thanks again for this feedback it helps immensely. I have a workflow application designed in Mathematica and it&#8217;s important I stay in that environment but I appreciate the suggestion to switch the MatLab. I will potential move this to LABVIEW later to be embedded on an FPGA also.**


He&#8217;s seriously considering using an FPGA; now, that **is** a smart move if you need your data filtered efficiently in real time at high rates, no doubt, but that data is lying somewhere on a hard drive or SSD; it&#8217;s sampled at 220 Hz. Doing this in hardware does sound a bit like overkill, doesn&#8217;t it? How comes someone who wants to stay in a Mathematica environment even considers doing hardware?

Now, I couldn&#8217;t help but simply test how far we&#8217;ll be getting with my flow graph:

> I tried this with a 200MB &#8220;dummy&#8221; file, creating eight 100MB output files – this, to and from a temp directory, took a whole 13 seconds. I&#8217;m pretty hopeful it&#8217;s fast enough! I benchmarked this a bit, and it seems the source is able to push through about 20 million samples per second; the slow part is the writing to the 8 files.

Notice how, even if we assume that starting Python, and loading the GNU Radio libraries took a whole second, the effective time spent (13s) on these 50 million samples says we&#8217;re doing but a little more than 4MS/s, and yet I claim that one can do about 20 MS/s on my machine – how can I come to that bold statement?

I actually modified the flow graph a bit just to be able to ignore the file interactions. For that, I used GNU Radio Companion&#8217;s &#8220;disable&#8221; <img class="alignnone wp-image-1040 size-full" src="https://gnuradio.org/wp-content/uploads/2016/05/disable.png" alt="disable button" width="24" height="23" /> functionality to get rid of all the File Sources and Sinks. They get grayed out and will not be present in the Python code that GRC is going to generate:


![](https://gnuradio.org/wp-content/uploads/2016/05/bandpasses_null.grc_.png "https://gnuradio.org/wp-content/uploads/2016/05/bandpasses_null.grc_.png")


Excerpt of modified flow graph for benchmarking

In their place, I added **Null Sinks** and a **Null Source** instead. These do nothing then constantly consume all their input (and do nothing with it), and constantly producing zeros as fast as possible to their output, respectively. I added a **Head** block, which makes the flow graph terminate after a Billion items have been produced – otherwise, it would run on forever.

So, executing this flow graph, we can eliminate the whole file read `and write overhead, and just focus on the operations GNU Radio still needs to do (we&#8217;re neglecting the fact that the Null Source has to write zeros, and the Head block copies its in- to its output, but aside from that (which should be really fast), there&#8217;s no touching of these samples).

The **Probe Rate** block just counts the number of items that &#8220;whoosh&#8221; by, and sends them as a message to the **Message Debug** block, which prints them:


    ******* MESSAGE DEBUG PRINT ********
	(((rate_now . 2.03108e+07) (rate_avg . 2.07489e+07)))
	************************************
	******* MESSAGE DEBUG PRINT ********
	(((rate_now . 2.09953e+07) (rate_avg . 2.07858e+07)))
	************************************
	******* MESSAGE DEBUG PRINT ********
	(((rate_now . 2.08624e+07) (rate_avg . 2.07973e+07)))
	************************************
	...



As you can see, we&#8217;re doing about \\(2\cdot10^7\\) S/s = 20MS/s here – pretty OK for for having nine filters here.

Next time, I&#8217;ll write a shorter blog post about why we&#8217;re using the ninth, &#8220;pre-filter&#8221; here, and why the output files are sampled at half the input rate.
