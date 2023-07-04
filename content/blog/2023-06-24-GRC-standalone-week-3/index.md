---
title: "GSoC Standalone GRC : week-3"
author: "Rahul Balaji"
date: "2023-06-24"
categories: ["GSoC", "GRC"]
---

hello,

Here's the updates for week 3! there are quite a few developments for this week.

### The current objectives:

with the discussions of workflows underway, we also decided on two main objectives that are of prime focus for the coming weeks.

1) To start modularizing the options block.
2) To sync gnuradio-companion with the main project as a sub-module.

### Modularizing options block:

So in the folder src/blocks, we have .yml files that are essentially templates that are used to render actual python classes with attribute behind the scenes for GRC at runtime, like the ones defined in src/core/blocks.

So when we have the need for pluggable workflows, we have to translate the options.block.yml file from the current format to the python files like the one in the src/core/blocks, just as is for now and make sure that GRC still runs.

So we have the template which can be customised with a bunch of options. After this step, we will have a static file which essentially functions the same. Then, the next step would be to make the options be dynamic, where we allow the users to define the options through a yml file, and the options.py file will fetch these options from the .yml file. 

### About syncing companion back to gnuradio main project:

So to make sure that the changes we make get incorporated to the main project, we plan to open a new repo in gnuradio so that we can have gnuradio-companion be installed as a sub-module to gnuradio at the end of this project. This will also give me a good place within the org where I can regularly push my code changes.

That brings us to the end of updates on week 3.