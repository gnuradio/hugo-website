---
title: "Website Update: Goodbye Wordpress!"
author: "Andrej Rode"
date: 2018-05-09T12:18:12+02:00
draft: false
---
Today we switched over from a static dump of our old Wordpress instance to a new website based on markdown files and rendered by a custom flask application.
<!--more-->

This switch was necessary due to continuous severe security vulnabilities in Wordpress and a lack of knowledge about successfully hardening Wordpress (if that's even possible at all) among GNU Radio officers.

Our news, blog and event content is now (mostly) generated from the [gr-website repository](https://github.com/gnuradio/gr-website.git).
The GRCon 2018 website has been ported to the new structure as well. Content from previous GRCons is in the process of conversion.

There are still some bits and pieces missing which will be worked on in the upcoming weeks. Therefore the GNU Radio website might experience more frequent maintenance downtime. We try to keep downtimes as short as possible.

A website overhaul wouldn't have been possible without the great work of the GNU Radio officers Nate Temple and Andrej Rode.
