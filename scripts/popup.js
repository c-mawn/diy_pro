document.addEventListener('DOMContentLoaded', () => {
  const imageSearchButton = document.getElementById('image-search');
  if (imageSearchButton) {
    imageSearchButton.onclick = () => {
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const activeTab = tabs[0];
        if (activeTab && activeTab.id) {
          chrome.scripting.executeScript({
            target: { tabId: activeTab.id },
            files: ['scripts/content.js']
          });
        } else {
          console.error("Could not find active tab.");
        }
      });
    };
  }

  const loginButton = document.getElementById('log-in');
  if (loginButton) {
    loginButton.onclick = () => {
      chrome.tabs.create({ url: "http://127.0.0.1:8000/accounts/login" });
    };
  }

  const searchUsersButton = document.getElementById('search-users');
  if (searchUsersButton) {
    searchUsersButton.onclick = () => {
      chrome.tabs.create({ url: "http://127.0.0.1:8000/accounts/search_users/" });
    };
  }
});
