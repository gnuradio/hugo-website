---
type: "grcon/grcon18"
layout: "presentation"
title: "UHD for Pythonistas"
authors: ["Brent Stapleton"]
slides: "09-BrentStapleton-UHD_Pythonistas.pdf"
youtube: "https://www.youtube.com/watch?v=Vk4GACPLqFQ"
conference-day: "Thursday"
weight: 9
---
Ettus Research's USRP Hardware Driver (UHD) release 3.13 includes a new way to control and interact with USRPs, a Python API. User applications can now be developed in Python, with no need to recompile, cross languages, or use third party solutions. The Python API has already eased development of various USRP-based tests within Ettus Research.

In the recent Colosseum channel emulator project, a calibration solution was created which measured the EVM of a known waveform transmitted across pairs of USRPs. Development of this Python API-based framework was facilitated by Python's ability to rapidly iterate on and test designs.

The Python API has been used within Ettus Research to develop internal continuous integration tests. One example is the Multi-USRP API tester, which uses the Python API to probe all available Multi-USRP function calls. Because the Python API is meant to mirror the C++ Multi-USRP API, it can be used to verify that every facet behaves as expected. Additionally, many continuous integration tests which require only basic DSP have been simplified. For example, the USRP phase alignment testing has moved from GNU Radio flowgraphs to simple scripts which use only the Python API and NumPy. This has greatly reduced the amount of setup and configuration required for these tests.

Python has also grown to become a popular language for many DSP applications. Tooling for Python development has also made great strides in recent years, allowing UHD users to now leverage technologies like Jupyter Notebooks, Plotly, and others to aid in development, collaboration, and teaching. The Python API allows users to integrate their favorite Python modules with UHD without crossing languages manually, saving samples to file, or using some other form of IPC. For example, many machine learning frameworks have Python interfaces (such as TensorFlow, Scikit-Learn, and Theano), which can now be seamlessly combined with UHD. Furthermore, Ettus Research hopes that users will find new and novel ways to use Python modules in conjunction with UHD's Python API.
