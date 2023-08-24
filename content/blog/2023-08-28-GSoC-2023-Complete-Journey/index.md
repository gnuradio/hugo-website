---
title: "GSoC 2023 Qt Widgets Improvement Recap [ Complete Journey ]"
author: "Rohit Bisht"
date: 2023-08-24T05:34:25+05:30
categories: ["GSoC", "QTgui"]
---

{{<figure src="https://summerofcode.withgoogle.com/assets/media/logo.svg" width="800px">}}

*As the summer draws to a close, I am thrilled to present the culmination of my efforts in the GSoC 2023 project focused on enhancing the Qt Widgets for GNU Radio. This journey has been a rewarding experience, and I am excited to share the progress and achievements made over the course of this project.*

#### Basic Info

* **Name :** Rohit Bisht
* **Email :** rbtunes02@gmail.com
* **Github Username :** [R-ohit-B-isht](https://github.com/R-ohit-B-isht)
* **LinkedIn :** [Rohit Bisht](https://www.linkedin.com/in/rohit-bisht-a96b581bb/)
* **Organization :** [GNU Radio](https://github.com/gnuradio/gnuradio)
* **Project Title :** Qt Widgets Improvement
* **Project Mentors :** [Håkon Vågsether](https://github.com/haakov), [Andrej Rode](https://github.com/noc0lour)



## Project Overview

The goal of this project was to elevate the user experience of GNU Radio flowgraphs by introducing new GUI sinks, refactoring existing Qt GUI sinks, and integrating Qt Designer with GNU Radio. This comprehensive approach aimed to provide users with more intuitive visualizations, customizable interfaces, and an overall enhanced workflow.

## New GUI Sinks :

#### **[Matrix Sink]((https://wiki.gnuradio.org/index.php?title=QT_GUI_Matrix_Sink))**

The Matrix Sink was conceived as a powerful tool for visualizing matrix data in a dynamic and insightful way. The journey began with the careful design of parameters and functionalities such as vector size, contour plots, color maps, and interpolation methods. Leveraging the Qwt Spectrogram library, I was able to present matrix data as captivating color maps, each element in the matrix represented by a distinctive color. This transformation allowed for quick interpretation and analysis of the data. The Matrix Sink block's appearance was polished through meticulous adjustments to the color map and other visual elements, ensuring an interface that was both user-friendly and informative.

***== Related Links ==***

**Matrix Sink Wiki Page** : [https://wiki.gnuradio.org/index.php?title=QT_GUI_Matrix_Sink](https://wiki.gnuradio.org/index.php?title=QT_GUI_Matrix_Sink)

**GitHub Repository** : [https://github.com/R-ohit-B-isht/gnuradio/tree/main](https://github.com/R-ohit-B-isht/gnuradio/tree/main)

**Related Blogs** : [Week-1 Blog](https://www.gnuradio.org/blog/2023-06-06-GSoC-2023-Qt-Widgets-Improvement-Week-1/), [Week-2 Blog](https://www.gnuradio.org/blog/2023-06-14-GSoC-2023-Qt-Widgets-Improvement-Week-2/) 

**Merge Request Link** : [Matrix Sink PR](https://github.com/gnuradio/gnuradio/pull/6718)


{{<figure src="https://wiki.gnuradio.org/images/a/a4/Matrix_sink.png" alt="Matrix Sink" width="800px">}}

#### *`Future improvements for the Matrix Sink :`*

* Add more customization options for the color map, axis labels, and other visual elements.

* Integrate zoom and pan functionalities.

* Add support for more data types.

* Improve the performance of the Matrix Sink.


#### **[Video Display Sink](https://wiki.gnuradio.org/index.php?title=QT_GUI_Video_Display)**

The Video Display Sink brought dynamic video visualization capabilities to GNU Radio. Leveraging the Qt Multimedia library, I implemented real-time video display and audio playback. This sink was designed with a user-friendly interface, incorporating playback controls, seek functionality, volume adjustments, and more. It was a significant step towards enriching the multimedia experience within GNU Radio.

***== Related Links ==***

**Video Display Sink Wiki Page** : [https://wiki.gnuradio.org/index.php?title=QT_GUI_Video_Display](https://wiki.gnuradio.org/index.php?title=QT_GUI_Video_Display)

**GitHub Repository** : [https://github.com/R-ohit-B-isht/gnuradio/tree/VideoDisplay](https://github.com/R-ohit-B-isht/gnuradio/tree/VideoDisplay)

**Related Blogs** : [Week-3 Blog](https://www.gnuradio.org/blog/2023-06-21-GSoC-2023-Qt-Widgets-Improvement-Week-3/), [Week-4 Blog](https://www.gnuradio.org/blog/2023-06-29-GSoC-2023-Qt-Widgets-Improvement-Week-4/) 

**Merge Request Link** : [Video Display Sink PR](https://github.com/gnuradio/gnuradio/pull/6746)

{{<figure src="https://wiki.gnuradio.org/images/e/e8/Video_display.png" alt="Video Display Sink" width="800px">}}

#### *`Future improvements for the Video Display :`*

* **Consider the changes in the Qt Multimedia API** : The Qt Multimedia API has undergone significant changes in Qt 6, including the rewritten GStreamer backend. This means that the Video Display Sink will need to be updated to use the new API when transitioning to Qt6.

* **Add new features** : The Video Display Sink could be extended to support new features, such as the ability to save the current display as an image.

* Add support for more data types.

* Improve the performance of the Video Display.

## **[Refactoring Qt GUI Sinks](https://github.com/gnuradio/gnuradio/pull/6790)**
The refactoring process involved enhancing the existing Frequency Sink, Waterfall Sink,Time Sink, Time Raster Sink, Eye Sink and Sink blocks. By adopting a generic and template-based approach, I ensured compatibility with various data types. This not only streamlined the codebase but also resulted in better performance and increased flexibility. 

***== Related Links ==***

**GitHub Repository** : [https://github.com/R-ohit-B-isht/gnuradio/tree/qt-gui-refactoring](https://github.com/R-ohit-B-isht/gnuradio/tree/qt-gui-refactoring)

**Related Blogs** : [Week-5 Blog](https://www.gnuradio.org/blog/2023-07-07-GSoC-2023-Qt-Widgets-Improvement-Week-5/), [Week-6 Blog](https://www.gnuradio.org/blog/2023-07-16-GSoC-2023-Qt-Widgets-Improvement-Week-6/) 

**Merge Request Link** : [Refactoring Qt GUI Sinks PR](https://github.com/gnuradio/gnuradio/pull/6790)

## **[Integration of Qt Designer](https://wiki.gnuradio.org/index.php?title=QT_Designer_Integration)**
The integration of Qt Designer with GNU Radio brought a new level of convenience and flexibility to GUI creation. The process of creating custom layouts was simplified through the generation of .ui files from flowgraphs. These files could be easily loaded into Python code using the uic module, thus streamlining the creation of interactive and visually appealing interfaces. Users could now design and modify their GUI interfaces with unprecedented ease. This development eliminated the need for manual GUI creation, fostering the creation of interactive and visually appealing layouts.

***== Related Links ==***

**Integrating Qt Designer Wiki Page** : [https://wiki.gnuradio.org/index.php?title=QT_Designer_Integration](https://wiki.gnuradio.org/index.php?title=QT_Designer_Integration)

**GitHub Repository** : [https://github.com/R-ohit-B-isht/gnuradio/tree/Qt-designer-integration](https://github.com/R-ohit-B-isht/gnuradio/tree/Qt-designer-integration)

**Related Blogs** : [Week-7 Blog](https://www.gnuradio.org/blog/2023-07-23-GSoC-2023-Qt-Widgets-Improvement-Week-7/), [Week-8 Blog](https://www.gnuradio.org/blog/2023-08-07-GSoC-2023-Qt-Widgets-Improvement-Week-8/) 

**Merge Request Link** : [Integrating Qt Designer PR](https://github.com/gnuradio/gnuradio/pull/6791)

{{<figure src="https://wiki.gnuradio.org/images/f/f4/TestOM.jpg" alt="Qt Designer" width="800px">}}


#### *`Future improvements for the Qt Designer Integration :`*

* **QML Support**: Adding QML support for even more flexible and customized UI implementations beyond the capabilities of .ui files.

* **UI Templates**: Developing a library of UI templates for common use cases, accelerating the creation of interactive interfaces.


## What I Learned

This journey provided a profound learning experience. The journey has taught me not only technical skills but also the art of collaborative coding, meticulous testing, and adapting to project constraints. I've honed my abilities in C++, Qt, design patterns, debugging, and Git. I also delved into advanced topics such as Qt Designer integration, multimedia visualization, and template-based programming. The project taught me the art of optimizing GUI components for both functionality and performance. I also gained valuable insights into collaborative open-source development, community discussions, and mentorship. This journey has rekindled my love for coding and the joy of problem-solving. I am immensely grateful for this opportunity and the growth it has enabled.

## Acknowledgments

*Thank You*

*This journey wouldn't have been possible without the support of the GNU Radio community, the guidance of mentors, and the GSoC program. Your invaluable feedback, discussions, and encouragement have been the driving force behind the success of this project. I extend my heartfelt thanks to all who have been part of this journey.*

*As this chapter concludes, I look forward to witnessing how these improvements reshape the landscape of GNU Radio, making it even more user-friendly, powerful, and accessible to all.*

*Thank you for being part of this exhilarating adventure!*

## Mentors

{{< figure src="https://avatars.githubusercontent.com/u/1413378?v=4" width="180px" alt="Håkon Vågsether">}} | {{< figure src="https://avatars.githubusercontent.com/u/4438327?v=4" width="180px" alt="Andrej Rode">}}
---|---
[Håkon Vågsether](https://github.com/haakov) |[Andrej Rode](https://github.com/noc0lour)



