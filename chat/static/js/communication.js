var chatSocket = new WebSocket("ws://" + window.location.host + "/");
window.socket = chatSocket
chatSocket.onopen = function (e) {
    console.log("The connection was setup successfully !");
};
chatSocket.onclose = function (e) {
    console.log("Something unexpected happened !");
};
chatSocket.onmessage = function (message) {
    const messageJson = JSON.parse(message.data);


    const chatHistory = document.getElementById("chat-history");

    console.log(message);

    if(messageJson.message_text)
        chatHistory.innerHTML += messageJson.user_id + ": " + messageJson.message_text + "<br/>";
};