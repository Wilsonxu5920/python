def calculate_income(class_a_tickets, class_b_tickets, class_c_tickets):
    price_class_a = 20
    price_class_b = 15
    price_class_c = 10

    income_class_a = class_a_tickets * price_class_a
    income_class_b = class_b_tickets * price_class_b
    income_class_c = class_c_tickets * price_class_c

    total_income = income_class_a + income_class_b + income_class_c

    return income_class_a, income_class_b, income_class_c, total_income

class_a_tickets = int(input("Enter the number of Class A tickets sold: "))
class_b_tickets = int(input("Enter the number of Class B tickets sold: "))
class_c_tickets = int(input("Enter the number of Class C tickets sold: "))

income_class_a, income_class_b, income_class_c, total_income = calculate_income(class_a_tickets, class_b_tickets, class_c_tickets)

print(f"Income from Class A seats: ${income_class_a}")
print(f"Income from Class B seats: ${income_class_b}")
print(f"Income from Class C seats: ${income_class_c}")
print(f"Total income: ${total_income}")
