# This is a comment. The computer ignores anything after the # symbol.
# Comments help other people (and future you) understand what your code does.

# Variables: These are like labeled boxes where we can store information
user_name = input("What's your name? ")  # This asks the user for their name

# Conditional statements (if/else): These let your program make decisions
if user_name == "":  # If the user didn't type anything
    print("Hello, stranger!")
else:  # Otherwise, use their name
    print(f"Hello, {user_name}!")  # The f before the string and {} allow us to insert variables

# Let's ask a follow-up question
feeling = input("How are you feeling today? ")

# Let's use more conditions to respond appropriately
if "good" in feeling.lower() or "great" in feeling.lower() or "happy" in feeling.lower():
    print("That's wonderful to hear!")
elif "bad" in feeling.lower() or "sad" in feeling.lower() or "tired" in feeling.lower():
    print("I'm sorry to hear that. I hope your day gets better.")
else:
    print("Thanks for sharing!")
    
print("It was nice chatting with you!")
