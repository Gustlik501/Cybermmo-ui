# Cybermmo UI Design Guide

This document describes the visual design language for the application. The look and feel should emulate the appearance of early-2000s Winamp skins and software keygens.

## Layout and Style

- Use dark backgrounds with neon or metallic accents.
- Opt for pixel fonts or bitmap-style fonts reminiscent of the era.
- Rounded rectangles and beveled edges should be prominent.
- Apply subtle gradients to create a faux-3D effect.
- Use small, pixel-art icons for buttons and controls.
- Windows, panes and other panels should be completely transparent with thick
  outlines like in Winamp since sprite-based backgrounds will provide the
  backdrop.
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
- Group related controls into window-like panels. These panels should have
  completely transparent backgrounds and thick outlines reminiscent of Winamp
  skins, since backgrounds will always be sprite based.
- Navigation should appear as a set of small tabs or buttons styled with the same pixel-art look.

## Fixed Central Layout

- Design for a base resolution of **900×600–720**. The active UI occupies this
  fixed-size area and is centered horizontally within the viewport.
- Do not scale the UI. All components should be positioned with fixed pixel
  values to maintain sprite alignment. The main viewport element itself should
  remain in normal document flow (not absolutely positioned) so the page width
  expands to the full 900px. This ensures horizontal scrolling works correctly
  on narrow displays.
- The outer frame (unused side margins) should display neutral or thematic background visuals—such as textures or ambient illustrations—to fill the remaining screen width.
- Responsive techniques like flexbox, grid, or scaling transforms should not be used. This static layout mirrors early 2000s browser games like Travian or Urban Rivals, ensuring consistent visuals across displays.
- On small screens, horizontal scrolling is acceptable; the layout must remain at native scale.
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

## Implementation Notes

- Pages import `98.css` for basic form and button styling. The neon palette and
  layout rules are defined in `style.css`.
- The fixed `#viewport` element is `900×720` and centered with `margin: 0 auto`.
  Sprites and panels are positioned relative to this container.
- Transparent panels are centered using `transform: translate(-50%, -50%)` and a
  custom `<simple-border>` component draws the thick outline around them.
- Sprites are stored as Base64 text in the `sprites/` directory and loaded at
  runtime with `loadSprite`, `renderSprite`, and `loadBackground` functions in
  `script.js`.
- Z-index values ensure sprites appear beneath panel contents so controls remain
  interactive while still layering above the background.

