const viewport = document.getElementById('viewport');

function renderSprite(name, originX, originY, zIndex, fit = 0, scale = 1) {
  const img = document.createElement('img');
  img.style.position = 'absolute';
  img.style.left = `${originX}px`;
  img.style.bottom = `${originY}px`;
  img.style.pointerEvents = 'none';
  img.style.zIndex = String(zIndex);

  img.onload = () => {
    let finalScale = scale;
    if (fit === 1) {
      finalScale = viewport.clientHeight / img.naturalHeight;
    } else if (fit === 2) {
      finalScale = viewport.clientWidth / img.naturalWidth;
    }
    img.style.width = `${img.naturalWidth * finalScale}px`;
    img.style.height = `${img.naturalHeight * finalScale}px`;
  };

  viewport.appendChild(img);
  loadSprite(name, img);
  return img;
}

renderSprite('Shia', 0, 0, -1, 0, 1);
