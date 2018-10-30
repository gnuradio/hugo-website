---
{{- $titlesplit := (split .Name "-") }}
{{- $date := (substr .Name 0 10) }}
{{- $title := (replace (substr .Name 11) "-" " ") }}
title: "{{ $title | title }}"
date: {{ $date | plainify | time }}
publishDate: {{ now }}

eventtype: "devcall" # {devcall,meetup,conference}
callurl: "https://hangouts.google.com/$url"
draft: true
---

