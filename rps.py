import random

def rock_paper_scissors_game():
    while True:
        #ask the user a question then wait for their input
        user_action = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        #this is the winning logic
        #tie
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        #user rock
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        #user paper
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        #user scissors
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        # asks the user if they want to play again
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            exit()