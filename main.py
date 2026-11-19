#!/usr/bin/env python3
"""Entrypoint for the news-image-20261119 entry.

Copies the poster (entry.png) to the output directory as entry.png.
The poster itself is deterministic: it was drawn once by build_poster.py
and is shipped in this repository, so both runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# No network, no randomness: the shipped PNG is copied byte for byte.


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(OUT, "entry.png"))


if __name__ == "__main__":
    main()
