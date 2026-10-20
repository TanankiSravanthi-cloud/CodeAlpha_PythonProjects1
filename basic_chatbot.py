"""A simple rule-based chatbot using if/elif and a loop."""


def reply(message):
    message = message.strip().lower()
    if message in {"hello", "hi", "hey"}:
        return "Hi! How can I help you?"
    elif "how are you" in message:
        return "I'm fine, thanks! How are you?"
    elif "your name" in message:
        return "I'm PyBot, a simple Python chatbot."
    elif message in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye!"
    elif "help" in message:
        return "You can say hello, ask how I am, ask my name, or say bye."
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see what I can do."


def main():
    print("\n=== Basic Chatbot ===")
    print("PyBot: Hello! Type 'bye' to end the chat.")
    while True:
        message = input("You: ")
        answer = reply(message)
        print(f"PyBot: {answer}")
        if message.strip().lower() in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    main()
