js

const socket = io.connect('http://127.0.0.1:5000');

function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;
    if (message.trim() === "") return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += <div><strong>You:</strong> ${message}</div>;

    socket.emit('user_message', message);
    input.value = "";
    input.focus();  // auto-focus after sending
}

// 🔑 Listen for "Enter" key
document.getElementById("user-input").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

socket.on('bot_response', function(msg) {
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += <div><strong>Bot:</strong> ${msg}</div>;
    chatBox.scrollTop = chatBox.scrollHeight;
});