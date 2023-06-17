---
title: "GSoC standalone GRC : week-2"
author: "Rahul Balaji"
date: "2023-06-16"
categories: ["GSoC", "GRC"]
---

hello,

time for the week 2 update! So what's new this week ?

### Installing GRC separately :

We had a lot of discussion on this particular topic, on what we could do for the users to let them install GRC separately. We arrived on the solution to use the flit packaging tool to make a package that can be installed using 'pip' as the code for python right now is completely python. So the files have been refactored to allow flit to build a package of GRC, but there are a few more steps left. The free desktop files and launchers are still yet to be refactored. For now, a person using only GRC on a terminal would theoretically be unaffected by this, but for the ones using GRC on a desktop, they would not be able to have the desktop launcher setup and installed properly as of now. So we are working on it. 

### How do we change the current workflow ?

When last week's goal was to understand the current workflow that is used to generate and run the flow-graphs built using GRC, this week's goal was to try and introduce ways to let the user have the control of it. Currently, we can generate code in python and c++, which are known as the workflows of GRC. To my current understanding of GRC, my vision is to allow the users to generate code in any language they want, or in a format specified by the users themselves. To what extent such features can be made, or the specifics of how and if it is possible to give users such freedom is currently under discussion with my mentors, and I am working towards a solution under their guidance.

### moving forward :

The work that lies ahead is largely exploratory. Coming up with ideas to redefine workflows and to think about ways to implement them will be a large chunk of the process. We need to figure out what files should a user provide to GRC to generate code in a different language or template.

This brings us to the end of updates for week-2.
