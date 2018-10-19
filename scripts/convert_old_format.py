#!/usr/bin/env python

import yaml
import os
import argparse
from urllib.request import urlretrieve
from pathlib import Path

def handle_thumbnail(root, thumbnail):
    if thumbnail.endswith("gr_web.svg"):
        return None
    elif thumbnail.endswith("gsoc.png"):
        return "gsoc"
    elif thumbnail.endswith("conference_web.svg"):
        return "conference"
    else:
        extension = thumbnail.split(".")[-1]
        urlretrieve(
            thumbnail,
            Path(root, "thumbnail." + extension))
        return None

def convert_blog(directory):
    for root, dirs, files in os.walk(directory):
        if "index.yml" in files:
            with open(Path(root, "index.yml"), "r") as f:
                metadata = yaml.load(f)
            if metadata.get("type", "internal") == "external":
                with open(Path(root, "index.md"), "w") as new_file:
                    new_file.write("---\n")
                    new_file.write("title: \"{}\"\n".format(
                        metadata.get("title")))
                    new_file.write("author: \"{}\"\n".format(
                        metadata.get("author")))
                    new_file.write("date: \"{}\"\n".format(
                        metadata.get("date")))
                    new_file.write("externalurl: \"{}\"\n".format(
                        metadata.get("url")))
                    new_file.write("sponsored: \"{}\"\n".format(
                        metadata.get("sponsored")))
                    new_file.write("aliases: [\"blog/{}\"]\n".format(
                        metadata.get("full_title")))
                    new_file.write("---\n")
                    new_file.write("{}\n".format(
                        metadata.get("description")))
                    new_file.write("<!--more-->")
                    handle_thumbnail(root, metadata.get("thumbnail"))
                os.remove(Path(root, "index.yml"))
            elif metadata.get("type", "internal") == "internal":
                with open(Path(root, "index.md"), "r") as article_file:
                    article_text = article_file.read()
                with open(Path(root, "index.md"), "w") as new_file:
                    new_file.write("---\n")
                    new_file.write("---\n")
                    new_file.write("title: \"{}\"\n".format(
                        metadata.get("title")))
                    new_file.write("author: \"{}\"\n".format(
                        metadata.get("author")))
                    new_file.write("date: \"{}\"\n".format(
                        metadata.get("date")))
                    new_file.write("sponsored: \"{}\"\n".format(
                        metadata.get("sponsored")))
                    new_file.write("aliases: [\"blog/{}\"]\n".format(
                        metadata.get("full_title")))
                    thumbnail = handle_thumbnail(root, metadata.get("thumbnail"))
                    if thumbnail is not None:
                        new_file.write("thumbnail: \"{}\"\n".format(
                            thumbnail))
                    new_file.write("---\n")
                    new_file.write(article_text)
                    new_file.truncate()
                os.remove(Path(root, "index.yml"))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", default="blog")
    parser.add_argument("-d", "--directory", default="./")
    return parser.parse_args()


def main():
    """go,go,go"""
    args = parse_args()
    if args.type == "blog":
        convert_blog(args.directory)

    return True


if __name__ == "__main__":
    exit(not main())
