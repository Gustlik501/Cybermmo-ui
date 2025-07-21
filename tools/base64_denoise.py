#!/usr/bin/env python3
"""Apply a 3x3 median denoise to a base64-encoded sprite."""
import argparse
import base64
from io import BytesIO
from pathlib import Path
import sys

import cv2
import numpy as np
from PIL import Image


def median_denoise_array(arr: np.ndarray) -> np.ndarray:
    """Return a median-filtered version of the image array."""
    if arr.ndim == 3 and arr.shape[2] == 4:
        rgb = arr[:, :, :3]
        alpha = arr[:, :, 3]
        denoised_rgb = cv2.medianBlur(rgb, 3)
        return np.dstack((denoised_rgb, alpha))
    return cv2.medianBlur(arr, 3)


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
    parser = argparse.ArgumentParser(description="Apply a 3x3 median denoise to a base64 encoded image")
    parser.add_argument("input", nargs="?", help="Input text file with base64 data. Reads stdin if omitted")
    parser.add_argument("output", nargs="?", help="Output text file for base64 result. Writes to stdout if omitted")
    args = parser.parse_args()

    img_bytes = read_base64(args.input)
    img = Image.open(BytesIO(img_bytes))

    if img.mode == "RGBA":
        arr = np.array(img)
        denoised = median_denoise_array(arr)
        result = Image.fromarray(denoised, mode="RGBA")
    else:
        arr = np.array(img.convert("RGB"))
        denoised = median_denoise_array(arr)
        result = Image.fromarray(denoised)

    buf = BytesIO()
    result.save(buf, format="PNG")
    write_base64(buf.getvalue(), args.output)


if __name__ == "__main__":
    main()
