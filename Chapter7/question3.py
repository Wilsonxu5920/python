rainfall_data = []

# Loop through each month of the year 
for month in range(1, 13):
    while True:
# Prompt the user to enter the total rainfall for the current month.
        rainfall = float(input(f"Enter the total rainfall for month {month}: "))
# Check if the entered rainfall is a non-negative number.
        if rainfall >= 0:
# If valid, add the rainfall amount to the rainfall_data list.
            rainfall_data.append(rainfall)
 # Exit the inner while loop and proceed to the next month.
            break
        else:
# If the input is negative, prompt the user to try again.
            print("Rainfall cannot be negative. Please try again.")

# Calculate the total rainfall 
total_rainfall = sum(rainfall_data)

# Calculate the average monthly 
average_rainfall = total_rainfall / 12

# Find the maximum.
max_rainfall = max(rainfall_data)
# Find the minimum .
min_rainfall = min(rainfall_data)

# Initialize lists to keep track of which months had the highest and lowest rainfall.
months_highest = []
months_lowest = []

# Iterate over the rainfall_data list to determine the position of the max and min values.
for i in range(len(rainfall_data)):
    # If the current month's rainfall matches the max rainfall, record its month number.
    if rainfall_data[i] == max_rainfall:
        months_highest.append(i + 1)
    # If the current month's rainfall matches the min rainfall, record its month number.
    if rainfall_data[i] == min_rainfall:
        months_lowest.append(i + 1)

print(f"Total rainfall for the year: {total_rainfall} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
print("Month(s) with the highest rainfall:", ', '.join(str(month) for month in months_highest))
print("Month(s) with the lowest rainfall:", ', '.join(str(month) for month in months_lowest))
