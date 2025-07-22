# Tools

This folder contains helper scripts for working with sprites.

## `sprite_to_base64.py`

Converts an image file to a Base64-encoded text format used by the project.

### Usage

```bash
python3 tools/sprite_to_base64.py input.png output.txt
```

If `output.txt` is omitted, the Base64 string is written to stdout.

## `base64_toonify.py`

Applies a cel-shaded "toon" effect to an input image provided as a Base64 string.
The processed result is returned as another Base64 string.

### Usage

```bash
# Read base64 data from input.txt and write the processed result to output.txt
python3 tools/base64_toonify.py input.txt output.txt
```

Omit `input.txt` to read from standard input or omit `output.txt` to write the
base64 result to standard output.

## `base64_denoise.py`

Applies a 3x3 median filter to an image provided as a Base64 string. This helps remove salt-and-pepper noise while preserving edges. The processed image is returned as another Base64 string.

### Usage

```bash
# Read base64 data from input.txt and write the denoised result to output.txt
python3 tools/base64_denoise.py input.txt output.txt
```

Omit `input.txt` to read from standard input or omit `output.txt` to write the result to standard output.

## `base64_mirror.py`

Horizontally flips a Base64 sprite so left becomes right and vice versa.

### Usage

```bash
# Read base64 data from input.txt and write the mirrored result to output.txt
python3 tools/base64_mirror.py input.txt output.txt
```

As with the other tools, omit `input.txt` to read from stdin or omit
`output.txt` to write the Base64 result to stdout.

## `base64_resize.py`

Resizes a Base64 sprite to the given width and height.

### Usage

```bash
# Resize sprite to 32x32 pixels
python3 tools/base64_resize.py 32 32 input.txt output.txt
```

As with the other tools, omit `input.txt` to read from stdin or omit
`output.txt` to write the Base64 result to stdout.
