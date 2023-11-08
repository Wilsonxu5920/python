# Import the random module 
# Define a dictionary with U.S. 
# Define the quiz function
# Initialize a counter for the number of correct answers.
# Initialize a counter for the number of incorrect answers.
# Begin an infinite loop
# Select a random state 
# Retrieve the corresponding capital for the chosen state.
# Prompt the user for the capital of the randomly chosen state
# Capture and format the user's input.
# If the user types 'quit', exit the loop and end the quiz.
# Check if the user's answer matches the correct capital.
# Once the user quits, print the total number of correct and incorrect answers.
# Check if this script is being run as the main program.
# Greet the user and initiate the quiz function.
import random

state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
}

def quiz_user(state_capitals):
    correct = 0
    incorrect = 0

    states = list(state_capitals.keys())

    while True:
        state = random.choice(states)
        correct_answer = state_capitals[state]

        print(f"What is the capital of {state}? (Type 'quit' to exit)")
        user_input = input("Enter the capital: ").strip().title()

        if user_input == 'Quit':
            break

        if user_input == correct_answer:
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.\n")
            incorrect += 1

    print(f"Quiz completed. You got {correct} correct and {incorrect} incorrect.")

if __name__ == "__main__":
    print("Welcome to the U.S. States and Capitals Quiz!")
    quiz_user(state_capitals)
