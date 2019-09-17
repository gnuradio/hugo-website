---
type: "grcon/grcon19"
layout: "presentation"
title: "Spectrum Monitoring Network: Tradeoffs, Results, and Future Directions"
slides: "noslides"
authors: ['Peter Mathys', 'Todd Schumann', 'Jeff Wepman', 'Mike Cotton']
youtube: ""
conference-day: Tuesday
weight: 5 
---
Due to its high inherent cost, there is limited use of professional grade test equipment in the field to monitor, or even identify, spectrum usage. Therefore, to supplement existing, high-accuracy measurements, there is a large interest in using lower-cost software defined radio (SDRs) receivers as replacements for the high-cost spectrum analyzers in RF measurement systems which are far less expensive to construct. Doing this allows measurements that are (1) continuous or at least much more frequent, (2) more densely located (in frequency and location), and (3) remotely controllable, and even allows additional measurements not practical using current solutions (e.g. simultaneous measurements of the same signal from many locations). However, there is an inherent trade-off in using the less expensive equipment to make these measurements in terms of price versus performance. Additionally, there can be a complex up-front characterization procedure necessary to ensure the accuracy of measurements.

Signal analyzers and SDRs can span several decades in terms of cost, some as low as $10, others over $10,000 or even $100,000. The obvious tradeoff between the different tiers is measurement accuracy/reliability versus the number of deployable sensors within a project budget. However, without a comparison between the tiers of SDRs, no intelligent determination can be made. In this report, we look at several of the key comparators between four representative signal analyzers/SDRs, representing a professional-grade (>$100,000), field-grade (>$10,000), middle-grade (~$1000), and economic-grade (<$100). We identify expected performance when used as a spectrum monitor and any additional circuitry considerations required to ensure that the analyzers are accurately measuring the spectrum. 

### Presentation Outline 

* Spectrum Monitoring Goals
* Signal Analyzer Architectures
* Superheterodyne vs Direct Conversion
* Examples of Signal Analyzers
    * Professional Grade: Keysight PxA N9030B
    * Field Grade: Keysight N6841A
    * Middle Grade: Ettus B210/B200 mini
    * Economic Grade: ADALM PLUTO Pluto SDR (Analog Devices)
* SDRs on a Chip
    * Analog Devices 9361, 9363, 9364
* Tradeoffs
    * Price
    * Performance
    * Size, Weight
    * Power Consumption
    * Sensor Density vs Performance Parameters
    * Example: Boulder Wireless Testbed (BWTB)
* System Architecture
* Sensor/RF Calibration
* Data Management
* User Access Management
* Computer Resources
* Single Board Computers
    * Example: Raspberry Pi 4
* Data Storage/Transmission
* Future Developments
* Signal Analyzers for Specific Bands vs Fully Tunable
* Using ML to Improve Monitoring
