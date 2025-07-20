#!/usr/bin/env python3
"""Apply toon-shading to a base64-encoded image.

The script reads a base64 string from a file or stdin, applies a toon/cel shading
style using OpenCV, and outputs the processed image as a base64 string. The
output is written to stdout or an optional file path.
"""
import argparse
import base64
from io import BytesIO
from pathlib import Path

import cv2
import numpy as np
from PIL import Image


def stylize_array(img: np.ndarray) -> np.ndarray:
    """Return a toon-shaded version of the provided RGB image array."""
    # Slight resize for smoother effect
    small = cv2.pyrDown(img)
    small = cv2.pyrUp(small)

    # Bilateral filter preserves edges
    smooth = cv2.bilateralFilter(small, d=9, sigmaColor=75, sigmaSpace=75)

    # Edge detection
    gray = cv2.cvtColor(smooth, cv2.COLOR_RGB2GRAY)
    edges = cv2.adaptiveThreshold(
        cv2.medianBlur(gray, 7),
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        2,
    )

    # Posterization via k-means
    z = smooth.reshape((-1, 3))
    z = np.float32(z)
    k = 8
    _, labels, centers = cv2.kmeans(
        z,
        k,
        None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
        10,
        cv2.KMEANS_RANDOM_CENTERS,
    )
    poster = centers[labels.flatten()].reshape(smooth.shape).astype(np.uint8)

    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    cartoon = cv2.bitwise_and(poster, edges_colored)
    return cartoon


def read_base64(path: str | None) -> bytes:
    """Read base64 data from file or stdin."""
    if path:
        data = Path(path).read_text().strip()
    else:
        data = input().strip()
    return base64.b64decode(data)


def write_base64(data: bytes, path: str | None) -> None:
    b64 = base64.b64encode(data).decode("ascii")
    if path:
        Path(path).write_text(b64)
    else:
        print(b64)


def main() -> None:
    parser = argparse.ArgumentParser(description="Toon-shade a base64 encoded image")
    parser.add_argument("input", nargs="?", help="Path to text file with base64 data. Reads stdin if omitted")
    parser.add_argument("output", nargs="?", help="Output text file for base64 result. Writes to stdout if omitted")
    args = parser.parse_args()

    img_bytes = read_base64(args.input)
    img = Image.open(BytesIO(img_bytes)).convert("RGB")
    arr = np.array(img)
    toon = stylize_array(arr)
    result = Image.fromarray(toon)
    buf = BytesIO()
    result.save(buf, format="PNG")
    write_base64(buf.getvalue(), args.output)


if __name__ == "__main__":
    main()
