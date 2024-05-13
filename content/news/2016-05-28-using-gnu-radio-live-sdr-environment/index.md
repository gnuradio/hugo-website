---
title: "Using the GNU Radio Live SDR Environment"
author: "Johnathan Corgan"
date: "2016-05-28"
sponsored: "0"
aliases: ["/blog/using-gnu-radio-live-sdr-environment", "/news/using-gnu-radio-live-sdr-environment"]
---

# Using the GNU Radio Live SDR Environment

## The GNU Radio Live SDR Environment

The GNU Radio Project provides a live, bootable image for download that contains a full installation of Ubuntu Linux, all of GNU Radio, numerous third party GNU Radio-based libraries and applications, support for a variety of hardware SDR peripherals, and tutorials and documentation. It was explicitly designed to be used in the following ways:

- To be burned onto a recordable DVD, to provide a quick and easy way to test applications and hardware without modifying one&#8217;s own workstation software,
- To be converted into a bootable USB drive, for use as an operating environment with the ability to extend and save work, or
- To be used as a virtual DVD in a virtualization environment such as KVM, Xen, VMware, or others.

### Obtaining the GNU Radio Live SDR Image

The full ISO image is downloadable via Bittorrent (preferred) or via direct link from one of our mirrors, as documented in the [GNU Radio Live DVD](https://gnuradio.org/redmine/projects/gnuradio/wiki/GNURadioLiveDVD) wiki page. The typical size is around 2.5G.  The ISO image checksum is published on the download page, and if desired, a digital signature produced by the GNU Radio Project [release signing key](https://gnuradio.org/redmine/projects/gnuradio/wiki/ReleaseKey) can by used to cryptographically verify the integrity of the download.

### Using the Live SDR Environment as a bootable DVD

<img class="size-medium wp-image-1054 alignleft" src="https://gnuradio.org/wp-content/uploads/2016/05/brasero-300x191.png" alt="brasero" width="300" height="191" srcset="/wp-content/uploads/2016/05/brasero-300x191.png 300w, /wp-content/uploads/2016/05/brasero.png 713w" sizes="(max-width: 300px) 100vw, 300px" />This option gives you a fast and easy way get into a known, working GNU Radio environment that you can use to quickly test ideas, verify hardware operation, or debug system configurations. Make one of these and throw it into your kit as a backup. You can also use it as a development environment, but since it only emulates a disk system using RAM, all your work is lost at power down unless you take steps to save it elsewhere. Furthermore, any operating system package installations or upgrades are lost as well.

Creating a DVD is straightforward using any number of operating system included DVD burning software packages. The important part to get correct is to indicate to the software that you want to burn the DVD from an entire disc image (ISO file), not store the ISO file itself, as shown on the left using the example Brasero disc burner software on Ubuntu Linux.

Of course, you&#8217;ll need to configure your laptop or PC to be able to boot from the DVD.  This typically involves interrupting the normal boot process by pressing a function key (often F12, but varies by manufacturer and BIOS), resulting in a &#8220;one time boot menu.&#8221;  Select the one that identifies as a CD, DVD, or optical media storage.  Depending on the speed of your DVD drive, booting can take up to several minutes, but you&#8217;ll eventually end up directly on the main Linux desktop screen and be ready to go.  During operation, the first time you access something new, like running the GNU Radio Companion software, it will take a while to load from the DVD, but thereafter will be cached in memory and operate at normal speed.

### Creating a Bootable USB Drive with Persistence

Creating a bootable USB drive with the Live SDR Environment on it takes more effort, but results in a GNU Radio development environment that can be extended and have work saved across multiple sessions. This is useful to avoid having to modify existing operating system installations and software configurations on a PC or laptop. In fact, this is the arrangement we (Corgan Labs) use when conducting our on-site GNU Radio technical courses.

The<img class="size-medium wp-image-1055 alignleft" src="https://gnuradio.org/wp-content/uploads/2016/05/unetbootin-300x183.png" alt="unetbootin" width="300" height="183" srcset="/wp-content/uploads/2016/05/unetbootin-300x183.png 300w, /wp-content/uploads/2016/05/unetbootin-400x245.png 400w, /wp-content/uploads/2016/05/unetbootin-270x165.png 270w, /wp-content/uploads/2016/05/unetbootin.png 635w" sizes="(max-width: 300px) 100vw, 300px" /> only requirement is a pre-formatted USB 2.0 or USB 3.0 flash drive of 8GB or larger (though the extra space beyond 8GB will not be used or accessible.)  After downloading the ISO image file, you can use Ubuntu Startup Disk Creator, UNetbootin (available on both Linux and Windows), or other live USB creator to convert the ISO image into a bootable live environment on the USB drive. You will have the option to dedicate a portion of the USB drive space up to 4GB to store new files and changes to the system (&#8220;persistence&#8221;).

Booting from the Live USB is simliar to the DVD; pressing F12 (or whichever) during the boot sequence gives a &#8220;one time boot menu&#8221;, where you can select the appropriate entry shown for the USB drive used.  Fast USB3.0 drive speeds can result in a system that feels like a regular hard disk.

There are some anecdotal reports that UNetbootin doesn&#8217;t always create the proper boot entries for operation on some systems.  Corgan Labs has created custom boot configuration files for this situation, described further in [this GNU Radio mailing list post](https://lists.gnu.org/archive/html/discuss-gnuradio/2016-02/msg00215.html).

### Operating GNU Radio from the Live Environment

The live environment is based on Ubuntu Linux 14.04 LTS, with a small number of modifications to improve operation. There is a full installation of all GNU Radio components, examples, documentation, and source code, as well as optional dependencies to run some GNU Radio examples. In addition, approximately 20 &#8220;Out of Tree&#8221; modules, that is, GNU Radio modules/applications written by community members have been installed. More specifics can be found on the [gnuradio.org wiki page](https://gnuradio.org/redmine/projects/gnuradio/wiki/GNURadioLiveDVD).

Specific hardware support for the following SDR products has been included:

- [Ettus Research™](http://ettus.com/) USRP™ family of products
- [Nuand](https://nuand.com/) bladeRF SDR plaform (GNU Radio support through [osmocom GNU Radio blocks](https://sdr.osmocom.org/trac/wiki/GrOsmoSDR))
- [Great Scott Gadgets](https://greatscottgadgets.com/hackrf/) hackRF family of products  (GNU Radio support through [osmocom GNU Radio blocks](https://sdr.osmocom.org/trac/wiki/GrOsmoSDR))
- The [Airspy](http://airspy.com/) (GNU Radio support through [osmocom GNU Radio blocks](https://sdr.osmocom.org/trac/wiki/GrOsmoSDR))
- Many common &#8220;RTL-SDR&#8221; dongles (GNU Radio support through [osmocom GNU Radio blocks](https://sdr.osmocom.org/trac/wiki/GrOsmoSDR))

If you have created a live USB drive with persistence, you can install additional hardware support in the same way you would for a native installation of GNU Radio.

All supported hardware drivers have already been configured for proper use, so you should be able to just plug in and use one of the above.  (If using a USRP™ N-series device, you should ensure the the network configuration has properly chosen &#8220;USRP&#8221; instead of &#8220;DHCP&#8221;.)

### Navigating the Live Environment

<img class="size-medium wp-image-1057 alignleft" src="https://gnuradio.org/wp-content/uploads/2016/05/shortcuts-136x300.png" alt="shortcuts" width="136" height="300" srcset="/wp-content/uploads/2016/05/shortcuts-136x300.png 136w, /wp-content/uploads/2016/05/shortcuts.png 147w" sizes="(max-width: 136px) 100vw, 136px" />The Live Environment has a small number of shortcuts available through the desktop and sidebar.

The GNU Radio Companion is accessible by clicking the GNU Radio logo on either the left side launchbar or the desktop, or by opening a terminal window and entering **grc.**

A terminal window may be opened by clicking on the terminal icon on the left or by typing **Ctrl-Alt-T.**

The GNU Radio documentation maybe opened in the Firefox browser by clicking the documentation link on the desktop.

A local copy of the [online GNU Radio Tutorials](https://gnuradio.org/redmine/projects/gnuradio/wiki/Guided_Tutorials) may be opened in the Firefox browser by clicking the tutorial link on the desktop.

A shortcut to all of the GNU Radio examples is in the live user home directory under &#8216;examples&#8217;. You can navigate there from a terminal to run the Python scripts, or from the **File|Open** menu inside the GNU Radio companion.

### Extras

The live image has a few non-GNU Radio specific applications installed that are often useful when working with digital signal processing and numerical processing.

- [GNU Octave ](https://www.gnu.org/software/octave/) provides a Matlab-like interface for performing array-based processing of signals
- [Numeric Python](http://www.numpy.org/) (numpy), [Scientific Python](https://www.scipy.org/) (scipy), [Matplotlib](http://matplotlib.org/), and [Jupyter Notebooks](https://jupyter.org/) provide an excellent environment for offline signal analysis
- The [GNU Emacs](https://www.gnu.org/software/emacs/) editor, used by [RealProgrammers™](https://xkcd.com/378/)

&nbsp;

### Feedback

Whether you are a hobbyist, student, or industry professional, we hope you find the GNU Radio Live SDR Environment useful for your activities. Feedback is welcome! The GNU Radio project may be reached via the links below and we look forward to your experiences and suggestions for improvement.

## Johnathan Corgan
