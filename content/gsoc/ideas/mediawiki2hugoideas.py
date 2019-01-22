#!/usr/bin/env python3
import re
import enum

lines = open("ideas.mw", encoding="utf8")


class Parsestate(enum.Enum):
    IDLE = (0, [1]),
    IN_IDEA = (1, [0, 2, 3])
    IN_MENTOR = 3


class Idea(object):
    def __init__(self, title):
        self.title = title
        self.name = title.strip().replace(" ", "_")
        self.hash = hash(title)
        self.description = ""
        self.mentors = []
        print(title)

    def __str__(self):
        return """---
title: "{idea.title}"
name: "{idea.name}"
hash: "{idea.hash}"
mentors: [{mentorstring}]
type: idea
---

{idea.description}
""".format(idea=self,
           mentorstring=','.join(
               ['"{mentor}"'.format(mentor=m) for m in self.mentors]))


def idlestate(line, state, *args):
    match = re.match("=== (.*) ===", line)
    if match:
        idea = Idea(match.group(1).strip())
        return (Parsestate.IN_IDEA, True, idea)
    return (Parsestate.IDLE, True, None)


def ideastate(line, state, idea, *args):
    match = re.match("=====* (.*) =*====", line)
    if match:
        heading = match.group(1)
        if heading.lower().strip().startswith("mentor"):
            state = Parsestate.IN_MENTOR
            return (state, True, idea)
        idea.description += "## " + heading
        return (state, True, idea)
    match = re.match("=== (.*) ===", line)
    if match:
        print("Done with idea.")
        with open(
                "{name}.md".format(name=idea.name), "w", encoding="utf8") as f:
            f.write(str(idea))
        return (Parsestate.IDLE, False, None)

    if line.strip().startswith("*"):
        idea.description += "\n"
    if line.strip().startswith("**"):
        line = line.replace("*", "  ", 1)
    idea.description += line
    return (state, True, idea)


def mentorstate(line, state, idea, *args):
    line = line.strip()
    if line.startswith("="):
        return (Parsestate.IN_IDEA, False, idea)
    idea.mentors += line.split(",")
    return (state, True, idea)


statedict = {
    Parsestate.IDLE: idlestate,
    Parsestate.IN_IDEA: ideastate,
    Parsestate.IN_MENTOR: mentorstate
}
next_line = True
cont = True
line = None
idea = None
state = Parsestate.IDLE

while cont:
    if next_line:
        line = lines.readline()
        if not line:
            break
    func = statedict[state]
    state, next_line, idea = func(line, state, idea)
    print(state)
