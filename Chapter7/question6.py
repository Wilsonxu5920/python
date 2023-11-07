import random

def roll(number_of_throws):
    return sorted([random.randint(1, 6) for _ in range(number_of_throws)])

while True:
    number_of_throws = int(input("Enter the number of throws (a positive integer): "))
    if number_of_throws > 0:
        break
    else:
        print("Please enter a positive integer.")

result = roll(number_of_throws)
print("Sorted list of random numbers:", result)
