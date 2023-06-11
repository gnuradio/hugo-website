---
title: "GSoC: week-0"
author: "Rahul Balaji"
date: "2023-06-05"
categories: ["GSoC", "GRC"]
---

Hello,

So moving ahead, week 1 really marks the beginning of my coding period, and I am happy to share the progress we have made so far since the last post, so here are a few of my notes on the project.

### recording dependencies :

After separating GRC from gnuradio with the commit history of the folder still intact, I got to recording all the instances of imports from gnuradio in GRC. There are quite a few of them, some are used in files like ```params/dtypes.py``` that use ```gr.top_block()```, to prevent users from using certain ids, to simple imports that are used to just display the version number.

when we had the initial idea of removing all these dependencies, Jeff Long had suggested from the previous blog discussion that :

_If the end goal is to remove grc from the gnuradio repo (in addition to making it useful outside gnuradio), another task would be to identify reverse dependencies. GRC contains gnuradio-specific logic and blocks, which might be factored out and left as an app-specific plugin. App-specific plugins seem like a good idea anyway, if grc is to be usable in different domains._

which was a point that I had not considered before; and it made sense, that if we are to remove grc entirely from gnuradio as a standalone application, why not remove the related app-specific logic also entirely ?

But on the other hand, GRC at the moment is specifically, used in context along with gnuradio. Majority of the user-base will use grc for gnuradio even after it's extraction for the immediate future. So we decided on keeping those dependencies as they are for now, and make changes only if necessary.

### about defining the workflow of gnuradio_companion :

The discussions brought us to define "a modular workflow" which is one of the goals for this project. Currently, we have the functions to build a flowgraph and then to generate code. I aim to understand what happens when we call for these functions and essentially break down these functions into smaller workflows. To read code samples and understand the flow of code is one of the main goals for the coming week.

### other minor updates :

I have also added a pyproject.toml file for flit packaging. On discussions regarding how users will install the project, flit was agreed upon to be a tool that we can use to create the package. So I restructured the files, and created a toml file with configuration to make a package, but have encountered a few errors that needs some fixes.

### going forward :

This week, my objectives are to understand and breakdown the workflow of gnuradio companion and to work further on using flit to create a package so that it can be installed.


That brings us to the updates on week-1.