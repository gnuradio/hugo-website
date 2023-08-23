---
title: "GSoC 2023 Qt Widgets Improvement Week-10 [ Refactoring and Bug Fixes ]"
author: "Rohit Bisht"
date: 2023-08-21T20:21:14+05:30
categories: ["GSoC", "QTgui"]
---

## Overview

In this week's update on my GSoC journey, I'm thrilled to share the progress I've made in the Qt GUI Refactoring project. Week 10 has been all about opening a new pull request and addressing some important issues, as well as improving the codebase for enhanced efficiency.

## Opening a Pull Request

One of the highlights of this week was opening a new pull request for the qt-gui-refactoring branch. The pull request aims to refactor redundant code and improve the overall functionality of the Qt GUI widget component. The pull request is currently under review and will be merged into the main repository once the review process is complete.

## Bug Fixes and Error Corrections

One notable change was made in the matrix sink component. In the previous implementation, a loop was consuming only a single vector out of the several available, resulting in the loss of data. To rectify this, I reworked the code to properly utilize all the available vectors.

## Rebase and Incorporating Latest Changes

To keep the codebase up-to-date and aligned with the latest developments in the upstream repository, I performed a rebase of the "qt-gui-refactoring" branch. This process involved incorporating the latest changes from the main repository while ensuring that my own changes remained intact and functional.
