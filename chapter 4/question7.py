
days = int(input('Please enter the number of days:'))
salary = 0 
n = 1

for day in range(1, days + 1):
    salary += n
    n *= 2
    print("Day", day, 'Salary is', salary / 100)

print('The total salary:', salary / 100)