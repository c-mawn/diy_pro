// Wait for the DOM to be ready
document.addEventListener('DOMContentLoaded', () => {
  // Find the image search button
  const imageSearchButton = document.getElementById('image-search');

  if (imageSearchButton) {
    // Listen for a click
    imageSearchButton.onclick = () => {
      // Get the current active tab
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const activeTab = tabs[0];
        if (activeTab && activeTab.id) {
          // Inject the content.js script into the active tab
          chrome.scripting.executeScript({
            target: { tabId: activeTab.id },
            files: ['scripts/content.js']
          });

          // Close the popup window so the user can see the page
          // window.close();
        } else {
          console.error("Could not find active tab.");
        }
      });
    };
  }
});