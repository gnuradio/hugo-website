---
title: "GSoC Standalone GRC : week-4"
author: "Rahul Balaji"
date: "2023-06-30"
categories: ["GSoC", "GRC"]
---

hello,

So we are almost a month into this project's timeline. I am elated to have the project progress to such an extent from the days of week-0. This of course could not be possible without the constant support from the organisation and my mentors. The greatest of projects are always of collaborative effort, and I am reminded of that fact everyday while working to accomplish this task. I would like to thank you all once again for all of your support. I look forward to work further to complete the project in the following week as well. With that, lets get to the updates for week-4.

### Modularizing options block:

So most of the translation for options.block.yml is over this week, however, there are some bugs that prevent GRC from running, so one of the first hurdles to cross this week is to remove all such errors that arise from this translation of options.block.yml and ensure that it runs smoothly as expected.

Once this task is accomplished, we are going to build a manager object for the workflows.yml files that will be managed during runtime. Then we make use of the information provided by the instance of the manager in the options block, which configures based on that information.

### Syncing gnuradio-companion:

Moving ahead, the coming week, we can have a discussion on the repo name, and how we will be moving the code pushed so far into the newly created repo.

so the general steps are :

1) To decide on a name for the repo.
2) create a repo on gnuradio org.
3) Update the main branch of [https://github.com/haru-02/GRC](https://github.com/haru-02/GRC).
4) create a PR on gnuradio, that  
	- removes all files in `grc/` except for the CMakeLists.txt, and the `conf.in` files  
	- adds new repo as a submodule `grc/<NAME_OF_THE_NEW_REPO`  
	- changes `grc/CMakeLists.txt` use the files form inside the submodule for the install

This brings us to the end of updates on week-4.
