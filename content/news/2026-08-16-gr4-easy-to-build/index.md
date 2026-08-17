---
title: "GNU Radio 4: Official Github Repository"
date: "2026-08-16"
author: "Josh Morman"
categories: ["gnuradio", "gr4", "github", "community", "official"]
aliases: ["/news/gnuradio4-easy-to-build"]
banner: "GR4-logo-embedded.svg"
---

We have been working hard getting GNU Radio 4 ready for an official release. Part of this endeavor has been restructuring and refactoring the repositories for future maintainability, better build and CI efficiency, and the flexibility to support different licensing models across the ecosystem.

GNU Radio 4 is now organized around a super-repo builder capable of pulling together foundational projects such as the core runtime and key DSP libraries, modules containing both official and experimental blocks, and applications built on top of them.

We also wanted to make the whole thing **really easy to build**.

The current super-repo is now live at https://github.com/gnuradio/gnuradio4. It provides the top-level workspace that knows which repositories make up GNU Radio 4, their dependencies, and the order in which everything needs to be built.  (Note: the git history from the previous gnuradio4 repo has been preserved in its entirety in the constituent components gnuradio4-core, gnuradio4-blocks, and gnuradio4-library).  As discussed in https://www.gnuradio.org/news/2026-05-21-gr4-community-stewardship/ - this repo fully supercedes the earlier prototype implementations.

For a normal development build, the workflow is essentially:

```
    git clone https://github.com/gnuradio/gnuradio4.git
    cd gnuradio4
    cmake --preset dev
    cmake --build --preset dev
    source build/dev/activate.sh
```

If you want the whole workspace including the incubator, control plane, and desktop Studio application, the workflow is similarly straightforward:

    cmake --preset full
    cmake --build --preset full
    source build/full/activate.sh
    gr4-studio

This full workspace build will also include GR4 versions of modtool and python bindings as these projects become ready.  

The initial build automatically clones the component repositories it needs into the workspace and builds them in dependency order. After that, those repositories under `src/` are just normal Git working copies. The super-repo doesn't try to take ownership of their Git state - you decide when to fetch, update, switch branches, or work directly in one of the component repositories.

For a standalone "hello world" module, see Derek's [example project](https://github.com/dkozel/gnuradio4-example) that will easily compile against a built GNU Radio 4 workspace!

## Maintainability

One of the biggest reasons for splitting the repositories is simply separation of concerns.

The runtime, schedulers, DSP algorithms, blocks, and applications have very different development characteristics. They don't all need to change together, and in most cases they probably shouldn't.

This separation has become even more useful as AI-assisted development tools have become part of normal software workflows. These tools are incredibly useful, but there is a tendency for intent to leak from one part of a large codebase into another. A change that is supposed to be about a block can suddenly start "improving" runtime code along the way.

Breaking the project into focused repositories gives us some useful boundaries, and in particular keeps the GNU Radio 4 (GR4) core boring.

Unless you are working deeply on the runtime, scheduler, graph infrastructure, or APIs, there should be very little reason to touch it. The core should be small, stable, well tested, and fairly difficult to accidentally disturb.

Blocks are the opposite. We want blocks to flow freely. New blocks, experimental ideas, hardware support, algorithms, and integrations should be able to evolve without requiring changes to the foundational runtime.

That separation should make both sides healthier.

And because the super-repo sits above all of this, users don't need to care very much about where those boundaries are when they simply want to build GNU Radio. The workspace takes care of selecting the required dependencies and assembling the pieces into a single development environment.

## CI Efficiency

There are many ways to skin this cat, and a sufficiently sophisticated monorepo CI system can certainly determine exactly what needs to be rebuilt.

But our previous default was much simpler: a pull request could result in rebuilding the core and essentially the entire block library, even when most of that code had nothing to do with the proposed change.

With smaller, more focused repositories, the natural unit of CI becomes much smaller. If a change is made to a block library, we build and test that block library and its dependencies. A change doesn't automatically imply rebuilding the entire GNU Radio 4 ecosystem.

There is certainly room to make this more granular over time, but this gives us a good starting point without requiring a complicated CI dependency engine.

We have also reduced the number of types instantiated by default for each official block to roughly the set of types supported by GNU Radio 3.

This does **not** prevent a GR4 block from supporting additional types. The underlying framework remains flexible. It just means the official block library will not instantiate every theoretically possible type combination unless there is a reason to do so.

That makes builds smaller and faster while keeping the flexibility available when it is actually needed.

## Licensing

Another important goal of this structure is licensing flexibility.

Our vision for GNU Radio 4 is a permissively licensed core on top of which a healthy copyleft ecosystem can grow.

There are users and organizations that are prevented from using or contributing to GPL-licensed software, or for whom doing so creates enough legal and organizational friction that they simply won't participate. A permissive core allows those users to build systems using GNU Radio 4 and, importantly, contribute improvements back to the foundational infrastructure.

At the same time, we do **not** want that to mean abandoning the copyleft ecosystem that has been such an important part of GNU Radio's history.

Block authors and application developers who want to publish their work under GPL or other copyleft licenses should absolutely be able to do so, and we fully support that model. 

In fact, GR4 Studio, which is becoming the primary user interface for GNU Radio 4, is already developed under GPLv3 in the spirit of GNU Radio's copyleft heritage.  Also, as blocks are ported from GNU Radio 3, we plan to create a `gnuradio4-blocks-gpl` repo so that these licenses are clearly preserved, and bring these into the super-build.

The repository structure makes this much easier to manage. The foundational runtime can remain permissively licensed while GPL block libraries, applications, and other components can live naturally alongside it without creating ambiguity about the licensing of the core.

## One ecosystem, without one giant repository

The end result is something that is a little different from how GNU Radio has traditionally been organized.

GNU Radio 4 is no longer defined by one large source tree. Instead, it is an ecosystem of focused projects that can be assembled into a complete GNU Radio installation.

But we don't want "multiple repositories" to translate into "go read six READMEs and figure out how to build all of this yourself."

That is really the purpose of the super-build repo. Clone one repository. Pick a build preset. Build it.

Underneath that simple entry point, we get much cleaner boundaries between the parts of GNU Radio that should be stable and the parts that should be able to move quickly.

For developers who want to dig deeper, the component repositories remain ordinary Git working copies and can be worked on independently. For someone who just wants GNU Radio 4 running, those details can mostly disappear.

There is still plenty of work to do before we officially tag GNU Radio 4 **released**. But the structure we have now feels much better suited to the project we want GNU Radio to become.

## Join Us

GNU Radio 4 will continue to be an active community effort, and if you are interested in what we are building, we would love to have you involved.

The best place for day-to-day discussion is the [GR4 Technical Users Matrix room](https://matrix.to/#/#gr4-technical-users:gnuradio.org). This is where we talk through development issues, design ideas, new blocks, build problems, and generally figure out where GR4 is going next.

We also hold **twice-monthly GNU Radio 4 developer calls**. These are open meetings where we discuss current development, architectural decisions, priorities, and whatever else needs attention that week. You can find the upcoming calls on the [GNU Radio community calendar](https://calendar.google.com/calendar/u/0/newembed?src=u4l8u9vsi2r6pe5ht86act1tec@group.calendar.google.com).

You do not need to be a core developer to join either one. If you are experimenting with GR4, thinking about writing blocks, building an application on top of it, or just want to see where things are headed, come join us.