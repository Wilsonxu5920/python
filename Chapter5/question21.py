import random

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    user_input = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ")

    if user_input == 'q':
        break

    if user_input == 'rock':
        user_choice = 1
    elif user_input == 'paper':
        user_choice = 2
    else:
        user_choice = 3

    computer_choice = get_computer_choice()

    print(f"You chose {user_input}")
    if computer_choice == 1:
        print("Computer chose rock")
    elif computer_choice == 2:
        print("Computer chose paper")
    else:
        print("Computer chose scissors")

    result = determine_winner(user_choice, computer_choice)
    print(result)
