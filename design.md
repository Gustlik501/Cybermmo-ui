# Cybermmo UI Design Guide

This document describes the visual design language for the application. The look and feel should emulate the appearance of early-2000s Winamp skins and software keygens.

## Layout and Style

- Use dark backgrounds with neon or metallic accents.
- Opt for pixel fonts or bitmap-style fonts reminiscent of the era.
- Rounded rectangles and beveled edges should be prominent.
- Apply subtle gradients to create a faux-3D effect.
- Use small, pixel-art icons for buttons and controls.
- Use [98.css](https://github.com/jdan/98.css) to style tabs, buttons, and other controls, but avoid using its window components.

## Color Palette

- Base colors: black or very dark gray.
- Accent colors: bright neon green, cyan, magenta and orange.
- Use high contrast to keep text readable over backgrounds.

## Typography

- Primary font should mimic the pixelated style of Windows 98, such as `"Pixelated MS Sans Serif"` from 98.css.
- Headers can use a slightly larger size but keep them blocky and minimal.

## Layout Rules

- Keep UI elements compact, with small padding and margins.
- Group related controls into window-like panels with thin borders.
- Navigation should appear as a set of small tabs or buttons styled with the same pixel-art look.
- Ensure the layout scales well on mobile devices so the interface remains usable on small screens.

## Sprites

All images and icons should be stored in the `sprites/` directory as Base64-encoded text files to avoid storing binary files in the repository.

- Each sprite should have a descriptive name ending in `.txt` (e.g. `play-button.txt`).
- The text file contains only the Base64 string of the image data.
- When loading sprites in the application, read the Base64 contents and create an `img` element via `src="data:image/png;base64,<contents>"`.
- Focus on large background sprites featuring cyber‑style characters. Think of the vibe of shows like *Cowboy Bebop* as a placeholder. Small decorative icons are optional and can be omitted.
- Controls and panels should match these backgrounds so the interface feels cohesive.

## Consistency

- Every page must follow this design language for fonts, colors, and layout.
- Reuse sprites across pages whenever possible.
- Keep the window/panel layout consistent to emulate a desktop-app look.

