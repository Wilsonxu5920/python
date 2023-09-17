days = int(input("Enter the number of days: "))

total = 0
salary = 1
print("Day\tSalary($)")
print("----------------")

for day in range(1, days + 1):
        print(f"{day}\t{salary:.2f}")
        total += salary
        salary *= 2  
       
print(f"\nThe total pay at the end of the period is: ${total:.2f}")