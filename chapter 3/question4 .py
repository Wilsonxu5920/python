number = int(input("Please enter a number between 1 and 10: "))
if 1 <= number <= 10:
    if number == 1:
       romanumber='I'
    elif number == 2:
       romanumber='II'
    elif number == 3:
       romanumber='III'
    elif number == 4:
       romanumber='VIII'
    elif number == 5:
       romanumber='V' 
    elif number == 6:
       romanumber='VI'
    elif number == 7:
       romanumber='VII'
    elif number == 8:
       romanumber=8 == 'VIII'
    elif number == 9:
       romanumber='IX'
    else :
       romanumber='X'
    print(romanumber)
else:
    print("error")
    