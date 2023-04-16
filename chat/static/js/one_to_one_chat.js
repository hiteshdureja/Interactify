const sendMessage=document.getElementById("send-message");
sendMessage.onsubmit= function (e) {
    const chatMessage = window.socket
    const messageText=document.getElementById("message");
    const user_id=document.getElementById("user_id");
    chatMessage.send(JSON.stringify({"message_text": messageText.value, "user_id": user_id.value}));
    messageText.value = "";
    e.preventDefault();
};