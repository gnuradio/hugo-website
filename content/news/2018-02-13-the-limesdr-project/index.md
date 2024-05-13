---
title: "The Limesdr Project"
author: "limemicro"
date: "2018-02-13"
sponsored: "0"
aliases: ["/blog/the-limesdr-project", "/news/the-limesdr-project"]
---

# The LimeSDR Project

*Last month Lime presented at the GNU Radio Conference in San Diego and launched its follow up to the LimeSDR &#8211; a smaller, $139 software defined radio board. We asked for a look at the progress of LimeSDR project:*

A little over a year ago we launched the LimeSDR campaign. This has the backing of over 5,000 developers. The project has since grown, bringing with it carrier- and enterprise-class SDR equipment (LimeNET) and now a small, very low-cost one too.

On one hand we are asking operators and service providers to deploy app enabled, commoditised open source radio access  network hardware solutions. On the other hand we are enabling the developers, the crowd and everybody out there to make use of the radio that will ultimately be implemented and deployed by the operators and service providers.

Which means, if you have a great idea that works on LimeSDR, we can get into some more detailed discussions with our partner operators, or similar customers seeking to roll out a service. That’s why we’re working with Canonical/Ubuntu, to make sure that all the hardware platforms that we sent out there could benefit from availability of  associated applications that essentially make the whole ecosystem possible.

### **Where are we with operators**

Operators (we’ve announced two of our operator partners so far) are backing this idea publically; essential as they are also a driving force behind the eventual deployment of this technology.

BT/EE (the UK’s largest fixed and mobile telecom provider) wants to add coverage and we are concerned with technology as a potential for such deployments.

Vodafone (the world’s second largest mobile operator, with 516 million subscribers) is looking to add services on top of our Network in a Box solutions, providing end users with new applications and  services.

We are also working with a number of additional organisations to build the ecosystems &#8211; from additional operators, to silicon vendors, box manufacturers, system integrators and service providers . This ecosystem will ultimately take care of the eventual deployments &#8211; from silicon design to network definement.  The key aspect of this are the community of developers who could provide game changing applications that will run on most innovative networks of the future.

### **Applications**

From the commercial space we have the key software platforms, such as EPC from Quortus and LTE stack from Amarisoft. There are also a significant number of applications that includes GNU Radio applications. We’ve seen some developing applications on wide ranging CPUs from incredibly high-powered X86 based PCs  to Raspberry Pi &#8211; such as a receiver to listen for the International Space Station.

Some of our favourites so far have been:

#### ***Gqrx receiver for weather satellites, by Alexandru Csete***

One of the first tests that Alexandru Csete ran was as a receiver for the NOAA weather satellites. These constantly scan the earth and transmit in the VHF- and L-bands, making it (along with FM receivers) an ideal early project to run. And Information on how this was done is on Alexandre’s blog ([here](https://myriadrf.org/blog/first-tests-limesdr-gqrx/)).

Below are the first two NOAA weather satellite images received by Alexandru &#8211; the raw infrared sensor data (left), and thermal infrared.

<img class="size-medium" src="https://myriadrf.org/app/uploads/2016/05/limesdr-noaa19.jpg" width="2080" height="979" />

#### ***LTE ***

Organisations like Amarisoft and Quortus have now produced software solutions that together let you establish LTE networks. We have als seen an impressive  LTE demo from Eurecom’s Raymond Knopp.

In the test Raymond establishes a base station with the LimeSDR, running OpenAirinterface eNodeB software and operating at 10 MHz bandwidth. The resulting LTE cell enabled a 20 Mbps transfer rate for both down and uplink.

To find out more information about OpenAirInterface, including links to the code, installation instructions, documentation and tutorials, see the [OAI wiki](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home).

&lt;iframe src=&#8221;https://player.vimeo.com/video/170507191&#8243; width=&#8221;640&#8243; height=&#8221;360&#8243; frameborder=&#8221;0&#8243; webkitallowfullscreen mozallowfullscreen allowfullscreen&gt;&lt;/iframe&gt;

#### ***LoRa Modem***

[Josh Blum’s blog post](https://myriadrf.org/blog/lora-modem-limesdr/) on encoding and decoding in LoRa is worth a read.

Josh was among a select group of wireless developers that we gave a LimeSDR to during the campaign and in his blog he looks not just at how he creates the modem, but the essentials of modulation, techniques and encoding before setting up two PCs to exchange messages over the LimeSDR using the LoRa blocks.

<iframe src="https://www.youtube.com/embed/UAHQRHQD75U" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

## **Opening access to more people &#8211; the Mini**

At the GNU Radio Conference we announced the LimeSDR Mini crowdfunding campaign. The new board wasn’t created as a replacement for the LimeSDR, but to make it more affordable and increase access to this type of technology. And also to enable people to come up with applications beyond cellular, particularly IoT, but also any application-defined wireless connectivity.

You can see information on the campaign at Crowd Supply &#8211; [https://www.crowdsupply.com/lime-micro/limesdr-mini](https://www.crowdsupply.com/lime-micro/limesdr-mini).

We think the Mini will be ideally suited to IoT radio applications in addition to the above, but we’re already seeing people with more ideas &#8211; and we’d love to hear your thoughts on potential future developments.

Like the LimeSDR, the Mini uses the LMS7002M transceiver to give the flexibility. To bring the cost down to the point where we can sell it at $139 (originally $99 on earlybird) we’ve used the Altera MAX 10 FPGA, which has 16k, rather than 40k programmable logic gates. We’ve also taken the RF bandwidth down to 30.72 MHz, implemented SISO, rather than MIMO and the frequency range is now 10 MHz to 3.5 GHz.

The sample rate, the oscillator precision, the transmit power are, however, all the same as its bigger brother.

### **Next stages**

We want to get more people innovating with wireless systems and playing about to learn how it works. This means getting the technology into as many hands as possible &#8211; especially students, hobbyists and those who would never have been able to afford to access such technology until relatively recently. We want them to learn about wireless technology in a practical sense and be able to go all the way to products and applications, which can then be made available to operators and system integrators that are deploying networks.

For more information on the LimeSDR Mini, please visit [https://www.crowdsupply.com/lime-micro/limesdr-mini](https://www.crowdsupply.com/lime-micro/limesdr-mini).

<iframe src="https://player.vimeo.com/video/233749031" width="640" height="360" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

## limemicro
