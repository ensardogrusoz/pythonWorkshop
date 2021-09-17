import random

def rock_paper_scissors_game():
    while True:
        #ask the user a question then wait for their input
        user_action = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions) #computer will choose from the list of possible_actions
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n") #prints out a message saying what you chose, and what the computer chose

        #this is the winning logic
        #tie
        if user_action == computer_action: #if both players pick the same thing, it's a tie
            print(f"Both players selected {user_action}. It's a tie!")
        #user rock
        elif user_action == "rock":
            if computer_action == "scissors": #checks to see if computer chose scissors after you chose rock, meaning you win
                print("Rock smashes scissors! You win!")
            else: #same as above, but with computer choosing paper instead, meaning you lose
                print("Paper covers rock! You lose.")
        #user paper
        elif user_action == "paper":
            if computer_action == "rock": #checks if computer chose rock after you chose paper, meaning you win
                print("Paper covers rock! You win!")
            else: #computer chose scissors after you chose paper, meaning you lost
                print("Scissors cuts paper! You lose.")
        #user scissors
        elif user_action == "scissors":
            if computer_action == "paper": #computer chose paper after you chose scissors, meaning you won
                print("Scissors cuts paper! You win!")
            else: #computer chooses rock while you choose scissors, meaning you lose
                print("Rock smashes scissors! You lose.")

        # asks the user if they want to play again
        play_again = input("Play again? (y/n): ") 
        if play_again.lower() != "y": #if you dont choose y as your answer to play again, the program is exited
            exit()