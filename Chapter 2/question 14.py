Principal_amount = float(input("enter the principal amount that was originally deposited into the account."))
rate = float(input("the annual interest rate."))
number_time = float(input("the number of times per year that the interest is compounded"))
t = float(input("the specified number of years"))

balance_of_account = amount = Principal_amount * (1 + rate / number_time) ** (number_time * t)
print('The formula for calculating the balance of the account after a specified number of years is:', balance_of_account)
