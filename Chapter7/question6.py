import random
def roll(number_of_throws):
# Use a list comprehension to generate a list of random numbers.
# For each throw (represented by '_' as the iteration variable, since it's not used), 
# 'random.randint(1, 6)' simulates a die roll, which can be any integer from 1 to 6.
    return sorted([random.randint(1, 6) for _ in range(number_of_throws)])

# Start an infinite loop to repeatedly ask the user for input until a valid input is given.
while True:
# Prompt the user to input the number of dice throws and convert the input to an integer.
    number_of_throws = int(input("Enter the number of throws (a positive integer): "))
    if number_of_throws > 0:
        break
    else:
# If the input is not a positive integer, inform the user and continue the loop.
        print("Please enter a positive integer.")

result = roll(number_of_throws)
print("Sorted list of random numbers:", result)
