// This script runs on the user's webpage, not in the popup.

// --- 1. Create the UI ---
// Create a full-page overlay
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

// Create the selection box
const selectionBox = document.createElement('div');
selectionBox.id = 'diy-pro-selection';
Object.assign(selectionBox.style, {
  position: 'absolute',
  border: '2px dashed #3AB0FF',
  backgroundColor: 'rgba(58, 176, 255, 0.2)',
  zIndex: '9999999',
  pointerEvents: 'none' // So it doesn't block mouse events
});
document.body.appendChild(selectionBox);

// --- 2. State variables ---
let isDrawing = false;
let startX = 0;
let startY = 0;
console.log("in content.js");

// --- 3. Event Listeners ---
overlay.addEventListener('mousedown', (e) => {
  // Start drawing
  isDrawing = true;
  startX = e.clientX;
  startY = e.clientY;
  
  // Position the box
  selectionBox.style.left = `${startX}px`;
  selectionBox.style.top = `${startY}px`;
  selectionBox.style.width = '0px';
  selectionBox.style.height = '0px';
});

overlay.addEventListener('mousemove', (e) => {
  if (!isDrawing) return;

  // Calculate width, height, and position
  const currentX = e.clientX;
  const currentY = e.clientY;

  const width = currentX - startX;
  const height = currentY - startY;

  // Handle drawing in all directions (up-left, down-right, etc.)
  selectionBox.style.width = `${Math.abs(width)}px`;
  selectionBox.style.height = `${Math.abs(height)}px`;
  selectionBox.style.left = `${width > 0 ? startX : currentX}px`;
  selectionBox.style.top = `${height > 0 ? startY : currentY}px`;
});

overlay.addEventListener('mouseup', (e) => {
  isDrawing = false;
  
  // Get the final coordinates of the box
  const rect = {
    left: parseInt(selectionBox.style.left, 10),
    top: parseInt(selectionBox.style.top, 10),
    width: parseInt(selectionBox.style.width, 10),
    height: parseInt(selectionBox.style.height, 10)
  };

  // --- 4. Clean up and Send Message ---
  // Remove the UI
  document.body.removeChild(overlay);
  document.body.removeChild(selectionBox);

  // Send the coordinates to the background script
  if (rect.width > 0 && rect.height > 0) {
    // Send a message to the "brain" (background.js)
    chrome.runtime.sendMessage({
      type: 'TAKE_SCREENSHOT',
      data: rect
    });
  }
});