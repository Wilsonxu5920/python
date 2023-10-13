import random

choices = {1: "rock", 2: "paper", 3: "scissors"}
    
computer_choice = choices[random.randint(1, 3)]
user_choice = input("Choose rock, paper, or scissors: ")
     
print(f"Computer chose {computer_choice}.")
if user_choice == computer_choice:
            print("Choose again.")

if ((user_choice == 'rock' and computer_choice == 'scissors') or 
        (user_choice == 'paper' and computer_choice == 'rock') or 
        (user_choice == 'scissors' and computer_choice == 'paper')):
    
    print("You win!")
else:
    print("You lose!")
    
