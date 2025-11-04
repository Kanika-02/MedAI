document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keypress", function (e) {
  if (e.key === "Enter") sendMessage();
});

function appendMessage(sender, text) {
  const chatBox = document.getElementById("chat-box");
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender === "user" ? "user-message" : "bot-message");
  messageDiv.textContent = text;
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const input = document.getElementById("user-input");
  const userText = input.value.trim();
  if (!userText) return;

  appendMessage("user", userText);
  input.value = "";

  const response = await fetch("/get", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userText }),
  });

  const data = await response.json();
  appendMessage("bot", data.response);
}
