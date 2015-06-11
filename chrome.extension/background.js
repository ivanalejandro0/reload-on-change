var state = false;  // refresh starts turned off
var refreshInterval;
var count = 0;

chrome.tabs.onUpdated.addListener(function(tab){
    var icon = state ? 'logo-on.png' : 'logo-off.png';

    chrome.browserAction.setIcon({
        path: icon,
        tabId: tab.id
    });
});

chrome.browserAction.onClicked.addListener(function(tab) {
    state = !state;

    var icon = state ? 'logo-on.png' : 'logo-off.png';

    chrome.browserAction.setIcon({
        path: icon,
        tabId: tab.id
    });

    if (!state) {
        clearInterval(refreshInterval);
        return;
    }

    refreshInterval = setInterval(function() {
        try {
            chrome.tabs.executeScript(tab.id, { file: "reloader.js" });
        } catch (err) {}
    }, 250);
});
