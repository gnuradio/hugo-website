---
type: "grcon/grcon18"
layout: "presentation"
title: "RadioML Redux: GTRI Efforts on the Army Signal Classification Challenge"
authors: []
slides: "7-Bhattacharjea-RadioML_Redux.pdf"
youtube: "https://www.youtube.com/watch?v=HOrGe6BsgLI"
conference-day: "Thursday"
weight: 4
---
In the spring of 2018, the Army Signal Classification Challenge (ASCC) was announced to enhance the state-of-the-art in signal classification and modulation recognition using machine learning. A series of I/Q data examples were provided by the US government, and for each example, the modulation type was provided as one among a class of 24 modulations. The challenge was to develop machine learning-based algorithms to perform automatic modulation recognition after training on, and learning from, the labeled examples. This talk discusses the novel solutions that were developed by Georgia Tech Research Institute (GTRI) to address the ASCC, as well as how the government dataset fits into the broader efforts by members of the GNU Radio community to develop benchmark datasets for radio machine learning (radioml). The novel aspects to be covered include:

* Neural networks for streaming I/Q samples
* Complex-valued behavior out of real-valued machine learning frameworks
* New activation functions for complex-valued I/Q data
* Max-pooling for complex-valued data
* Balancing "zero-human-expert" philosophy with heuristics that improve performance
* Evolutionary algorithms for hyperparameter optimization
