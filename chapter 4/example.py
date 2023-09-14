# File: <NAME OF FILE>
# Description: <A DESCRIPTION OF YOUR PROGRAM>
# Assignment Name and Number:
#
# Name: <YOUR NAME>
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

# File: repitition.py
# Description: for and while loops
# Assignment Name and Number: N/A
#
# Name: Mr.Lopez
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.


# For loop examples using range:

# Range with 1 argument goes from 0 through n-1
for num in range(10):
    print (num)

# Range with 2 arguments goes from the first number through the last-1
for num in range(7, 15):
    print (num)

# Range with 3 arguments goes from the first number through the
# second-1, in increments determined by the third number
for num in range(2, 12, -2): # What happens if the 3rd number is negative?
    print (num)


# A while loop example

# Initialize a counter
count = 1
print ("Count is initially", count)
# Want to keep looping until the counter is bigger than 100
while count < 100:
 count = count * 9
 print ("Now count is", count)

# When we get here, the while loop is done - so count must be > 100
#print "the counter is", count