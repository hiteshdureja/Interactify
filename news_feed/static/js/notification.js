const sendFeed=document.getElementById("send_feed");
sendFeed.onsubmit= function (e) {
    const feedMessage = window.socket
    const feedText=document.getElementById("feed_text");
    const user_id=document.getElementById("user_id");
    feedMessage.send(JSON.stringify({"type": "notifications", "feed_text": feedText.value, "user_id": user_id.value}));
    feedText.value = "";
    e.preventDefault();
};