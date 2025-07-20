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
