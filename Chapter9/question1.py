# Dictionaries containing data about the Galilean moons of Jupiter.
# Each moon has its mean radius in kilometers, surface gravity in m/s², and orbital period in days.
mean_radius_dict = {
    "Io": 1821.6,
    "Europa": 1560.8,
    "Ganymede": 2634.1,
    "Callisto": 2410.3
}

surface_gravity_dict = {
    "Io": 1.796,
    "Europa": 1.314,
    "Ganymede": 1.428,
    "Callisto": 1.235
}

orbital_period_dict = {
    "Io": 1.769,
    "Europa": 3.551,
    "Ganymede": 7.154,
    "Callisto": 16.689
}
# Function to display moon data.
# If the moon is in the dictionary, it prints its mean radius, surface gravity, and orbital period.
# If the moon is not found, it prints an error message.
def display_moon_data(moon_name):
    if moon_name in mean_radius_dict:
        print(f"Mean Radius: {mean_radius_dict[moon_name]} kilometers")
        print(f"Surface Gravity: {surface_gravity_dict[moon_name]} m/s²")
        print(f"Orbital Period: {orbital_period_dict[moon_name]} days")
    else:
        print("Moon not found.")
# Main loop that continues to ask the user to enter a moon name.
# It breaks and exits if the user types 'quit'.

while True:
    moon_name = input("Enter the name of a Galilean moon of Jupiter (Io, Europa, Ganymede, Callisto) or 'quit' to exit: ").capitalize()
    
    if moon_name == 'Quit':
        break

    display_moon_data(moon_name)
