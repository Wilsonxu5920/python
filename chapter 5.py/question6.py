def fat_grams (fat_grams):
    return fat_grams*9
def crab_grams(crab_grams):
    return crab_grams*4
fat_grams_input= float(input("enter the number of fat_grams"))
crab_grams_input= float(input("enter the number of the crab_grams"))
print(f"calories from fat{fat_grams(fat_grams_input)}"f"calories from crab{crab_grams(crab_grams_input)}")