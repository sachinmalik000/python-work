def chatbot():
    print("🤖 Hello! I am CLI ChatBot. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("🤖 ChatBot: Goodbye!")
            break

        # Basic responses
        elif "hello" in user_input.lower():
            print("🤖 ChatBot: Hello! How can I help you today?")
        elif "how are you" in user_input.lower():
            print("🤖 ChatBot: I'm just code, but I'm running fine!")
        elif "your name" in user_input.lower():
            print("🤖 ChatBot: I'm a CLI ChatBot.")
        else:
            print("🤖 ChatBot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()
