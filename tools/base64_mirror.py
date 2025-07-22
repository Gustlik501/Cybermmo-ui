#!/usr/bin/env python3
"""Mirror a base64-encoded sprite horizontally."""
import argparse
import base64
from io import BytesIO
from pathlib import Path
import sys

from PIL import Image


def read_base64(path: str | None) -> bytes:
    """Read base64 data from a file or stdin."""
    if path:
        data = Path(path).read_text().strip()
    else:
        data = sys.stdin.read().strip()
    return base64.b64decode(data)


def write_base64(data: bytes, path: str | None) -> None:
    b64 = base64.b64encode(data).decode("ascii")
    if path:
        Path(path).write_text(b64)
    else:
        print(b64)


def main() -> None:
    parser = argparse.ArgumentParser(description="Mirror a base64 encoded image left-to-right")
    parser.add_argument("input", nargs="?", help="Input text file with base64 data. Reads stdin if omitted")
    parser.add_argument("output", nargs="?", help="Output text file for base64 result. Writes to stdout if omitted")
    args = parser.parse_args()

    img_bytes = read_base64(args.input)
    img = Image.open(BytesIO(img_bytes))

    mirrored = img.transpose(Image.FLIP_LEFT_RIGHT)

    buf = BytesIO()
    mirrored.save(buf, format="PNG")
    write_base64(buf.getvalue(), args.output)


if __name__ == "__main__":
    main()
