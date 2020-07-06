# GNU Radio website

## Install Prequisites

To render the GNU Radio website a recent [hugo](https://gohugo.io) installation in the "extended" mode is required.  To install hugo on your system choose from one of the following options:

1. If you already have `go get` set up, the easiest way to get `hugo` in the required version is: `go get --tags extended -u github.com/gohugoio/hugo/`.
2. Download and install hugo [from one of their releases](https://github.com/gohugoio/hugo/releases), make sure to download the "hugo_extended_XXXX" file for your OS.  The latest version should work, at the time of writing this it is 0.73.  Either install it, or unpack and put the binary in your path.  On Ubuntu this process can be done with:
   * `cd ~/Downloads`
   * `wget https://github.com/gohugoio/hugo/releases/download/v0.73.0/hugo_extended_0.73.0_Linux-64bit.deb`
   * `sudo dpkg -i hugo_extended_0.73.0_Linux-64bit.deb`

Avoid using the hugo packaged by your distro, their version of hugo is likely not the "extended" variant.

## Run local development version

For viewing a new blogpost/news/article draft run `hugo -D server` and visit the rendered version in your browser at `localhost:1313`. The `-D` is required to show entries which are not yet marked for publishing with `draft: false`.

## How to add stuff to the website

If you want to make a change to the website, add a news or blog item, fix a
typo or whatever, simply clone this repo and make a pull request against it.
When the admins approve the PR, we will re-generate the website and upload the
new version.

This website uses the Hugo static site generator. Its documentation can be
found here: https://gohugo.io/documentation/

### How to add a news or blog article

If you have Hugo installed in a reachable path, simply run

    hugo new content/news/2018-XX-XX-short-title.md

or

    hugo new content/blog/2018-XX-XX-short-title.md

and it will create a template for a new article on the news or blog page. Alternatively, copy an old news or blog item (if you don't have Hugo running) and modify it accordingly.

Before submitting a pull request, make sure to remove the `draft: true` line
from the file.

### How to add a topic to the splash screen on the greeting page (the carousel)

When you go to https://gnuradio.org/, the first thing you see (under the menu)
is a great big picture, a "Learn More" button, and some tag line. It's called
the carousel because you can click the arrows on the left and right and it'll
give you different content.

To add one of those, or to change the order, go to `data/carousel` and add
another TOML file. The order is determined by the weight.
