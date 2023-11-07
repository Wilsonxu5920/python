def kilometers_to_miles(kilometers):
    miles = kilometers * 0.6214
    return miles
kilometers = float(input("Enter the number of kilometers: "))
print(kilometers,"kilometers is equal to",kilometers_to_miles(kilometers), "miles")
