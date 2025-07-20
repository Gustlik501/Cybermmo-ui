const viewport = document.getElementById('viewport');
const bg = document.getElementById('bg-sprite');
function positionSprite() {
  const bottomOffset = window.innerHeight - (viewport.offsetTop + viewport.offsetHeight);
  bg.style.bottom = bottomOffset + 'px';
}
bg.style.position = 'fixed';
bg.style.left = 0;
bg.style.height = '100vh';
bg.style.width = 'auto';
bg.style.pointerEvents = 'none';
bg.style.zIndex = '-1';
positionSprite();
window.addEventListener('resize', positionSprite);
loadSprite('Shia', bg);
