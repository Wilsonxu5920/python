def multiply(x, y):

    if y == 1:
        return x
  
    else:
        return x + multiply(x, y-1)
x = int(input("Enter a positive nonzero integer for x: "))
y = int(input("Enter a positive nonzero integer for y: "))

result = multiply(x, y)
print(x, "times", y, "equals", result)