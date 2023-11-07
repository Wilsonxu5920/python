numbers = []

for i in range(20):
    while True:
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)
        break

lowest = min(numbers)
highest = max(numbers)


total = sum(numbers)
average = total / len(numbers)

print(f"Lowest number: {lowest}")
print(f"Highest number: {highest}")
print(f"Total of the numbers: {total}")
print(f"Average of the numbers: {average:.2f}")
