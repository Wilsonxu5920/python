def process_numbers(numbers):
    valid_numbers = []
    total = 0

    for number in numbers:
        if 0 <= number <= 100:
            valid_numbers.append(number)
            total += number

    return valid_numbers, total

def calculate_average(valid_numbers, total):
    if len(valid_numbers) > 0:
        average = total / len(valid_numbers)
    else:
        average = 0
    return average

numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

valid_numbers, total = process_numbers(numbers)
average = calculate_average(valid_numbers, total)

print("Valid numbers:", valid_numbers)
print("Total of valid numbers:", total)
print("Average of valid numbers:", average)
