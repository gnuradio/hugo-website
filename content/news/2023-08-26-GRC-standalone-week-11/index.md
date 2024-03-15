---
title: "GSoC Standalone GRC : week-11"
author: "Rahul Balaji"
date: "2023-08-26"
categories: ["GSoC", "GRC"]
---

Hello,

With week 11, finally over, we are almost at the end of the term for GSoC'23.

I am truly grateful for the opportunity to work for GNU-Radio. I applied for GSoC with the desire to contribute to this project and to improve myself as a software engineer, and I am happy to have achieved it to an extent.

With the end of week-11, let us take a review of the deliverables decided on at the start of the project in the proposal, how the project has evolved over the coding period, and what the future goals for the project are.

### Initial goals of the proposal:

The initial main goals for the proposal were defined by me on a surface level with a very basic knowledge on GNU Radio and GNU Radio Companion. They are,

- Move GRC to a separate repository and to remove dependency on GNU Radio.
- Modularize options block.
- Modularize templates block.
- Allowing templating with Jinja.

However, as the project progressed, I discovered a lot of sub-goals that were to be achieved for this project.

### The goals achieved during the term:

Here are the list of goals achieved during the term of GSoC coding period.

- Separation of GRC from GNU Radio with intact commit history and to remove dependency with GNU Radio, making it run standalone.
- Restructuring of GRC for packaging using FLIT.
- Removing options block as a .yml file and translating it to python.
- defining a .workflow.yml file that can allow the user to customise parameters.
- adding workflow manager that can parse the .workflow.yml file and manage the parameters.
- Each of these steps have been tested and reviewed every week, with bugs noted and fixed at regular intervals.

As seen, there have been a multitude of major steps that required proper planning and focus during the coding period, pushing a little of the goals originally planned a bit behind schedule.

### The current state of the project:

As the project stands, it has achieved the objective to kick- start the separation of GRC from GNU Radio as a standalone project, and I have no doubt that it soon will be available for public use for use-cases beyond GNU Radio.

I am excited to see the evolution of GNU Radio as a project and as a community with the inclusion of this project.

### Future goals:

Of course, with the current state of the project still being a work in progress, there are a few goals that are still left to be completed in order to be recognised as a project which is production ready.

we need to,

- Override the functions rewrite and import_data from block.py, which almost completes the need to modularize options block.
- Modularize templates.
- Allow for templating using Jinja.

I will continue to work on these goals beyond the term for this project, and will also contribute to the organisation with my newfound experience.

Once again, I would like to thank my mentors [Håkon Vågsether](https://github.com/haakov), [Sebastian Koslowski](https://github.com/skoslowski), [Josh Morman](https://github.com/mormj) and also the community for their invaluable support during this term. Thank you for joining me on this coding journey.

A Github gist of the progress of the project for the same can also be found [here](https://gist.github.com/haru-02/369d1e15feb3b82247eb3fece75754c4), It contains all the links to the proposal, the repository, and also all the other weekly reports.
