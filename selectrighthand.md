# Select Righthand Screen

This page is shown immediately after a user completes registration. The layout follows the fixed `900×720` viewport described in `design.md`. The screen is split vertically into two equal halves.

## Left Half

* **Character Preview** – a large frame at the top displays the currently selected character's full‑body sprite.
* **Stats & Description** – a frame below the preview shows text fields for stats (e.g., HP, attack, defence) and a short background description.

## Right Half

* **Heading** – centered text reading `Choose your right hand`.
* **Character Selection** – two rows of framed thumbnails. Each frame contains:
  * a small sprite of the character
  * the character's name beneath the image
  * a radio button to select the character

## Layout Sketch

```
+--------------------------------------------------------------+
|                             | Choose your right hand         |
|  Large character image      |                                |
|  [preview area]             |  [thumb] Name (O)  [thumb] Name|
|                             |                                |
|                             |  [thumb] Name (O)  [thumb] Name|
|-----------------------------+--------------------------------|
|   Stats and description     |                                |
|   HP: ???                   |                                |
|   ATK: ???                  |                                |
|   ...                       |                                |
+--------------------------------------------------------------+
```

The overall aesthetic uses the Winamp/keygen–inspired look defined in `style.css` and `design.md`: dark background, neon accents, pixel fonts and outlined transparent panels.
