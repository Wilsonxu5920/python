def kinetic_energy(mass, velocity):
    kinetic_energy = 0.5 * mass * velocity**2
    return kinetic_energy

mass = float(input("Enter the object's mass (in kilograms): "))
velocity = float(input("Enter the object's velocity (in meters per second): "))

ke = kinetic_energy(mass, velocity)

print(f"The object's kinetic energy is {ke:.2f} joules.")





