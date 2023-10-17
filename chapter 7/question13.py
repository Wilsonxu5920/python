import random


with open('responses.txt', 'r') as infile:
    answers = [line.rstrip('\n') for line in infile]

while True:
    x = input('Please enter a yes or no question(enter quit to quit):')
    if x != 'quit':
        print(random.choice(answers))
    else:
        break

print('You quit the game')