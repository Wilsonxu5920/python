numbers = []
for i in range(20):
    user = int(input(f"Enter number {i + 1}: "))
    numbers.append(user)
    lowest = min(numbers)
highest = max(numbers)
total = sum(numbers)
average = total / len(numbers)


print(f"Lowest number: {lowest}")
print(f"Highest number: {highest}")
print(f"Total: {total}")
print(f"Average: {average}")