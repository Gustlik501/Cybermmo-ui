const viewport = document.getElementById('viewport');

// Load a sprite from a base64 .txt file and assign it to an image element
async function loadSprite(name, imgEl) {
  try {
    const resp = await fetch(`sprites/${name}.txt`);
    const base64 = (await resp.text()).trim();
    imgEl.src = `data:image/png;base64,${base64}`;
  } catch (e) {
    console.error('Failed to load sprite', name, e);
  }
}

// Render a sprite at a given position with optional fit/scale
// zIndex defaults to 20 so sprites appear between the panel and its contents
function renderSprite(name, originX, originY, zIndex = 20, fit = 0, scale = 1) {
  const img = document.createElement('img');
  img.style.position = 'absolute';
  img.style.left = `${originX}px`;
  img.style.bottom = `${originY}px`;
  img.style.pointerEvents = 'none';
  img.style.zIndex = String(zIndex);

  // Attach scaling logic after image loads
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
  loadSprite(name, img); // Async load sets src and triggers onload
  return img;
}

// Optional: Load a background from a base64 sprite
async function loadBackground(name, element = document.body) {
  try {
    const resp = await fetch(`sprites/${name}.txt`);
    const base64 = (await resp.text()).trim();
    element.style.backgroundImage = `url(data:image/png;base64,${base64})`;
  } catch (e) {
    console.error('Failed to load background sprite', name, e);
  }
}

// Simple border overlay component
class SimpleBorder extends HTMLElement {
  connectedCallback() {
    const selector = this.getAttribute('target');
    const zIndex = this.getAttribute('z-index') || '10';
    const target = document.querySelector(selector);
    if (!target) return;

    const rect = target.getBoundingClientRect();
    const parentRect = this.parentElement.getBoundingClientRect();
    const style = this.style;

    const border = this.getAttribute('border') || '2px solid red';
    const borderRadius = this.getAttribute('border-radius') || '0';

    style.position = 'absolute';
    // Position relative to the parent element so the border matches the target
    style.top = `${rect.top - parentRect.top}px`;
    style.left = `${rect.left - parentRect.left}px`;
    style.width = `${rect.width}px`;
    style.height = `${rect.height}px`;
    style.boxSizing = 'border-box';
    style.border = border;
    style.borderRadius = borderRadius;
    style.pointerEvents = 'none';
    style.zIndex = zIndex;
  }
}

customElements.define('simple-border', SimpleBorder);

// Basic drawing utilities
function drawRect(x, y, width, height, color = '#0ff', zIndex = 30) {
  const div = document.createElement('div');
  Object.assign(div.style, {
    position: 'absolute',
    left: `${x}px`,
    bottom: `${y}px`,
    width: `${width}px`,
    height: `${height}px`,
    boxSizing: 'border-box',
    border: `1px solid ${color}`,
    pointerEvents: 'none',
    zIndex: String(zIndex)
  });
  viewport.appendChild(div);
  return div;
}

function drawLine(x1, y1, x2, y2, color = '#0ff', width = 2, zIndex = 30) {
  const length = Math.hypot(x2 - x1, y2 - y1);
  const angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
  const div = document.createElement('div');
  Object.assign(div.style, {
    position: 'absolute',
    left: `${x1}px`,
    bottom: `${y1}px`,
    width: `${length}px`,
    height: `${width}px`,
    background: color,
    transformOrigin: '0 0',
    transform: `rotate(${angle}deg)`,
    pointerEvents: 'none',
    zIndex: String(zIndex)
  });
  viewport.appendChild(div);
  return div;
}

