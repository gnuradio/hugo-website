# GNU Radio website

## Install Prequisites

To render the GNU Radio website a recent (https://gohugo.io)[hugo] installation in the extended mode is required.
If you already have a go environment setup and you are familiar with `go get`. The easiest way to get `hugo` in the required version: `go get ---tags extended -u github.com/gohugoio/hugo/`.


## Run local development version

For viewing a new blogpost/news/article draft run `hugo -D server` and visit the rendered version in your browser at `localhost:1313`. The `-D` is required to show entries which are not yet marked for publishing with `draft: false`.
