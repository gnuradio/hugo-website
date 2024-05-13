---
title: "GSoC 2017 Retrospective"
author: "Martin Braun"
date: "2018-02-13"
sponsored: "0"
aliases: ["/blog/gsoc-2017-retrospective", "/news/gsoc-2017-retrospective"]
banner: gsoc.png
---

# GSoC 2017: A retrospective

With GSoC 2018 ahead of us, it&#8217;s time to look back what students worked on last year. We were very lucky to be accepted into both GSoC (Google Summer of Code) and SOCIS (Summer of Code in Space, a similar program run by the European Space Agency ESA).  Three projects were completed:

## C++ Code Generation with GRC

The ability to generate C++ applications from within GRC has been on our ideas list since the first GSoC. Finally, someone picked up the slack and implemented this feature: Håkon Vågsether from Norway.

Håkon did way more than simply enable this feature though. In a bold move, he started working off of our experimental Python 3 branch, and significantly contributed to making it more stable. As of the end of 2017, his code hasn&#8217;t been merged into the GNU Radio master branch yet, but that&#8217;s mostly because of outstanding dependencies. All of his code is available on public branches for perusal and testing.

In February 2018, Håkon was able to travel out to Brussels and meet fellow GNU Radio developers at FOSDEM, and gave a presentation on his work.

<iframe width="500" height="281" src="https://www.youtube.com/embed/JJ_OgduYXvs?feature=oembed&#038;wmode=opaque" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- [Håkon&#8217;s Blog](https://grccpp.wordpress.com/)
- [FOSDEM Talk Page](https://fosdem.org/2018/schedule/event/grccpp/)

## A DAB/DAB+ Transceiver Application

The evolution from analogue to digital audio broadcasting promises better sound quality and higher coverage, allowing even more radio<br />
stations to share the spectrum. Digital Audio Broadcasting (DAB/DAB+) is a very popular standard for digital radio and DAB/DAB+ stations can be<br />
found in Europe, Asia, and Australia. Thanks to Luca&#8217;s work during GSoC 2017, gr-dab enhances the GNU Radio project by providing a complete<br />
DAB/DAB+ transmitter and receiver application. Luca based his work on  an existing implementation of the physical layer and complemented it by<br />
implementing the entire transport protocol as well as a nice GUI application called &#8220;DABstep&#8221; that bundles all the features in one place.

DABStep &#8212; A GNU Radio-based DAB transceiver application

He described his work in weekly blog posts that can be found here: [https://dabtransceiver.wordpress.com/. ](https://dabtransceiver.wordpress.com/)Luca was able to travel to GRCon 2017 in San Diego to present his work as a poster.

## A Web-Based Display Mechanism (gr-bokehgui)

All visualizations in GNU Radio are typically done using the gr-qtgui widget set (or in some cases, the deprecated gr-wxgui elements). For standalone applications, that&#8217;s great &#8212; but what about web-based applications? Kartik Patel took it upon himself to enable visualization from GRC using the Bokeh toolkit.

<img class="alignnone wp-image-2030" src="/wp-content/uploads/2018/02/Waterfall_Screenshot-300x163.jpeg" alt="" width="758" height="412" srcset="/wp-content/uploads/2018/02/Waterfall_Screenshot-300x163.jpeg 300w, /wp-content/uploads/2018/02/Waterfall_Screenshot-1024x555.jpeg 1024w, /wp-content/uploads/2018/02/Waterfall_Screenshot.jpeg 1366w" sizes="(max-width: 758px) 100vw, 758px" />

Kartik has published his code as an out-of-tree module, but all necessary modifications to GNU Radio were upstreamed.

- [Kartik&#8217;s Blog](http://kartikpatel.in/GSoC2017/)
- [gr-bokehgui github page](https://github.com/kartikp1995/gr-bokehgui)
- [gr-bokehgui tutorial](http://kartikpatel.in/GSoC2017/tutorial/)

## Summary

With students and projects like these, we couldn&#8217;t be happier. We hope that all three students stay contributors to the project!

## Martin Braun
