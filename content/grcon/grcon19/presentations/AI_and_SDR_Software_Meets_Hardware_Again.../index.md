---
type: "grcon/grcon19"
layout: "presentation"
title: "AI and SDR: Software Meets Hardware Again..."
slides: ""
authors: ['Manuel Uhm', 'Jason Vidmar']
youtube: ""
conference-day: Tuesday
weight: 8
---
Over the course of the last 30 years, SDR has become the de facto industry standard for the implementation of waveforms for communications, both military and commercial. During that time, the desire for waveforms to be fully realized in software running on general purpose processors (GPPs) had to be tempered against size, weight and power (SWaP) restrictions that required compute intensive portions of the waveform software to be run on hardware such as field programmable gate arrays (FPGAs) or hardened IP accelerators. 

More recently, artificial intelligence (AI) and Machine Learning (ML) have come to the forefront of research efforts worldwide. Led by the development of open source ML frameworks, such as TensorFlow and PyTorch, there is again a desire for AI/ML algorithms to be fully realized in software which has to be balanced against SWaP restrictions, particularly for inference at the edge. Is the fate of AI/ML to follow the course of SDR technology development in combining both software and hardware development to get to market? 

Fortunately, there have been technology advancements in both the semiconductor and tools industry which will greatly influence the answer to this question. In this presentation, we will discuss a new category of heterogeneous processor, the Adaptive Compute Acceleration Platform (ACAP), and the supporting tools which will make hardware far more accessible to software developers and AI/data scientists, for both AI/ML processing, as well as increasingly compute intensive communication needs, such as anti-jam, MIMO and adaptive beam forming.
