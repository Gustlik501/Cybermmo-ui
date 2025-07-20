#!/usr/bin/env python3
"""Convert an image file to a base64 text file for sprites."""
import argparse
import base64
from pathlib import Path

parser = argparse.ArgumentParser(description="Convert image to base64 text for sprites")
parser.add_argument("image", help="Input image file")
parser.add_argument("output", nargs="?", help="Output text file. If omitted, prints to stdout")
args = parser.parse_args()

with open(args.image, 'rb') as img:
    b64 = base64.b64encode(img.read()).decode('ascii')

if args.output:
    Path(args.output).write_text(b64)
else:
    print(b64)
