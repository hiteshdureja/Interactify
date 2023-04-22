const sendFeed=document.getElementById("send_feed");
sendFeed.onsubmit= function (e) {
    const feedMessage = window.socket
    const feedText=document.getElementById("feed_text");
    feedMessage.send(JSON.stringify({"type": "notification.message", "feed_text": feedText.value}));
    window.location.href = "/";
};