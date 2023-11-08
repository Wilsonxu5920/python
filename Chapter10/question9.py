# Import the random module
# Define a 'Question' class
# Initialize a 'Question' object with the question text
# Create a list of 'Question' objects
# Define the main function to control the flow of the quiz game
# Initialize score variables for player 1 and player 2 to zero
# Loop through each question in the quiz
# Display the prompt for player 1 and show the question
# Inform player 1 if their answer was correct or incorrect
# Repeat the same process for player 2
# Display the prompt for player 2 and show the same question
# Inform player 2 if their answer was correct or incorrect
# Once all questions have been answered, display the end game message
# Check if the script is the main program and if so, execute the main function to start the game

import random

class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_option


questions = [
    Question("What is the capital of France?",
             ["Paris", "London", "Berlin", "Madrid"],
             1),
    Question("Which planet is known as the 'Red Planet'?",
             ["Mars", "Venus", "Jupiter", "Saturn"],
             1),
    Question("What is the largest mammal in the world?",
             ["Elephant", "Giraffe", "Whale Shark", "Blue Whale"],
             4),
]

def main():
    player1_score = 0
    player2_score = 0

    for question in questions:
        print("\nPlayer 1's Turn:")
        question.display_question()
        player1_answer = int(input("Enter your answer (1-4): "))
        if question.check_answer(player1_answer):
            print("Correct! Player 1 earns a point.")
            player1_score += 1
        else:
            print("Incorrect. Player 1 doesn't earn a point.")

        print("\nPlayer 2's Turn:")
        question.display_question()
        player2_answer = int(input("Enter your answer (1-4): "))
        if question.check_answer(player2_answer):
            print("Correct! Player 2 earns a point.")
            player2_score += 1
        else:
            print("Incorrect. Player 2 doesn't earn a point.")

    print("\nGame Over!")
    print(f"Player 1's Score: {player1_score}")
    print(f"Player 2's Score: {player2_score}")
    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
