while True:
    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Hello!")

    elif user == "hello":
        print("Bot: Hi there!")

    elif user == "how are you":
        print("Bot: I am fine!")

    elif user == "your name":
        print("Bot: My name is AI Bot")

    elif user == "thank you":
        print("Bot: Welcome!")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand")