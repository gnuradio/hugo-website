---
type: "grcon/grcon18"
layout: "presentation"
title: "Communicating with satellites using Starcoder: a lightweight gRPC server for managing GNU Radio flowgraphs in production"
authors: ["Reiichiro Nakano"]
slides: "8-Reiichiro_Nakano_Communicating_with_satellites.pdf"
youtube: ""
conference-day: "Tuesday"
weight: 9
---
At Infostellar, we are building a worldwide ground station network to allow satellite operators to communicate with their respective satellites around the world. As each satellite uses different methods for communication, we use GNU Radio flowgraphs to quickly switch between the different communication protocols our users require. With multiple satellites passing over our ground stations daily, every ground station must dynamically run multiple GNU Radio flowgraphs everyday. To keep our ground station business logic separate from the management of GNU Radio flowgraphs, we built an open-source project called Starcoder. Starcoder is a lightweight gRPC server that allows clients to start and stop multiple GNU Radio flowgraphs at will. It also provides direct hooks into these flowgraphs to allow clients to receive and send messages from or to the various blocks inside, through the same gRPC connection. To support this, Starcoder provides a direct mapping from GNU Radio Polymorphic Types (PMTs) to Google's language-neutral and platform-neutral protocol buffer format. This lets us run GNU Radio flowgraphs and send/receive PMTs from any programming language gRPC supports. In our ground station software written in Go, we have successfully used this functionality to receive data packets from satellites, send transmission commands, correct for Doppler shift, and more. The talk will include the motivations behind Starcoder, Infostellar's experience using it in production, a roadmap for future work, and some code examples from different programming languages for a quick demonstration of Starcoder's capabilities.
