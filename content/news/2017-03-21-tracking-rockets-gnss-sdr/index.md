---
title: "Tracking Rockets Gnss SDR"
author: "Philip Hahn"
date: "2017-03-21"
sponsored: "0"
aliases: ["blog/tracking-rockets-gnss-sdr"]
---

# Tracking Rockets with GNSS-SDR

I&#8217;ve always liked radio. As a kid I met a HAM with a nice mobile setup and was enthralled. I loved the idea &#8211;  but being a quiet, introverted kid I could never see myself [ragchewing](https://en.wikipedia.org/wiki/Contact_(amateur_radio)) for hours on end. I lived in a fairly rural area where packet wasn&#8217;t an option. So I read and listened to shortwave and local repeaters off and on through the years, until I discovered the [SoftRock](http://www.wb5rvz.com/sdr/) software-defined radio kit &#8211; which I bought instantly, and promptly discovered my soldering skills were not up to snuff. Interest waxed and waned until the RTL-SDR came along. BINGO! As an engineer with a heavy programming background, the idea of building code for radio was appealing. So I played with GNU Radio and listened to the HAM bands and &#8230; boredom. I had no mission, no goal, just playing around wasn&#8217;t doing it for me. Back on the shelf.

Until I ran into [Paul Breed](https://unreasonablerocket.blogspot.com/). I knew Paul by way of an online email list, he reached out on Twitter asking for help getting a software-defined GPS solution working on an Intel Compute Stick. Knowing Paul&#8217;s background I knew rockets were involved. Now, I had a mission and a reason to learn! I responded to Paul and he sent a package containing another RTL-SDR, an Intel Compute Stick and antenna and a few other goodies. I put together a [quick real-time demo](https://sdrgps.blogspot.com/2015/12/first-proof-of-concept-gps-fix-in.html) using GNSS-SDRLIB and RTKLIB.

Which, unfortunately, is the most popular post on my blog by a long shot. While the codes served their purpose in getting a demo put together quickly, the combination of software packages was finnicky at best (evidenced by the number of responses to that post) and offered little opportunity for further learning. I moved on to working on a more robust solution for post-flight reconstruction. The initial capability idea was to take an RTL-SDR and the Intel compute stick, log RF data before and during flight, then download the RF baseband to a desktop computer and post-process the trajectory. We were able to test this capability offline &#8211; I wrote a script which would create a unique filename and call [rtl_sdr](https://osmocom.org/projects/sdr/wiki/rtl-sdr#rtl_sdr) to record the RF. After downloading the file I was able to reconstruct the position using [gnss-sdr](http://gnss-sdr.org/), an open-source GNSS receiver built on GNU Radio. After testing a few antenna and LNA combinations, we moved on to flight testing.

Paul designed the GPS payload for his rocket, which he shows off below. The blue box outlines a 6DOF IMU, the orange box is a [LNA4ALL low noise amplifier](https://lna4all.blogspot.com/). On the reverse the orange box outlines a 2S LiPo battery, the green box a [Nooelec 0.5PPM TXCO in aluminum case](https://www.nooelec.com/store/sdr/sdr-receivers/nesdr-mini-plus.html) and the blue box an [Intel Compute Stick](http://www.intel.com/buy/us/en/product/desktop/intel-boxstck1a8lfc-463163) running Ubuntu, and the yellow trapezoid a quadrifilar antenna GPS antenna from [antennas.us](http://www.antennas.us/store/c/41-GPS-Antennas.html).

<img class="alignnone size-medium aligncenter" src="https://gnuradio.org/wp-content/uploads/2017/03/gps1.jpg" alt="gps1" width="600" height="424" />

<img class="alignnone aligncenter" src="https://gnuradio.org/wp-content/uploads/2017/03/gps2.jpg" alt="gps2" width="716" height="422" />

The payload is packaged inside the nose cone fairing of the rocket. Below, the rocket is mounted on the launch rail in a horizontal configuration. Before launch the rail is elevated to near vertical, but this orientation allows for easy handling of the rocket. At T-2 minutes (2 minutes prior to launch) the rocket begins acquiring data &#8211; Paul SSHs over WiFi into the Intel Compute Stick to trigger a script which calls[ rtl_sdr ](https://sdr.osmocom.org/trac/wiki/rtl-sdr#rtl_sdr)centered on the L1 frequency with a bandwidth of 2048000 Hz. Two minutes is sufficient time to get multiple GPS fixes on the pad prior to launch.

<img class="size-medium aligncenter" src="https://gnuradio.org/wp-content/uploads/2017/03/DSCN0865.jpg" alt="DSCN0865" width="600" height="450" />

And at T-0, smoke and flames!

<img class="size-medium aligncenter" src="https://gnuradio.org/wp-content/uploads/2017/03/Snapshot-3-Paul-Breed.png" alt="Snapshot 3 Paul Breed" width="798" height="250" />

This test flight took place on Febuary 6th, 2016.

Now, with data in hand the fun part begins &#8211; figuring out why you could reconstruct the data on a bench test but not on the flight data![ Initially](https://sdrgps.blogspot.com/2016/04/paul-breed-rocket-flight-test-data.html), I could get a fix on the pad, but as soon as the rocket motor ignited I lost all of the GPS satellites and could not get a valid fix during the next 30 seconds of flight (after about 30 seconds the parachute deployed and the GPS antenna would be dangling upside down under chutes &#8211; this was visible in the RF as we could see satellites being rapidly acquired and dropped in succession). After a little fiddling I was able to get a brief [fix near apogee](https://sdrgps.blogspot.com/2016/04/paul-breed-rocket-flight-test-data-2.html), which coincided well with the commercial GPS logger ([Big Red Bee](http://www.bigredbee.com/)) Paul had on board.

Now wait a second &#8211; if Paul had a commercial GPS logger why were we going through all this trouble? Commercial devices have to abide by the so-called [COCOM limits](https://en.wikipedia.org/wiki/Coordinating_Committee_for_Multilateral_Export_Controls#Legacy) which restrict commercial GPS operation to Mach numbers &lt; 1 and altitudes &lt; 59,000ft. Most commercial devices are even more restricted than this &#8211; the GPS logger on board much like my current RF solution completely loses it at launch and doesn&#8217;t regain a GPS fix until under chutes.

At a dead end, I [turned to Reddit](https://www.reddit.com/r/RTLSDR/comments/4dccb3/help_flew_an_rtlsdr_on_a_rocket_capturing_gps_l1/) &#8211; advertising the data set and looking for help figuring out why I couldn&#8217;t decode GPS in flight. User jddes identified distinct interference at 150 seconds, when the rocket lifts off. Inspecting the RF with [Inspectrum ](https://github.com/miek/inspectrum)it is quite clear that there is some on-off keying going on:

<img class="size-medium aligncenter" src="https://gnuradio.org/wp-content/uploads/2017/03/inspectrum.jpg" alt="inspectrum" width="600" height="416" />

Paul was able to confirm:

<img class="aligncenter size-full" src="https://gnuradio.org/wp-content/uploads/2017/03/reddit.jpg" alt="reddit" width="1332" height="296" />

So now we had a clue. I used some [band pass filters](https://sdrgps.blogspot.com/2016/04/paul-breed-rocket-test-flight-data-3.html) in an attempt to remove the noise. Although it removed some signal in the process, I lost the noise and was able to get my best to-date fix in gnss-sdr:

<img class="alignnone size-full" src="https://gnuradio.org/wp-content/uploads/2017/03/updated.png" alt="updated" width="600" height="381" />

The red GPS tracker and the gnss-sdr output line up well at liftoff and gnss-sdr recovers and gives about 15 seconds of valid fixes late in flight prior to parachute deployment. The red GPS tracker recovers under chutes and follows the vehicle to the ground.

Almost done. At this point I didn&#8217;t know enough to dig into the gnss-sdr code to look for bugs or compare models so I turned my attention back to a code I had evaluated and discarded, SoftGNSS. It&#8217;s a standalone code which runs serially (acquire satellites once, iterate over the RF signal in a loop for each satellite) built in Matlab, so it had two strikes against it from the get-go. But it was a relatively simple to interrogate code which accompanied the textbook [A Software-Defined GPS and Galileo Receiver: A Single-Frequency Approach](https://www.amazon.com/Software-Defined-GPS-Galileo-Receiver-Single-Frequency/dp/0817643907). The code required numerous bug fixes (I maintain a cleaned up version [on github](https://github.com/hahnpv/SoftGNSS)), but ultimately I was able to track [from ground to apogee](https://sdrgps.blogspot.com/2016/08/softgnss-w5-satellites.html), as shown below. The red trace is the GPS tracker, the black trace is gnss-sdr and the yellow trace is SoftGNSS. 

<img class="aligncenter size-full" src="https://gnuradio.org/wp-content/uploads/2017/03/google_earth.jpg" alt="google_earth" width="1527" height="953" />

Now what? Well, I want to get an end-to-end solution working in gnss-sdr as this ultimately has traceability to real-time tracking. The Intel Compute stick might be a bit underpowered but the [Raspberry Pi 3 has demonstrated real-time tracking](https://zenodo.org/record/266493).

If you found this interesting I of course recommend you follow my blog [sdrgps.blogspot.com](https://sdrgps.blogspot.com/) where I&#8217;ve also looked at GPS simulation and simulated orbital rocket trajectories. I also highly recommend the book [Software-Defined GPS and Galileo Receiver: A Single-Frequency Approach](https://www.amazon.com/Software-Defined-GPS-Galileo-Receiver-Single-Frequency/dp/0817643907) if you are interested in GPS. For learning SDR, anything by [Balint Seeber](http://spench.net/) or Michael Ossman&#8217;s [SDR with HackRF](https://greatscottgadgets.com/sdr/) series are both great resources I used for learning GNU Radio.

## Philip Hahn
