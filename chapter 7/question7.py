import random

def roll(number_of_throws):
    return sorted([random.randint(1, 6) for _ in range(number_of_throws)])

throws = int(input("Enter number of throws: "))
result = roll(throws)
print(result)