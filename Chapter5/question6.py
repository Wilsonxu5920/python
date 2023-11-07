def calories_from_fat(fat_grams):
    return fat_grams * 9
def calories_from_carbs(carb_grams):
    return carb_grams * 4
fat_grams_input = float(input("Enter the number of fat grams consumed in a day: "))
carb_grams_input = float(input("Enter the number of carbohydrate grams consumed in a day: "))
print(f"Calories from fat: {calories_from_fat(fat_grams_input)}")
print(f"Calories from carbohydrates: {calories_from_carbs(carb_grams_input)}")