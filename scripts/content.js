// --- Prevent duplicate injection ---
if (window.diyProOverlayActive) {
  console.log("DIY Pro overlay already running — skipping reinjection.");
} else {
  window.diyProOverlayActive = true;

  // --- 1. Create the UI ---
  const overlay = document.createElement('div');
  overlay.id = 'diy-pro-overlay';
  Object.assign(overlay.style, {
    position: 'fixed',
    top: '0',
    left: '0',
    width: '100vw',
    height: '100vh',
    backgroundColor: 'rgba(0, 0, 0, 0.3)',
    cursor: 'crosshair',
    zIndex: '9999998'
  });
  document.body.appendChild(overlay);

  const selectionBox = document.createElement('div');
  selectionBox.id = 'diy-pro-selection';
  Object.assign(selectionBox.style, {
    position: 'fixed',
    border: '2px dashed #3AB0FF',
    backgroundColor: 'rgba(58, 176, 255, 0.2)',
    zIndex: '9999999',
    pointerEvents: 'none'
  });
  document.body.appendChild(selectionBox);

  let isDrawing = false;
  let startX = 0;
  let startY = 0;
  console.log("in content.js");

  overlay.addEventListener('mousedown', (e) => {
    isDrawing = true;
    startX = e.clientX;
    startY = e.clientY;
    selectionBox.style.left = `${startX}px`;
    selectionBox.style.top = `${startY}px`;
    selectionBox.style.width = '0px';
    selectionBox.style.height = '0px';
  });

  overlay.addEventListener('mousemove', (e) => {
    if (!isDrawing) return;
    const currentX = e.clientX;
    const currentY = e.clientY;
    const width = currentX - startX;
    const height = currentY - startY;
    selectionBox.style.width = `${Math.abs(width)}px`;
    selectionBox.style.height = `${Math.abs(height)}px`;
    selectionBox.style.left = `${width > 0 ? startX : currentX}px`;
    selectionBox.style.top = `${height > 0 ? startY : currentY}px`;
  });

  overlay.addEventListener('mouseup', () => {
    isDrawing = false;
    const rect = {
      left: parseInt(selectionBox.style.left, 10),
      top: parseInt(selectionBox.style.top, 10),
      width: parseInt(selectionBox.style.width, 10),
      height: parseInt(selectionBox.style.height, 10)
    };

    document.body.removeChild(overlay);
    document.body.removeChild(selectionBox);
    window.diyProOverlayActive = false;

    if (rect.width > 0 && rect.height > 0) {
      chrome.runtime.sendMessage({
        type: 'TAKE_SCREENSHOT',
        data: rect
      });
    }
  });
}
