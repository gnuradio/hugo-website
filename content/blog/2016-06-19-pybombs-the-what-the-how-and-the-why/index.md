---
title: "PyBOMBS ? The What, the How and the Why"
author: "Martin Braun"
date: "2016-06-19"
sponsored: "0"
aliases: ["blog/pybombs-the-what-the-how-and-the-why"]
---

# PyBOMBS ? The What, the How and the Why

For a few years now, GNU Radio has had its own &#8220;package manager&#8221;, PyBOMBS. Nearly a year ago, development was started to completely rewrite PyBOMBS, and we switched over to the new version a few months ago. Finally, the dust is settling for version 2 of PyBOMBS, it&#8217;s becoming more and more stable, and more widely adopted. Soon, we will be releasing PyBOMBS 2.1.0. As such, this is a great time to formally introduce the world to the new PyBOMBS.

## What is PyBOMBS?

Package manager is really not a good term for this chunk of software &#8212; it&#8217;s a tool to assist in installing GNU Radio, out-of-tree modules and other software packages, from source or binaries, mostly system-independent.<br />
<!--more--><br />
In an ideal world, a tool like PyBOMBS wouldn&#8217;t be required. Every operating system and distribution would have access to up-to-date binary packages for everything, and compiling software would be straightforward and hassle-free. Sadly, this is not the case: Even on very recent distributions, the latest GNU Radio version is often at least months behind the latest tagged version of GNU Radio, and the same goes for its dependencies, such as UHD, or popular out-of-tree modules, such as gr-osmosdr, if they even have binary packages. As such, to make best use of GNU Radio, it is often required to compile multiple software packages, which can be very cumbersome.

For most users and use cases, PyBOMBS is the solution. It will automatically perform tasks such as installing dependencies, fetching correct source packages, configuring them with the correct arguments, building and installing them, keeping track of dependencies, and all that. Furthermore, it is designed to work on a multitude of platforms, always using the same commands. This also makes it a great choice for automated setup of GNU Radio systems.

For example, imagine you have a brand new laptop, with the latest version of your favourite distribution freshly installed. Of course, the first thing you want to do is install GNU Radio. Can you remember all the dependencies? Do you know all the source repositories? Can you remember all the CMake settings?

Doesn&#8217;t matter. Just install PyBOMBS and let it do all the work.

## How does it work?

<br />
> <b>NOTE: THIS SECTION IS DEPRECATED</b>
> 
> An updated usage guide can be found in the [PyBOMBS README](https://github.com/gnuradio/pybombs#pybombs).

<br />
Here&#8217;s a couple of commands that will set you up in no time:

    $ sudo pip install pybombs
    $ pybombs recipes add gr-recipes git+https://github.com/gnuradio/gr-recipes.git
    $ mkdir prefix/
    $ pybombs prefix init -a default prefix/default/ -R gnuradio-default

The first command actually installs PyBOMBS onto your computer (you have to start somewhere). Then, PyBOMBS needs to be initialized with a list of recipes (a recipe is a file that tells PyBOMBS about specific packages, but more of that later). We will pick the default GNU Radio recipe list to start with. Next, we create a directory called prefix which we will use to store all the installations. Finally, we tell PyBOMBS to install GNU Radio and gr-osmosdr and all their dependencies into the directory prefix/default. That&#8217;s it!

The final command will take a while to execute, and you&#8217;ll see it chugging along while it&#8217;s working. In this step, it does the following:

- Determine all required dependencies
- Install packages into your system which are required to build the software, such as compilers, Boost, SWIG, etc. (For this step, it may ask you for a password)
- Download all source packages
- Configure, build and install them

You may have noticed that PyBOMBS didn&#8217;t install GNU Radio into a system directory (such as /usr/local). PyBOMBS can do that, but it&#8217;s highly recommended not to (we consider this advanced usage of PyBOMBS, and won&#8217;t talk about it in this article). Using custom prefixes allows you to more easily uninstall versions and have multiple versions installed alongside each other. Installing to a system prefix may seem convenient, but it&#8217;s easy to screw up your installation, which can be painful to fix. If you screw up your installation to a custom directory, you only need to delete that directory.

So how can you run software that was installed into a custom prefix? Not a problem, simply open your terminal, head to your prefix directory and run a script called setup_env.sh:``

<code>$ cd prefix/default<br />
$ source ./setup_env.sh<br />
</code>

Now, you can run applications such as GNU Radio Companion:

<code>$ gnuradio-companion<br />
</code>

You can now add more software packages to this prefix. To add the gr-radar package, you simply call

<code>$ pybombs install gr-radar<br />
</code>

If you want to install it into a different prefix than the default one, you specify it with the -p switch. Remember we initialized the prefix above with the -a switch, and called it &#8220;default&#8221;. Now let&#8217;s create another prefix, just for gr-radar development, and install gr-radar into that:

<code>$ pybombs prefix init -a radar ~/prefix/radar<br />
$ pybombs -p radar install gr-radar<br />
</code>

The new prefix does not yet have GNU Radio installed, but since it&#8217;s a dependency of gr-radar, PyBOMBS will automatically pull it in and build it as well.

If you ran these commands, you&#8217;d have two independent prefixes in ~/prefix, one in ~/prefix/default, and one in ~/prefix/radar. Note that every prefix can quickly grow up to several gigabytes in size, since every prefix will pull in everything it needs, even if it&#8217;s already available in a different prefix.

### And how does PyBOMBS know what to do?

Everything is configured through recipes or configuration files, which, conveniently, all use the same file format (YAML). PyBOMBS itself has no hard-coded knowledge of packages. This easy configurability allows PyBOMBS to always do the right job depending on any specific system&#8217;s or user&#8217;s requirements. Does your company&#8217;s network have rules about what gets installed from where? Simply tweak the recipe files, and have them signed off by your IT department. Are you working on bleeding-edge development of a certain packet? Simply change that packet&#8217;s recipe, and make PyBOMBS do your bidding.

## Why do we need PyBOMBS?

Need is such a strong word. The world will keep turning without PyBOMBS. A lot of people are used to simply building GNU Radio from source, and will always be able to do so.<br />
But it can be very, very useful and save you a lot of time.

Some free software purists like to point out that other software, such as portage, would probably be able to do the same as PyBOMBS. This is probably true, and yet PyBOMBS provides a lot of value since it&#8217;s simple to install, and is tightly integrated into the GNU Radio project and community.

PyBOMBS provides us with a single path for any user on any distribution to install GNU Radio. It does not require virtualization of any kind, and yet it allows to easily contain GNU Radio installs.

Plus, the combination of PyBOMBS and CGRAN provide an easy way to build the community of GNU Radio developers and users and ease sharing of code, even if the code is fairly experimental and wants to be tried by novice users &#8212; who become more experienced users this way, quickly and easily.

System administrators can benefit from PyBOMBS, since a simple recipe file is all that&#8217;s needed to install PyBOMBS in any configuration that is considered safe.

### Prefixes, Dockers?

Ah, I knew someone would bring that up. Docker and PyBOMBS have some similarities, and in fact, thanks to a few community members, work has been done to let them work as a team, e.g. use PyBOMBS to initialize a GNU Radio Docker image.

PyBOMBS by itself requires nothing such as Docker. All it needs is a Python interpreter, and from there it can download, install, and compile whatever it needs to into whatever location it is told to. Note however, that PyBOMBS can also install packages into the system itself. For example, most prefixes will use the standard Boost package that is provided by the host operating system. Since PyBOMBS prefixes are not virtualized, are not chrooted, or anything like that, it make sense to install dependencies such as Boost, compilers and similar packages into the system itself (e.g. using apt-get on Debian or Ubuntu systems).

## So what&#8217;s next?

The PyBOMBS issue tracker has a list of items which need to be addressed before PyBOMBS is considered complete; and of course, it will probably never be fully complete, like any other good free software project. There are a couple of interesting features coming in the following months, though: Ravi Sharan is working on a QT-based GUI for PyBOMBS as part of this summer of code project. Also, we&#8217;re working hard to make it easier to install GNU Radio (and any other registered package) behind firewalled or even airgapped machines. And, very importantly, we want to increase the number of platforms PyBOMBS supports. We already natively support Debian, Ubuntu, Fedora, Gentoo, CentOS and Mac OS X. FreeBSD would be a nice addition, and who knows, maybe we&#8217;ll even get Windows support somewhere down the line!<br />
Of course, we&#8217;ll try and keep PyBOMBS bug free, Python 2 and 3 compatible, and easy to use. Want to help us achieve any of these goals? Please give it a try, and report bugs!

## Resources

- [PyBOMBS Homepage (github)](https://github.com/gnuradio/pybombs/)
- [Issue tracker](https://github.com/gnuradio/pybombs/issues)

## Martin Braun