---
title: "FreeSRP – A New USB Software-Defined Radio"
author: "Lukas Lao Beyer"
date: "2016-09-30"
sponsored: "0"
aliases: ["/blog/freesrp-new-usb-software-defined-radio", "/news/freesrp-new-usb-software-defined-radio"]
---

# FreeSRP – A New USB Software-Defined Radio

The [FreeSRP](http://electronics.kitchen/misc/freesrp) is a software-defined radio I’ve been working on for the past two years as a side project. It’s based on the [Analog Devices AD9364 transceiver](http://www.analog.com/en/products/rf-microwave/integrated-transceivers-transmitters-receivers/wideband-transceivers-ic/ad9364.html), a [Xilinx Artix 7 FPGA](http://www.xilinx.com/products/silicon-devices/fpga/artix-7.html) and the [Cypress EZ-USB FX3](http://www.cypress.com/products/ez-usb-fx3-superspeed-usb-30-peripheral-controller) USB 3.0 controller. This allows it to deliver:

- 56 MHz bandwidth
- 70 MHz to 6 GHz center frequency
- 12-bit resolution
- Full-duplex operation

Hardware and software will be [fully open source](https://github.com/FreeSRP), but I still want to do cleanup before releasing the FPGA design and USB controller firmware. [Schematics are available](https://s3.amazonaws.com/freesrp/prototype-r2/freesrp-sch.pdf), and the board layout will be released once all issues are fixed.

## Designing the hardware

When starting this project, I had very limited hardware design experience: The most complex PCB I had designed was low speed, two layer, and using through-hole or fairly large surface mount components. Therefore, I learned a lot by designing a multilayer board with multiple complex ICs and high frequency RF traces.

It took me three revisions to get the transceiver working.

Three FreeSRP revisions

The first revision had various issues in the power delivery system, but allowed me to verify the FPGA and USB controller were working. The second revision fixed all that, but there were problems in the pin assignments of the FPGA (a clock not routed to a clock-capable input) and in the support circuitry for the AD9364, which I could not get to work. Finally, the design is basically fully working in the third revision.

For more information on the hardware design process, you can [check out this article on my website](http://electronics.kitchen/misc/freesrp). In this post, I’ll focus on the firmware, FPGA design and software for the SDR.

## <a id="Writing_the_software_22"></a>Writing the software

There are several components in the system that need to be programmed in order to make it usable:

- A design for the FPGA that can interface with both the AD9364 and the USB controller
- Firmware for the USB controller
- Some form of driver for the PC

For the PC software, I decided to write a C++ library ([libfreesrp](https://github.com/FreeSRP/libfreesrp)) using [libusb](http://www.libusb.org/).

However, to actually make data processing user-friendly, I needed to integrate FreeSRP support into some signal processing framework. The obvious choice for this was GNU Radio, as it is widely used and open source. Its modular design would make writing extensions to it straightforward, and with its blocks being written in C++, interfacing with my library would be easy.

### <a id="GNURadio_integration_70"></a>GNU Radio integration

I considered writing a completely custom block for GNU Radio, but then I discovered the [gr-osmosdr](https://sdr.osmocom.org/trac/wiki/GrOsmoSDR) project. It’s a block that integrates support for most of the available SDRs, comes with various utilities such as a spectrum analyzer and a signal generator, and is used by [various other applications](https://sdr.osmocom.org/trac/wiki/GrOsmoSDR#KnownApps) (e.g. [Gqrx](http://gqrx.dk/), [AirProbe/gr-gsm](https://github.com/ptrkrysik/gr-gsm)). Thus, integrating FreeSRP support into gr-osmosdr would make my SDR compatible not only with the GNU Radio environment but also with all the existing applications using gr-osmosdr.

So I made a copy of gr-osmosdr, and it was very straightforward to incorporate support for my SDR as I just needed to look at what additions any of the other supported SDRs did to gr-osmosdr. I ended up only having to do minor changes to some general files in order for the build system and the general source/sink block implementations to be aware of the FreeSRP. I also needed to implement functions for setting frequency, bandwidth, sample rate, etc. For the implementation of the block’s `work`function, which actually produces or consumes the data accessible in GNU Radio’s flowgraph, I initially resorted to busy waiting on FIFOs of the data to be received/transmitted, which worked and allowed me to effortlessly start receiving and sending data, but was very inefficient. By now I have reimplemented it using libfreesrp’s callbacks and synchronization with the `work` function using [condition variables](https://en.wikipedia.org/wiki/Monitor_(synchronization)), which is how many of the other devices supported by gr-osmosdr do it.

Now, just by specifying `freesrp` in the device arguments to the gr-osmosdr block, everything works as it should, making the FreeSRP fully controllable with GNU Radio.

### Verifying correct data flow through the hardware

I started working on the GNU Radio support with the second revision hardware, which did not have a working transceiver. However, having GNU Radio support this early on turned out to be very useful for generating test signals that could be looped back and again received in GNU Radio. This allowed me to test the data transfer between the USB 3.0 controller and the FPGA, including the state machine in charge of doing the DMA transfers between the USB controller and the FPGA.

Before implementing data loopback, I resorted to a very simple approach using the “probe rate” GNU Radio block to verify the FreeSRP was consuming samples at the correct rate, which allowed me to quickly find errors in the FPGA state machine and drivers. For this, I implemented a simple counter in the FPGA to generate a fake received signal.

Ramp generated in the FPGA, received in GNU Radio (note the sample rate set in GNU Radio is ignored in this early version; it’s just hardcoded into the FPGA); sample rate displayed in the debug print

Next, I had to test the transmitter signal chain. This time I generated a signal in GNU Radio and connected it up to the sink block:

Signal generated in GNU Radio connected to the gr-osmosdr sink

Now, I needed to verify that the FPGA properly decoded the data it received: The driver outputs 32-bit word which should contain two 12-bit samples (I and Q) and an unused padding. By using the Integrated Logic Analyzer in the FPGA, I could get access to the 12-bit samples as decoded by the FPGA design, verifying that they are correctly encoded on the PC and properly extracted by the FPGA design.

I and Q signals at the end of the transmitter signal chain in the FPGA

The GNU Radio flowgraph was outputting sine/cosine waves, but the data got garbled somewhere in the signal chain! It turned out to be my libfreesrp library, which was not formatting the samples correctly.

With that fixed, I implemented a very simple loopback in the FPGA. This would allow me to verify both the transmitter and receiver signal chain.

Loopback GNU Radio flowchart

It almost worked, however, samples were periodically being lost and replaced with zeros instead. The following GNU Radio time sink displays the signal being generated in blue (for I) and red (for Q), and the signal looped back from the FreeSRP in green (for I) and black (for Q).

Loopback signal periodically dropping to zero

The periodicity of the fault indicated that the fault was most likely in the state machine that handles writing and reading samples to and from the USB controller: the transition to the write state was happening one cycle before data had propagated into the registers that contain the data to be written. Offsetting the write state by one cycle fixed that:

Once I finished the third revision prototype, I repeated that same process to verify the system was functioning properly. For loopback testing, I made use of the AD9364’s internal loopback: this way, the interface between FPGA and transceiver could be verified to be working.

## Experiments with the FreeSRP and GNU Radio

Now that the hardware and software were fully functional, I wanted to try decoding some real signals with the FreeSRP. I decided I’d try decoding GSM and Zigbee, mainly because there are existing GNU Radio out-of-tree (OOT) modules for both GSM and Zigbee: [gr-gsm](https://github.com/ptrkrysik/gr-gsm) and [gr-ieee802-15-4](https://github.com/bastibl/gr-ieee802-15-4). This would allow me to verify interoperability with the existing GNU Radio ecosystem.

### GSM

As all OOT modules use the CMake build system, compiling and installing them is very straightforward. In the module’s directory, you need to run:<br />
<code><br />
mkdir build # Creates a blank directory for the build to run in<br />
cd build<br />
cmake .. # Load CMake build script in root of the module's directory and run it<br />
make # Run the CMake-generated makefile</code><code><br />
sudo make install # Install the module<br />
sudo ldconfig </code>

gr-gsm comes with a variety of sample applications. The most interesting ones are grgsm_scanner and grgsm_livemon. grgsm_scanner tunes to different frequencies trying to find GSM broadcast channels it can get IDs and location area codes from, and then shows a list of nearby GSM basestations. As grgsm_scanner uses the gr-osmosdr block, which the FreeSRP is compatible with, you can just tell it to use the FreeSRP in the device arguments:

gr-gsm scanner results

Note that gr-gsm scanner was not written with the FreeSRP in mind, but thanks to using GNU Radio and gr-osmosdr, everything just works.

grgsm_livemon lets you tune into one of the GSM broadcast channels, decodes the data received, and re-transmits it on your local network. This allows you to use [Wireshark](https://wireshark.org/), a network packet analysis program, to see the decoded packets.

The following screenshot shows a slightly modified version of grgsm_livemon running. Modifying it is very easy, as the program is just a GNU Radio flowgraph you can open in GRC (located in `apps/grgsm_livemon.grc`). The big colorful spectrum is a [gr-fosphor](https://sdr.osmocom.org/trac/wiki/fosphor) sink which I added to grgsm_livemon’s flowchart. The window on the right is grgsm_livemon’s usual interface, and the output on the bottom shows the raw decoded packets.

### 802.15.4 (Zigbee)

Having some XBee Zigbee-compatible modules on hand, I wanted to try interfacing with them. This would also allow me to test transmitting in a real-world protocol. Again, being able to use an existing OOT module implementing the 802.15.4 standard (gr-ieee802-15-4) was not only convenient but also a way of verifying compatibility and proper behavior of the FreeSRP GNU Radio sink.

To install the module the same procedure used for gr-gsm can be followed. However, gr-ieee802-15-4 also includes hierarchical blocks used in the Zigbee transceiver reference flowcharts. Because of that, these hierarchical blocks (located in `examples/ieee802_15_4_*_PHY.grc`) need to be opened in GRC and installed for GRC to recognize later using the &#8220;Generate&#8221; command. To generate and install the block, just press F5.

The examples that come with gr-ieee802-15-4 are made for the Rime Communications Stack, so I stripped them down to contain only the actual Zigbee encoding/decoding, and added a TCP source to accept messages to send on the local network. Received messages go into a TCP sink other applications can connect to on the local network, providing a very easy to use interface between the GNU Radio flowchart and other applications.

Zigbee transceiver flowchart using gr-ieee802-15-4

For a simple demo, I wrote two Python scripts: one connects to the XBee (the hardware Zigbee transceiver) over USB, and the other one connects to the two TCP ports the GNU Radio flowchart provides. Both scripts have a simple, chatroom-like interface that allow entering text to be transmitted, and show messages received over the 802.15.4 protocol.

### Details of the Driver Implementation

#### <a id="FPGA_design_and_USB_controller_34"></a>FPGA design and USB controller

Right now, the FPGA doesn’t do much apart from being a bridge between the AD9364 and the USB controller. Also, because it was just easier to work with, I decided to add a MicroBlaze soft processor for running the AD9364 SPI driver that performs all the necessary transceiver calibrations and settings. This interfaces with the USB controller over UART. I’ll soon move the AD9364 driver onto the USB controller, which has a fairly high performance ARM core.

The AD9364 outputs received samples on a 12-bit port, alternating I and Q. There’s a second 12-bit port where alternating I and Q values for the transmitter can be input. The AD9364 also provides a DDR clock corresponding to the configured sample rate. In the receiver signal path, the samples are first deinterleaved an then stored in a 24-bit wide FIFO buffer.

The FX3 USB controller has a DMA mechanism by which the FPGA can directly write to or read from the FX3’s buffers using a 32-bit data bus, a 2-bit address for choosing the buffer and some flags for signaling availability of empty/full buffers or requesting to read/write. So, when there are enough received samples in the FPGA’s receiver FIFO and the FX3 is ready to receive, the state machine controlling the FX3 interface (called “general programmable interface”, GPIF) writes samples from its FIFO into the FX3’s memory.

The FX3 is configured to have multiple of these buffers, such that full buffers can be emptied after processing USB bulk-IN transfers for receiver data while empty buffers get filled again with the data the FPGA writes.

Right now, only 24 of the 32 available bits are used, fitting one full sample’s I and Q values and discarding the other 8 available bits for simplicity. To achieve full bandwidth in full-duplex operation using the full 32 bits will be required.

Transmitting is analogous to receiving, and in full-duplex operation, the GPIF state machine on the FPGA alternates between reading and writing samples.

The USB controller provides four endpoints:

- INTERRUPT OUT, for sending commands to the MicroBlaze running the AD9364 driver
- INTERRUPT IN, for receiving errors or responses from these commands
- BULK OUT, for submitting data to be transmitted
- BULK IN, for receiving samples

When starting up, the FPGA is not configured, and the INTERRUPT OUT endpoint can be used to send a configuration bitstream to the FPGA.

#### <a id="libfreesrp_57"></a>libfreesrp

The library for communicating with the FreeSRP is very simple. For receiving and transmitting, it uses libusb’s asynchronous interface. This way, many transfers can be queued to be most efficiently processed by the operating system. When the transfers are processed, callbacks get called that extract the samples or prepare new samples and submit new transfers.

When starting to receive or transmit, the user specifies a callback that gets called once data is available or data for transmitting is needed.

Sending commands to configure center frequency, sample rate, gain, etc. uses libusb’s synchronous interface. It just sends a 16 byte command containing command ID and a parameter, and then waits for another 16 byte response which can contain an error ID and a parameter.

## <a id="Future_plans_81"></a>Future plans

I’ve already been contacted by gr-osmosdr’s developer, Dimitri Stolnikov, inviting me to merge my changes back to the official gr-osmosdr. I will definitely do that once I’m happy with libfreesrp’s API and my implementation for gr-osmosdr.

When I eliminate the MicroBlaze processor and move its functions onto the FX3, the FPGA will be almost empty. I’d like to experiment with using this free space to do on-board, real-time signal processing.

What I’d still like to do is proper characterization of the RF performance. I haven’t gotten around to doing that yet as I’m still working on the software and I don’t have the easiest access to the required test instruments.

I’m also currently working on a new revision of the FreeSRP, which will include a connector for adding hardware expansions and fix the last remaining issues, but I’m pretty sure not much else will change.

## <a id="Resources_90"></a>Resources

- [FreeSRP project page](http://electronics.kitchen/freesrp)
- [Building an SDR from scratch](http://electronics.kitchen/misc/freesrp), my first post on the FreeSRP
- [FreeSRP source code on GitHub](https://github.com/FreeSRP)

&nbsp;

## Lukas Lao Beyer
