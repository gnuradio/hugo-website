---
title: "GSoC Standalone GRC : week-8"
author: "Rahul Balaji"
date: "2023-08-01"
categories: ["GSoC", "GRC"]
---

Hello,

So this week, the focus was to make .yml files for different workflows with which we could test the module and to fix any errors in the 
implementation of code.

There are also a few changes required in the way we store the data as currently, the module does not store them properly. So we need to 
make changes in workflow-manager to make sure all workflows are stored properly.

A possible implementation is to make a "workflow" class that stores an instance of all the information available which will then be 
accessed by other modules.

We currently only made one .yml file which will not help us make a good test case. So we need at-least one more such file to conduct 
proper test case to see if we can switch workflows.

### What's next ?

As discussed earlier the focus of the coming week is:

1) Change the way the info is handled in the workflow manager.
2) Create a new workflow class to store the info.
3) Also focus on making a proper test case for the module with proper .yml files.

That brings us to the end of updates for week 8.
