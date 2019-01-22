---
title: "Block header parsing tool"
name: "Block_header_parsing_tool"
hash: "-8020863130869251701"
mentors: ["","Martin Braun"," Nicolas Cuervo",""]
type: idea
---


Rough ideas:

* Python-based tool

* Can extract info from block headers (and maybe, if it has to, also from the .cc file)

  * Analyse factory signature ("make function"), analyze getters/setters

  * Analyse I/O signature

Utilities:

* Auto-generate YAML files for GRC (would require another tool, also part of this project)

* Facilitate inclusion of GNU Radio with other tools/frameworks

There is some code in gr_modtool which does this, which can be reused and
extended.

## Prerequisites

* Strong knowledge of Python, including Py3k idiosyncrasies

* Some text parsing experience

* Some understanding of GNU Radio block structure

## Outcome

* A tool, written in Python, merged into the GNU Radio source tree, which can turn a block definition into some kind of abstract representation (the design which of is also part of this project)

* Another tool, which takes the abstract representation, and produces YAML files for GRC.

* An API into calling this which can be used by other tools (external to GNU Radio).

* Make gr_modtool use this tool instead of its builtin code.


