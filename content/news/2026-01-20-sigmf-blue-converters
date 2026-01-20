---
title: "SigMF converter for MIDAS Blue recordings now part of sigmf-python"
author: "Marc Lichtman"
date: "2026-01-20"
categories: ["sigmf","bluefiles"]
aliases: ["/news/sigmf-blue-converters"]
banner: "sigmf_logo.png"
---

### Bluefile Converter

The SigMF leadership is excited to announce that the [sigmf-python package Release v1.6.1](https://github.com/sigmf/sigmf-python/releases/tag/v1.6.1) includes the addition of a converter for the MIDAS Blue and Platinum BLUE RF recording formats (commonly `.cdif` files).
This allows you to seamlessly integrate BLUE file recordings into your SigMF workflows.
The converter automatically detects BLUE file formats and can create standard SigMF file pairs, archives, or Non-Conforming Datasets (NCDs) that reference the original recording.
Original BLUE header information is preserved in the SigMF metadata under the `blue:` namespace.
A big thanks to Teque5 and KelseyCreekSoftware for their work!

### Python API Example

You can use the converter directly within your Python scripts. If no output path is provided, a metadata-only `SigMFFile` object for a Non-Conforming Dataset (NCD) is returned without writing any files.

```python
from sigmf.convert.blue import blue_to_sigmf

# Convert a BLUE file to a standard SigMF file pair
meta = blue_to_sigmf(blue_path="recording.cdif", out_path="recording")

# Create an NCD object in memory (no files written)
meta = blue_to_sigmf(blue_path="recording.cdif")

# Access samples and metadata
all_samples = meta.read_samples()
sample_rate = meta.sample_rate

# Original bluefile metadata preserved (in `fixed`, `adjunct`, and `extended` keys)
meta.get_global_field('blue:adjunct')
```

```json
{'xstart': 0.025, 'xdelta': 5.5555555555555555e-08, 'xunits': 1}
```

### Command-Line Example

The converter is also integrated into the unified `sigmf_convert` command-line tool, which automatically detects the input file format.

```bash
# Convert a .cdif file to a SigMF archive
sigmf_convert recording.cdif recording.sigmf --archive

# Create a non-conforming dataset (metadata only, references original data)
sigmf_convert recording.cdif recording --ncd
```

For questions/comments/feedback feel free to post a new issue to the [python package github repo](https://github.com/sigmf/sigmf-python/issues).
