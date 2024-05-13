---
title: "GNU Radio 3.8.0.0"
author: "Marcus Müller"
date: "2019-08-10"
sponsored: "0"
aliases: ["/news/3.8-release"]
categories: ["release"]
banner: gr_release_web.svg
---
# Release 3.8.0.0

Witness me!

Tonight, we release GNU Radio 3.8.0.0.

It's the first minor release version since more than six years, not without
pride this community stands to face the brightest future SDR on general purpose
hardware ever had.

Since we've not been documenting changes in the shape of a Changelog for the
whole of the development that happened since GNU Radio 3.7.0, I'm afraid that
these release notes will be more of a GLTL;DR (git log too long; didn't read)
than a detailed account of what has changed.

What has _not_ changed is the fact that GNU Radio is centered around a very
simple truth:

> Let the developers hack on DSP. Software interfaces are for humans, not the
> other way around.

And so, compared to the later 3.7 releases, nothing has fundamentally modified
the way one develops signal processing systems with GNU Radio: You write blocks,
and you combine blocks to be part of a larger signal processing flow graph.

With that as a success story, we of course have faced quite a bit of change in
the systems we use to develop and in the people that develop GNU Radio. This has
lead to several changes that weren't compatible with 3.7.

**This is an excerpt only:**

## Fixed

### Project Scope

- Roughly 36 dBBug, (ETOOMANYBUGS)
- Fixed .so versioning

## Changed

### Project Scope

- C++11
- merged the wholeness of the `next` branch
- Dependency version bumps: CMake, GCC, MSVC, Swig, Boost
- New dependencies: MPIR/GMP, Qt5, gsm, codec2
- Removed dependencies: libusb, Qt4, CppUnit
- Python: Python 2 & Python 3 compatible. 3.8 will be the last Py2k-compatible
  release series
- gengen was replaced by templates (if you don't know gengen, don't do any
  research; save yourself that sorrow)
- Modern CMake (as far as feasible at this point)
- VOLK version updated to v2.0.0
- .clang-format file now dictates coding style
- clang-format'ed the whole tree.
- installed CMake files now tell about configuration

### gnuradio-runtime

- reworked fractional tag time handling, especially in the context of resamplers

### GRC

- C++ generation as option
- YAML instead of XML
- removed `blks2`
- much better canvas tooling
- consistent gobject usage
- ROUNDED ARROWS

### gr-qtgui

- moving from Qt4 to Qt5

### gr-utils

- `gr_modtool` now vastly improved

### gr-vocoder

- improved versatility
- removed in-tree libgsm, libcodec2, use system-wide libs


## Removed

### Project Scope
- Modules `gr-comedi`, `gr-fcd` and `gr-wxgui` are gone

### gr-comedi

- nobody could remember who used this, or for what. It has seen 0 active code
  contributions in the 3.7 lifecycle

### gr-digital

- python-based `packet_encoder` and related tools: Bugs that were sporadic and
  never fixed, so after long deprecation, we're removing it

### gr-fcd

- since it's currently untestable by the CI, it's being removed, as there was no
  code contributions. Generally, we strive to include all batteries with GNU
  Radio. Re-integration within a more general SDR interface would be desirable.

### gr-utils

- removed PyQwt (dead) based tools

### gr-wxgui

- Unmaintained, breaks on increasingly many systems, always was slower than
  Qtgui. We've been starting to tell people to migrate to Qt since at
  least 2015. Now, we're finally removing it.


# Contributors

-   Maitland Bottoms <bottoms@debian.org>
-   Abhishek Bhowmick <abhowmick22@gmail.com>
-   Achilleas Anastasopoulos <anastas@umich.edu>
-   Adrian Suciu <adrian.suciu@analog.com>
-   Alexander Willecke <willecke@ibr.cs.tu-bs.de>
-   Alexandru Csete <oz9aec@gmail.com>
-   Alistair Bird <alistair.bird@gmail.com>
-   Andrej Lajovic <andrej.lajovic@ad-vega.si>
-   Andrej Rode <mail@andrejro.de> (formerly <andrej.rode@ettus.com>)
-   Andrew Davis <glneolistmail@gmail.com>
-   Andrew F. Davis <glneolistmail@gmail.com>
-   Andriy Gelman <andriy.gelman@gmail.com>
-   André Løfaldli <andre.lofaldli@gmail.com>
-   Andy Sloane <andy@a1k0n.net>
-   Andy Walls <andy@silverblocksystems.net>
-   Antonio Ramosdet <antonio.ramosdet@gmail.com>
-   Arpit Gupta <guptarpit1997@gmail.com>
-   Artem Pisarenko
-   AsciiWolf <mail@asciiwolf.com>
-   Balint Seeber <balint256@gmail.com> (formerly: <balint@ettus.com>)
-   Bastian Bloessl <mail@bastibl.net> (formerly:
    <bastian.bloessl@uibk.ac.at> <bloessl@ccs-labs.org>)
-   Ben Hilburn <bhilburn@gnuradio.org> (formerly:
    <ben.hilburn@ettus.com>)
-   Ben Reynwar <ben@reynwar.net>
-   Bernhard M. Wiedemann <bwiedemann@suse.de>
-   Bill Clark <saikbc89@gmail.com> / <saikou@vt.edu>
-   Bob Iannucci <bob@sv.cmu.edu>
-   Bogdan Diaconescu <b_diaconescu@yahoo.com>
-   Bogdan Radulescu <bogdan@nimblex.net>
-   Bolin Hsu <bolin.hsu@gmail.com>
-   Brandon P. Enochs <brandon.enochs@nrl.navy.mil>
-   Brennan Ashton <bashton@brennanashton.com>
-   Brent Stapleton <brent.stapleton@ettus.com>
-   Brian Orr <brian.orr@gmail.com>
-   Brian Padalino <bpadalino@gmail.com>
-   Camilo Solano <solano@ti.rwth-aachen.de>
-   Cate <cate@skysafe.io>
-   Chris Kuethe <chris.kuethe+github@gmail.com>
-   Christoph Mayer <hcab14@gmail.com>
-   Christopher Chavez <chrischavez@gmx.us>
-   Chuck Swiger <cswiger@swigerco.com>
-   Clayton Smith <argilo@gmail.com>
-   Dan Robertson <dan@dlrobertson.com>
-   Daniel Estévez <daniel@destevez.net>
-   Daniel Grambihler <af7ss.ham@gmail.com>
-   Darek Kawamoto <darek@he360.com>
-   DaulPavid <pudavid@fastmail.com> (formerly: <paul.david@ettus.com>)
-   Derek Kozel <derek@bitstovolts.com> (formerly:
    <derek.kozel@ettus.com>)
-   Dhruvadityamittal <dhruvadityamittal@gmail.com>
-   Dimitri Stolnikov <horiz0n@gmx.net>
-   Douglas Anderson <danderson@ntia.doc.gov>
-   Douglas Geiger <doug.geiger@bioradiation.net>
-   Douglas Weber <douglas.weber@student.kit.edu>
-   Edward Kigwana <edwardwwgk@gmail.com>
-   Eral Tuerkyilmaz <eral@gmx.net>
-   Eric Johnson <ejohnson73@gmail.com>
-   Eric Statzer <eric.statzer@gmail.com>
-   Ethan Trewhitt <ethan.trewhitt@gtri.gatech.edu> /
    <ethan@trewhitt.org>
-   Federico
-   Felix Wunsch <felix.wunsch@kit.edu> (formerly:
    <uncnr@student.kit.edu>)
-   Flamewires
-   Florian Franzen <FlorianFranzen@gmail.com>
-   Garrett Vanhoy <basebzombie@gmail.com>
-   Geof Nieboer <gnieboer@gcndevelopment.com> / <gnieboer@corpcomm.net>
-   Gilad Beeri <giladb.dev@gmail.com>
-   Glenn Richardson <glenn.richardson@live.com>
-   Gregory Eslinger <gregjesl@gmail.com>
-   Gwenhael Goavec-Merou <gwenhael.goavec-merou@trabucayre.com>
-   Harm te Hennepe <d.h.tehennepe@student.utwente.nl>
-   Head4che <kmurat67@gmail.com>
-   Henry Xu <xuweihong.cn@gmail.com>
-   Håkon Vågsether <haakonsv@gmail.com>
-   Imad-Eddine Srairi <imad.srairi@mckay-brothers.com>
-   Jacob Gilbert <jacob.gilbert@sandia.gov>
-   Jakub Zy <jakub@openmailbox.org>
-   James Saari <jsaari@defense.mrcy.com>
-   Jan Krämer / spectrejan <kraemer.jn@googlemail.com>
-   Jared Boone <jboone@earfeast.com>
-   Jared Dulmage <jared.dulmage@aero.org>
-   Jaroslav Škarvada <jskarvad@redhat.com>
-   Jason Hein <jason.j.hein@gmail.com>
-   Jeff Long <willcode4@gmail.com>
-   Jeremy Drake <github@jdrake.com>
-   Jiri Pinkava <j-pi@seznam.cz>
-   Jiří Pinkava <j-pi@seznam.cz>
-   Johannes Demel <demel@ant.uni-bremen.de> / <demel@uni-bremen.de> /
    <johannes@demels.de> (formerly: <ufcsy@student.kit.edu>)
-   Johannes Schmitz <johannes.schmitz1@gmail.com> /
    <schmitz@ti.rwth-aachen.de>
-   Johnathan Corgan <johnathan@corganlabs.com>
-   Jon Szymaniak <jon.szymaniak@gmail.com>
-   Jonathan Brucker <jonathan.brucke@gmail.com>
-   Jonathon Pendlum <jonathon.pendlum@ettus.com>
-   Josh Blum <josh@joshknows.com>
-   Josh Morman <jmorman@perspectalabs.com>
-   Joshua Schueler <joshua.schueler@rohde-schwarz.com>
-   Julian Arnold <julian.arnold@ettus.com>
-   Julien Olivain <julien.olivain@lsv.ens-cachan.fr>
-   Julius Durst <julius.durst@student.kit.edu>
-   Karel <karelparlin@gmail.com>
-   Kartik Patel <kartikpatel1995@gmail.com>
-   Kevin Gentile <kg168212@ohio.edu>
-   Kevin McQuiggin <mcquiggi@sfu.ca>
-   Kevin Reid <kpreid@switchb.org>
-   Kevin Zheng <kevinz5000@gmail.com>
-   Kristian Maier <kristian.maier@gmx.de>
-   Kyle Unice <kyle.unice@L-3com.com>
-   Laur Joost <daremion@gmail.com>
-   Lennart <Lennart@bastl-instruments.com>
-   Louis Philippe Lessard <git@louif.com>
-   Ludovic LANGE <github@lange.nom.fr>
-   Lukas Kuzmiak <lukash@backstep.net>
-   Luke Berndt <lukekb@gmail.com>
-   MBoerschig code+github at boerschig dot net
-   Marc Lichtman / 777arc <marcll@vt.edu> / <mlichtman@appcomsci.com> /
    <mlichtman@perspectalabs.com>
-   Marcus Müller / funkylab <mmueller@gnuradio.org> /
    <marcus@hostalia.de> / <mueller@kit.edu> /
    <marcus.mueller@ettus.com> (formerly:
    <marcus.mueller@student.kit.edu>)
-   Mark Cottrell <mark.cottrell@taitradio.com>
-   Martin Braun <martin.braun@ettus.com> (formerly:
    <martin.braun@kit.edu>)
-   Mathieu Rene <mrene@avgs.ca>
-   Matt Ettus (formerly: <matt@ettus.com>)
-   Maximilian Stiefel <stiefel.maximilian@online.de>
-   Michael Berman <michael@gpstoo.com>
-   Michael De Nil <michael@morsemicro.com>
-   Michael Dickens <michael.dickens@ettus.com> / <mlk@alum.mit.edu>
-   Michael Ossmann <mike@ossmann.com>
-   Mike Jameson <mike.jameson@ettus.com> / <mike@scanoo.com>
-   Mike Walters <mike@flomp.net>
-   Miklos Maroti <mmaroti@gmail.com>
-   Moritz Fischer (formerly: <moritz@ettus.com> /
    <moritz.fischer@ettus.com>)
-   Nate Goergen <nate.goergen2@mile10.com>
-   Nathan West <nathan.west@gnuradio.org> / <nathan.west@nrl.navy.mil>
    / <nathan.west@okstate.edu>
-   Nicholas Corgan <n.corgan@gmail.com> (formerly:
    <nick.corgan@ettus.com>)
-   Nicholas McCarthy <namccart@gmail.com>
-   Nick Foster <bistromath@gmail.com> (formerly: <nick@ettus.com>)
-   Nick McCarthy <namccart@gmail.com>
-   Nick Østergaard <oe.nick@gmail.com>
-   Nicolas Cuervo (formerly: <nicolas.cuervo@ettus.com>)
-   Paul Boven <p.boven@xs4all.nl>
-   Paul Cercueil <paul.cercueil@analog.com>
-   Paul David <pudavid@vt.edu>
-   Paul Garver <garverp@gatech.edu>
-   Paul Wicks <pwicks86@gmail.com>
-   Pedro Lobo <pedro.lobo@upm.es>
-   Peter A. Bigot <pab@pabigot.com>
-   Peter Horvath <ejcspii@gmail.com>
-   Peter Witkowski <pete@deepwavedigital.com>
-   Philip Balister <philip@balister.org> / <philip@opensdr.com>
-   Philipp Aigner <philipp.aigner@orderman.com> / <phaigner@gmail.com>
-   Philippe Gauthier <philippe.gauthier@deuxpi.ca>
-   Piotr Krysik <pkrysik@elka.pw.edu.pl> / <ptrkrysik@gmail.com>
-   Ravi Sharan <ravisharan@iith.ac.in>
-   Richard C. Bell <richard.bell1@navy.mil>
-   Rick Spanbauer <rspanbauer@ieee.org>
-   Ron Economos <w6rz@comcast.net>
-   Roy Thompson <rthompso@gmail.com>
-   Ruben Undheim <ruben.undheim@gmail.com>
-   Ryan Volz <rvolz@mit.edu>
-   Scott Talbert <swt@techie.net>
-   Scott Torborg <storborg@gmail.com>
-   Sean Nowlan <nowlans@ieee.org> / <sean.nowlan@gtri.gatech.edu>
-   Sebastian Koslowski <sebastian.koslowski@gmail.com> (formerly:
    <koslowski@kit.edu>)
-   Sebastian Müller <senpo@posteo.de>
-   Seth Hitefield <sdh11@vt.edu> / <sdhitefield@gmail.com>
-   Shane <shane@skysafe.io>
-   Spencer Ross <brashendeavours@gmail.com>
-   Sreeraj Rajendran <rsreeraj@gmail.com>
-   Stefan Oltmanns <stefan-oltmanns@gmx.net>
-   Stefan Wunsch (formerly: <stefan.wunsch@student.kit.edu>)
-   Stefano Banti <ik2yxt@gmail.com>
-   Stephan Ludwig (donludovico) <st.lu@web.de>
-   Stephen Larew <stephen@slarew.net>
-   Steve Glass <smg@hush.com>
-   Steve Haynal <softerhardware@gmail.com>
-   Steve Markgraf <steve@steve-m.de>
-   Sugandha Gupta <sugandha.gupta@ettus.com>
-   Swapnil Negi <swapnil.negi09@gmail.com>
-   Sylvain Munaut <246tnt@gmail.com> / <tnt@246tNt.com>
-   Thaddeus Koehn <tkoehn@vt.edu>
-   Thomas Habets <habets@google.com>
-   Tim Kuester <tpkuester@gmail.com>
-   Tim Newman <tim.newman@gmail.com>
-   Tim O'Shea <tim.oshea753@gmail.com>
-   Timo Lindfors <timo.lindfors@iki.fi>
-   Tobias Blomberg
-   Toby Flynn <tflynn@redwiretechnology.com>
-   Tom Rondeau <tom@trondeau.com> / <trondeau@vt.edu>
-   Uwe Hermann <uwe@hermann-uwe.de>
-   Volker Schroer <dl1ksv@gmx.de>
-   Yang Dae Hyun <daehyun.yang@gmail.com>
-   Zero\_Chaos <sidhayn@gmail.com>
-   aidan <aidandbush@gmail.com>
-   anshulthakur <anshulthakur@rediffmail.com>
-   beitler
-   EJ Kreinar <ejkreinar@gmail.com>
-   fengzhe29888 <fengzhe29888@gmail.com>
-   flarroca <flarroca@fing.edu.uy>
-   gmazilla
-   gr-sp <shawnp@signalscape.com>
-   hatsunearu
-   ilovezfs <ilovezfs@icloud.com>
-   jan-safar <jan.safar@gla-rrnav.org>
-   japm48
-   jwl <willcode4@gmail.com>
-   kolen <incredible.angst@gmail.com>
-   lazydodo <github@lazydodo.com>
-   linwei <zlinwei@zlinwei.com>
-   luz.paz
-   m-ri
-   mhostetter
-   mi-a <kermitalter@gmail.com>
-   phanselv
-   qarlosalberto <carlosruiznaranjo@gmail.com>
-   rajb245 <rbhattacharjea@gmail.com>
-   rear1019 <rear1019@posteo.de>
-   riatsila <alistair.bird@gmail.com>
-   soggysec <sagui.gvsu@gmail.com>
-   tracierenea <tracie.perez@mavs.uta.edu>
-   vermillionsands
-   krk <keremkat@gmail.com>

