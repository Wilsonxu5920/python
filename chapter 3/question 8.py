people= int(input("enter the number of the people "))
number = int(input('Please enter the amount of hotdogs each person will eat: '))
total_hotdogs_required = people * number
packages_required = total_hotdogs_required // 8
if total_hotdogs_required % 8 != 0:
    packages_required += 1
package_leftovers = (packages_required * 8) - total_hotdogs_required
hotdogs_required = total_hotdogs_required // 10
if total_hotdogs_required % 10 != 0:
    hotdogs_required += 1
hotdog_leftovers = (hotdogs_required * 10) - total_hotdogs_required
print('The minimum amount of hotdog packages needed is', packages_required)
print('The minimum amount of hotdogs needed is', hotdogs_required)
print('The amount of hotdog packages that will be leftover is', package_leftovers)
print('The amount of hotdogs that will be leftover is', hotdog_leftovers)