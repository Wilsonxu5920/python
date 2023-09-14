number = int(input("Enter a pocket number: "))
if 0 <= number <= 36:
    if number == 0:
        color = "green"
    elif 1 <= number <= 10 or 19 <= number <= 28:
        color = "red"  if number % 2 == 1 else "black"
    else:
        color = "black" if number % 2 == 1 else "red"
    print(color)
else:
    print("error")
   