---
title: "GSoC Standalone GRC : week-7"
author: "Rahul Balaji"
date: "2023-07-23"
categories: ["GSoC", "GRC"]
---

Hello,

So the main focus of this week was to store the information during runtime so that it is accessible in a proper format.

So the workflow manager was set to store information with chainmaps, where we store each parameter with the corresponding workflow id,
like so.

```
class WorkflowManager(Element):

	workflow_labels= []
	workflow_ids = []
	param_list = ChainMap()
	
	def load_workflow_description(self, data, filepath):
"""parse the .workflow.yml file and add it to the list"""
		log = logger.getChild('workflow_loader')
		log.debug('loading %s', filepath)
		label = data['label']
		workflow_id = data['id']
		
		for l in workflow_labels:
			if l == label:
				log.error('file already parsed')
			else
				self.workflow_labels.append(label)
				self.workflow_ids.append(workflow_id)
				
	doc = data['description']
	flags = data['flags']
	new_param = {workflow_id: data['parameters']}
	param_list = param_list.new_child(new_param)
```

The chain-map param_list is how we plan to access the parameters and add or replace the parameters in other files like options.py, thus
controlling the workflow.

### what's next?

The next set of steps is to make sure the system works as intended and to fix a few errors in the code. Making a .yml file and testing the 
module to ensure that it is correctly storing data will be the focus.

That brings us to an end to the updates for week 7.
