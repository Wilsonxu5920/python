year = int(input("enter the year"))
month = input("enter the mouth")
day = int(input("enter the day"))
number = int(input("enter the number of the days"))
 # Lists of months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
remaining_days = days_in_month[months.index(month)] - day   

if year % 400 == 0 or (year % 4 ==0, year % 100 !=0):
  days_in_month[1] = 29 

if number <= remaining_days: # should we skip 
            day += number
            number = 0

else:
         
    number -= (remaining_days + 1)
    day = 1
    month_index = (months.index(month) + 1) % 12 #move next mouth
    month = months[month_index]
    if month_index == 0:# move new year
          year += 1
 





