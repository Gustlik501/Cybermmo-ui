async function loadSprite(name, imgEl) {
  try {
    const resp = await fetch(`sprites/${name}.txt`);
    const text = await resp.text();
    imgEl.src = `data:image/png;base64,${text.trim()}`;
  } catch (e) {
    console.error('Failed to load sprite', name, e);
  }
}
