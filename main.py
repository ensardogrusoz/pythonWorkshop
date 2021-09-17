from bot import related, send_message

if __name__ == "__main__":
    print("BOT: Hello! What is your name!")
    user_name = input()

    print(f"BOT: Nice meeting you {user_name}!")
    print("BOT: Ask a question!\nExamples:\n- Whats the weather\n- Play Game\n- Are you a robot?")

    while True:
        my_input = input()
        my_input = my_input.lower()

        related_text = related(my_input)
        send_message(related_text)

        if my_input == "exit":
            exit()
