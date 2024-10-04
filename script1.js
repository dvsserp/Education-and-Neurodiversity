console.log("hello")

const sendChatbtn = document.querySelector(".chat-input button");
const chatInput = document.querySelector(".chat-input textarea");
const chatbox = document.querySelector(".chatbox");

const createChatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);
    let chatContent = className === "outgoing" 
        ? `<p>${message}</p>` 
        : `<span class="material-symbols-outlined">smart_toy</span><p>${message}</p>`;
    chatLi.innerHTML = chatContent;
    return chatLi; 
};

const handleChat = () => {
    const userMessage = chatInput.value.trim(); 
    if (!userMessage) return;

    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatInput.value = ""; 

    setTimeout(() => {
        chatbox.appendChild(createChatLi("thinking...", "incoming"));
    }, 600);
};

sendChatbtn.addEventListener("click", handleChat);

chatInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        event.preventDefault(); 
        handleChat();
    }
});