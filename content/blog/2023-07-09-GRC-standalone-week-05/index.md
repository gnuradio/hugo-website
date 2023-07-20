---
title: "GSoC Standalone GRC : week-5"
author: "Rahul Balaji"
date: "2023-07-09"
categories: ["GSoC", "GRC"]
---

Hello,

Week 5 of GSoC has mainly been spent on coding and fixing bugs that were present on just translating options.py, and analysing the code in core/platform.py.

Now that options.py is ported, we can now focus on creating the workflow manager object. We need to create a loader that loads the .yml files like the ones in core/platform.py, like so,

```
 if file_path.endswith('.block.yml'):
                    loader = self.load_block_description
                    scheme = schema_checker.BLOCK_SCHEME
                elif file_path.endswith('.domain.yml'):
                    loader = self.load_domain_description
                    scheme = schema_checker.DOMAIN_SCHEME
                elif file_path.endswith('.tree.yml'):
                    loader = self.load_category_tree_description
                    scheme = None
                elif file_path.endswith('.workflow.yml'):
                    loader = self.workflows.load_workflow_description
                    scheme = None
                else:
                    continue

```

Now, it's a matter of defining ```workflows.load_workflow_description``` to load the .yml file.

So that will mainly be the focus of this coming week, along with syncing with GNU Radio. Almost all the latest changes made to GRC is uploaded in my repo, so we can start by porting it to a new repo made in the GNU radio org.
