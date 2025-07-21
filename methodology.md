# UI Methodology

This document outlines a common approach for rendering sprites and borders across the pages in this repository. It also notes where CSS and drawing utilities should live so every screen behaves consistently.

## Sprite Loading and Rendering

* **Base64 sprites** – All images are stored in the `sprites/` folder as Base64 text files. The existing `loadSprite` and `renderSprite` helpers in `script.js` read these files and attach them to `<img>` elements.
* **Layering** – Sprites rendered with `renderSprite` are absolutely positioned inside `#viewport`. They default to `z-index: 20` so that sprites appear above the background but below panel content as shown in `script.js` lines 16–38.
* **Reuse across pages** – Each page calls these functions rather than duplicating logic. For example `login.html` renders a sprite once the page loads (lines 29–33) and `register.html` does the same (lines 31–35).
* **Backgrounds** – `loadBackground` can apply a sprite as a CSS background. It should be used if a page needs a full‑screen image.

## Borders

* **No direct borders on elements** – Layout elements such as panels should not include their own border styles. Instead a separate overlay element is used. `index.html` shows a `<simple-border>` element positioned over the `.panel` (lines 21–22).
* **SimpleBorder component** – The custom element defined at the end of `script.js` (lines 52–81) draws a rectangular border around a target element. It reads the target’s size and position, then creates a matching overlay. All pages currently use this component to outline panels.
* **Future sprite borders** – More elaborate borders will be implemented later using a similar element (e.g. `<sprite-border>`). Keeping borders as separate components allows them to be swapped without touching page markup.

## CSS Placement

* **Centralized stylesheet** – All styling lives in `style.css`. Pages should not include inline `<style>` blocks. For instance, the layout rules for `selectrighthand.html` are currently embedded in the page (lines 9–35) and should be moved into the stylesheet so every page shares the same classes.
* **Reusable classes** – Define classes such as `.panel`, `.thumb-grid`, or `.thumb` in `style.css` and apply them in HTML. This keeps the markup clean and ensures consistent look and feel.

## Draw Utilities

* **Basic drawing helpers** – In addition to sprite helpers, the project should expose small utilities for drawing simple shapes (lines, rectangles) on top of the viewport. These can be placed in a new module or alongside the sprite functions in `script.js` so pages can import and reuse them.
* **Use cases** – These utilities can highlight regions, draw separators, or annotate sprites without modifying the sprite images themselves.

## Summary

By loading sprites through shared helpers, using overlay components for borders, and keeping all CSS inside `style.css`, pages remain uniform. Future enhancements like sprite-based borders or additional drawing utilities can plug into the same structure without rewriting existing screens.
