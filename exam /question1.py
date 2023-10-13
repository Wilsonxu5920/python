def gcd(x, y):
    for i in range(y): 
        if y == 0:
         break
        x, y = y, x % y
    return x

print(gcd(12345, 67890))