def calculate_paint_job(square_feet, paint_price):

    square_feet_per_gallon = 112
    labor_hours_per_gallon = 8
    labor_rate = 35.00

    gallons_required = square_feet / square_feet_per_gallon

    labor_required = gallons_required * labor_hours_per_gallon

    paint_cost = gallons_required * paint_price

    labor_charges = labor_required * labor_rate

    total_cost = paint_cost + labor_charges

    return gallons_required, labor_required, paint_cost, labor_charges, total_cost

square_feet = float(input("Enter the square feet of wall space to be painted: "))
paint_price = float(input("Enter the price of paint per gallon: "))

gallons_required, labor_required, paint_cost, labor_charges, total_cost = calculate_paint_job(square_feet, paint_price)

print(f"Number of gallons of paint required: {gallons_required:.2f} gallons")
print(f"Hours of labor required: {labor_required:.2f} hours")
print(f"Cost of the paint: ${paint_cost:.2f}")
print(f"Labor charges: ${labor_charges:.2f}")
print(f"Total cost of the paint job: ${total_cost:.2f}")
