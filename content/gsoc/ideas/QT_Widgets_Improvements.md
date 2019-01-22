---
title: "QT Widgets Improvements"
name: "QT_Widgets_Improvements"
hash: "7642631426118119884"
mentors: ["","Tim O'Shea",""]
type: idea
---


The gr-qtgui in-tree component provides some QT widgets for signal visualization. This component needs some improvement to become more useful.<br />
This project is cleanly divided into several sub-projects:


* Add new widgets

  * Compass display (e.g. for direction-finding applications)

  * MPEG display (e.g. for video demod output)

  * Matrix sink (e.g. for radar Doppler/range plane visualization, or 2D-equalizer taps visualization)


* Improve current widgets

  * Better code structure to make the current widgets more manageable, extensible and remove code duplication between widgets

  * More Control Panels on other widgets (follow lead on the frequency sink)

  * Improve UI, make more intuitive, more power to mouse users

  * Set trigger point with mouse


* Integration / Support for QT Creator

  * QML design

  * Allow to build full GUI applications from, say, GRC

## Prerequisites
Familiarity with QT is essential. Widgets are written in C+'', so some C''+ knowledge is also required. Python skills are highly useful.


