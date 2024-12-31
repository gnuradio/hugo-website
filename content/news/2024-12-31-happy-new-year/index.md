---
title: "Happy New Year from GNU Radio"
author: "The GNU Radio Board"
date: "2024-12-31"
categories: ["project updates"]
aliases: ["/news/happy-new-year-2025"]
---

Greetings GNU Radio Community!  We wanted to take a moment to look back on all the awesome things that have gone on in this incredible community over the past year, some of which we may not have been so great at making everyone aware - there’s our first New Year’s Resolution!

### ARDC Grant
2024 saw the completion of our usability grant that was generously issued by ARDC in 2022 (https://www.ardc.net/apply/grants/2022-grants/grant-gnu-radio-usability-enhancements/).  This allowed several key advancements in the codebase and documentation to make GNU Radio more accessible to users, notably the QT GRC version that has become a part of the main branch and launchable with the –qt flag.  Through this grant we also had several key improvements to documentation, both tutorials and in-code machinery, as well as work toward functional installers for Windows/Mac.  

### Releases
Our 3.10 series saw several key releases in 2024 - including the packaging of v3.10.9.2. into Ubuntu 24.04.  Thanks to the hard work of Jeff Long our Maintainer for the past several years, releases have been churning out consistently.  Unfortunately Jeff has stepped back in his role as Maintainer, and we are working to fill in the void with a more distributed group of module maintainers.  So in 2025 we would love to hear from you if you want to get involved in a particular area of the codebase.  There are also a number of github issues listed as “good first issue” if you want to try your hand at contributing to the codebase.

### Google Summer of Code
We had 2 excellent GSoC students taking on interesting projects this past summer.  Kayla took on the task of improving our FEC module and integrating features from AFF3CT.  Her work can be seen here: https://github.com/kaylacomer/gr-fec_dev.  Zaky tackled the task of introducing modular workflows into GRC, and much of this is on its way into the mainline codebase (see https://github.com/gnuradio/gnuradio/pull/7548).  We hope to participate in GSoC again this year!

### FOSDEM
Though there was only a partially dedicated Software Radio dev room this past year, we set up a booth at FOSDEM for the first time.  This led to a different level of interaction at the event, and we are planning to do the same next year.

### EU GR Days
EU GR Days 2024 was held at the FAIR particle accelerator near Darmstadt, Germany in August.  This was a unique opportunity to learn about the advances in GR4 in a hands-on manner, but also continue the tradition of EU GR Days with presentations and tutorials (thanks to JM Freidt) of current GNU Radio (GR3) as well.  On the GR4 front, we saw incredibly informative presentations from the core GR4 development team at FAIR including Mattias Kretz (https://www.youtube.com/live/3NgXFUQxtss?si=kq41imTsKMpdqFEn&t=18772), and an in-depth tutorial by Simon Ledbevev and Alex Krimm (https://www.youtube.com/live/ce496ZCwlqA?si=ogI7OASo9dVbyHsT&t=1114).  These brought many of the motivations of utilizing modern c++ and rebuilding the core as well as examples of how to use the GR4 runtime in practice through some hands-on tutorials.  Dani Estevez also presented his work on using GR4 to develop a working packet radio which was an exciting “kicking of the tires” for the framework (https://www.youtube.com/watch?v=Utpvxn77P8k).  We are especially grateful to Ralph Steinhagen and FAIR for spearheading the planning and hosting of this event.

### GNU Radio Conference 2024
It feels like we just wrapped up an exciting GRCon - but it has been over 2 months already.  All of the presentations can be seen here (https://www.youtube.com/@GNURadioProject/streams).  But it was an incredible event with notable keynotes from Jack Dongarra, Shahriar Shahramian, Philip Erickson, and Christina Collins, as well as invited workshops from Dan Boschen.  The technical track and workshops were all terrific this year, but the best part of GRCon is always the interaction with the community which we got to extend with several social events.  And of course none of this is possible without our generous sponsors that made the event possible.  

### Leadership Updates
Marcus Mueller, longtime GNU Radio architect, maintainer, and answerer of questions stepped up to join the board along with Marc and Josh.  A sincere thank you to Martin Braun for his years of service on the board and all the efforts he drove along the way.  We also were happy to welcome Seth Hitefield earlier in the year as part of the General Assembly.

### Help Wanted
We are always open to more people getting involved in the efforts that keep this project healthy.  Specifically we are looking for:
Maintainers of specific code modules, as well as general reviewers of PRs - reach out info@gnuradio.org
Media / Outreach - help improve our presence on youtube/X
Conference - Lots of ways to help - reach out grcon@gnuradio.org

## What to look forward to in 2025
- FOSDEM
  - Stop by our booth!
- GRCon25 Announcement
  - We are very close to announcing our location for GRCon25 - so please start thinking about the work you want to come present this coming year
- Native Installers
  - This has been in the works as part of the ARDC grant, but we hope to make the end result of this public very soon
- New Developments, OOTs, Academic Research, etc
  - The great thing about an open source project and ecosystem is that we don’t know what types of project will transpire in the community.  We love to hear how GNU Radio is being used, OOTs that have been developed, and look forward to all the incredible work in the ecosystem in 2025 that can be used to enable innovation in scientific applications
- GR4 Advancement
  - GR4 has made great progress the last couple of years especially in its use at FAIR, but in 2025 we hope to continue adoption into the broader community. 
  - It has been fairly quiet in Architecture Working Group, but we met one last time in 2024 very productively - prioritizing features that we should pursue in the near term, and are planning to have a standing monthly meeting to maintain consistency

Wishing you a happy new year!

Sincerely,
Josh, Marc, Marcus
