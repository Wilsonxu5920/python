rainfall_data = []

for month in range(1, 13):
    while True:
        rainfall = float(input(f"Enter the total rainfall for month {month}: "))
        if rainfall >= 0:
            rainfall_data.append(rainfall)
            break
        else:
            print("Rainfall cannot be negative. Please try again.")

total_rainfall = sum(rainfall_data)

average_rainfall = total_rainfall / 12

max_rainfall = max(rainfall_data)
min_rainfall = min(rainfall_data)

months_highest = []
months_lowest = []

for i in range(len(rainfall_data)):
    if rainfall_data[i] == max_rainfall:
        months_highest.append(i + 1)
    if rainfall_data[i] == min_rainfall:
        months_lowest.append(i + 1)

print(f"Total rainfall for the year: {total_rainfall} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
print("Month(s) with the highest rainfall:", ', '.join(str(month) for month in months_highest))
print("Month(s) with the lowest rainfall:", ', '.join(str(month) for month in months_lowest))
