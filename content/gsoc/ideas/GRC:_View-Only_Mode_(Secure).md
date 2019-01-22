---
title: "GRC: View-Only Mode (Secure)"
name: "GRC:_View-Only_Mode_(Secure)"
hash: "1283570219066312005"
mentors: ["","Sebastian Koslowski","",""]
type: idea
---


When a flowgraph from an untrusted source is opened if GRC, arbitrary Python code can be executed. This poses a potential security risk. Storing the all evaluated values of all parameters within a flow graph (.grc) file would allow us to open such flow graphs without compromising security. No code would be have to executed to draw the flow graph and block parameters can be viewed safely. Only if the flow graph is modified the user would have to choose to trust the flow graph thus enabling normal eval operations.

## Prerequisites
GRC is implemented using Python. So, Python should be known pretty well.

## Outcome
Safely view other people's flowgraphs without putting your PC at risk.


