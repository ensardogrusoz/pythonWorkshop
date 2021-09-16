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

print("BOT: Hello! What is your name")
user_name = input()

# These templates will act as a placeholder for conversations going 
# back and forth between the bot and user- 
# the {0} are responsive
bot_template = "BOT : {0}"
user_template = user_name + " : {0}" 

# By using the format function, we can fill in the value inside of {}
print(bot_template.format("Ask a question. ex: 'whats the weather', 'play game', 'are you a robot?'"))

weather = "rainy" 

# this is a dictionary
responses = { 
    "what's today's weather?": [ 
    "The weather is {0}".format(weather), 
    "It's {0} today".format(weather), 
    "Let me check, it looks {0} today".format(weather) ],
    
    "Are you a robot?": [ 
    "What do you think?", 
    "Maybe yes, maybe no!", 
    "Yes, I am a robot with human feelings.", ],
    
    "exit": [
        "Bye, see you next time!"
    ],

    "default": [
    "Sorry I did not understand that."] 
}

def respond(message):
    if message in responses: 
        bot_message = random.choice(responses[message])
    else: 
        # good practice to have a default response.
        bot_message = random.choice(responses["default"])
    return bot_message

# this function will map the key words in the input to a response
def related(x_text): 
    if "weather" in x_text: 
        y_text = "what's today's weather?"
    elif "robot" in x_text: 
        y_text = "Are you a robot?"
    elif "exit" in x_text: 
        y_text = "exit"
    elif "game" in x_text:
        rock_paper_scissors_game()
    else: 
        y_text = ""
    return y_text

def send_message(message): 
  print(user_template.format(message)) 
  response = respond(message) 
  print(bot_template.format(response))

# this is what keeps the code/bot conversation
while True: 
  # gets the users input
  my_input = input() 
  my_input = my_input.lower()
  # gets the key word from the input 
  related_text = related(my_input) 
  # returns a bot response in relation to that key word
  send_message(related_text)
  if my_input == "exit": 
    exit()
