dstarting_organisms = float(input("Enter the starting number of organisms: "))
average_daily_increase = float(input("Enter the average daily population increase (as a percentage): "))
number_of_days = int(input("Enter the number of days the organisms will be left to multiply: "))
current_population = dstarting_organisms
print("\nDay\tApproximate Population")
for day in range(1, number_of_days + 1):
    print(f"{day}\t{current_population:.5f}")
    current_population += current_population * (average_daily_increase / 100)