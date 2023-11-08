import random  # Imports the random module
def generate_lottery_number():
    lottery_number = []  
    for _ in range(7):  # Loops 7 times to generate a 7-digit lottery number
        random_digit = random.randint(0, 9)  # Generates a random integer between 0 and 9
        lottery_number.append(random_digit)  # Appends the random digit to the lottery_number list
    return lottery_number  # Returns the completed list of 7 random digits

def display_lottery_number(number):
    print("The generated lottery number is:")  
    for digit in number:  
        print(digit, end=" ")  
    print("\n")  # Prints a newline character for formatting purposes

lottery_number = generate_lottery_number()  # Calls the function to generate a lottery number and stores it
display_lottery_number(lottery_number)  # Calls the function to display the generated lottery number
