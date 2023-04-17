var chatSocket = new WebSocket("ws://" + window.location.host + "/");   // socket client created by creating object of web socket
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
    const notificationDiv = document.getElementById("notification-div")


    if(messageJson.type==="chat.message")
        chatHistory.innerHTML += messageJson.user_id + ": " + messageJson.message_text + "<br/>";
    else
        notificationDiv.innerHTML += "<b>Message From: </b>>" + messageJson.user_id + "<br/>" + "<b>Message Content: </b>" + messageJson.message_text + "<hr><br>";
};