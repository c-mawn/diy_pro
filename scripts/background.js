// Listen for messages from content.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === 'TAKE_SCREENSHOT') {
    // Take a screenshot of the entire visible tab
    chrome.tabs.captureVisibleTab(null, { format: 'png' }, (dataUrl) => {
      if (chrome.runtime.lastError || !dataUrl) {
        console.error(chrome.runtime.lastError || "Failed to capture tab.");
        return;
      }
      
      // Now we crop the full image
      cropImage(dataUrl, request.data);
    });
    // Return true to indicate we will send a response asynchronously
    // (though in this case we don't, it's good practice)
    return true; 
  }
});

async function cropImage(fullImageUrl, rect) {
  // --- This is the new, service-worker-safe method ---

  // 1. Fetch the image dataUrl as a Blob
  const blob = await fetch(fullImageUrl).then(res => res.blob());

  // 2. Create an ImageBitmap from the Blob
  const imageBitmap = await createImageBitmap(blob);

  // 3. Create an OffscreenCanvas to draw on
  const canvas = new OffscreenCanvas(rect.width, rect.height);
  const ctx = canvas.getContext('2d');

  // 4. Draw the *cropped* part of the ImageBitmap onto the canvas
  // The parameters are:
  // sourceImage, sourceX, sourceY, sourceWidth, sourceHeight,
  // destX, destY, destWidth, destHeight
  ctx.drawImage(
    imageBitmap,
    rect.left, rect.top, rect.width, rect.height, // Source rectangle (the part we want)
    0, 0, rect.width, rect.height // Destination rectangle (fill the canvas)
  );

  // 5. Get the cropped image as a new Blob from the canvas
  const croppedBlob = await canvas.convertToBlob();

  // 6. Convert the Blob to a Data URL to be stored
  const croppedDataUrl = await new Promise(resolve => {
    const reader = new FileReader();
    reader.onloadend = () => resolve(reader.result);
    reader.readAsDataURL(croppedBlob);
  });
  // 7. Save image to storage
  chrome.storage.local.set({ lastImage: croppedDataUrl }, () => {
    console.log('Image saved to chrome.storage.local');

    // --- 8. Open your local website in a new tab ---
    chrome.tabs.create({ url: "http://127.0.0.1:8000/tools/closest_matches" });
  });
}
