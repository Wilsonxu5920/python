calories_minute = 4.2
minutes_list = [10, 15, 20, 25, 30]

calories_dict = {}

for minutes in minutes_list:
    calories_burned = minutes * calories_minute
    calories_dict[minutes] = calories_burned
for minutes, calories in calories_dict.items():
    print(f"calories burned after {minutes} minutes:", calories)
#calories_burned_1 = 10 * calories_minute
#calories_burned_2 = 15 * calories_minute
#calories_burned_3 = 20 * calories_minute
#calories_burned_4 = 25 * calories_minute
#calories_burned_5 = 30 * calories_minute
#print("calories burned after 10:",calories_burned_1)
#print("calories burned after 15:",calories_burned_2)
#print("calories burned after 20:",calories_burned_3)
#print("calories burned after 25:",calories_burned_4)
#print("calories burned after 30:",calories_burned_5)