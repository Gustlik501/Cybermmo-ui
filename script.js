const viewport = document.getElementById('viewport');
const bg = document.getElementById('bg-sprite');

bg.style.position = 'absolute';
bg.style.left = '0';
bg.style.bottom = '0';
bg.style.height = '100%';
bg.style.width = 'auto';
bg.style.pointerEvents = 'none';
bg.style.zIndex = '-1';

loadSprite('shia-toonified', bg);
