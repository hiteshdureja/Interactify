const chatSocket = new WebSocket("wss://localhost/");   // socket client created by creating object of web socket
window.socket = chatSocket     // socket client made global
chatSocket.onopen = function (e) {
    console.log("The connection was setup successfully !");
};
chatSocket.onclose = function (e) {
    console.log("Something unexpected happened !");
};
chatSocket.onmessage = function (message) {
    const messageJson = JSON.parse(message.data);
    const chatHistory = document.getElementById("chat-history");
    const notificationDiv = document.getElementById("notificationDiv");
    console.log(messageJson)
    if(messageJson.type==='notification.message')
        notificationDiv.innerHTML +=  "<div class='noftification-div'><b>" + messageJson.user_id + ": </b>"
            + messageJson.feed_text + "</div><hr>";
    else
        chatHistory.innerHTML += "<strong>" + messageJson.user_id + ": " + "</strong>" + messageJson.message_text + "<br/>";
};