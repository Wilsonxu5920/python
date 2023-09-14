number = int(input("enter a integer:"))
if number < 0:
    display = "negetive"
elif number > 0:
    display = "positive"
else : 
    display ="zero"
print(display)

if number % 2 == 0:
    print("Even")
else:
    print("Odd")