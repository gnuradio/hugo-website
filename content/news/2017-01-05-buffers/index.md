---
title: "Behind the Veil: A Peek at GNU Radio’s Buffer Architecture"
author: "Marcus Müller"
date: "2017-01-05"
sponsored: "0"
aliases: ["blog/buffers"]
---
GNU Radio's job is making it easy to write awesome signal processing applications – and offering a block-based approach to accomplish that. Which, of course, means that there needs to be a high-throughput, low-overhead interface between blocks to exchange data:

{{< img "fromhtt*" "How do samples get transported through a flow graph?" >}}

## Different Marshalling Approaches

GNU Radio can be a bit surprising if you're used to digital signal processing that is based on handling a discrete set of buffers (e.g., sound card drivers). To understand the difference, here is a visualization of what software like sound card drivers do (**not** what GNU Radio does):

### Discrete Buffer Exchange

{{< img "classical_buffering*" "Pool-based discrete buffer handling: A Producer takes an empty buffer from the buffer pool, fills it with data, and hands it over to the Consumer, which uses the data, and returns the buffer to the buffer pool. That is **not** what GNU Radio does." >}}

### FIFOs in RAM

This is a bit different from what you often find in real-time Digital Signal Processors' (as in: the silicon chip) software, where data comes in at one end, often via hardware interrupts (e.g., from an integrated ADC), and then has to be processed as fast as possible with very limited RAM, and often with no means to have virtual memory, so that you have to be extra careful not to clutter your memory space with unused sections.

What one would intuitively want in this situation is some kind of FIFO (First In, First Out) queue:

{{< img "FIFO*" "A FIFO queue" >}}

One could implement something like this with a kind of shift register – whenever the consumer has read something, each sub-buffer gets moved to "the right". But: Copying data just to have it where you want to read it is almost always a bad idea; it puts an unnecessary load at least on the memory bus, if not also on the CPU, and DSP is usually either Memory-bandwidth or CPU-time bound, so that's exactly the kind of thing you'd want to avoid.

So, let's instead just **ignore** the buffers we've already read, then, and advance the **read pointer** every time we consume an item; the problem with that is that in order for this to work within a linear address space, you'd need to have (countably) infinitely many addresses – as time progresses on, the "written" end always proceeds towards new, unused addresses. Since we don't have infinite RAM, this can't work (at least not for any reasonable amount of time). Also, if you're on a operating system with virtual memory support, you'd have to ask for memory to be allocated (malloc'ed), and that is a notoriously slow operation (partially, because it includes a search for free memory, and because it often includes a context switch).

### Ring Buffers with AGUs

Digital Signal Processors often (and most famously for that: the 56k family of DSPs) have a unit built into their Address Generation Unit (AGU) that offers exactly that: A seemingly infinite linear address space.

What happens there is that you can program the AGU to "wrap" around at a certain address boundary – pretty much, a modulo operation on the addresses you use to access your data. That way, you can always advance your read and write pointers monotonously:

{{< img "ring-buffers*" "Ring Buffers with AGU support: you can simply move \"forward\" the pointers; the address generation unit will give you the right address to your data, as if memory was actually circular. From a software perspective, it doesn't matter where the actual boundary of linear memory is – all memory locations that you get and put data from/to are generated with that wrapping in mind automatically." >}}

One Problem that this approach does **not** solve is that if, for some reason, your producer is faster than the consumer, your write pointer might "overtake" the read pointer, and thus, you'd overwrite data that the consumer hasn't yet touched. You can also fail the other way around, by overtaking your write pointer with your read pointer, and processing data twice instead of waiting for the producer to actually give you new data. You typically need some additional logic to avoid that.

### Ring Buffers for Machines with MMU: The GNU Radio way

Memory Management Units (MMUs) are the heart of modern multi-task computing: These units within modern CPUs have the task of

- Converting physical RAM address ranges (which typically are scattered across the 32 or 64 bit address space range you theoretically have) to one linear address space (which is what the Operating System sees, or cares about) and, more importantly for us here,
- Translating between **pages** in this linear address space and the **virtual address space** that each process has.

On modern Operating Systems for general purpose computing (read: things like Windows NT and later, Linux, OS X, *BSD, …), each and every single process has its own address space, and can't access the address space of other processes. Elements, so-called **pages**, are **mapped** into that space from the linear address space (and back!). That's the **segmentation** that you notice when your program has a bug and tries to access an address that was never mapped into your process' address space &#8211; you get a SEGFAULT, or **segmentation fault**, on most unixoids, and a general access violation on Windows systems (they are the same thing).

But wait, that means, that by virtue of supporting that address space mapping in the first place, we can instruct the MMU to map the same page multiple times; including mapping them in a manner that allows us to emulate a circular buffer, if we're just a bit careful:

{{< img "mmuringbuffer*" "MMU tricks to emulate a ring buffer: By mapping the original pages twice, right behind the original, we can, for any "viewport" smaller or equal to the original ring buffer size, emulate the ring buffer. Shown is how three consecutive viewports of the same size, just a little more than a page size, can be mapped into the memory space. For simplicity, only two pages were shown; the same principle applies to buffers consisting of more pages, too." >}}

GNU Radio does exactly that: It asks the operating system to give it memory-mappable memory, and map twice, "back to back". Blocks then get called with pointers to the "earliest" position of a workload within this memory region – guaranteeing that they can access all memory they were offered in a linear fashion, as if they'd actually be dealing with hardware ring buffers.

## GNU Radio Buffers at Run Time

What happens with buffers at run time is that at flowgraph initialization every output buffer gets allocated once.

Then, the flowgraph starts to run. The GNU Radio Scheduler just "informs" the individual threads (each block has its own thread) how much output space it has and how much input there is in the "upstream" output (==own input) buffer.

Then, naturally, the sources call their work() function, which eventually return with a number of items they put in the circular output buffer. A condition variable on the block executors "receiving end(s)" of that output buffer gets updated, and thus, if these blocks aren't already work()ing themselves, they typically start to (with an updated number of input items available).

Hence, the flexibility for any block to consume as much input as it can/wants to is a core aspect of the GNU Radio contract – GNU Radio just <b class="moz-txt-star">asks</b> each block to produce as much as possible, because it has shown that maximum workload size leads to maximized throughput (which really isn't as surprising if you consider things like cache locality and linear memory fetching). This asking can be seen from a block developer's point of view by the fact that your work() function gets an noutput_items parameter, which contains how much output items you can produce at most, given the available output space, and if specified, the constraints you set for your input to output item relation (sync block, interpolator, decimator) and the available input.

### A run-time example

A typical flow graph might be:

{{< img "filesinksource*" "A minimal flowgraph" >}}

Notice there's only two separate buffers allocated here, the File Source's and the Multiply's output buffers.

Then, the flow graph execution starts. The block executors of the File Sink and Multiply blocks are blocked at this time – there's simply no input to be processed. However, the File Source doesn't care about any input buffer (it doesn't even have one) and calls its work() – that just happily fills let's say 4096 of the 8192 items worth of output buffer space it has.

Hence, the work function returns 4096 as the number of generated items, and the Multiply block executor gets notified that, hey, now there's input available.

Right after File Source's work() has returned, the executor checks whether its blocked by a lack of output buffer. It's not (only half has been filled), so it directly calls File Source's work() again. Simultaneously, the Multiply's work() gets called in its block executor.

However, for some random reason, Multiply can only consume 3000 of the 4096 items it's been offered at once. Of course, multiplication is relatively fast, so its work finishes before the second "round" of File Source's work() has finished. That means, of the 4096 items it leaves 1096 in its input buffer (==File Source's output buffer), and puts 3000 in its output buffer.

Both the upstream block executor is notified that there have been samples consumed, so that there's now 3000 items more circular output buffer space, as well as the downstream block executor (==File Sink's executor) that there's now input.

As mentioned, multiplication is probably faster than reading from a file. Which means that while File Source is still working (still in its second round), Multiply's work() is called again, with the request to process the remaining 1096 items. It does so.

After it returns, File Source still hasn't returned from its work(), so there's nothing to do for multiply just yet – it has to idle.

However, in a more complex flow graph, this would mean that it now doesn't use any CPU time until there's input to process, while both File Sink and File Source can work in parallel.

Heuristically, this mechanism of just "consuming how much there is, and producing how much output space there is, whichever is less" maximizes parallelism whilst also leading to relatively large "workload chunks" that are processed per individual call to work(). However, it's worth noting, that this leads to **nondeterministic** workload sizes that **will vary** during execution.
