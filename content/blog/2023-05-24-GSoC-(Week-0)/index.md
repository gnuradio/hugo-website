---
title: "GSoC: week-0"
author: "Rahul Balaji"
date: "2023-05-24"
categories: ["GSoC", "GRC"]
---

Hello, 

I am Rahul Balaji, a new contributor to GNU Radio. I have been selected to undertake this project as a Google Summer of Code. 

### so what's the project about ?

Over time, we have come to realise that GRC has some use-cases outside GNU Radio, and that it has somewhat become it's own standalone application. Different orgs also have maintained their own forks of GRC.

That brings us to mainly 3 objectives that must be achieved by this project :

1. Extract GRC from GR, so that people can install it as a standalone application and select workflows.
2. Make GRC more modular, especially the block templates.
3. To allow templating with Jinja.

Testing and bug-fixes will also be conducted throughout this project to ensure that the program works as intended.

### About extracting GRC from GR

After discussion with my mentors, we agreed on a few milestones that define the successful extraction of GRC from GR.

1. Separate the GRC folder into a new repository from GNU Radio, while keeping the commit history of GRC.
2. Next, we need to record all the files in the GRC folder that use imports from GNU Radio.
3. Next, we need to replace these dependencies so that GRC can run as a standalone application.
4. Ideally, we would also like to provide the option where a user, after installing GRC, can "select" the version on GNU Radio that they have locally installed on their system.

My vision for the first month following up to the midterm evaluation for GSoC is to achieve these milestones.

### About modularizing templates and Jinja

The objectives of modularizing the templates and to allow templating using jinja are objectives that I wish to present for my endterm evaluation. I plan to break down these objectives and analyze them in further detail beyond my proposal after I achieve the extraction of GRC.

### So how do we plan on users installing GRC ?

The current idea is to use flit to make a package, so that users can install it using pip, as all of it's code is python. So, I am also learning on how we can create this package. This will affect the documentation moving forward, especially how we install GNU Radio and GRC.

### The progress so far

The official coding period begins on may 29th. However, I have already created a repository where I have extracted the GRC folder from GNU Radio and have managed to retain the commit history. You can find the repo [here](https://github.com/haru-02/GRC)

Currently, I am recording all dependencies of GRC on GNU Radio, i.e, the files which import gr as `from gnuradio import gr`. I am trying to learn and understand why each file imports it, if they do.

For example in main.py, gr is imported to source the version number of gnuradio so it can display it, as GRC and GNU Radio share the same version number. So if we remove this import, how will we display the new version number ? Do we hardcode it into the pyproject.toml file and source it from there, or get it from git ? I am trying to find the answers to such questions with the help of my mentors.

### Project timeline

I have also attached my proposal for this project with a detailed timeline here. They may be subject to slight changes timeline wise as it was just a prototype prior to my selection, but there won't be too much of deviation from what has been set. [Here's](https://github.com/haru-02/gsoc-proposal) the proposal, titled "GRC: Standalone applications and pluggable workflows".

### Going forward

For the next week, my goal is to finish recording most instances of gr imports in the repository and to make a list of the functionalities they are used for, so that we can then discuss on how to replace them effectively.

Before we go, I would like to express my sincere gratitude to the community and especially my mentors Håkon Vågsether, Josh morman and Sebastian Koslowski. They have helped me immensely in setting realistic goals, and also helping me realize potential solution methods and the problems that I have to tackle while undertaking this project.

That brings us to the updates on week-0.
