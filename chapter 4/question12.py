
number = int(input("Enter a nonnegative integer: "))

if number >= 0:
    factorial = 1
    for i in range(1, number + 1):
            factorial *= i
    print(f"{number}! = {factorial}")

else:
     print("Please enter a nonnegative integer.")