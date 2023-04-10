const sendMessage=document.getElementById("send-message");
const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

// function generateString(length) {
//     let result = ' ';
//     const charactersLength = characters.length;
//     for ( let i = 0; i < length; i++ ) {
//         result += characters.charAt(Math.floor(Math.random() * charactersLength));
//     }
//
//     return result;
// }
sendMessage.onsubmit= function (e) {
    document.cookie = "user_id=; expires=; path=/;";
    const chatMessage = window.socket
    const messageText=document.getElementById("message");
    const user_id=document.getElementById("user_id");
    chatMessage.send(JSON.stringify({"message_text": messageText.value, "user_id": user_id.value}));
    messageText.value = "";
    e.preventDefault();
};