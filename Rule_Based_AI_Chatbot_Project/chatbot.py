responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "how are you": "I am fine. Thanks for asking!",
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to perform intelligent tasks.",
    "your name": "I am a Rule-Based AI Chatbot.",
    "help": "You can ask me about AI, my name, or greetings.",
    "bye": "Goodbye! Have a great day."
}

print("================================")
print("   Rule-Based AI Chatbot 🤖")
print("Type 'exit' to close chatbot")
print("================================")

while True:
    user_input = input("You: ")
    user_input = user_input.lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye! Ending conversation.")
        break

    if user_input in responses:
        print("Bot:", responses[user_input])
    else:
        print("Bot: Sorry, I don't understand. Please try another question.")
