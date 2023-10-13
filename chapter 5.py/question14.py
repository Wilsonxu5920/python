def kinetic_energy(mass, velocity):  
    k= 0.5 * mass * velocity ** 2
    return k
mass = float(input("Enter the  mass in kilograms: "))
velocity = float(input("Enter the  velocity in meters per second: "))

k = kinetic_energy(mass, velocity)
print(f"The object has {k} joules.")




