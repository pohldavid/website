#!/usr/bin/python3

import pathlib

from pathlib import Path

source = Path("bp.md")
destination = Path("/home/dave/Desktop/website/public/static/bp.md")

#if not destination.exists():
#    source.replace(destination)
source.replace(destination)
