---
type: "grcon/grcon18"
layout: "presentation"
title: "SirenJack: Cracking a ‘Secure’ Emergency Warning Siren System"
authors: ["Balint Seeber"]
slides: ""
youtube: "https://www.youtube.com/watch?v=1bznf118C-Y"
conference-day: "Wednesday"
weight: 9
---
SirenJack is a vulnerability that was found to affect radio-controlled emergency warning siren systems from ATI Systems. It allows a bad actor, with a $30 handheld radio and a laptop, to set off all sirens in a deployment. Hackers can trigger false alarms at will because the custom digital radio protocol does not implement encryption in vulnerable deployments.

Emergency warning siren systems are public safety tools used to alert the population of incidents, such as weather and man-made threats. They are widely deployed in cities, industrial sites, military installations and educational institutions across the US and abroad.

Sirens are often activated via a radio frequency (RF) communications system to provide coverage over a large area. Does the security of these RF-based systems match their status as critical infrastructure? The 2017 Dallas siren hack showed that many older siren systems are susceptible to replay attacks, but what about more modern ones?

I studied San Francisco's Outdoor Public Warning System, an ATI deployment, for two years to learn how it was controlled. After piecing together clues on siren poles, and searching the entire radio spectrum for one unknown signal, I found the system's frequency and began passive analysis of the protocol. Monitoring the weekly siren tests, I made sense of patterns in the raw binary data and found the system was insecure and vulnerable to attack.

This presentation will take you on the journey of the research, and detail the tools and techniques used, including leveraging Software Defined Radio and GNU Radio to collect and analyse massive sets of RF data, and analyse a custom digital protocol. It will also cover the Responsible Disclosure process with the vendor, their response, and subsequent change to the protocol. A proof-of-concept will be shown for good measure.
