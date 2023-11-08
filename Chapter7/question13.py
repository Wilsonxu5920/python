import random  
# Open the file 'responses.txt' in read mode as 'infile'.
with open('responses.txt', 'r') as infile:
# Read lines from the file, remove the newline character from the end of each line, and store them in a list.
    answers = [line.rstrip('\n') for line in infile]

# Start an infinite loop to keep asking the user for input.
while True:
# Prompt the user to enter a yes or no question or 'quit' to exit the game.
    x = input('Please enter a yes or no question(enter quit to quit):')
    if x != 'quit':
# If the user input is not 'quit', randomly select an answer from the list and print it.
        print(random.choice(answers))
    else:
# If the user input is 'quit', break out of the loop to end the game.
        break
print('You quit the game')
