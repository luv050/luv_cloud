
# Importing required libraries
import random
import os
# Dictionary of predefined responses
responses = {
    "greeting": ["Hello!", "Hi!", "Welcome!","Hey, how are you?"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "My pleasure!"],
    "reply": ["I'm fine!", "Hey I'm good, thanks for asking!!", "I'm doing just well, how are you?"],
    "response": ["That's great!!", "I'm glad", "Yay"],
    "default": ["I'm sorry, I didn't understand.", "Could you please rephrase?"]
}
# Function to generate a response based on user input
def generate_response(user_input):
    user_input = user_input.lower()
# Check for common keywords in user input
    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"])
    elif "goodbye" in user_input or "bye" in user_input:
        return random.choice(responses["farewell"])
    elif "thank" in user_input:
        return random.choice(responses["thanks"])
    elif "are you" in user_input:
        return random.choice(responses["reply"])
    elif "fine" in user_input or "good" in user_input:
        return random.choice(responses["response"])
    elif "open" in user_input:
        if "open" in user_input and "notepad" in user_input:
            os.system("notepad")
            return "Opening Notepad..."
        if "open" in user_input and "paint" in user_input:
            os.system("paint")
            return "Opening paint..."

    else:
        return random.choice(responses["default"])
# Main interaction loop
while True:
# Get user input
    user_input = input("User: ")
# Generate and display bot response
    bot_response = generate_response(user_input)
    print("Bot:", bot_response)
    if "Bye" in user_input or "goodbye" in user_input:
        break
