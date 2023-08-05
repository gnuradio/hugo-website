---
title: "GSoC Standalone GRC : week-6"
author: "Rahul Balaji"
date: "2023-07-16"
categories: ["GSoC", "GRC"]
---

Hello,

So the main focus of this week was to construct a Workflow Manager module that will manage all the parameters fetched from a .yml file provided by the user.

### so what does it actually do?

The main function of the workflow manager is to read from a .yml file, defined like this:

```
workflow:

	id: workflow_id

	label: xyz_label

	description: """
give a brief description here
"""

# parameters will contain the options form the options.block.yml.

	flags: [cpp, python]

	parameters:

		- id: sizing_mode
		  label: Sizing Mode
		  dtype: enum
		  default: fixed
		  options: [fixed, stretch_both, scale_width, scale_height, scale_both]
		  option_labels: [Fixed, Stretch Both, Scale Width, Scale Height, Scale Both]
		  hide: ${ ('part' if generate_options == 'bokeh_gui' else 'all') }
		  ...

	actions:

		- label: Generate
		  description: "generate the flowgraph"
		  method: generate
		- label: Run ...
		- label: Kill ...
	entrypoint: gnuradio_companion.workflows.top_block:Generator
```

The above-given template is an example of what it should look like. The workflow manager will now take information from this file and manage it at the top level, so that other files can take this information and then use it to define workflows.

So, the workflow manager is defined as such, with a function to load the .workflow.yml files and then store the parameters and other data that will be used in files like options.py, where the parameters will be dynamically replaced based on the workflow chosen.

### what's next?

The workflow manager can now read and access the .yml files, now, we need to find a suitable method to store this data properly in runtime so that files like options.py can retrieve it.

That brings us to the end of updates for week 6.
