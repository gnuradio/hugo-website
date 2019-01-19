---
type: "grcon/grcon18"
layout: "presentation"
title: "CASPER: Security Monitoring Using Unintended RF Emissions"
authors: []
slides: "3-casper_v10a.pdf"
youtube: "https://www.youtube.com/watch?v=gDGzc_4wcjM"
conference-day: "Wednesday"
weight: 3
---
This presentation describes how the CASPER system uses GNU Radio and USRP hardware to detect unintended processor emissions in order to determine if there is anomalous activity occurring on a device being monitored. This approach provides a layer of security physically removed from target hardware, which does not require monitoring code running on the device itself.

Utilizing commercial SDRs and GNU Radio, RF signal features are extracted and used to classify the program states running on the target processor. By understanding the causes and the propagation of these unintended emanations, we show that RF emanations are present across the spectrum, but there are bands that lead to higher SNR features depending on the environment. We find these suitable bands empirically using an automated band scan, which employs multiple metrics to assess expected feature content including received power, kurtosis, and mode clustering. We have also developed multi-antenna processing algorithms to further extend range and increase the SNR of the extracted RF features by mitigating the interference encountered in realistic training and monitoring environments.

Of particular interest among targets are IoT devices, many of which are severely lacking in security controls, making them susceptible to a variety of threats. Due to the nature of these devices, and not having the ability to modify the source code, we rely on unsupervised machine learning methods based on clustering for both training and monitoring to identify known and unknown program states. Additionally, the system includes a framework for anomaly detection engines based on n-grams, statistical frequency, and control flow, to alert the system when the expected program execution has deviated in a newly detected way.

CASPER is an ongoing research project funded under the DARPA Leveraging the Analog Domain for Security (LADS) program. The views, opinions and/or findings expressed are those of the author and should not be interpreted as representing the official views or policies of the Department of Defense or the U.S. Government.
