import random
from rps import rock_paper_scissors_game

# ---------------- CONSTANTS -------------------------------
WEATHER = "rainy"
RESPONSES = {
    "what's today's weather?": [
        f"The weather is {WEATHER}",
        f"It's {WEATHER} today",
        f"Let me check, it looks {WEATHER} today"],

    "are you a robot?": [
        "What do you think?",
        "Maybe yes, maybe no!",
        "Yes, I am a robot with human feelings.", ],

    "exit": [
        "Bye, see you next time!",
        "see you later"
    ],

    "default": [
        "Sorry I did not understand that."]
}

# ---------------- BOT HELPERS -----------------------------------

def respond(message):
    if message in RESPONSES: 
        bot_message = random.choice(RESPONSES[message])
    else: 
        # good practice to have a default response.
        bot_message = random.choice(RESPONSES["default"])
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
  print(f"USER: {message}") 
  response = respond(message) 
  print(f"BOT: {response}")