To add a new sponsor-specific page,

1- in hugo-website/layouts/grcon/grcon20/sponsors create a new .html file (e.g. by copying one of the existing ones) and fill it out with whatever we want on the page.  It's specifically not parameterized so we can customize it however we want, not all sponsors will want the same stuff
2- decide on a "shortname" for the sponsor, one word all lowercase, you'll use it in the next step
3- in hugo-website/content/grcon/grcon20/sponsors create a new directory with the sponsor's shortname
4- inside that new directory create a _index.md and set layout to sponsors shortname, set title to sponsor's full name, and then also set the last line to sponsor's full name
5- also inside that new directory you have to stick the sponsor's logo, yes it's duplicated from the sponsors directory but i couldn't figure out how to get it to use the existing one
6- in hugo-website/config.yml you need to add the new page
