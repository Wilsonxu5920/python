def falling_distance(time): 
    g = 9.8 
    distance = 0.5 * g * time**2
    return distance

for t in range(1, 11):
    dist = falling_distance(t)
    print(f"In {t} second, an object has fallen {dist} .")