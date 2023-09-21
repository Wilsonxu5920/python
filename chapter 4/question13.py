dstarting_organisms = float(input("Enter the starting number of organisms: "))
average_increase = float(input("Enter the average daily population increase (as a percentage): "))
number_days = int(input("Enter the number of days the organisms will be left to multiply: "))
current_population = dstarting_organisms
print("DayApproximate Population")
for day in range(1, number_days + 1):
    population = dstarting_organisms * (1+average_increase**( day-1))
    print(day, population)
