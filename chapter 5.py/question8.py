def main():
   
    square_feet = float(input("Enter the square feet of wall space to be painted: "))
    paint__gallon = float(input("Enter the price of the paint per gallon: "))

   
    gallons_required = square_feet / 112
    labor_required = 8 * gallons_required
    cost_of_paint = gallons_required * paint__gallon
    labor_charges = labor_required * 35.00 
    total_cost = cost_of_paint + labor_charges
    print(f"Gallons of paint required: {(gallons_required)}")
    print(f"Hours of labor required: {(labor_required)}")
    print(f"Cost of the paint: ${(cost_of_paint, 2)}")
    print(f"Labor charges: ${round(labor_charges, 2)}")
    print(f"Total cost of the paint job: ${(total_cost, 2)}")

main()