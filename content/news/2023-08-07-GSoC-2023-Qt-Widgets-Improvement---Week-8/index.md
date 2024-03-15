---
title: "GSoC 2023 Qt Widgets Improvement Week-8 [ Qt integration ]"
author: "Rohit Bisht"
date: 2023-08-07T00:05:55+05:30
categories: ["GSoC", "QTgui"]
---

Welcome to another update on the progress of the GSoC 2023 Qt Widgets Improvement project. In this Week 8 blog post, I'm thrilled to share some exciting developments that have taken place over the past week, as well as provide a detailed guide on using custom layouts, generating .ui files, and integrating them into our GNU Radio projects.

## Bug Fixes and Enhancements
Since our last update, I've been working on addressing bugs and enhancing the overall functionality of the Qt GUI widget component. These improvements are aimed at providing a smoother and more user-friendly experience when designing and customizing GUIs for our flowgraphs.

## Harnessing the Power of .ui Files
One of the highlights of this week's progress is the integration of .ui file support within the gr-qtgui module. .ui files are created using Qt Designer and contain the layout and design information of our GUI. These files can now be seamlessly generated from within Qt Designer, capturing all our customization settings. This feature allows for easy collaboration between designers and developers, enabling a streamlined workflow.

### Generating .ui Files from GRC
To generate a .ui file from our GNU Radio Companion (GRC) flowgraph, follow these steps:

1. Open our GRC flowgraph.
2. Add the desired gr-qtgui widgets to our flowgraph.
3. Save our flowgraph.
4. In the GRC menu, navigate to "Top Horizontal Bar" -> "Generate the UI File" OR press F4 on our keyboard.
5. The output location will be the same as our GRC and python file.

{{< figure src="generate_ui_file.gif" width="800px" >}}


### Editing .ui Files in Qt Designer
Once we have our .ui file, we can open it in Qt Designer to further customize the layout and appearance of our GUI. Qt Designer provides an intuitive interface for adding widgets, arranging elements, and applying formatting options.

{{< figure src="testing.png" width="800px" >}}
{{< figure src="testO.png" width="800px" >}}

## Creating Custom Layouts for Qt Widgets
Custom layouts offer a powerful way to organize and arrange widgets within our GUI. We can easily create layouts such as grids, stacked widgets, and more, to achieve the desired visual structure.

{{< figure src="creating_custom_layout.gif" caption="Creating Custom Layout" width="800px" >}}

### Running the Custom Layout
After designing our custom layout in Qt Designer, we can seamlessly integrate it into our GNU Radio project. Simply load the .ui file within our Python code and set it as the layout for our application.

{{< figure src="running_custom_layout.gif" caption="Running Custom Layout" width="800px" >}}
## Tips and Common Errors

- **No Layout**: This error occurs when we do not set a layout for our widget. 

{{< figure src="error_empty.png" width="800px" >}}

{{< figure src="Error.png" width="800px" >}}

To resolve this, ensure that we set a layout for our widget, either by using the default layout or a custom layout.

{{< figure src="layout_error.gif" width="800px" >}}

