def process_numbers(numbers):
    # Initialize an empty list to hold numbers that are within the valid range
    valid_numbers = []
    # Initialize a variable to keep track of the sum of valid numbers
    total = 0

    # Iterate over each number in the list of numbers
    for number in numbers:
        # Check if the number is within the valid range (inclusive)
        if 0 <= number <= 100:
            # If it is, append it to the list of valid numbers
            valid_numbers.append(number)
            # And add it to the running total
            total += number

    # Return a tuple containing the list of valid numbers and their total sum
    return valid_numbers, total

# Define a function to calculate the average of the valid numbers
def calculate_average(valid_numbers, total):
    # Check if the list of valid numbers is not empty
    if len(valid_numbers) > 0:
        # Calculate the average as the sum of valid numbers divided by their count
        average = total / len(valid_numbers)
    else:
        average = 0
    # Return the calculated average
    return average

# List of numbers to be processed
numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

# Process the list of numbers to get valid numbers and their total
valid_numbers, total = process_numbers(numbers)
# Calculate the average of the valid numbers
average = calculate_average(valid_numbers, total)

print("Valid numbers:", valid_numbers)
print("Total of valid numbers:", total)
print("Average of valid numbers:", average)




