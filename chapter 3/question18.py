vegetarian = input('Is anyone in your party a vegeterian?')
vegan = input('Is anyone in your party a vegan?')
gluten_free = input('Is anyone in your party a gluten-free?')
print('Here is the restaurant choice:')
if vegetarian != 'yes' and vegan != 'yes' and gluten_free != 'yes':
    print("Joe's Gourmet Burgers")
if vegan != 'yes':
    print('Main Street Pizza Company—Vegetarian')
print('Corner Café—Vegetarian')
if vegan != 'yes' and gluten_free != 'yes':
    print("Mama's Fine Italian")
print("The Chef's Kitchen")
