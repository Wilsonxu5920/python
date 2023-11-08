numbers = []

# Loop 20 times to collect 20 numbers
for i in range(20):
    while True:
        # Prompt the user to input a number and cast it to float
        number = float(input(f"Enter number {i + 1}: "))
        # Append the number to the list of numbers
        numbers.append(number)
        # Break out of the inner while loop
        break

# Calculate the lowest 
lowest = min(numbers)
# Calculate the highest number 
highest = max(numbers)

# Calculate the total sum of the numbers 
total = sum(numbers)
# Calculate the average of the numbers 
average = total / len(numbers)

print(f"Lowest number: {lowest}")
print(f"Highest number: {highest}")
print(f"Total of the numbers: {total}")
print(f"Average of the numbers: {average:.2f}")
