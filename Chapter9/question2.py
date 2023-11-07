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
