import random

def generate_lottery_number():
    lottery_number = []
    for _ in range(7):
        random_digit = random.randint(0, 9)
        lottery_number.append(random_digit)
    return lottery_number

def display_lottery_number(number):
    print("The generated lottery number is:")
    for digit in number:
        print(digit, end=" ")
    print("\n")

lottery_number = generate_lottery_number()
display_lottery_number(lottery_number)
